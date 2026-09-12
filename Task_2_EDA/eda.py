# ============================================================
# CodeAlpha Data Analytics Internship
# Task 2 - Exploratory Data Analysis (EDA)
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from pathlib import Path


# ============================================================
# 1. FILE PATH SETUP
# ============================================================

# Get the folder where this Python file is located
BASE_DIR = Path(__file__).resolve().parent

# Dataset path
DATA_PATH = BASE_DIR / "data" / "books_dataset.csv"

# Visualization folder path
VISUALIZATION_DIR = BASE_DIR / "visualizations"

# Create visualization folder automatically if it does not exist
VISUALIZATION_DIR.mkdir(exist_ok=True)


# ============================================================
# 2. LOAD DATASET
# ============================================================

df = pd.read_csv(DATA_PATH)

print("\n========== DATASET LOADED ==========")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")


# ============================================================
# 3. MEANINGFUL ANALYSIS QUESTIONS
# ============================================================

print("\n========== ANALYSIS QUESTIONS ==========")

print("1. What is the distribution of book prices?")
print("2. How are book ratings distributed?")
print("3. Is there a relationship between book price and rating?")
print("4. Are there unusually high or low-priced books?")
print("5. Are there missing or duplicate records?")
print("6. What data-quality issues should be addressed?")


# ============================================================
# 4. DATASET STRUCTURE
# ============================================================

print("\n========== DATASET STRUCTURE ==========")

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Information:")
df.info()


# ============================================================
# 5. MISSING VALUE ANALYSIS
# ============================================================

print("\n========== MISSING VALUES ==========")

missing_values = df.isnull().sum()

print(missing_values)

if missing_values.sum() == 0:
    print("\nNo missing values found.")
else:
    print("\nMissing values are present and should be handled.")


# ============================================================
# 6. DUPLICATE ANALYSIS
# ============================================================

print("\n========== DUPLICATE CHECK ==========")

duplicate_rows = df.duplicated().sum()
duplicate_titles = df["Title"].duplicated().sum()

print(f"Duplicate rows: {duplicate_rows}")
print(f"Duplicate titles: {duplicate_titles}")


# ============================================================
# 7. DATA CLEANING
# ============================================================

# Convert Price from string (£51.77) to numeric value
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("£", "", regex=False)
    .astype(float)
)

# Convert Rating from text to numeric values
rating_mapping = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_mapping)


print("\n========== AFTER DATA CLEANING ==========")

print("\nUpdated Data Types:")
print(df.dtypes)

print("\nCleaned Dataset:")
print(df.head())


# ============================================================
# 8. STATISTICAL SUMMARY
# ============================================================

print("\n========== STATISTICAL SUMMARY ==========")

print(df[["Price", "Rating"]].describe())


# ============================================================
# 9. PRICE ANALYSIS
# ============================================================

print("\n========== PRICE ANALYSIS ==========")

minimum_price = df["Price"].min()
maximum_price = df["Price"].max()
average_price = df["Price"].mean()
median_price = df["Price"].median()
std_price = df["Price"].std()

print(f"Minimum Price: £{minimum_price:.2f}")
print(f"Maximum Price: £{maximum_price:.2f}")
print(f"Average Price: £{average_price:.2f}")
print(f"Median Price: £{median_price:.2f}")
print(f"Price Standard Deviation: £{std_price:.2f}")


# ============================================================
# 10. RATING ANALYSIS
# ============================================================

print("\n========== RATING ANALYSIS ==========")

rating_counts = df["Rating"].value_counts().sort_index()

print("\nNumber of Books by Rating:")
print(rating_counts)


# ============================================================
# 11. PRICE VS RATING ANALYSIS
# ============================================================

print("\n========== PRICE VS RATING ==========")

average_price_by_rating = df.groupby("Rating")["Price"].mean()

print("\nAverage Price by Rating:")
print(average_price_by_rating)


# ============================================================
# 12. CORRELATION ANALYSIS
# ============================================================

correlation = df["Price"].corr(df["Rating"])

print(f"\nPearson Correlation: {correlation:.4f}")


# ============================================================
# 13. HYPOTHESIS TESTING
# ============================================================

print("\n========== HYPOTHESIS TESTING ==========")

print("""
Null Hypothesis (H0):
There is no meaningful relationship between book price and rating.

Alternative Hypothesis (H1):
There is a meaningful relationship between book price and rating.
""")

correlation_value, p_value = pearsonr(
    df["Price"],
    df["Rating"]
)

