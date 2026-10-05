from flask import Flask, render_template, send_file, redirect
import pandas as pd
import os

app = Flask(__name__)

CSV_FILE = os.path.join("data", "crypto_prices.csv")


@app.route("/")
def home():
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        latest_data = df.tail(10).to_dict(orient="records")

        for coin in latest_data:
            coin["change_value"] = float(
                str(coin["change_24h"]).replace("%", "").strip()
            )
            coin["price_value"] = float(
    str(coin["price"]).replace("$", "").replace(",", "").strip()
)

        if latest_data:
            top_gainer = max(
                latest_data,
                key=lambda x: x["change_value"]
            )
        else:
            top_gainer = None

    else:
        latest_data = []
        top_gainer = None

    return render_template(
        "index.html",
        coins=latest_data,
        top_gainer=top_gainer
    )
@app.route("/update")
def update_data():

    import subprocess
    import sys

    subprocess.run(
        [sys.executable, "live_scraper.py"],
        check=True
    )

    return redirect("/")


@app.route("/download")
def download_csv():

    return send_file(
        CSV_FILE,
        as_attachment=True,
        download_name="crypto_prices.csv"
    )


if __name__ == "__main__":
    app.run(debug=True)