import sqlite3
from textblob import TextBlob

def get_reviews_from_database():
    conn = sqlite3.connect('database.db')  # Connect to the SQLite database
    cursor = conn.cursor()
    
    # Fetch all reviews from the database
    cursor.execute("SELECT review_title, review_text FROM reviews")
    reviews = cursor.fetchall()
    
    conn.close()  # Close the connection
    return reviews

def analyze_sentiment(review_text):
    analysis = TextBlob(review_text)  # Create a TextBlob object
    return analysis.sentiment.polarity  # Return the polarity score

def main():
    reviews = get_reviews_from_database()  # Get reviews from the database
    results = []
    
    for title, text in reviews:
        sentiment_score = analyze_sentiment(text)  # Analyze sentiment
        results.append((title, text, sentiment_score))  # Store results
    
    # Output the results
    for title, text, score in results:
        print(f"Title: {title}, Sentiment Score: {score}")

if __name__ == "__main__":
    main()  # Execute the main function
