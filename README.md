📈 Nova Financial Solutions – Financial News Sentiment Analysis
🧠 Objective
This project by Nova Financial Solutions explores how financial news sentiment correlates with market movements. We use NLP, time series analysis, and publisher behavior tracking to identify impactful trends that inform better trading strategies and insights.

📂 Project Structure
bash
Copy
Edit
├── .vscode/                     # VSCode configuration
│   └── settings.json
├── .github/                    # GitHub Actions CI/CD config
│   └── workflows/
│       └── unittests.yml       # Automated testing with pytest
├── .gitignore                  # Ignored files/folders
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview (this file)
├── src/                        # Core Python source code
│   └── __init__.py
├── notebooks/                  # Jupyter Notebooks for EDA & modeling
│   ├── __init__.py
│   └── README.md
├── tests/                      # Unit test cases for validation
│   └── __init__.py
└── scripts/                    # Utility or pipeline scripts
    ├── __init__.py
    └── README.md
🔍 Key Features
📊 Sentiment Analysis
Classifies headline sentiments (positive, negative, neutral, etc.)

Percent breakdown:

🟰 Neutral: 53.54%

👍 Positive: 28.71%

👎 Negative: 14.95%

🚀 Very Positive: 2.23%

⚠️ Very Negative: 0.57%

⏱️ Time Series Trends
Publication frequency over:

Years, Months, Weekdays, Hours

Event-based filtering (e.g., during earnings seasons)

Spike detection for impactful news cycles

🗞️ Publisher & Email Domain Analysis
Top publishing sources by count and type of sentiment

Extracted email domains from publisher names (if available)

Visualized domain contributions (bar charts and percentages)

🧾 Headline Statistics
Basic text metrics: mean, median, and standard deviation of headline length

Tokenization and keyword frequency for financial terms

Common terms: stock, shares, eps, price, estimate, q1-q4

📦 Installation
Clone the repo:

bash
Copy
Edit
git clone https://github.com/yourusername/Nova-Financial-Solutions.git
cd Nova-Financial-Solutions
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
🧪 Testing
Run the unit tests via:

bash
Copy
Edit
pytest
GitHub Actions in .github/workflows/unittests.yml automates testing on push.

🚀 Future Enhancements
Link stock price data with sentiment

Develop ML model to predict price movements

Create real-time dashboard for financial sentiment signals

