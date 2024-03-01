import spacy
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

def clean_text(whole_review_data):
    """
    Clean the text data by removing stop words and converting to 
    lowercase.

    Parameters:
    - whole_review_data: list of raw review strings

    Returns:
    - cleaned_reviews: dictionary of raw review strings mapped to 
    cleaned strings
    """
    cleaned_reviews = {}
    for review in whole_review_data:
        doc = nlp(review)
        cleaned_text = ' '.join([token.text.lower() for token in doc if
                                 not token.is_stop])
        cleaned_reviews[review] = cleaned_text
    return cleaned_reviews


def sentiment_analysis(cleaned_data):
    """
    Perform sentiment analysis on cleaned review data.

    Parameters:
    - cleaned_data: dictionary of raw review strings mapped to cleaned 
    strings

    Returns:
    - results: list of dictionaries containing review and sentiment 
    score
    """
    results = []
    for key, value in cleaned_data.items():
        doc = nlp(value)
        sentiment = doc._.polarity
        results.append({"Review": key, "Sentiment": sentiment})
    return results


def compare_reviews(reviews_data):
    """
    Compare similarity between pairs of reviews.

    Parameters:
    - reviews_data: list of review strings

    Prints:
    - Similarity score between each pair of reviews
    """
    for i in range(len(reviews_data)):
        for j in range(i+1, len(reviews_data)):
            doc1 = nlp(reviews_data[i])
            doc2 = nlp(reviews_data[j])
            similarity_score = doc1.similarity(doc2)

            print(f"\nReview 1: {reviews_data[i]}")
            print(f"Review 2: {reviews_data[j]}")
            print(f"Similarity Score: {similarity_score}")


if __name__ == "__main__":
    # Load Amazon data
    amazon_data = pd.read_csv("amazon_product_reviews.csv", 
                              low_memory=False)
    amazon_data = amazon_data.dropna(subset=['reviews.text'])

    # Select sample reviews
    reviews_data = amazon_data['reviews.text'].iloc[[0, 24, 43, 437,
                                                     2000, 6000, 9000,
                                                     11501, 13503, 
                                                     17000, 
                                                     25066]].tolist()

    # Clean text and perform sentiment analysis
    cleaned_reviews = clean_text(reviews_data)
    sentiment_results = sentiment_analysis(cleaned_reviews)

    # Print sentiment analysis results
    for result in sentiment_results:
        sentiment = result['Sentiment']
        sentiment_class = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
        
        print(f"\nReview: {result['Review']}")
        print(f"Sentiment: {sentiment}")
        print(f"Sentiment Class: {sentiment_class}")

    # Compare reviews for similarity
    compare_reviews(reviews_data)
