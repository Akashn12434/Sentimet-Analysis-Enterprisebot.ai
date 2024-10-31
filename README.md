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
