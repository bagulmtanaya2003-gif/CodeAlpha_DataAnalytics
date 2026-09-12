import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("books_dataset.csv")

# Display basic information
print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())


# Visualization 1: Top 10 Most Expensive Books
df["Price_Value"] = df["Price"].str.replace("£", "", regex=False).astype(float)

top_expensive = df.nlargest(10, "Price_Value")

plt.figure(figsize=(10, 6))
plt.barh(top_expensive["Title"], top_expensive["Price_Value"])

plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


# Visualization 2: Rating Distribution
plt.figure(figsize=(8, 5))

rating_order = ["One", "Two", "Three", "Four", "Five"]

sns.countplot(
    data=df,
    x="Rating",
    order=rating_order
)

plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.show()


# Visualization 3: Availability of Books
availability_counts = df["Availability"].value_counts()

plt.figure(figsize=(7, 5))
availability_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Book Availability")
plt.ylabel("")
plt.tight_layout()
plt.show()


# Visualization 4: Price Distribution
plt.figure(figsize=(9, 5))

sns.histplot(
    df["Price_Value"],
    bins=20,
    kde=True
)

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.show()


# Visualization 5: Average Price by Rating
avg_price = df.groupby("Rating")["Price_Value"].mean()
avg_price = avg_price.reindex(rating_order).dropna()

plt.figure(figsize=(8, 5))
avg_price.plot(kind="bar")

plt.title("Average Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()