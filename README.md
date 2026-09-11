# CodeAlpha Web Scraping Project

## 📚 Books Data Web Scraping Using Python

This project was developed as part of the **CodeAlpha Data Analytics Internship**.

The objective of this project is to collect structured book data from the public website **Books to Scrape** using Python web scraping techniques. The project automatically navigates through multiple pages, extracts relevant information, and stores the collected data in a CSV dataset for further analysis.

---

## 🎯 Project Objective

The main objectives of this project are:

- Extract book information from a public website
- Automate data collection using Python
- Handle website HTML structure using BeautifulSoup
- Implement pagination to scrape multiple pages
- Create a structured dataset using Pandas
- Store the scraped data in CSV format
- Prepare the dataset for future data analysis and visualization

---

## 🌐 Website Used

**Books to Scrape**

https://books.toscrape.com/

Books to Scrape is a public website designed for practicing web scraping and data extraction.

---

## 🛠️ Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- HTML Parsing
- Web Scraping
- Data Collection
- CSV

---

## 📊 Data Collected

The scraper collects the following information for each book:

| Column | Description |
|---|---|
| Title | Name of the book |
| Price | Price of the book |
| Rating | Book rating |
| Availability | Availability status |
| Product_URL | URL of the individual book |

---

## 🔄 Project Workflow

The project follows this workflow:

**Website → Requests → BeautifulSoup → HTML Parsing → Data Extraction → Pagination → Pandas DataFrame → CSV Dataset**

### 1. Send HTTP Request
Python Requests is used to access the website pages.

### 2. Parse HTML
BeautifulSoup is used to parse the HTML content and locate the required elements.

### 3. Extract Book Information
The scraper extracts:

- Book title
- Price
- Rating
- Availability
- Product URL

### 4. Handle Pagination
The scraper automatically identifies the **Next** page and continues scraping until all available pages are processed.

### 5. Create Dataset
All extracted records are stored in a Pandas DataFrame.

### 6. Export Dataset
The final dataset is saved as a CSV file.

---

## 📈 Dataset Summary

The scraper successfully collected data from:

- **50 pages**
- **1,000 books**
- **5 attributes per book**

The final dataset is available in:

```text
data/books_dataset.csv