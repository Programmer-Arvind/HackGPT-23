from gpt_results import gpt_get

from flask import Flask, render_template, request

travel_comp_app = Flask(__name__)

# Adding post and get methods to the base route
@travel_comp_app.route("/", methods=["POST", "GET"])
def home():
    # If method is post, using gpt_get to get the food list 
    if request.method == "POST":
        common_phrases, common_phrases_eng, tourist_places, place_descs, foods, food_descs = gpt_get(request.form["Destination"])
        # Sending the foods list to the html
        return render_template("Travel_companion_webpage.html", common_phrases=common_phrases,
                               common_phrases_eng=common_phrases_eng, tourist_places=tourist_places,
                               place_descs=place_descs, foods=foods, food_descs=food_descs, )
    else:
        return render_template("Travel_companion_webpage.html")

if __name__ == "__main__":
    travel_comp_app.run(debug=True)
