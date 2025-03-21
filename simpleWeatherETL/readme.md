## Quick ETL example using weather data

This is a quick project to perform ETL process by gathering data of weather from a city using Open Weather Map API and uploading it to a PostgreSQL database.

### Initiliaze database using docker


Initialize docker container for PostgreSQL database

```
docker run --name postgres -e POSTGRES_PASSWORD=1234 -p 5432:5432 -d postgres
```
Access the terminal of PostgreSQL running in the container

```
docker exec -it postgres psql -U postgres
```

Create database

```
CREATE DATABASE etl_project;
```

Create table for the data will upload

```
CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    description TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Create conda environment

To create conda environment with the need configuration, execute

```
conda env create -f etlEnv.yaml
```

Activate conda environment

```
conda activate etlEnv
```

### Running ETL Python code

For this step, you'll need to modify etl.py with your own [OpenWeather API](https://openweathermap.org/api)

After succesfully modifying the code with your own API key, run the code

```
python etl.py
```

To see the data inserted in the database, enter PostgreSQL

```
docker exec -it postgres psql -U postgres -d etl_project
```

And execute the next query

```
SELECT * FROM weather_data;
```