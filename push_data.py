import os
import sys
import json
from dotenv import load_dotenv

load_dotenv() ## looks for a file named .env


mongodb_url=os.getenv("MONGO_DB_URL")
print(mongodb_url)

import certifi
ca=certifi.where()


import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import proj_exception

from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise proj_exception(e,sys)


    def cv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise proj_exception(e,sys)


    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(mongodb_url) ## This creates a connection to your MongoDB Atlas cluster.
            # At this point, you're connected to the cluster, but you haven't selected any database yet.
            self.database=self.mongo_client[self.database]
            # This tells MongoDB: "Give me the database named self.database"
            # Now self.database is no longer a string.
            self.collection=self.database[self.collection]
            ## ex: "Inside the NetworkSecurity database, give me the phishing_data collection."
            # Now self.collection is no longer a string.
            # It becomes a MongoDB Collection object.
            self.collection.insert_many(self.records)
            #MongoDB's insert_many() method takes multiple documents and inserts them into the collection.
            # After insertion, your collection might look like:

            # phishing_data

            # Document 1:
            # {
            #     "url": "google.com",
            #     "label": 0
            # }

            # Document 2:
            # {
            #     "url": "fake-site.com",
            #     "label": 1
            # }
            return len(self.records)
        

        except Exception as e:
            raise proj_exception(e,sys)


if __name__=="__main__":
    file_path="Network_Data\phisingData.csv"
    database="mlops_database_by_raj"
    collection="NetworkData"
    # // it creates a collection named "mlops_database_by_raj" inside my cluster
    networkobj=NetworkDataExtract()
    records=networkobj.cv_to_json_convertor(file_path=file_path)
    # print(records)
    no_of_rec=networkobj.insert_data_mongodb(records,database,collection)
    print(no_of_rec)