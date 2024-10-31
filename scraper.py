import requests
from bs4 import BeautifulSoup
import sqlite3
import re
import time

def save_to_database(data):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.executemany(''' 
        INSERT INTO reviews (review_title, review_text, style_name, color, verified_purchase, rating) 
        VALUES (?, ?, ?, ?, ?, ?) 
        ''', data)
        conn.commit()

def scrape_reviews():
    headers = {
        "User-Agent": "Your Actual User Agent",  # Replace with your actual User Agent
    }
    base_url = "https://www.amazon.in/Apple-New-iPhone-12-128GB/dp/B08L5TNJHG/"
    data = []
    seen_titles = set()  # Initialize an empty set to track seen titles
    
    for page in range(1, 5):  # Scraping multiple pages
        url = f"{base_url}&pageNumber={page}"
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            soup = BeautifulSoup(response.text, "html.parser")

            reviews = soup.find_all("div", {"data-hook": "review"})
            
            for review in reviews:
                title = review.find("a", {"data-hook": "review-title"}).text.strip() if review.find("a", {"data-hook": "review-title"}) else None
                
                if title in seen_titles:  # Check if the title has already been processed
                    continue  # Skip to the next review if it's a duplicate
                
                seen_titles.add(title)  # Add the title to the set of seen titles

                text = review.find("span", {"data-hook": "review-body"}).text.strip() if review.find("span", {"data-hook": "review-body"}) else None
                style = review.find("a", {"data-hook": "format-strip"}).text.strip() if review.find("a", {"data-hook": "format-strip"}) else None
                color = re.search(r"Color Name: (\w+)", style).group(1) if style and "Color Name" in style else None
                verified_purchase = review.find("span", {"data-hook": "avp-badge"}).text.strip() if review.find("span", {"data-hook": "avp-badge"}) else "Not Verified"
                rating = int(float(review.find("i", {"data-hook": "review-star-rating"}).text.split()[0])) if review.find("i", {"data-hook": "review-star-rating"}) else None
                
                data.append((title, text, style, color, verified_purchase, rating))
                
            # Save data after each page
            save_to_database(data)
            data.clear()  # Clear the data list after saving
            
            time.sleep(2)  # Delay to avoid overwhelming the server
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_reviews()  # Start scraping
