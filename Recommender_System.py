# Recommender system

#import pandas library
import pandas as pd

#import library for visualization
import matplotlib.pyplot as plt
import seaborn as sns


#get the data
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
path = 'file.tsv'
df = pd.read_csv(path, sep='\t', names=column_names) 

# Check out all the movies and their respective IDs 
movie_titles = pd.read_csv('Movie_Id_Titles.csv') 

#merge the data on the bases of item_id
data = pd.merge(df, movie_titles, on='item_id') 
# Calculate mean rating of all movies 
#data.groupby('title')['rating'].mean().sort_values(ascending=False).head() 
# Calculate count rating of all movies 
#data.groupby('title')['rating'].count().sort_values(ascending=False).head()

#process the data according the ratings and number of people ratings.
#Makes the data matrix acording to the user's review of every movie.
# creating dataframe with 'rating' count values
ratings = pd.DataFrame(data.groupby('title')['rating'].mean())
ratings['num of ratings'] = data.groupby('title')['rating'].count()
# Convert data table using pivot like : every user give rating every kind of movie.
moviemat = data.pivot_table(index ='user_id', columns ='title', values ='rating')
# Sorting values according to the 'num of rating column'
ratings.sort_values('num of ratings', ascending = False)

# analysing correlation with similar movies
starwars_user_ratings = moviemat['Star Wars (1977)']
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
corr_starwars = pd.DataFrame(similar_to_starwars, columns =['Correlation'])
corr_starwars.dropna(inplace = True)
corr_starwars = corr_starwars.join(ratings['num of ratings'])
r= corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False).head()
print(r)


# analysing correlation with similar movies
liarliar_user_ratings = moviemat['Liar Liar (1997)']
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)
corr_liarliar = pd.DataFrame(similar_to_liarliar, columns =['Correlation'])
corr_liarliar.dropna(inplace = True)
corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
p = corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation', ascending = False).head()
print(p)
