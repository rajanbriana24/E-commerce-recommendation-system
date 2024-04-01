import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def compute_basic_statistics(df):
    return df['RATING'].describe()

def visualize_rating_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['RATING'], bins=20, kde=True, color='skyblue')
    plt.title('Distribution of Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.show()

def visualize_rating_over_time(df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='TIMESTAMP', y='RATING', data=df)
    plt.title('Distribution of Ratings Over Time')
    plt.xlabel('Time')
    plt.ylabel('Rating')
    plt.show()
