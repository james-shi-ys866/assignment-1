# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, requests, render_template

cocktail_routes = Blueprint("cocktail_routes", __name__)

@cocktail_routes.route("/cocktails")
def cocktails_list():
    print("COCKTAILS...")

    request_url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic"
    response = requests.get(request_url)
    

    data = response.json()
    

    cocktails = []
    for drink in data["drinks"][:20]:
        cocktail = {
            "name": drink["strDrink"],
            "image": drink["strDrinkThumb"],
            "id": drink["idDrink"]
        }
        cocktails.append(cocktail)


    return render_template("cocktails.html", cocktails=cocktails)