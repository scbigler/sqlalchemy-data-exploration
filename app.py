from cgi import print_exception
import datetime as dt
import numpy as np
import pandas as pd
from scipy import stats


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify



# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def welcome():

    
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/<start><br/>"
        f"/api/v1.0/temp/<start>/<end><br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # precipitation data for the last year of data
    most_recent = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    most_recent = pd.to_datetime(most_recent[0])
    day = int(most_recent.strftime("%d"))
    month = int(most_recent.strftime("%m"))
    year = int(most_recent.strftime("%Y"))
    one_year_prior = dt.date(year, month, day) - dt.timedelta(365)
    
    results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > one_year_prior).\
    order_by(Measurement.date).all()
    
    # Calculate the date 1 year ago from last date in database
    # Query for the date and precipitation for the last year
    # Dict with date as the key and prcp as the value
    ly_precip  = []
    for date, prcp in results:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp 
        ly_precip.append(precip_dict)

    return jsonify(ly_precip)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations."""
    results = session.query(Measurement.station).distinct().all()
    
    # Unravel results into a 1D array and convert to a list
    station_list = list(np.ravel(results))
    
    return jsonify(station_list)
    

@app.route("/api/v1.0/tobs")
def temp_monthly():
    """Return the temperature observations (tobs) for previous year."""
    # Calculate the date 1 year ago from last date in database
    most_recent = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    most_recent = pd.to_datetime(most_recent[0])
    day = int(most_recent.strftime("%d"))
    month = int(most_recent.strftime("%m"))
    year = int(most_recent.strftime("%Y"))
    one_year_prior = dt.date(year, month, day) - dt.timedelta(365) 
        
    # Query the primary station for all tobs from the last year
    primary = session.query(Measurement.station).order_by(func.count(Measurement.station).\
        desc()).group_by(Measurement.station).first()[0]
    
    last_year_data = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date > one_year_prior, Measurement.station == primary).\
    order_by(Measurement.date).all()
    
    # Unravel results into a 1D array and convert to a list
    measurements = list(np.ravel(last_year_data))
    
    # Return the results
    return jsonify(measurements)
   

@app.route("/api/v1.0/temp/<start>")
def stats1(start=None):
    """Return TMIN, TAVG, TMAX."""
    # calculate date of most recent data
    most_recent = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    
     # calculate TMIN, TAVG, TMAX with start until the most recent data
    tempstats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),\
            func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= most_recent[0]).all()
    
    # Unravel results into a 1D array and convert to a list
    mystats = list(np.ravel(tempstats))
    
    return jsonify(mystats)


@app.route("/api/v1.0/temp/<start>/<end>")
def stats2(start=None, end=None):
    """Return TMIN, TAVG, TMAX."""
    
    # Select statement
   # calculate TMIN, TAVG, TMAX with start until end
    tempstats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),\
            func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()

       # Unravel results into a 1D array and convert to a list
    mystats = list(np.ravel(tempstats))

    return jsonify(mystats)

if __name__ == '__main__':
    app.run()
