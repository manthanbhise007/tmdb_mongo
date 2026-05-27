import os
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.components.data_preprocessing import DataProcessing
from src.utils import save_object
from src.exception import CustomException

class ModelTrainer:
    try:
        def train_model(self):

            processor=DataProcessing()

            new_df=processor.preprocessed()

            cv=CountVectorizer(max_features=5000,stop_words='english')

            vectors=cv.fit_transform(new_df['tags']).toarray()

            similarity=cosine_similarity(vectors)

            os.makedirs("artifacts",exist_ok=True)

            save_object("artifacts/movies.pkl",new_df)

            save_object("artifacts/similarity.pkl",similarity)

            print("Model training completed")
    except Exception as e:
        raise CustomException(e,sys)

if __name__=="__main__":

    trainer=ModelTrainer()

    trainer.train_model()