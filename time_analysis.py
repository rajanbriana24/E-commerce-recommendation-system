import pandas as pd
import matplotlib.pyplot as plt

def analyze_daily_ratings(df):
    df['date'] = df['TIMESTAMP'].dt.date
    daily_ratings = df.groupby('date')['RATING'].mean()

    plt.figure(figsize=(12, 6))
    daily_ratings.plot()
    plt.title('Daily Average Ratings Over Time')
    plt.xlabel('Date')
    plt.ylabel('Average Rating')
    plt.show()

def analyze_peak_times(df):
    daily_ratings = df.groupby('date')['RATING'].mean()
    peak_times = daily_ratings.idxmax(), daily_ratings.max()
    return peak_times

def analyze_monthly_ratings(df):
    monthly_ratings = df.groupby(df['TIMESTAMP'].dt.to_period('M'))['RATING'].mean()

    plt.figure(figsize=(12, 6))
    monthly_ratings.plot(kind='bar')
    plt.title('Monthly Average Ratings')
    plt.xlabel('Month')
    plt.ylabel('Average Rating')
    plt.show()
