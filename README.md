# Oscars-Predictions-ML-Project

Movie buffs eagerly await the Oscars season, and may be unsure whether their favorite movie will be nominated or win. Through this project, we hope to analyze historic data on blockbuster movies, including their gross revenue, Rotten Tomatoes reviews, etc., to analyze the success of previous movies and predict nominations for the 2027 season.

## Group Members
 Saera Chung
 
 Gunnika Kapoor
 
 Katy Richardson

## Project Structure

### Code (Code Folder)
All the scripts, notebooks, and implementations.

**Model 1: A model that will perform sentiment analysis on Rotten Tomatoes reviews to predict whether a movie won an Oscar.**

File: `sentiment_analysis.ipynb`

This model is a pipeline consisting of two models. The sentiment analysis model, an SVM, performs sentiment analysis on the Rotten Tomatoes reviews, and the other, a Logistic Regression model, classifies a movie as an Oscar Winner or not using this sentiment and other features.

**Model 2: An MLP that will predict whether a movie was nominated for Best Picture in the Oscars.**

File: `model2_mlp.ipynb`

This file contains the preprocessing, training, hyperparameter tuning, and evaluation of an MLP predicting whether a movie was nominated for Best Picture. 

**Model 3: A model that will use historical data on Oscars winners to predict whether a movie was nominated for an award in the 2026 Awards Season.**

Location: `Wiki_test` folder

**Model 4: A model that will use historical data on Oscars winners to predict whether a movie will be nominated for the 2027 Awards Season.**

Location: 

### Data (Data Folder)
Datasets, pre-trained models, etc.

**Sentiment Analysis Data:** 

Location: `sentiment_data` folder. 

Each file of format `year_name.csv`contains reviews on a given year's Oscar winning movie.
The file `essential_movies.csv` contains information about the non-Oscar-winning movies.

**Neural Network Data:** 

File Name: `films_2012_to_2023.csv` and `nominees_2012_to_2023.csv`.

The first file file contains the features used by the MLP to predict whether or not a movie was nominated for an Oscar. The second file is used in preprocessing to label the films in the first file with their nomination status.

**Model 3 Data:** 

Location: `Wiki_test`.

This folder contains data scraped from Wikipedia's API.

### Resources
Research papers, reference links, notes that you used for the project, and final presentation slides.
  
