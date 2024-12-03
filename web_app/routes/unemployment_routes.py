# this is the "web_app/routes/unemployment_routes.py" file ...

from flask import Blueprint, render_template, redirect, flash
import requests
import os
from dotenv import load_dotenv

load_dotenv()

unemployment_routes = Blueprint("unemployment_routes", __name__)


@unemployment_routes.route("/unemployment", methods=["GET", "POST"])
def unemployment_dashboard():
    print("UNEMPLOYMENT DASHBOARD...")

    try:
        api_key = os.getenv("ALPHAVANTAGE_API_KEY")
        url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={api_key}"
        response = requests.get(url)
        parsed_response = response.json()

        data = []
        for d in parsed_response["data"]:
            data.append({
                "date": d["date"],
                "value": float(d["value"])
            })

        flash("Fetched Unemployment Data!", "success")
        return render_template("unemployment.html",
            data=data
        )
    except Exception as err:
        print('OOPS', err)

        flash("Unemployment Data Error. Please try again!", "danger")

#
# API ROUTES
#

@unemployment_routes.route("/api/unemployment.json")
def unemployment_api():
    print("UNEMPLOYMENT DATA (API)...")

    try:
        api_key = os.getenv("ALPHAVANTAGE_API_KEY")
        url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={api_key}"
        response = requests.get(url)
        parsed_response = response.json()

        data = []
        for d in parsed_response["data"]:
            data.append({
                "date": d["date"],
                "value": float(d["value"])
            })

        return {"data": data}
    except Exception as err:
        print('OOPS', err)
        return {"message":"Unemployment Data Error. Please try again."}, 404