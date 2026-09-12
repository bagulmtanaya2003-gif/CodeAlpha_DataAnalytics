# ============================================================
# CodeAlpha Data Analytics Internship
# Task 4 - Sentiment Analysis
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud


# ------------------------------------------------------------
# 1. Download VADER Lexicon
# ------------------------------------------------------------

nltk.download("vader_lexicon")


# ------------------------------------------------------------
# 2. Load Dataset
# ------------------------------------------------------------

file_path = "data/amazon_vfl_reviews.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("AMAZON REVIEWS SENTIMENT ANALYSIS")
print("=" * 60)

print("\nDataset loaded successfully!")

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())


# ------------------------------------------------------------
# 3. Dataset Information
# ------------------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Information:")
df.info()


# ------------------------------------------------------------
# 4. Find Review Column
# ------------------------------------------------------------

possible_review_columns = [
    "review",
    "reviews",
    "Review",
    "Reviews",
    "reviewText",
    "Review Text",
    "review_text"
]

review_column = None

for column in possible_review_columns:
    if column in df.columns:
        review_column = column
        break

if review_column is None:
    raise ValueError(
        "Review column not found. Check the column names printed above."
    )

print("\nReview Column Used:", review_column)


# ------------------------------------------------------------
# 5. Clean Review Data
# ------------------------------------------------------------

df = df.dropna(subset=[review_column])

df[review_column] = df[review_column].astype(str)

df = df[df[review_column].str.strip() != ""]

print("\nDataset after cleaning:")
print(df.shape)


# ------------------------------------------------------------
# 6. Initialize Sentiment Analyzer
# ------------------------------------------------------------

sia = SentimentIntensityAnalyzer()


# ------------------------------------------------------------
# 7. Calculate Sentiment Score
# ------------------------------------------------------------

df["Compound_Score"] = df[review_column].apply(
    lambda text: sia.polarity_scores(text)["compound"]
)


# ------------------------------------------------------------
# 8. Classify Sentiment
# ------------------------------------------------------------

def classify_sentiment(score):

    if score >= 0.05:
        return "Positive"

    elif score <= -0.05:
        return "Negative"

    else:
        return "Neutral"


df["Sentiment"] = df["Compound_Score"].apply(
    classify_sentiment
)


# ------------------------------------------------------------
# 9. Sentiment Summary
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("SENTIMENT ANALYSIS RESULTS")
print("=" * 60)

sentiment_counts = df["Sentiment"].value_counts()

print("\nSentiment Counts:")
print(sentiment_counts)

sentiment_percentage = (
    df["Sentiment"].value_counts(normalize=True) * 100
)

print("\nSentiment Percentages:")
print(sentiment_percentage.round(2))


# ------------------------------------------------------------
# 10. Save Processed Dataset
# ------------------------------------------------------------

df.to_csv(
    "data/reviews_with_sentiment.csv",
    index=False
)

print("\nProcessed dataset saved successfully!")


# ------------------------------------------------------------
# 11. Create Results Folder
# ------------------------------------------------------------

import os

os.makedirs("results", exist_ok=True)


# ------------------------------------------------------------
# 12. Sentiment Distribution Bar Chart
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Sentiment"
)

plt.title("Sentiment Distribution of Amazon Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.tight_layout()

plt.savefig(
    "results/sentiment_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# ------------------------------------------------------------
# 13. Sentiment Percentage Pie Chart
# ------------------------------------------------------------

plt.figure(figsize=(7, 7))

plt.pie(
    sentiment_counts,
    labels=sentiment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Percentage Distribution of Sentiments")

plt.tight_layout()

plt.savefig(
    "results/sentiment_percentage.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# ------------------------------------------------------------
# 14. Sentiment Score Distribution
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

sns.histplot(
    df["Compound_Score"],
    bins=30,
    kde=True
)

plt.title("Distribution of Sentiment Scores")
plt.xlabel("Compound Sentiment Score")
plt.ylabel("Number of Reviews")

plt.tight_layout()

plt.savefig(
    "results/sentiment_scores.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# ------------------------------------------------------------
# 15. Word Cloud
# ------------------------------------------------------------

all_reviews = " ".join(
    df[review_column].astype(str)
)

wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color="white",
    stopwords=set()
).generate(all_reviews)


plt.figure(figsize=(12, 6))

plt.imshow(
    wordcloud,
    interpolation="bilinear"
)

plt.axis("off")

plt.title("Most Common Words in Amazon Reviews")

plt.tight_layout()

plt.savefig(
    "results/wordcloud.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# ------------------------------------------------------------
# 16. Business Insights
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

positive_percentage = sentiment_percentage.get(
    "Positive", 0
)

negative_percentage = sentiment_percentage.get(
    "Negative", 0
)

neutral_percentage = sentiment_percentage.get(
    "Neutral", 0
)

print(
    f"\nPositive Reviews: {positive_percentage:.2f}%"
)

print(
    f"Negative Reviews: {negative_percentage:.2f}%"
)

print(
    f"Neutral Reviews: {neutral_percentage:.2f}%"
)


if positive_percentage > negative_percentage:

    print(
        "\nInsight: Positive sentiment is higher than negative sentiment."
    )

else:

    print(
        "\nInsight: Negative sentiment requires attention."
    )


print("\nAll charts saved successfully in the 'results' folder.")

print("\nAnalysis completed successfully!")