print(f"Correlation: {correlation_value:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("\nResult: Reject H0.")
    print("There is statistically significant evidence of a relationship.")
else:
    print("\nResult: Fail to reject H0.")
    print("There is not enough statistical evidence of a relationship.")


# ============================================================
# 14. OUTLIER DETECTION USING IQR
# ============================================================

print("\n========== OUTLIER DETECTION ==========")

Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["Price"] < lower_bound) |
    (df["Price"] > upper_bound)
]

print(f"Q1: £{Q1:.2f}")
print(f"Q3: £{Q3:.2f}")
print(f"IQR: £{IQR:.2f}")
print(f"Lower Bound: £{lower_bound:.2f}")
print(f"Upper Bound: £{upper_bound:.2f}")
print(f"Number of Price Outliers: {len(outliers)}")


# ============================================================
# 15. VISUALIZATION 1 - PRICE DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

sns.histplot(
    df["Price"],
    bins=20,
    kde=True
)

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    VISUALIZATION_DIR / "price_distribution.png",
    dpi=300
)

plt.show()
plt.close()


# ============================================================
# 16. VISUALIZATION 2 - RATING DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

sns.countplot(
    x="Rating",
    data=df
)

plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    VISUALIZATION_DIR / "rating_distribution.png",
    dpi=300
)

plt.show()
plt.close()


# ============================================================
# 17. VISUALIZATION 3 - PRICE BOXPLOT
# ============================================================

plt.figure(figsize=(10, 6))

sns.boxplot(
    x=df["Price"]
)

plt.title("Book Price Boxplot")
plt.xlabel("Price (£)")

plt.tight_layout()

plt.savefig(
    VISUALIZATION_DIR / "price_boxplot.png",
    dpi=300
)

plt.show()
plt.close()


# ============================================================
# 18. VISUALIZATION 4 - PRICE VS RATING
# ============================================================

plt.figure(figsize=(10, 6))

sns.scatterplot(
    x="Rating",
    y="Price",
    data=df
)

plt.title("Book Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")

plt.tight_layout()

plt.savefig(
    VISUALIZATION_DIR / "price_vs_rating.png",
    dpi=300
)

plt.show()
plt.close()


# ============================================================
# 19. VISUALIZATION 5 - AVERAGE PRICE BY RATING
# ============================================================

plt.figure(figsize=(10, 6))

sns.barplot(
    x=average_price_by_rating.index,
    y=average_price_by_rating.values
)

plt.title("Average Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")

plt.tight_layout()

plt.savefig(
    VISUALIZATION_DIR / "average_price_by_rating.png",
    dpi=300
)

plt.show()
plt.close()


# ============================================================
# 20. DATA QUALITY SUMMARY
# ============================================================

print("\n========== DATA QUALITY SUMMARY ==========")

print(f"Total Records: {len(df)}")
print(f"Missing Values: {df.isnull().sum().sum()}")
print(f"Duplicate Rows: {duplicate_rows}")
print(f"Duplicate Titles: {duplicate_titles}")
print(f"Price Outliers: {len(outliers)}")

if df["Availability"].nunique() == 1:
    print("Availability has only one unique value: In stock")
    print("Therefore, Availability does not provide useful variation for analysis.")


# ============================================================
# 21. KEY INSIGHTS
# ============================================================

print("\n========== KEY INSIGHTS ==========")

print(
    f"1. Book prices range from £{minimum_price:.2f} "
    f"to £{maximum_price:.2f}."
)

print(
    f"2. The average book price is £{average_price:.2f}, "
    f"while the median is £{median_price:.2f}."
)

print(
    f"3. The most common rating is "
    f"{rating_counts.idxmax()} stars with "
    f"{rating_counts.max()} books."
)

print(
    f"4. The correlation between price and rating is "
    f"{correlation:.4f}, indicating a very weak relationship."
)

print(
    f"5. Statistical testing produced a p-value of "
    f"{p_value:.4f}, so there is not enough evidence "
    f"to conclude that price and rating are meaningfully related."
)

print(
    f"6. The dataset contains {len(outliers)} price outliers "
    f"based on the IQR method."
)

print(
    f"7. There are {duplicate_titles} duplicate book titles "
    f"that may require further investigation."
)


# ============================================================
# 22. COMPLETION MESSAGE
# ============================================================

print("\n========== EDA COMPLETED SUCCESSFULLY ==========")

print("All analysis completed successfully.")

print("\nVisualizations saved in:")

print(VISUALIZATION_DIR)

print("\nGenerated files:")
print("- price_distribution.png")
print("- rating_distribution.png")
print("- price_boxplot.png")
print("- price_vs_rating.png")
print("- average_price_by_rating.png")