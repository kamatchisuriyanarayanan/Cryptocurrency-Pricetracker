import csv
import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


CSV_FOLDER = "data"
CSV_FILE = os.path.join(CSV_FOLDER, "crypto_prices.csv")

CMC_URL = "https://coinmarketcap.com/"


def get_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    return driver


def get_live_data():
    driver = get_driver()

    records = []

    try:
        print("\nOpening CoinMarketCap...")
        driver.get(CMC_URL)

        print("Waiting for cryptocurrency data...")
        time.sleep(8)

        rows = driver.find_elements(
            By.CSS_SELECTOR,
            "table tbody tr"
        )

        print(f"Rows found: {len(rows)}")

        for row in rows[:10]:

            try:
                cells = row.find_elements(By.TAG_NAME, "td")

                if len(cells) < 7:
                    continue

                rank = cells[1].text.strip()
                coin = cells[2].text.strip()

                price = cells[3].text.strip()

                change_24h = cells[5].text.strip()

                market_cap = cells[7].text.strip()

                if not rank or not coin:
                    continue

                # Clean coin name
                coin_name = coin.split("\n")[0]

                records.append({
                    "timestamp": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                    "rank": rank,
                    "coin": coin_name,
                    "price": price,
                    "change_24h": change_24h,
                    "market_cap": market_cap
                })

            except Exception as e:
                print("Skipping row:", e)
                continue

    finally:
        driver.quit()

    return records


def save_to_csv(records):

    os.makedirs(CSV_FOLDER, exist_ok=True)

    fields = [
        "timestamp",
        "rank",
        "coin",
        "price",
        "change_24h",
        "market_cap"
    ]

    # If old CoinPaprika CSV exists, append to it.
    file_exists = os.path.exists(CSV_FILE)

    with open(
        CSV_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fields
        )

        if not file_exists:
            writer.writeheader()

        writer.writerows(records)


def main():

    print("\n" + "=" * 80)
    print("     CRYPTOCURRENCY PRICE TRACKER")
    print("     Source: CoinMarketCap")
    print("=" * 80)

    try:

        records = get_live_data()

        if not records:
            print("\nNo cryptocurrency data was found.")
            print(
                "CoinMarketCap may not be accessible "
                "or its page structure may have changed."
            )
            return

        save_to_csv(records)

        print("\nLIVE DATA SUCCESSFULLY FETCHED!")
        print("=" * 80)

        for coin in records:

            print(
                f"{str(coin['rank']):>3} | "
                f"{coin['coin']:<20} | "
                f"{coin['price']:<15} | "
                f"{coin['change_24h']:<10}"
            )

        print("=" * 80)

        print(f"\nTotal coins fetched: {len(records)}")
        print(f"Saved to: {CSV_FILE}")

    except Exception as e:

        print("\nUnable to fetch live data.")
        print("Error:", e)


if __name__ == "__main__":
    main()