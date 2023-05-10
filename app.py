# Import the dependencies.
################################################
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
  
from flask import Flask, jsonify




#################################################
# Database Setup
#################################################

# creating the engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn = engine.connect()

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Home Route that holds the directory
@app.route("/")
def home():
    "Lists All Available Routes"
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start> (Date Format: YYYY/MM/DD)<br/>"
        f"/api/v1.0/<start>/<end> (Date Format: YYYY/MM/DD)<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precip():
    
    # Create session (link) from Python to the DB
    session = Session(engine)

    # Calculate the date one year from the last date in data set.
    last_year = dt.datetime(2017,8,23) - dt.timedelta(days = 365)

    # Perform a query to retrieve the data and precipitation scores
    results1 = session.query(Measurement.date, Measurement.prcp).\
                            filter(Measurement.date >= last_year).\
                                group_by(Measurement.date).all()

    # Close Session
    session.close()

    precip_date = []
    for date, prcp in results1:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["precip"] = prcp
        precip_date.append(precip_dict)

    return jsonify(precip_date)


@app.route("/api/v1.0/stations")
def stat():
    # Creating the Session
    session = Session(engine)
    # Getting all of the distinct station names
    results2 = session.query(Station.station, Station.id).all()

    # Close Session
    session.close()

    stations = []
    for station, id in results2:
        station_dict = {}
        station_dict["station"] = station
        station_dict["id"] = id
        stations.append(station_dict)

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create session (link) from Python to the DB
    session = Session(engine)
    
    # Creating a variable to look nicer
    meas_count = func.count(Measurement.station)
    
    # Using data found in the Jupyter notebook set the date "1 year ago"
    last_year = dt.datetime(2017,8,23) - dt.timedelta(days = 365)
    
    # Getting the most active stations
    active_stations = session.query(Measurement.station, meas_count).\
        group_by(Measurement.station).\
            order_by(meas_count.desc()).all()
    
    # Choosing the most active station and storing it
    station_1 = active_stations[0][0]

    MAS_weather = session.query(Measurement.date, Measurement.station, Measurement.tobs).\
                            filter(Measurement.station == station_1).\
                                filter(Measurement.date >= last_year).\
                                    group_by(Measurement.date).all()
    
    tobs_values = []
    for date, station, tobs in MAS_weather:
        tobs_values_dict = {}
        tobs_values_dict["date"] = date
        tobs_values_dict["station"] = station
        tobs_values_dict["tobs"] = tobs
        tobs_values.append(tobs_values_dict)

    return jsonify(tobs_values)
        


if __name__ == '__main__':
    app.run(debug=True)