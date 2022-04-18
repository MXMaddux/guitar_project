from flask import render_template, session, redirect, request, flash
import re
import os
import requests
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message
from flask_app.models.guitar import Guitar


bcrypt = Bcrypt(app)


@app.route("/register", methods=["GET", "POST"])
def register():
    if not User.is_valid(request.form):
        return redirect("/")
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"])
    }
    id = User.save(data)
    if not id:
        flash("Email already taken", "register")
        return redirect("/")
    session['user_id'] = id
    return redirect("/dashboard")


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/login", methods=['POST'])
def login():
    data = {
        "email": request.form['email']
    }
    user = User.get_by_email(data)
    if not user:
        flash("Invalid Email/Password", "login")
        return redirect("/")

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect("/")
    session['user_id'] = user.id
    return redirect('/dashboard')


@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    user = User.get_one(data)
    guitars = Guitar.get_all()
    owner = User.get_one(data)
    return render_template("dashboard.html", user=user, owner=owner, guitars=guitars)


@app.route("/msg_dashboard")
def msg_dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    user = User.get_one(data)
    messages = Message.get_user_messages(data)
    users = User.get_all(data)
    return render_template("msg_dashboard.html", user=user, users=users, messages=messages)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/acoustic')
def acoustic():
    return render_template('acoustic.html')


@app.route('/get_weather', methods=['POST'])
def get_weather():
    zipcode = request.form['zipcode']
    headers = os.environ.get("APIKEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid={headers}"
    response = requests.get(url)
    print(response)
    session['temperature'] = int(
        (response.json()['main']['temp']) - 273.15) * 9 / 5 + 32
    session['humidity'] = response.json()['main']['humidity']
    session['name'] = response.json()['name']

    return redirect("/acoustic")


@app.route("/new/guitar")
def new_guitar():
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id": session['user_id']
    }
    return render_template("new_guitar.html", user=User.get_one(data))


