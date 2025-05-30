# article_utils.py

import pandas as pd
import matplotlib.pyplot as plt

def plot_top_publishers(df: pd.DataFrame, top_n: int = 20):
    """
    Prints and plots the top N publishers by article count.

    Parameters:
    - df (pd.DataFrame): Must contain a 'publisher' column.
    - top_n (int): Number of top publishers to show. Default is 20.
    """
    if 'publisher' not in df.columns:
        raise ValueError("DataFrame must contain a 'publisher' column.")

    # Count articles per publisher
    publisher_counts = df['publisher'].value_counts()

    # Print top publishers
    print(f"📰 Top {top_n} Publishers by Article Count:")
    print(publisher_counts.head(top_n))

    # Plot bar chart
    plt.figure(figsize=(10, 6))
    publisher_counts.head(top_n).plot(kind='bar', color='teal', edgecolor='black')
    plt.title(f"Top {top_n} Most Active Publishers")
    plt.xlabel("Publisher")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
