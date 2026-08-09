
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# from urllib.parse import quote_plus

# password = quote_plus("admin@243")

uri = "mongodb+srv://maritra36_db_user:admin243@cluster0.pgo5jc9.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)