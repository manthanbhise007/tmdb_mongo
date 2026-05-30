import streamlit as st
from src.utils import read_file


class App:

    def __init__(self):
        self.similarity = read_file("artifacts/similarity.pkl")
        self.movies_df = read_file("artifacts/movies.pkl")

    def recommend(self, movie):

        movie_index = self.movies_df[
            self.movies_df['title'] == movie
        ].index[0]

        distances = self.similarity[movie_index]

        movie_recommended = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x: x[1]
        )[1:6]

        rec_list = []

        for i in movie_recommended:
            rec_list.append(
                self.movies_df.iloc[i[0]].title
            )

        return rec_list

    def run(self):

        st.title("Movie Recommendation System")

        selected_movie = st.selectbox(
            "Select a movie",
            self.movies_df['title'].values
        )

        if st.button("Recommend"):

            recommendations = self.recommend(selected_movie)

            for movie in recommendations:
                st.write(movie)


if __name__ == "__main__":
    app = App()
    app.run()