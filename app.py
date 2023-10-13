import datetime as datetime
import numpy numpy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:////Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route("/")
def welcome():
    return(
        f"Welcome to my Hawaii Climate Analysis API<br/>",
        f"Available Routes:<br/>",
        f"/api/v1.0/precipitation<br/>",
        f"/api/v1.0/station<br/>",
        f"/api/v1.0/tobs<br/>",
        f"/api/v1.0/temp/start<br/>",
        f"/api/v1.0/temp/end<br/>",
        f"<p>'start' and 'end' date should be in the format MMDDYYY.</p>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_yr = dt.date(2017, 8, 23) - dt.timedelta(days = 365)

    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_yr).all()

    session.close()
    precip = { date : prcp for date, prcp in precipitation}

    return jsonify(precip)
if __name__ == "__main__":
    app.run(debug = True)