@app.route("/create/guitar", methods=['POST'])
def create():
    if "user_id" not in session:
        return redirect("/logout")
    if not Guitar.validate(request.form):
        return redirect("/create/guitar")
    if request.form['music_style'] == '5' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Epiphone",
            "model": "Les Paul Standard",
            "price": "499",
            "color": "Gold",
            "orientation": "Left",
            "image": "/static/img/guitars_project/epi_lp_gold_starving_left_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '5' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Epiphone",
            "model": "Les Paul Standard",
            "price": "499",
            "color": "Purple",
            "orientation": "Right",
            "image": "/static/img/guitars_project/Epi_lp_purple_starving_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '5' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Epiphone",
            "model": "Les Paul Standard",
            "price": "499",
            "color": "Tobacco Burst",
            "orientation": "Right",
            "image": "/static/img/guitars_project/epi_lp_tobburst_starving_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '5' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Epiphone",
            "model": "Les Paul Standard",
            "price": "499",
            "color": "Vintage Burst",
            "orientation": "Left",
            "image": "/static/img/guitars_project/epi_lp_vintageburst_starving_left_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '5' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Gibson",
            "model": "Les Paul Standard",
            "price": "2499",
            "color": "Amber",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gibson_lp_amber_superstar_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '5' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Gibson",
            "model": "Les Paul Standard",
            "price": "1499",
            "color": "Black",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gibson_lp_black_stud_left_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '5' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Gibson",
            "model": "Les Paul Standard",
            "price": "1499",
            "color": "Blueberry Fade",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gibson_lp_blueberryfade_stud.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '5' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Gibson",
            "model": "Les Paul Standard",
            "price": "2499",
            "color": "Bourbon Burst",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gibson_lp_bourbonburst_superstar.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '5' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Gibson",
            "model": "Les Paul Standard",
            "price": "2499",
            "color": "Green",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gibson_lp_green_superstar.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '5' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Gibson",
            "model": "Les Paul Standard",
            "price": "2499",
            "color": "Teal",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gibson_lp_teal_superstar_left.webp.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '5' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Gibson",
            "model": "Les Paul Standard",
            "price": "1499",
            "color": "Tobacco Burst",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gibson_lp_teal_superstar_left.webp.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '5' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Gibson",
            "model": "Les Paul Standard",
            "price": "1499",
            "color": "Wine",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gibson_lp_teal_superstar_left.webp.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '3' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Jazzmaster",
            "price": "2499",
            "color": "Burst",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_jazz_burst_superstar_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '3' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Jazzmaster",
            "price": "2499",
            "color": "Dark Knight",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_jazz_darkknight_superstar_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '3' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Jazzmaster",
            "price": "1499",
            "color": "Gray",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_jazz_gray_stud_left_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '3' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Jazzmaster",
            "price": "1499",
            "color": "Miami Blue",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_jazz_miami_stud_left_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '3' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Jazzmaster",
            "price": "499",
            "color": "Olympic White",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_jazz_olywhite_starving_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '3' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Jazzmaster",
            "price": "1499",
            "color": "Orange",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_jazz_orange_stud.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '3' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Jazzmaster",
            "price": "499",
            "color": "Silver",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_jazz_silver_starving_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '3' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Jazzmaster",
            "price": "2499",
            "color": "Sunburst",
            "orientation": "Right",
            "image": "static/img/guitars_project/fender_jazz_sunburst_superstar_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '3' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Jazzmaster",
            "price": "499",
            "color": "Surf",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_jazz_surf_starving_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '3' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Jazzmaster",
            "price": "499",
            "color": "Teal",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_jazz_teal_starving_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '3' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Jazzmaster",
            "price": "2499",
            "color": "Teal",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_jazz_teal_superstar.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
    if request.form['music_style'] == '3' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Jazzmaster",
            "price": "1499",
            "color": "Vintage White",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_jazz_vintagewhite_stud_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '6' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Ibanez",
            "model": "GRG",
            "price": "1499",
            "color": "Purple Burst",
            "orientation": "Right",
            "image": "/static/img/guitars_project/ibanez_axion_purpleburst_stud_2.jpg",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '6' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Ibanez",
            "model": "GRG",
            "price": "499",
            "color": "Blue Bomber",
            "orientation": "Left",
            "image": "/static/img/guitars_project/ibanez_grg_blue_starving_left_2.jpg",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '6' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Ibanez",
            "model": "GRG",
            "price": "499",
            "color": "Blue Ombre",
            "orientation": "Right",
            "image": "/static/img/guitars_project/ibanez_grg_blue_starving_left_2.jpg",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '6' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Ibanez",
            "model": "GRG",
            "price": "2499",
            "color": "Brownish Saphorite",
            "orientation": "Left",
            "image": "/static/img/guitars_project/ibanez_grg_brownishsaphorite_superstar_left_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '6' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Ibanez",
            "model": "GRG",
            "price": "499",
            "color": "Charcoal",
            "orientation": "Right",
            "image": "/static/img/guitars_project/ibanez_grg_charcoal_starving_2.jpg",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '6' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Ibanez",
            "model": "GRG",
            "price": "499",
            "color": "Charcoal",
            "orientation": "Left",
            "image": "/static/img/guitars_project/ibanez_grg_charcoal_starving_left_2.jpg",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '6' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Ibanez",
            "model": "GRG",
            "price": "2499",
            "color": "Cosmic Graphite",
            "orientation": "Left",
            "image": "/static/img/guitars_project/ibanez_grg_cosmicgraphite_superstar_left_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '6' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Ibanez",
            "model": "GRG",
            "price": "1499",
            "color": "White",
            "orientation": "Left",
            "image": "/static/img/guitars_project/ibanez_grg_white_stud_left_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '6' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Ibanez",
            "model": "Paul Stanley",
            "price": "1499",
            "color": "Black",
            "orientation": "Left",
            "image": "/static/img/guitars_project/ibanez_paulstanley_stud_left_2.jpg",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '6' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Ibanez",
            "model": "Paul Wagner",
            "price": "1499",
            "color": "White",
            "orientation": "Right",
            "image": "/static/img/guitars_project/ibanez_paulwagner_white_stud_2.jpg",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '6' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Ibanez",
            "model": "Prestige",
            "price": "2499",
            "color": "Sunburst",
            "orientation": "Right",
            "image": "/static/img/guitars_project/ibanez_prestige_sunburst_superstar_2.jpg",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '6' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Ibanez",
            "model": "Satriani",
            "price": "2499",
            "color": "Purple",
            "orientation": "Right",
            "image": "/static/img/guitars_project/ibanez_satriani_purple_superstar.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' or request.form['music_style'] == '10' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Gretsch",
            "model": "G2655T",
            "price": "1499",
            "color": "Brown",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gretsch_G2655T_brown_stud.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' or request.form['music_style'] == '10' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Gretsch",
            "model": "G2655T",
            "price": "499",
            "color": "Cream",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gretsch_G2655T_cream_starve.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' or request.form['music_style'] == '10' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Gretsch",
            "model": "G2655T",
            "price": "1499",
            "color": "Dark Sky Blue",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gretsch_G2655T_darkskyblue_stud_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' or request.form['music_style'] == '10' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Gretsch",
            "model": "G2655T",
            "price": "499",
            "color": "Georgia Green",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gretsch_G2655T_georgiagreen_starve_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' or request.form['music_style'] == '10' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Gretsch",
            "model": "G2655T",
            "price": "499",
            "color": "Green Mist",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gretsch_G2655T_greenmist_starve.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' or request.form['music_style'] == '10' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Gretsch",
            "model": "G2655T",
            "price": "2499",
            "color": "Green Ocean",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gretsch_G2655T_greenocean_superstar_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' or request.form['music_style'] == '10' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Gretsch",
            "model": "G2655T",
            "price": "2499",
            "color": "Orange Stain",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gretsch_G2655T_orangestain_superstar.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' or request.form['music_style'] == '10' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Gretsch",
            "model": "G2655T",
            "price": "1499",
            "color": "Riviera Blue",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gretsch_G2655T_rivierablue_stud.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' or request.form['music_style'] == '10' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Gretsch",
            "model": "G2655T",
            "price": "499",
            "color": "Natural Stain",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gretsch_G2655T_stain_starve_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' or request.form['music_style'] == '10' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Gretsch",
            "model": "G2655T",
            "price": "1499",
            "color": "Streamline Stain",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gretsch_G2655T_streamlinestain_stud_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' or request.form['music_style'] == '10' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Gretsch",
            "model": "G2655T",
            "price": "2499",
            "color": "Torino Green",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gretsch_G2655T_torinogreenplain_superstar_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' or request.form['music_style'] == '10' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Gretsch",
            "model": "G2655T",
            "price": "2499",
            "color": "White",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gretsch_G2655T_white_superstar.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    return redirect("/dashboard")

@app.route("/guitar/<int:id>")
def show_guitar(id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("show_guitar.html", user=User.get_one(user_data), guitar=Guitar.get_one(data))


@app.route("/destroy/guitar/<int:id>")
def destroy(id):
    data = {
        "id": id
    }
    Guitar.destroy(data)
    return redirect("/dashboard")
