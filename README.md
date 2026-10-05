 🚀 Cryptocurrency Price Tracker

A Python and Flask-based web application for monitoring cryptocurrency market data through a simple and user-friendly dashboard.

## 📌 Project Overview

The **Cryptocurrency Price Tracker** automates the collection and monitoring of cryptocurrency market information.

The application displays the **Top 10 cryptocurrencies** with their:

- Current Price
- 24-Hour Price Change
- Market Capitalization
- Rank
- Latest Update Time

The collected data is stored in a CSV file and displayed through the **CryptoTrack** web dashboard.

## 🎯 Objectives

- Automate cryptocurrency market data collection
- Monitor the Top 10 cryptocurrencies
- Display current price and 24-hour price changes
- Store timestamped cryptocurrency records
- Provide a simple and user-friendly dashboard
- Allow users to search and filter cryptocurrency data
- Provide CSV download functionality

## ✨ Features

- 📊 Top 10 Cryptocurrency Monitoring
- 💰 Current Price Display
- 📈 24-Hour Price Change
- 💵 Market Capitalization
- 🔍 Cryptocurrency Search
- 🎯 24-Hour Percentage Filter
- 🔄 Fetch Live Data
- 📁 CSV Data Storage
- ⬇️ CSV Download
- 🕒 Timestamped Records
- 📊 Market Performance Display
- 🌙 Dark Dashboard Interface

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| Flask | Backend web framework |
| Pandas | Data processing |
| Requests | Live data collection |
| Selenium | Browser automation |
| HTML | Dashboard structure |
| CSS | Dashboard styling |
| JavaScript | Search and filtering |
| CSV | Data storage |

## 🔄 Project Workflow

```text
Data Source
     ↓
Data Collection
     ↓
Data Processing
     ↓
CSV Storage
     ↓
Flask Backend
     ↓
Web Dashboard
````

## 🏗️ Project Architecture

```text
                Cryptocurrency Data
                        ↓
                live_scraper.py
                        ↓
              crypto_prices.csv
                        ↓
                    app.py
                  Flask Backend
                        ↓
                  index.html
                        ↓
              CryptoTrack Dashboard
```

## 📂 Project Structure

```text
Cryptocurrency/
│
├── app.py
├── live_scraper.py
├── tracker.py
├── requirements.txt
│
├── data/
│   └── crypto_prices.csv
│
└── templates/
    └── index.html
```

## ⚙️ How It Works

### 1. Data Collection

The `live_scraper.py` file collects cryptocurrency market information.

The application collects:

* Cryptocurrency Rank
* Coin Name
* Current Price
* 24-Hour Change
* Market Capitalization
* Timestamp

### 2. Data Storage

The collected information is stored in:

```text
data/crypto_prices.csv
```

The CSV file maintains timestamped cryptocurrency records.

### 3. Backend Processing

The `app.py` file acts as the Flask backend.

It:

* Reads cryptocurrency data from the CSV file
* Processes the latest records
* Identifies the Top Gainer
* Sends the data to the dashboard
* Handles live data refresh
* Provides CSV download

### 4. Dashboard

The `index.html` file provides the frontend dashboard.

The dashboard includes:

* Summary cards
* Search functionality
* 24-hour filters
* Market performance
* Top 10 cryptocurrency table
* Fetch Live Data button
* Download CSV button

## 🚀 Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-LINK>
```

### Step 2: Open the Project

```bash
cd Cryptocurrency
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Scraper

```bash
python live_scraper.py
```

### Step 5: Start the Flask Application

```bash
python app.py
```

### Step 6: Open the Dashboard

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

## 📊 Dashboard Features

### Summary Cards

The dashboard displays:

* **Total Coins**
* **Top Gainer**
* **Highest Price**
* **Latest Update**

### Search

Users can search for a specific cryptocurrency by name.

### 24-Hour Filter

Users can filter cryptocurrencies based on their 24-hour percentage change.

### Market Performance

The dashboard visually displays the 24-hour performance of cryptocurrencies.

### CSV Download

Users can download the stored cryptocurrency data as a CSV file.

## 📁 CSV Data

The CSV file contains the following fields:

```text
Timestamp
Rank
Coin
Price
Change_24h
Market_Cap
```

## 🧪 Testing

The following features were tested:

* Live cryptocurrency data retrieval
* CSV data storage
* Dashboard loading
* Summary cards
* Search functionality
* 24-hour filtering
* Fetch Live Data
* CSV Download
* Market Performance display

All major functional test cases were successfully completed.

## 🔮 Future Enhancements

The project can be further improved by adding:

* 📈 Interactive cryptocurrency charts
* 🔔 Price alerts and notifications
* 💼 Portfolio tracking
* 🗄️ MySQL database integration
* 📊 Moving average and volatility analysis
* ⏱️ Automatic periodic updates
* 👤 User login system
* 📱 Mobile application support
* 🌐 Multiple cryptocurrency data sources

## 👩‍💻 Author

**Kamatchi**

B.Tech – Artificial Intelligence and Data Science

## 📜 License

This project is developed for educational and academic purposes.



