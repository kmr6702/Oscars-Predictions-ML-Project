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
sentiment_analysis.ipynb
```

Model 1 is a sentiment analysis model pipeline that uses Rotten Tomatoes reviews and statistics such as the creation date of the review, the rating assigned to it, and whether or not the reviewer was a verified reviewer to predict whether a movie won an Oscar. It uses two models to accomplish this task. The first uses an SVM to assign a sentiment rating from 1 to 5 to a movie based on its Rotten Tomatoes review. The second is a Logistic Regression model that uses the sentiment prediction and other columns from the dataset to classify the movie as an Oscar Winner or not.

**Model 2: An MLP that will predict whether a movie was nominated for Best Picture in the Oscars.**

File: `model2_mlp.ipynb`

This file contains the preprocessing, training, hyperparameter tuning, and evaluation of an MLP predicting whether a movie was nominated for Best Picture. 

**Model 3: A model that will use historical data on Oscar Best Picture nominees and non-nominees to predict whether a movie was nominated for an award in the 2026 Awards Season.**

Location: `oscar_nominee_only_2025.ipynb`

This model uses historical movie data from 2000-2024 in order to predict whether a movie released in 2025 will be nominated for an Oscar Best Picture. It also prints out the top ten movies predicted to be nominated for Best Picture, as well as searching and printing the prediction for the actual nominees for the award. 

Some notes for this model: 
* This model only predicts for eligible movies. The data that the model was trained and tested on only includes movies that are eligible to be nominated for an Oscar; the model itself cannot differentiate between an eligible and non-eligible movie.

**Model 4: A model that will use historical data on Oscar Best Picture nominees and non-nominees to predict whether a movie will be nominated for the 2027 Awards Season.**

Location: `oscar_nominee_only_2026.ipynb`

This model is nearly identical to model 3; it shares all the same preprocessing, with some minor hyperparameter tuning. This model was trained on historical movie data from 2000-2025 and predicts which movies released in 2026 will be nominated to win an Oscar Best Picture. Again, this model prints out the top ten movies with the highest probability of being nominated, and also searches and prints out the probability of movies that the developers think will be nominated.

Some notes on this model:
* The movie data is not complete. Since this model was trained in early November of 2026, not all movies coming in 2026 have been released yet. This might potentially skew the model predictions, as the features IMDb rating and Gross Income are filled with zeros for movies not released yet.
* This model only predicts for eligible movies. The data that the model was trained and tested on only includes movies that are eligible to be nominated for an Oscar; the model itself cannot differentiate between an eligible and non-eligible movie. 
* There is no way to validate the model's predictions. As the Oscars' nominees for Best Picture will not be announced until January of 2027, we cannot confirm that the predicted movies will actually be nominated. 

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
└──essential_movies.csv
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

The first file contains the features used by the MLP to predict whether or not a movie was nominated for an Oscar. The relevant features are:
* Worldwide Revenue
* Domestic Revenue
* Domestic Percent
* Foreign Revenue
* Foreign Percent
* Genres
* Rating
* Vote Count
* Original Language
* Production Countries
* Director
* Duration
* Is Winner

To narrow the dataset, this file only includes movies where the production countries are USA, United Kingdom, or both.

The second file contains all the nominees for Best Picture from 2012 to 2023. It is used in preprocessing to label the films in the first file with their nomination status. These labels are used as the targets. 

**Model 3 Data:** 

Location: `Predict_2025_Data` folder.
```
Predict_2025_Data/
|
├──american_films_2025_final.csv
└──movies_2000_to_2024.csv
```

The features present in the datasets are:
* Title
* Oscar Year
* Opening Month
* Director(s)
* Star(s)
* Production Company
* Award
* Movie Genre
* Domestic Income
* IMDb Rating 

The file `american_films_2025_final.csv` contains the eligible American movies released in 2025. This data was gathered by scraping the Wikipedia page "List of American Films of 2025" using the code from the `wiki_test` folder. This data was supplemented with data from IMDb's website as well as Rotten Tomatoes. This data was used as the test set. 

The file `movies_2000_to_2024.csv` contains a 50/50 split of nominated movies and non-nominated movies from the years 2000 to 2024. This data was used as the training and validation set, with an 80/20 split. 

**Model 3 Data:** 

Location: `Predict_2026_Data` folder.
```
Predict_2026_Data/
|
├──american_films_2026.csv
└──movies_2000_to_2025.csv
```

The features present in the datasets are:
* Title
* Oscar Year
* Opening Month
* Director(s)
* Star(s)
* Production Company
* Award
* Movie Genre
* Domestic Income
* IMDb Rating 

The file `american_films_2026.csv` contains the eligible American movies released in 2026. This data was gathered by scraping the Wikipedia page "List of American Films of 2026" using the code from the `wiki_test` folder. This data was supplemented with data from IMDb's website as well as Rotten Tomatoes. This data was used as the test set. 

The file `movies_2000_to_2025.csv` contains a 50/50 split of nominated movies and non-nominated movies from the years 2000 to 2025. This data was used as the training and validation set, with an 80/20 split. 

### Resources (Resources Folder)
This folder contains the research and notes we used for this project, as well as our final presentation slides.

The following documents contain our research:
```
|
├──96_general_entry_rules.pdf
├──A Practical Guide to Frequency Encoding and Its Impact on Machine Learning _ by Farhan S _ Medium.pdf4
├──Belief in the Machine - Investigating Epistemological Blind Spots of Language Models.pdf
├──Judging facts, judging norms - Training machine learning models to judge humans requires a modified approach to labeling data.pdf
└──Sentiment Analysis Research.pdf
```

Our final slides presentation can be found in the file `FILE`.

