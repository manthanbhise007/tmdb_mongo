import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URL=os.getenv("MONGO_URI")
DATABASE_NAME=os.getenv("DATABASE_NAME")
COLLECTION_NAME=os.getenv("COLLECTION_NAME")

class DataProcessing():
    def fetch_data_from_mongodb(self):
        client=MongoClient(MONGO_URL)
        db=client[DATABASE_NAME]
        collection=db[COLLECTION_NAME]
        data=list(collection.find())
        df=pd.DataFrame(data)
        return df
    
    def preprocessed(self):

        movies=self.fetch_data_from_mongodb()

        new_df=movies[['movie_id','title','tags']].copy()

        new_df.dropna(inplace=True)

        new_df['tags']=new_df['tags'].astype(str)

        print(new_df.head())

        return new_df
        
        
    
if __name__=="__main__":
    data_p=DataProcessing()
    data_p.preprocessed()

