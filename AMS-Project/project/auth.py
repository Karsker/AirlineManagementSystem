from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import Users
import sqlite3

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

connect = sqlite3.connect('./project/Users.db')
#connect.execute('CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,password TEXT NOT NULL,contact TEXT NOT NULL UNIQUE,email TEXT NOT NULL UNIQUE)')
@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('userEmail')
    name = request.form.get('userName')
    password = request.form.get('userPassword')
    contact = request.form.get('userContact')
    with sqlite3.connect("./project/Users.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO Users(name, email, contact, password) values(?,?,?,?)", (name, email, contact, password))
        con.commit()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    return 'Logout'