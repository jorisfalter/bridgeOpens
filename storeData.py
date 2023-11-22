import pymongo
import certifi
from dotenv import load_dotenv
import os
import datetime


from pymongo import MongoClient
ca = certifi.where()

# Load environment variables from .env file
load_dotenv()
mongoPass = os.getenv("MONGO_ATLAS_PASS")

client = pymongo.MongoClient(
    f'mongodb+srv://joris:{mongoPass}@cluster0.igx7ca5.mongodb.net/?retryWrites=true&w=majority&connectTimeoutMS=5000', tlsCAFile=ca)

db = client['bridgeOpenDb']
collection = db['bridgeOpenCollection']

now = datetime.datetime.now()

dataOneFlight = {"time": now}

result = collection.insert_one(dataOneFlight)
