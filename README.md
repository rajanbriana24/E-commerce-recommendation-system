# Recommendation System with Snowflake and PySpark

This project implements a recommendation system using data stored in a Snowflake database. The recommendation system is designed to provide personalized product recommendations to users based on their historical interactions with the platform. The system utilizes collaborative filtering techniques to analyze user-item interactions and make recommendations.

## Project Structure

The project consists of the following files:

1. `data_preprocessing.py`: This file contains functions for preprocessing the raw sales data retrieved from the Snowflake database. The preprocessing steps include data cleaning, handling missing values, and converting timestamps to datetime format.

2. `descriptive_analysis.py`: This file includes functions for conducting descriptive analysis on the sales data. It computes basic statistics of ratings, visualizes the distribution of ratings, and explores patterns in user ratings over time.

3. `exploratory_data_analysis.py`: This file contains functions for performing exploratory data analysis (EDA) on the sales data. It visualizes the relationship between ratings and other variables such as time, product ID, and user ID. It also identifies popular products with the most ratings and highly active users.

4. `time_analysis.py`: This file includes functions for analyzing temporal trends in the sales data. It visualizes how ratings change over time, identifies peak times for ratings, and investigates seasonal trends in ratings.

5. `cohort_analysis.py`: This file contains functions for conducting cohort analysis on the sales data. It transforms the data to create cohorts based on user activity timelines and calculates cohort retention rates and behavior patterns over time.

6. `recommendation_system.py`: This file implements a recommendation system using collaborative filtering techniques. It includes a class `RecommendationSystem` with methods for fitting the model, making predictions, and recommending top items for users.

7. `main.py`: This file serves as the entry point for the project. It imports functions from the other files and orchestrates the execution of the entire pipeline, from data preprocessing to recommendation generation.

## Functions and Business Perspective

1. **Data Preprocessing**:
   - `preprocess_data`: Cleans the raw sales data, handles missing values, and converts timestamps to datetime format. Business Perspective: Ensures the data is clean and formatted correctly for analysis, enabling accurate insights.

2. **Descriptive Analysis**:
   - `compute_basic_statistics`: Computes basic statistics of ratings, such as mean, median, and standard deviation. Business Perspective: Provides insights into the average satisfaction level and variability of opinions among customers.
   - `visualize_rating_distribution`: Visualizes the distribution of ratings using histograms and box plots. Business Perspective: Helps gauge overall satisfaction levels and identify potential trends or issues.
   - `explore_rating_over_time`: Explores how ratings change over time through line plots. Business Perspective: Reveals temporal patterns and trends, informing decisions related to marketing strategies and product offerings.

3. **Exploratory Data Analysis (EDA)**:
   - `visualize_rating_relationship`: Visualizes the relationship between ratings and other variables (time, product ID, user ID). Business Perspective: Offers insights into customer preferences and behavior, guiding decisions on product promotion and customer targeting.
   - `explore_popular_products`: Identifies popular products with the most ratings. Business Perspective: Informs inventory management and marketing efforts, helping capitalize on successful products.
   - `explore_active_users`: Recognizes highly active users to target marketing and engagement strategies effectively. Business Perspective: Leverages user feedback to enhance the overall shopping experience.

4. **Time Analysis**:
   - `analyze_rating_over_time`: Analyzes how ratings change over time (daily, weekly, monthly trends). Business Perspective: Uncovers temporal patterns and trends, aiding in understanding customer behavior shifts and identifying peak periods.
   - `identify_peak_times`: Identifies peak times for ratings to optimize marketing and resource allocation strategies. Business Perspective: Helps understand when customers are most engaged, informing decisions on promotions and customer support.
   - `investigate_seasonal_trends`: Investigates seasonal trends in ratings to tailor strategies to meet seasonal demand effectively. Business Perspective: Recognizes patterns such as sales spikes during holidays to implement targeted marketing strategies.

5. **Cohort Analysis**:
   - `transform_data_to_cohorts`: Converts the data to create cohorts based on user activity timelines. Business Perspective: Segments users into cohorts based on their engagement dates, providing insights into user behavior and retention patterns.
   - `calculate_cohort_retention`: Calculates cohort retention rates and behavior patterns over time. Business Perspective: Helps identify successful user acquisition strategies and assess the effectiveness of retention efforts.

6. **Recommendation System**:
   - `RecommendationSystem`: Implements a recommendation system using collaborative filtering techniques. Methods include fitting the model, making predictions, and recommending top items for users.
   - **Implementation with PySpark**: PySpark, a Python API for Apache Spark, is utilized to build and deploy the recommendation system. PySpark provides a distributed computing framework, enabling efficient processing of large-scale datasets in parallel.
   - **Collaborative Filtering**: The recommendation system employs collaborative filtering techniques to generate personalized recommendations for users. It analyzes user-item interactions to identify patterns and similarities among users.
   - **User-Item Matrix**: Using PySpark, the system constructs a user-item matrix from the input data. Each row of the matrix represents a user, each column represents an item, and the cells contain the corresponding ratings. PySpark's DataFrame operations facilitate the transformation of raw data into this structured format.
   - **Similarity Calculation**: PySpark's built-in functions are leveraged to calculate the cosine similarity between users based on their rating patterns. This similarity matrix forms the basis for generating recommendations.
   - **Prediction and Recommendation**: PySpark's distributed computing capabilities enable efficient prediction of ratings for all users and items. By taking a weighted sum of ratings from similar users, recommendations are generated for each user. The system recommends the top-N items with the highest predicted ratings to enhance user experience.
   - **Evaluation Metrics**: The system evaluates its performance using Root Mean Square Error (RMSE) and Mean Absolute Error (MAE). PySpark facilitates efficient computation of these metrics, enabling model validation and refinement.



## Running the Project

To run the project, follow these steps:

1. Install the required dependencies listed in `requirements.txt`.
2. Execute the `main.py` script to orchestrate the execution of the entire pipeline.
3. View the generated outputs and visualizations in the respective files.

## Conclusion

The recommendation system implemented in this project leverages Snowflake data and collaborative filtering techniques to provide personalized product recommendations to users. By analyzing user-item interactions and exploring temporal patterns in the data, the system offers valuable insights for businesses to enhance customer satisfaction, optimize marketing strategies, and drive growth.
