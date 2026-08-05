#This is a Netflix Data Set Project

#1 Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

#Load the dataset
data = pd.read_csv('netflix_subset.csv')

#Clean Data
data = data.dropna(subset=['cast', 'country', 'date_added', 'rating', 'duration'])

type_counts = data['type'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(type_counts.index, type_counts.values, color=['yellow', 'green'])
plt.title('Distribution of Content Types on Netflix')
plt.xlabel('Content Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()


rating_counts = data['rating'].value_counts()
plt.figure(figsize=(10, 6))
plt.pie(
    rating_counts.values,
    labels=rating_counts.index,
    colors=['skyblue', 'lightgreen', 'orange', 'pink', 'yellow'],
    autopct='%1.1f%%'
)
plt.title('Distribution of Ratings on Netflix')
plt.tight_layout()
plt.show()


movie_data = data[data['type'] == 'Movie']
movie_data['duration'] = movie_data['duration'].str.replace(' min', '').astype(int)
plt.figure(figsize=(10, 6))
plt.hist(movie_data['duration'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Movie Durations on Netflix')
plt.xlabel('Duration (minutes)')
plt.ylabel('Count')
plt.tight_layout()
plt.show()