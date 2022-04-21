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






