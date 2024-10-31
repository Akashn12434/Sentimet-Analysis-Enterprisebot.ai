import subprocess

def run_setup_database():
    subprocess.run(["python", "setup_database.py"])  # Adjust the filename if necessary

def run_scraper():
    subprocess.run(["python", "scraper.py"])  # Adjust the filename if necessary

def run_sentiment_analysis():
    subprocess.run(["python", "sentiment_analysis.py"])  # Adjust the filename if necessary

def main():
    run_setup_database()  # Create the database
    run_scraper()        # Scrape reviews and save them to the database
    run_sentiment_analysis()  # Analyze the sentiment of the reviews

if __name__ == "__main__":
    main()  # Execute the main function
