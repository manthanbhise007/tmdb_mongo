import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from src.exception import CustomException
import sys

load_dotenv()
MONGO_URI=os.getenv("MONGO_URI")
DATABASE_NAME=os.getenv("DATABASE_NAME")
COLLECTION_NAME=os.getenv("COLLECTION_NAME")

class DataIntegration:
    def connect_data_to_mongodb(self):
        try:
            movies=pd.read_csv("data/modified.csv")
            client=MongoClient(MONGO_URI)
            db=client[DATABASE_NAME]
            collection=db[COLLECTION_NAME]
            data=movies.to_dict(orient='records')
            collection.delete_many({})
            """
            collection.delete_many({}):
                is used to delete all existing documents from the MongoDB collection before inserting fresh data
            
            """
            collection.insert_many(data)
            print("Data uploaded successfully to MongoDB Atlas")
        except Exception as e:
            raise CustomException(e,sys)
    
if __name__=="__main__":
    obj=DataIntegration()
    obj.connect_data_to_mongodb()
    