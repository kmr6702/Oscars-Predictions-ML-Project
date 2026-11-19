# CSCI 635
# Oscars-Predictions-ML-Project

Movie buffs eagerly await the Oscars season, and may be unsure whether their favorite movie will be nominated or win. Through this project, we hope to analyze historic data on blockbuster movies, including their gross revenue, Rotten Tomatoes reviews, etc., to analyze the success of previous movies and predict winners and nominations for previous and future seasons.

## Group Members
 Saera Chung
 
 Gunnika Kapoor
 
 Katy Richardson

## Project Structure

### Code (Code Folder)
As we have four models, we separate our code into four files. Descriptions of the models and their locations are included in this section.

**Model 1: A model that will perform sentiment analysis on Rotten Tomatoes reviews to predict whether a movie won an Oscar.**

Location: 
```
sentiment_analysis.ipyn
```

Model 1 is a sentiment analysis model pipeline that uses Rotten Tomatoes reviews and statistics such as the creation date of the review, the rating assigned to it, and whether or not the reviewer was a verified reviewer to predict whether a movie won an Oscar. It uses two models to accomplish this task. The first uses an SVM to assign a sentiment rating from 1 to 5 to a movie based on its Rotten Tomatoes review. The second is a Logistic Regression model that uses the sentiment prediction and other columns from the dataset to classify the movie as an Oscar Winner or not.

**Model 2: An MLP that will predict whether a movie was nominated for Best Picture in the Oscars.**

File: `model2_mlp.ipynb`

This file contains the preprocessing, training, hyperparameter tuning, and evaluation of an MLP predicting whether a movie was nominated for Best Picture. 

**Model 3: A model that will use historical data on Oscars nominees and non-nominees to predict whether a movie was nominated for an award in the 2026 Awards Season.**

Location: 

**Model 4: A model that will use historical data on Oscars nominees and non-nominees to predict whether a movie will be nominated for the 2027 Awards Season.**

Location: 

**Wikipedia Scraping Code: This code was used to gather data from Wikipedia**

Location: `Wiki_test` folder

```
Wiki_test/
|
├──analyze_wiki.py
├──main.py
├──movies_2000.csv
├──scraper.py
└──txt_to_csv.py
```

This code uses Wikipedia's built-in scraper API to scrape Wikipedia pages that contain information about movies for a specific year. `scraper.py` calls the API, which writes the contents of the Wikipedia page to a JSON file; after that, the JSON file is passed to `analyze_wiki.py`, which rewrites the JSON into a text file. Finally, `txt_csv.py` converts the text file into a CSV file, accounting for differences in how Wikipedia has charts formatted. `main.py` allows the user to select how many pages they want to scrape, and will loop through all of the above functions, with all of the movies being appended to `movies_2000.csv`


### Data (Data Folder)
In this section, we describe the datasets used in each of our models.

**Model 1: Sentiment Analysis Data** 

Location:
```
sentiment_data/
|
├──2000_gladiator_user.csv
├──2001_a_beautiful_mind_user.csv
├──2002_chicago_user.csv
├──2003_the_lord_of_the_rings_the_return_of_the_king_user.csv
├──2004_million_dollar_baby_user.csv
├──2005_crash_user.csv
├──2006_the_departed_user.csv
├──2007_no_country_for_old_men_user.csv
├──2008_slumdog_millionaire_user.csv
├──2009_the_hurt_locker_user.csv
├──2010_the_kings_speech_user.csv
├──2011_the_artist_user.csv
├──2012_Argo_user.csv
├──2013_12_years_a_slave_user.csv
├──2014_birdman_user.csv
├──2015_spotlight_user.csv
├──2016_moonlight_user.csv
├──2017_the_shape_of_water_user.csv
├──2018_green_book_user.csv
├──2019_parasite_user.csv
├──2020_nomadland_user.csv
├──2021_coda_user.csv
├──2022_everything_everywhere_all_at_once_user.csv
├──2023_oppenheimer_user.csv
├──essential_movies.csv
```

Each file of format `year_name.csv` contains reviews on a given year's Oscar-winning movie. The file `essential_movies.csv` contains information about the non-Oscar-winning movies.

We combine the CSVs to create a final dataset consisting of 4800 rows of data. We take 100 reviews from each of the Oscar-winning movies, for a total of 2400 Oscar-winning reviews, and 2400 reviews from the non-Oscar-winning movies. 

From there, we use the following columns in our X and y datasets for each model.

Sentiment Analysis Model (SVM):

- `X = [quote]`
  - This is tokenized and preprocessed appropriately before use by the SVM.
- `y = [rating]`
  - This is processed to convert fractional ratings into integer ratings before use by the SVM.

Classification Model (Logistic Regression):

- `X = [isVerified, isSuperReviewer, hasSpoilers, hasProfanity, score, creationDate, movieTitle, sentiment_classification]`
  - Each column is appropriately preprocessed before use by the Logistic Regression model.
- `y = [oscarWinner]`


**Model 2: Neural Network Data** 

File Name: `films_2012_to_2023.csv` and `nominees_2012_to_2023.csv`.

The first file file contains the features used by the MLP to predict whether or not a movie was nominated for an Oscar. The second file is used in preprocessing to label the films in the first file with their nomination status.

**Model 3 Data:** 

Location: `Wiki_test`.

This folder contains data scraped from Wikipedia's API.

### Resources
Research papers, reference links, notes that you used for the project, and final presentation slides.
  
