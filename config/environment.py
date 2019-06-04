import os

db_uri = os.getenv('DATABASE_URL', 'postgres://localhost:5432/hiddengem-db')
secret = os.getenv('SECRET', 'jibberish gobbledegook')
google_geo_key = os.getenv('GOOGLE_GEO_KEY')
