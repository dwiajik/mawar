from os import environ

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

channel_access_token = environ.get('CHANNEL_ACCESS_TOKEN')
channel_secret = environ.get('CHANNEL_SECRET')

mysql_host = environ.get('MYSQL_HOST')
mysql_db = environ.get('MYSQL_DATABASE')
mysql_user = environ.get('MYSQL_USER')
mysql_password = environ.get('MYSQL_PASSWORD')
