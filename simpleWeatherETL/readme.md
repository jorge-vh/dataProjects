## This is a quick project to perform ETL process by gathering data of weather from a city using Open Weather Map API and uploading it to a Postgres database.

### Initiliaze database using docker

'''
docker run --name postgres -e POSTGRES_PASSWORD=1234 -p 5432:5432 -d postgres
'''