# CodeAlpha Task 4 — Sentiment Analysis

## 📌 Project Overview

This project performs sentiment analysis on Amazon product reviews using Natural Language Processing (NLP) techniques.

The reviews are classified into three sentiment categories:

* Positive
* Negative
* Neutral

The project helps understand customer opinions and identify overall sentiment patterns from product reviews.

## 🎯 Objectives

* Analyze customer review text.
* Clean and prepare review data.
* Apply NLP-based sentiment analysis.
* Classify reviews as Positive, Negative, or Neutral.
* Visualize sentiment distribution.
* Identify common words in customer reviews.
* Generate useful business insights.

## 🛠️ Technologies Used

* Python
* Pandas
* NLTK
* VADER Sentiment Analyzer
* Matplotlib
* Seaborn
* WordCloud

## 📂 Project Structure

```text
Task-4-Sentiment-Analysis
│
├── data
│   ├── amazon_vfl_reviews.csv
│   └── reviews_with_sentiment.csv
│
├── sentiment_analysis.py
├── requirements.txt
└── README.md
```

## 🔄 Project Workflow

```text
Amazon Reviews
       ↓
Data Loading
       ↓
Data Cleaning
       ↓
Text Preprocessing
       ↓
VADER Sentiment Analysis
       ↓
Positive / Negative / Neutral
       ↓
Visualization
       ↓
Business Insights
```

## 📊 Analysis Performed

The project performs:

1. Dataset loading and inspection
2. Missing-value checking
3. Review data cleaning
4. Sentiment score calculation
5. Sentiment classification
6. Sentiment distribution analysis
7. Sentiment percentage analysis
8. Sentiment score distribution
9. Word cloud analysis
10. Business insight generation

## 📈 Visualizations

The project generates:

* Sentiment Distribution Bar Chart
* Sentiment Percentage Pie Chart
* Sentiment Score Distribution
* Word Cloud of Common Review Words

## 💡 Business Insights

Sentiment analysis can help businesses:

* Understand customer satisfaction.
* Identify negative customer feedback.
* Monitor overall public opinion.
* Improve products and services.
* Support marketing and product-development decisions.

## ▶️ How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python sentiment_analysis.py
```

## 👩‍💻 Internship

**CodeAlpha Data Analytics Internship**

### Task 4 — Sentiment Analysis

This project was completed as part of the CodeAlpha Data Analytics Internship.
