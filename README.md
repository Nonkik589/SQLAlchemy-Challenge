# SQLAlchemy-Challenge

## Jupyter Notebook
-Finds the most active station
-Finds the last 12 months of precipitation data and plots the results and creates a list of stats for the data.
-Finds the total number of stations
-Finds the most active station and its Min, Max, and AVG temps
-fint the last 12 months of temperature observation data for this station and plots the results


## API
Contains these routes:

A precipitation route that:

    -Returns json with the date as the key and the value as the precipitation
    -Only returns the jsonified precipitation data for the last year in the database 

A stations route that:

    -Returns jsonified data of all of the stations in the database

A tobs route that:

    -Returns jsonified data for the most active station
    -Only returns the jsonified data for the last year of data

A start route that:

    -Accepts the start date as a parameter from the URL
    -Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset 

A start/end route that:

    -Accepts the start and end dates as parameters from the URL
    -Returns the min, max, and average temperatures calculated from the given start date to the given end date






## Sources
https://pandas.pydata.org/docs/
https://docs.sqlalchemy.org/en/20/
https://pythonbasics.org/flask-tutorial-routes/
previous bootcamp projects