import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationSystem:
    def __init__(self):
        self.user_item_matrix = None
        self.user_similarity_matrix = None

    def fit(self, df):
        # Create a user-item matrix
        self.user_item_matrix = df.pivot_table(index='USERID', columns='PRODUCTID', values='RATING', fill_value=0)

        # Calculate cosine similarity between users
        self.user_similarity_matrix = cosine_similarity(self.user_item_matrix)

    def predict(self, user_id):
        if self.user_item_matrix is None or self.user_similarity_matrix is None:
            raise ValueError("Model not trained yet.")
        return np.dot(self.user_similarity_matrix, self.user_item_matrix.loc[user_id])

    def recommend_top_items(self, user_id, n=10):
        if self.user_item_matrix is None or self.user_similarity_matrix is None:
            raise ValueError("Model not trained yet.")

        predictions = self.predict(user_id)
        top_indices = np.argsort(predictions)[::-1][:n]
        return top_indices
