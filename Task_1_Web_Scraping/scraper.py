import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"

all_books = []
page_url = BASE_URL

while page_url:

    print(f"Scraping: {page_url}")

    response = requests.get(page_url)
    response.encoding = "utf-8"

    if response.status_code != 200:
        print("Failed to access page")
        break

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find(
            "p", class_="price_color"
        ).text.strip()

        rating = book.find(
            "p", class_="star-rating"
        )["class"][1]

        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        book_url = urljoin(
            page_url,
            book.h3.a["href"]
        )

        all_books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product_URL": book_url
        })

    next_button = soup.find("li", class_="next")

    if next_button:
        next_page = next_button.a["href"]
        page_url = urljoin(page_url, next_page)
    else:
        page_url = None


df = pd.DataFrame(all_books)

print("\nScraping completed!")
print("Total books:", len(df))

print("\nFirst 5 records:")
print(df.head())

df.to_csv("data/books_dataset.csv", index=False, encoding="utf-8-sig")

print("\nDataset saved successfully!")