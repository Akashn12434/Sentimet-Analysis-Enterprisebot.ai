# Sentiment Analysis Project for Enterprise Bot.ai

This project performs sentiment analysis on Amazon product reviews for the iPhone 12. It scrapes reviews, saves them to a SQLite database, and analyzes their sentiment using TextBlob. The analysis is then accessible via two APIs: one for sentiment analysis and another for review retrieval based on color, storage size, and rating.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [APIs](#apis)
- [Future Improvements](#future-improvements)

---

## Project Overview
This project is broken down into three main steps:

1. **Scraping Amazon Reviews:** Reviews are collected for an iPhone 12 product on Amazon, including details like review title, review text, storage size, color, verified purchase status, and rating. Data is saved in a SQLite database.
   
2. **Sentiment Analysis:** Using TextBlob, we perform sentiment analysis on each review text and save the results.
   
3. **API Endpoints:** The project provides two API endpoints: one to analyze the sentiment of new reviews and another to retrieve reviews based on specific criteria.

## Technologies Used
- **Python Libraries:** Requests, BeautifulSoup, SQLite3, TextBlob, Flask (for APIs)
- **Database:** SQLite
- **Web Scraping:** BeautifulSoup for extracting review data
- **Sentiment Analysis:** TextBlob for polarity-based sentiment scoring

## Project Structure
sentiment_project/

app.py                           # Main application runner

scraper.py                       # Script to scrape reviews from Amazon

sentiment_analysis.py             # Script to perform sentiment analysis on reviews

setup_database.py                # Script to create the SQLite database

database.db                      # SQLite database storing reviews data

README.md                        # Project documentation


## Setup and Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/Akashn12434/Sentimet-Analysis-Enterprisebot.ai.git
    cd Sentimet-Analysis-Enterprisebot.ai
    ```

2. **Install dependencies**:
   - Install the required Python packages:
    ```bash
    pip install requests beautifulsoup4 textblob
    ```

3. **Initialize the Database**:
   - Create the database by running:
    ```bash
    python setup_database.py
    ```

## Running the Application

1. **Scraping Reviews**:
    ```bash
    python scraper.py
    ```
   - This script will scrape reviews from Amazon and store them in `database.db`.

2. **Sentiment Analysis**:
    ```bash
    python sentiment_analysis.py
    ```
   - This script reads reviews from the database and analyzes their sentiment scores using TextBlob.

3. **Running the App**:
   - Execute the main application to automate the entire process:
    ```bash
    python app.py
    ```

## APIs
1. **Sentiment Analysis API**:
   - This API takes a new review and returns the sentiment score.
   
2. **Review Retrieval API**:
   - Given criteria like color, storage size, and rating, this API fetches reviews matching the specified filters.

## Future Improvements
- Use a more advanced sentiment analysis model.
- Implement a web-based interface for users to interact with the APIs.
- Add more filtering options in the review retrieval API.

---

This project demonstrates web scraping, data storage, and sentiment analysis, all tied together through a user-friendly API. Let us know if you encounter issues, or feel free to contribute with improvements!


