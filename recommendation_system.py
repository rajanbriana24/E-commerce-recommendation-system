from pyspark.sql import SparkSession

class RecommendationSystem:
    def __init__(self):
        self.spark = SparkSession.builder \
            .appName("RecommendationSystem") \
            .getOrCreate()
        self.user_item_matrix = None
        self.user_similarity_matrix = None
        self.rmse = None
        self.mae = None

    def fit(self, df):
        # Convert pandas DataFrame to Spark DataFrame
        spark_df = self.spark.createDataFrame(df)

        # Create a user-item matrix
        self.user_item_matrix = spark_df.pivot_table(index='USERID', columns='PRODUCTID', values='RATING', fill_value=0)

        # Calculate cosine similarity between users
        self.user_similarity_matrix = self.user_item_matrix.stat.corr('USERID', 'PRODUCTID')

        # Predict ratings for all users and items
        predictions = self.user_similarity_matrix.dot(self.user_item_matrix)

        # Calculate RMSE and MAE
        mask = self.user_item_matrix != 0  # Mask for non-zero ratings
        diff_squared = (predictions - self.user_item_matrix) ** 2
        mse = diff_squared[mask].sum() / mask.sum()  # Mean Squared Error
        self.rmse = np.sqrt(mse)  # Root Mean Squared Error
        self.mae = np.abs(predictions - self.user_item_matrix)[mask].sum() / mask.sum()  # Mean Absolute Error

        print("Root Mean Squared Error (RMSE):", self.rmse)
        print("Mean Absolute Error (MAE):", self.mae)

    def predict(self, user_id):
        if self.user_item_matrix is None or self.user_similarity_matrix is None:
            raise ValueError("Model not trained yet.")
        return self.user_similarity_matrix.dot(self.user_item_matrix.loc[user_id])

    def recommend_top_items(self, user_id, n=10):
        if self.user_item_matrix is None or self.user_similarity_matrix is None:
            raise ValueError("Model not trained yet.")

        predictions = self.predict(user_id)
        top_indices = np.argsort(predictions)[::-1][:n]
        return top_indices

