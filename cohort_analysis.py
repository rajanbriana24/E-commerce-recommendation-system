import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_cohort_analysis(df):
    # Convert UNIX timestamp to datetime format
    df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'], unit='s')  # Change 's' to 'ms' if timestamps are in milliseconds

    # Extracting month and year from the 'TIMESTAMP' column
    df['cohort_month'] = df['TIMESTAMP'].dt.to_period('M')
    df['cohort_index'] = (df['TIMESTAMP'] - df.groupby('USERID')['TIMESTAMP'].transform('min'))

    # Convert cohort_index to months
    df['cohort_index'] = (df['cohort_index'].dt.days // 30)  # assuming 30 days per month

    # Cohort retention analysis
    cohort_pivot_retention = pd.pivot_table(df, index='cohort_month', columns='cohort_index', values='USERID', aggfunc=pd.Series.nunique)
    cohort_size = cohort_pivot_retention.iloc[:,0]
    retention_matrix = cohort_pivot_retention.divide(cohort_size, axis=0)

    # Plot cohort retention analysis
    plt.figure(figsize=(14, 5))
    plt.subplot(1, 2, 1)
    plt.title('Cohort Analysis - User Retention')
    sns.heatmap(data=retention_matrix, annot=True, fmt='.0%', cmap='Blues')
    plt.xlabel('Cohort Index')
    plt.ylabel('Cohort Month')

    # Cohort behavior analysis
    cohort_pivot_avg_rating = pd.pivot_table(df, index='cohort_month', columns='cohort_index', values='RATING', aggfunc='mean')

    # Plot cohort behavior analysis
    plt.subplot(1, 2, 2)
    plt.title('Cohort Analysis - Average Rating')
    sns.heatmap(data=cohort_pivot_avg_rating, annot=True, cmap='YlGnBu')
    plt.xlabel('Cohort Index')
    plt.ylabel('Cohort Month')

    plt.tight_layout()
    plt.show()
