from flask import Flask, render_template, request, session, redirect, url_for, flash, Blueprint
from flask_login import LoginManager, login_user, logout_user
from string import punctuation
from passlib.hash import sha256_crypt
from app.extensions import db, login_manager
from app.models import User, Recipe

auth_bp = Blueprint('auth', __name__, template_folder='templates')


@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(user_id)

 


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        details = request.form
        password = details.get('password')
        confirm = details.get('confirm')
        secure_password = sha256_crypt.encrypt(str(password))
        if " " in password:
            flash('There is a space in your password')
            return render_template("register.html","danger")

        if len(password) not in range(5,11):
            flash("Password should be b/w 5 and 10 chars","danger")
            render_template("register.html")

        special_chars=[True for x in password if x in punctuation]
        if len(special_chars)==0:
            flash("Your password should have atleat 1 special char","danger")
            return render_template("auth/register.html")

        nums=any(x.isdigit() for x in password)
        if not nums:
            flash("You should have at least 1 number","danger")
            return render_template("register.html")
        try:
            if password == confirm:
                print('confirm',confirm)
                print('email',request.form.get("email"))
                print('password',request.form.get("password"))
                
                try:
                    user = User(email=str(request.form.get("email")), password=secure_password)
                except Exception as e:
                    print(e)

                db.session.add(user)
                db.session.commit()

                flash("Account Created")
                return redirect(url_for('auth.login'))
            else:
                flash("password does not match","danger")
                return render_template("register.html")
        except Exception as err:
            flash("Please Create Database Manualy As recipedb","danger")
    return render_template("register.html")


@auth_bp.route("/login" , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password2")
        user = User.query.filter_by(email=email).first()
        if user:
            if sha256_crypt.verify(password, user.password):
                login_user(user)
                session['loggedin'] = True
                session['log'] = True
                session['password1'] = user.password
                session['email'] = user.email
            flash("Logged in successfully", "success")
            return redirect(url_for("main.home"))
        else:
            flash("Incorrect username/password","danger")
            return render_template('login.html')          
    return render_template("login.html")


@auth_bp.route('/logout')
def signout():
   session.clear()
   flash("You Are  Logged Successfully","success")
   return render_template("logout.html") 