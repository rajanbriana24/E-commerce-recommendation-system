import data_preprocessing
import descriptive_analysis
import exploratory_data_analysis
import time_analysis
import cohort_analysis
import recommendation_system

def main():
    # Data Preprocessing
    df = data_preprocessing.preprocess_sales_data()

    # Descriptive Analysis
    basic_stats = descriptive_analysis.compute_basic_statistics(df)
    descriptive_analysis.visualize_rating_distribution(df)
    descriptive_analysis.visualize_rating_over_time(df)

    # Exploratory Data Analysis
    most_rated_products = exploratory_data_analysis.explore_most_rated_products(df)
    most_active_users = exploratory_data_analysis.explore_most_active_users(df)

    # Time Analysis
    time_analysis.analyze_daily_ratings(df)
    peak_times = time_analysis.analyze_peak_times(df)
    time_analysis.analyze_monthly_ratings(df)

    # Cohort Analysis
    cohort_analysis.perform_cohort_analysis(df)

    # Recommendation System
    recommender = recommendation_system.RecommendationSystem()
    recommender.fit(df)

if __name__ == "__main__":
    main()
