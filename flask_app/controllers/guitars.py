# from flask import Flask, render_template, session,redirect, request,flash
# import re, os, requests
# from flask_bcrypt import Bcrypt
# from flask_app import app
# from flask_app.models.user import User
# from flask_app.models.message import Message
# from flask_app.models.guitar import Guitar

# app = Flask(__name__)
# app.secret_key = "mykey"

# @app.route('/acoustic')
# def acoustic():
#     return render_template('acoustic.html')

# @app.route('/get_weather', methods=['POST'])
# def get_weather():
#     zipcode = request.form['zipcode']
#     headers = os.environ.get("APIKEY")
#     url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid={headers}"
#     response = requests.get(url)
#     print(response)
#     session['temperature'] = int((response.json()['main']['temp']) -273.15) * 9 / 5 + 32
#     session['humidity'] = response.json()['main']['humidity']
#     session['name'] = response.json()['name']

#     return redirect("/acoustic")

# @app.route("/new/guitar")
# def new_guitar():
#     if "user_id" not in session:
#         return redirect("/logout")
#     data = {
#         "id":session['user_id']
#     }
#     return render_template("new_guitar.html", user = User.get_one(data))

# @app.route("/create/guitar", methods =['POST'])
# def create():
#     if "user_id" not in session:
#         return redirect("/logout")
#     if not Guitar.validate(request.form):
#         return redirect("/create/guitar")
#     if request.form['music_style'] == '5' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '2':
#         print("LP")
#         data = {
#             "make": "Epiphone",
#             "model": "Les Paul Standard",
#             "budget": "Starving artist",
#             "looks": "Plain Jane",
#             "orientation": "Left",
#             "user_id": session['user_id']
#         }
#         Guitar.save(data)
#         return redirect("/dashboard")
#     if request.form['music_style'] == '5' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '1':
#         print("LP")
#         data = {
#             "make": "Epiphone",
#             "model": "Les Paul Standard",
#             "budget": "Starving artist",
#             "looks": "Flashy Cathy",
#             "orientation": "Left",
#             "user_id": session['user_id']
#         }
#         Guitar.save(data)
#         return redirect("/dashboard")
#     return redirect("/dashboard")

# @app.route("/guitar/1")
# def show_guitar_1(id):
#     if "user_id" not in session:
#         return redirect("/logout")
#     # data = {
#     #     "id": id
#     # }
#     user_data = {
#         "id": session['user_id']
#     }
#     return render_template(f"show_guitar_{id}.html", user = User.get_one(user_data))

# @app.route("/destroy/guitar/<int:id>")
# def destroy(id):
#     data = {
#         "id": id
#     }
#     Guitar.destroy(data)
#     return redirect("/dashboard")