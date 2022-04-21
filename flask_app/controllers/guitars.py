from flask import Flask, render_template, session, redirect, request, flash
import re
import os
import requests
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message
from flask_app.models.guitar import Guitar

app = Flask(__name__)
app.secret_key = "mykey"

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


@app.route("/destroy/guitar/<int:id>")
def destroy(id):
    data = {
        "id": id
    }
    Guitar.destroy(data)
    return redirect("/dashboard")

@app.route("/create/guitar", methods=['POST'])
def create():
    if "user_id" not in session:
        return redirect("/logout")
    if not Guitar.validate(request.form):
        return redirect("/create/guitar")
    if request.form['music_style'] == '1' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '1':   
        data = {
            "make": "Fender",
            "model": "Stratocaster",
            "price": "499",
            "color": "Aged Cherry",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_strat_agedcherry_starve.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '1' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Stratocaster",
            "price": "499",
            "color": "Black",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_strat_black_starve_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '1' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Stratocaster",
            "price": "1499",
            "color": "Blue Burst",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_strat_blueburst_stud_left_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '1' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Stratocaster",
            "price": "499",
            "color": "Bold Burst",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_strat_boldburst_starve_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '1' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Stratocaster",
            "price": "2499",
            "color": "Honey Burst",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_strat_honeyburst_superstar_2..webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '1' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Stratocaster",
            "price": "2499",
            "color": "Mocha Burst",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_strat_mochaburst_superstar_left_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '1' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Stratocaster",
            "price": "2499",
            "color": "Neon Orange",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_strat_neonorange_superstar_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '1' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Stratocaster",
            "price": "499",
            "color": "Surf Powder",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_strat_surfpowder_starve_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '1' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Stratocaster",
            "price": "1499",
            "color": "Teal",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_strat_teal_stud_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '1' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Stratocaster",
            "price": "2499",
            "color": "Tropical",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_strat_tropical_superstar_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '1' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Stratocaster",
            "price": "1499",
            "color": "White",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_strat_white_stud_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '1' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Stratocaster",
            "price": "1499",
            "color": "White",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_strat_white_stud_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '2' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Telecaster",
            "price": "1499",
            "color": "Black",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_tele_black_stud_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '2' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Telecaster",
            "price": "499",
            "color": "Burst",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_tele_burst_starve_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '2' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Telecaster",
            "price": "499",
            "color": "Butterscotch",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_tele_butterscotch_starve_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '2'and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Telecaster",
            "price": "499",
            "color": "Capri Orange",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_tele_capriorange_starve.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '2' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Telecaster",
            "price": "2499",
            "color": "Flames",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_tele_flames_superstar_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '2' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Telecaster",
            "price": "499",
            "color": "Miami Blue",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_tele_miamiblue_starve_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '2' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Telecaster",
            "price": "1499",
            "color": "Orange",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_tele_orange_stud_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '2' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Telecaster",
            "price": "2499",
            "color": "Polar White",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_tele_polarwhite_superstar_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '2' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Telecaster",
            "price": "2499",
            "color": "Sand",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_tele_sand_superstar_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '2' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Telecaster",
            "price": "1499",
            "color": "Seafoam",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_tele_seafoam_stud_left_2.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '2' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Fender",
            "model": "Telecaster",
            "price": "2499",
            "color": "Surf",
            "orientation": "Left",
            "image": "/static/img/guitars_project/fender_tele_surf_superstar_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '2' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Fender",
            "model": "Telecaster",
            "price": "1499",
            "color": "Tobacco Burst",
            "orientation": "Right",
            "image": "/static/img/guitars_project/fender_tele_tob_burst_stud_2.webp",
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
    if request.form['music_style'] == '4' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "PRS",
            "model": "Custom 24",
            "price": "499",
            "color": "Black/Gold Sunburst",
            "orientation": "Left",
            "image": "/static/img/guitars_project/prs_custom24_ starve_blackgoldsunburst_plain_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '4' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "PRS",
            "model": "Custom 24",
            "price": "499",
            "color": "Faded Blue Burst",
            "orientation": "Left",
            "image": "/static/img/guitars_project/prs_custom24_ starve_fadedblueburst_flash_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '4' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "PRS",
            "model": "Custom 24",
            "price": "1499",
            "color": "Charcoal",
            "orientation": "Left",
            "image": "/static/img/guitars_project/prs_custom24_ stud_charcoal_plain_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '4' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "PRS",
            "model": "Custom 24",
            "price": "1499",
            "color": "Copper With Cherry",
            "orientation": "Left",
            "image": "/static/img/guitars_project/prs_custom24_ stud_copperwithcherry_flash_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '4' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "PRS",
            "model": "Custom 24",
            "price": "2499",
            "color": "Blue Matteo",
            "orientation": "Left",
            "image": "/static/img/guitars_project/prs_custom24_ superstar_bluematteo_flash_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '4' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "PRS",
            "model": "Fiore",
            "price": "2499",
            "color": "Black",
            "orientation": "Left",
            "image": "/static/img/guitars_project/prs_fiore_ superstar_black_plain_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '4' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "PRS",
            "model": "McCarty",
            "price": "2499",
            "color": "Aquamarine",
            "orientation": "Right",
            "image": "/static/img/guitars_project/prs_mccarty_superstar_aquamarine_flash.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '4' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "PRS",
            "model": "McCarty",
            "price": "2499",
            "color": "Gold Top",
            "orientation": "Right",
            "image": "/static/img/guitars_project/prs_mccarty_superstar_goldtop_plain.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '4' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "PRS",
            "model": "SE Custom",
            "price": "499",
            "color": "blue Burst",
            "orientation": "Right",
            "image": "/static/img/guitars_project/prs_secustom_blueburst_starve_flash.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '4' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "PRS",
            "model": "SE Custom",
            "price": "1499",
            "color": "Quilt Charcoal",
            "orientation": "Right",
            "image": "/static/img/guitars_project/prs_secustom_quiltcharcoal_stud_plain.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '4' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "PRS",
            "model": "SE Custom",
            "price": "499",
            "color": "Black/Gold Sunburst",
            "orientation": "Right",
            "image": "/static/img/guitars_project/prs_secustom_starve_blackgoldsunburst_plain.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '4' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "PRS",
            "model": "SE Custom",
            "price": "1499",
            "color": "Eriza Verde",
            "orientation": "Right",
            "image": "/static/img/guitars_project/prs_studio_erizaverde_stud_flash.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
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
            "image": "/static/img/guitars_project/gibson_lp_teal_superstar_left.webp",
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
            "image": "/static/img/guitars_project/gibson_lp_tobburst_stud.webp",
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
            "image": "/static/img/guitars_project/gibson_lp_wine_stud_left_2.webp",
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
    if request.form['music_style'] == '7' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "G & L",
            "model": "Fullerton",
            "price": "499",
            "color": "Alpine White",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gl_starve_alpinewhite_plain_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '7' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "G & L",
            "model": "Fullerton",
            "price": "499",
            "color": "Blue Burst",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gl_starve_blueburst_flash_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '7' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "G & L",
            "model": "Fullerton",
            "price": "499",
            "color": "Lake Placid Blue",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gl_starve_lakeplacidblue_flash.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '7' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "G & L",
            "model": "Fullerton",
            "price": "499",
            "color": "Pharoah Gold",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gl_starve_pharoahgold_plain.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '7' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "G & L",
            "model": "Fullerton",
            "price": "1499",
            "color": "Candy Apple",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gl_stud_candyapple_flash.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '7' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "G & L",
            "model": "Fullerton",
            "price": "1499",
            "color": "Sunburst",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gl_stud_sunburst_plain.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '7' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "G & L",
            "model": "Fullerton",
            "price": "1499",
            "color": "Tangerine Metallic",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gl_stud_tangerine_flash_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '7' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "G & L",
            "model": "Fullerton",
            "price": "1499",
            "color": "Tobacco Burst",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gl_stud_tobaccoburst_plain_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '7' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "G & L",
            "model": "Fullerton",
            "price": "2499",
            "color": "Ruby",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gl_superstar_ruby_flash_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '7' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "G & L",
            "model": "Fullerton",
            "price": "2499",
            "color": "Surf Green",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gl_superstar_surfgreen_flash.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '7' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "G & L",
            "model": "Fullerton",
            "price": "2499",
            "color": "Tobacco Burst",
            "orientation": "Left",
            "image": "/static/img/guitars_project/gl_superstar_tobaccoburst_plain_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '7' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "G & L",
            "model": "Fullerton",
            "price": "2499",
            "color": "Tobacco Burst",
            "orientation": "Right",
            "image": "/static/img/guitars_project/gl_superstar_tobaccoburst_plain.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Danelectro",
            "model": "59 M",
            "price": "499",
            "color": "Black",
            "orientation": "Left",
            "image": "/static/img/guitars_project/danelectro_59M_starve_black_plain_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Danelectro",
            "model": "59 M",
            "price": "499",
            "color": "Copper",
            "orientation": "Left",
            "image": "/static/img/guitars_project/danelectro_59M_starve_copper_flash_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "D'Angelico",
            "model": "Deluxe Bedford",
            "price": "499",
            "color": "Rust",
            "orientation": "Right",
            "image": "/static/img/guitars_project/dangelico_deluxebedford_starve_rust_plain.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "D'Angelico",
            "model": "Deluxe Bedford",
            "price": "499",
            "color": "Sage",
            "orientation": "Right",
            "image": "/static/img/guitars_project/dangelico_deluxebedford_starve_sage_flash.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "D'Angelico",
            "model": "Deluxe Brighton",
            "price": "2499",
            "color": "Desert Gold",
            "orientation": "Right",
            "image": "/static/img/guitars_project/dangelico_deluxebrighton_superstar_desertgold_plain.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "D'Angelico",
            "model": "Bob Weir",
            "price": "1499",
            "color": "Matte Stone",
            "orientation": "Right",
            "image": "/static/img/guitars_project/dangelico_stud_bobweir_mattestone_plain.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "D'Angelico",
            "model": "Deluxe Mini",
            "price": "1499",
            "color": "Blue",
            "orientation": "Right",
            "image": "/static/img/guitars_project/dangelico_stud_deluxemini_blue_flash.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "D'Angelico",
            "model": "Deluxe Brighton",
            "price": "2499",
            "color": "Sapphire",
            "orientation": "Right",
            "image": "/static/img/guitars_project/dangelico_superstar_deluxebrighton_sapphire_flash.webp.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Heritage",
            "model": "H-535",
            "price": "2499",
            "color": "Sunburst",
            "orientation": "Left",
            "image": "/static/img/guitars_project/heritage_h535_superstar_sunburst_plain_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Strandberg",
            "model": "Salen",
            "price": "2499",
            "color": "Burgundy",
            "orientation": "Left",
            "image": "/static/img/guitars_project/strandberg_salen_burgundy_flash_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "PRS",
            "model": "Zach Myers",
            "price": "1499",
            "color": "Myers Blue",
            "orientation": "Left",
            "image": "/static/img/guitars_project/prs_zachmeyers_myersblue_stud_flash_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '8' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Sire",
            "model": "Larry Carlton",
            "price": "1499",
            "color": "Black",
            "orientation": "Left",
            "image": "/static/img/guitars_project/sire_larrycarlton_black_plain_stud_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '9' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Schechter",
            "model": "C1-E",
            "price": "2499",
            "color": "Cat's Eye",
            "orientation": "Right",
            "image": "/static/img/guitars_project/schechter_c1e_catseye_superstar_flash.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '9' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Schechter",
            "model": "C1-E",
            "price": "2499",
            "color": "Black Fade",
            "orientation": "Left",
            "image": "/static/img/guitars_project/schechter_c1slselite_blackfade_superstar_plain_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '9' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Schechter",
            "model": "E1-FR",
            "price": "2499",
            "color": "Purple Burst",
            "orientation": "Left",
            "image": "/static/img/guitars_project/schechter_e1fr_purpleburst_.superstar_flash_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '9' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Schechter",
            "model": "Evil Twin",
            "price": "1499",
            "color": "Black",
            "orientation": "Left",
            "image": "/static/img/guitars_project/schechter_eviltwin_black_.stud_plain_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '9' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '2':
        data = {
            "make": "Schechter",
            "model": "Hellraiser",
            "price": "499",
            "color": "White",
            "orientation": "Left",
            "image": "/static/img/guitars_project/schechter_hellraiser_white_.starve_plain_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '9' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Schechter",
            "model": "Nick Johnson",
            "price": "499",
            "color": "Atomic Coral",
            "orientation": "Left",
            "image": "/static/img/guitars_project/schechter_nickjohnson_atomiccoral_.starve_flash_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '9' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '2':
        data = {
            "make": "Schechter",
            "model": "Solo II",
            "price": "1499",
            "color": "Nuclear Wood",
            "orientation": "Left",
            "image": "/static/img/guitars_project/schechter_soloii_nuclearwood_.stud_flash_left.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '9' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Schechter",
            "model": "Solo II",
            "price": "2499",
            "color": "Blackjack",
            "orientation": "Right",
            "image": "/static/img/guitars_project/schecter_soloii_blackjack_superstar_plain.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '9' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Squier",
            "model": "S-Classic Vibe",
            "price": "499",
            "color": "Black",
            "orientation": "Right",
            "image": "/static/img/guitars_project/squier_classicvibe_black_plain_starve.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '9' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '1':
        data = {
            "make": "Squier",
            "model": "Gold Edition",
            "price": "1499",
            "color": "Black",
            "orientation": "Right",
            "image": "/static/img/guitars_project/squier_Goldeditiontele_black_plain_stud.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '9' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Squier",
            "model": "Gold Edition",
            "price": "1499",
            "color": "Teal",
            "orientation": "Right",
            "image": "/static/img/guitars_project/squier_Goldeditiontele_teal_flash_stud.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '9' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '1':
        data = {
            "make": "Squier",
            "model": "Paranormal",
            "price": "499",
            "color": "Mint Green",
            "orientation": "Right",
            "image": "/static/img/guitars_project/squier_paranormal_mintgreen_flash_starve.webp",
            "user_id": session['user_id']
        }
        Guitar.save(data)
        return redirect("/dashboard")
    if request.form['music_style'] == '10' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '1':
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
    if request.form['music_style'] == '10' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '1':
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
    if request.form['music_style'] == '10' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '2':
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
    if request.form['music_style'] == '10' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '2':
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
    if request.form['music_style'] == '10' and request.form['budget'] == '3' and request.form['looks'] == '2' and request.form['orientation'] == '1':
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
    if request.form['music_style'] == '10' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '2':
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
    if request.form['music_style'] == '10' and request.form['budget'] == '1' and request.form['looks'] == '2' and request.form['orientation'] == '1':
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
    if request.form['music_style'] == '10' and request.form['budget'] == '2' and request.form['looks'] == '2' and request.form['orientation'] == '1':
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
    if request.form['music_style'] == '10' and request.form['budget'] == '3' and request.form['looks'] == '1' and request.form['orientation'] == '2':
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
    if request.form['music_style'] == '10' and request.form['budget'] == '2' and request.form['looks'] == '1' and request.form['orientation'] == '2':
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
    if request.form['music_style'] == '10' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '2':
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
    if request.form['music_style'] == '10' and request.form['budget'] == '1' and request.form['looks'] == '1' and request.form['orientation'] == '1':
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