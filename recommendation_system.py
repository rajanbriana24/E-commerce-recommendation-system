from functools import lru_cache

class RecommendationSystem:
    def __init__(self):
        self.user_item_matrix = None
        self.user_similarity_matrix = None
        self.rmse = None
        self.mae = None

    @lru_cache(maxsize=None)  # Cache results of the fit method
    def fit(self, df):
        # Create a user-item matrix
        self.user_item_matrix = df.pivot_table(index='USERID', columns='PRODUCTID', values='RATING', fill_value=0)

        # Calculate cosine similarity between users
        self.user_similarity_matrix = cosine_similarity(self.user_item_matrix)

        # Predict ratings for all users and items
        predicted_ratings = np.dot(self.user_similarity_matrix, self.user_item_matrix)

        # Calculate RMSE and MAE
        mask = self.user_item_matrix != 0  # Mask for non-zero ratings
        diff_squared = (predicted_ratings - self.user_item_matrix) ** 2
        mse = np.sum(diff_squared[mask]) / np.sum(mask)  # Mean Squared Error
        self.rmse = np.sqrt(mse)  # Root Mean Squared Error
        self.mae = np.sum(np.abs(predicted_ratings - self.user_item_matrix)[mask]) / np.sum(mask)  # Mean Absolute Error

        print("Root Mean Squared Error (RMSE):", self.rmse)
        print("Mean Absolute Error (MAE):", self.mae)

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
