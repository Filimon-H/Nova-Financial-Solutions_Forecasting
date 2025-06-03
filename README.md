📈 Nova Financial Solutions – Financial News Sentiment Analysis
This project explores the relationship between financial news sentiment and stock price movements. It combines natural language processing (NLP), time series analysis, and statistical correlation methods to uncover insights that can inform trading strategies and market behavior understanding.

🧠 Project Objectives
Main goals:

Analyze sentiment in financial news headlines.

Match sentiment with corresponding stock market behavior.

Identify meaningful correlations to support investment decisions.

📂 Project Structure
graphql
Copy
Edit
├── .vscode/                     # VSCode configuration
│   └── settings.json
├── .github/                    # CI/CD workflows
│   └── workflows/
│       └── unittests.yml       # GitHub Actions: automated testing
├── data/                       # Raw and processed data (CSV)
│   └── raw_analyst_ratings.csv
│   └── stock_prices/*.csv
├── notebooks/                  # EDA and model experimentation
│   ├── sentiment_analysis.ipynb
│   ├── AAPL_historical_data.ipynb
│   ├── AMZN_historical_data.ipynb
    ├── Correlation Analysis_All.ipynb
    ├── EDA.ipynb
    ├── GOOG_historical_data.ipynb
    ├── META_historical_data.ipynb
    ├── TSLA_historical_data.ipynb
│   └── README.md
├── src/                        # Core modules
│   ├── data_cleaning.py
│   ├── sentiment.py
│   ├── indicators.py
│   └── __init__.py
├── scripts/                    # Utility and analysis scripts
│   └── _init_.py
│   └── article_utils.py
    └── data_cleaning.py
    └── indicators.py
    └── stock_analysis.py
    └── utility.py
    └── visuals.py

├── tests/                      # Unit tests
│   └── test_sentiment.py
│   └── __init__.py
├── requirements.txt            # Python dependencies
└── README.md                   # You're here!
🔍 Key Features
📊 Sentiment Analysis
Extracts and classifies headline sentiment using rule-based NLP tools.

Sentiment class distribution:

🟰 Neutral: 53.54%

👍 Positive: 28.71%

👎 Negative: 14.95%

🚀 Very Positive: 2.23%

⚠️ Very Negative: 0.57%

📈 Time Series Trends
Publication frequency tracked over:

Years, Months, Weekdays, and Hours

Identifies spikes during financial events (e.g., earnings releases)

🗞️ Publisher Insights
Top publishing sources by volume and sentiment type

Domain extraction from publisher info

Publisher-level sentiment trends

🧾 Headline Statistics
Analyzes length, token frequency, and key financial terms

Frequent keywords: stock, EPS, price, estimate, Q1–Q4

⚙️ Data Processing Pipeline
🔄 Data Preparation
Normalize Dates: Ensures consistent date format across datasets

Sentiment Analysis: Applies a simple but robust sentiment scoring system to headlines

📉 Stock Movement Analysis
Compute Daily Returns: Calculates percent change in closing prices

🔗 Correlation Analysis
Aggregate Sentiment: Averages sentiment scores per stock per day

Merge with Returns: Aligns stock return data with sentiment by ticker and date

Calculate Correlation:

Pearson, Spearman, and Kendall coefficients

Heatmaps generated per ticker for visual insight

📦 Installation
bash
Copy
Edit
git clone https://github.com/yourusername/Nova-Financial-Solutions.git
cd Nova-Financial-Solutions
pip install -r requirements.txt
🧪 Running Tests
bash
Copy
Edit
pytest
Automated testing is enabled via GitHub Actions under .github/workflows/unittests.yml.

📊 EDA Highlights
Each notebook walks through:

📅 Time-based sentiment publishing trends

🧮 Sentiment score distribution

📈 Stock return trend analysis

🔗 Correlation between news sentiment and daily returns

🧭 Heatmaps per ticker to visualize sentiment–price relationships

🧠 Observations & Edge Cases
NaN correlations occur when a stock has too few matching news articles (e.g., TSLA, AMZN, AAPL with ≤2 data points).

Missing Stocks (META, MSFT) may be due to:

Lack of matching headlines in the dataset

Errors during data merging or filtering

For robust correlation, a minimum number of valid sentiment-return pairs per ticker is required (we use a threshold of >2).

🙌 Acknowledgments
Project for 10 Acadamy Week 1