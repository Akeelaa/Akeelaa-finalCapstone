finalCapstone

Description:
This project focuses on sentiment analysis of Amazon product reviews using SpaCy and SpacyTextBlob. It includes functions to clean text data by removing stop words and perform sentiment analysis on the cleaned data. Additionally, it allows for comparing the similarity between pairs of reviews.

Importance:
Understanding sentiment in product reviews is crucial for businesses to gain insights into customer opinions and preferences. This project provides a tool to analyse sentiment scores of Amazon product reviews, helping businesses make data-driven decisions.
________________________________________
Table of Contents

•	Installation

•	Usage

  •	Cleaning Text

  •	Sentiment Analysis

  •	Comparing Reviews

  •	Downloading CSV file

________________________________________
Installation

To use this project locally, follow these steps:
1.	Clone the repository:
git clone https://github.com/Akeelaa/Akeelaa-finalCapstone.git 
2.	Install the required dependencies:
pip install -r requirements.txt 
Usage
________________________________________
Usage

Cleaning Text

To clean the text data, use the clean_text function. Pass a list of raw review strings to get a dictionary of cleaned review strings.

cleaned_reviews = clean_text(whole_review_data) 
________________________________________
Sentiment Analysis

Perform sentiment analysis on the cleaned review data using the sentiment_analysis function. It returns a list of dictionaries containing the review and sentiment score.

sentiment_results = sentiment_analysis(cleaned_data) 
________________________________________
Comparing Reviews

Compare the similarity between pairs of reviews using the compare_reviews function. It prints the similarity score between each pair of reviews.

compare_reviews(reviews_data)
_______________________________________

Downloading CSV

Download the amazon_product_reviews.csv file from the repository. This CSV file contains the sample Amazon product reviews used in this project.

1.	Go to the CSV file in the repository.
   
2.	Click on the "Download" button to save the file to your local machine.

