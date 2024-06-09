from flask import Flask, render_template, request, session, redirect, url_for, flash, Blueprint
from flask_login import logout_user, current_user, login_required
from string import punctuation
from passlib.hash import sha256_crypt
from app.extensions import db, login_manager
from app.models import User, Recipe
import json

main_bp = Blueprint('main', __name__, template_folder='templates')



@main_bp.route("/")
def home():
    return render_template("home.html")   


@main_bp.route("/create" , methods=['GET', 'POST'])
@login_required
def create():
    if request.method == "POST":
        title = request.form.get('title')
        description = request.form.get('description')
        ingredients = request.form.get('ingredients')
        instructions = request.form.get('instructions')
        try:
            recipe = Recipe(title=title, description=description, ingredients=ingredients, instructions=instructions, created_by=current_user.id )
            db.session.add(recipe)
            db.session.commit()
        except Exception as e:
            print(e)
        flash("Recipe Has Been Added Successfully","success")
        return render_template("create.html") 
    return  render_template("create.html")


@main_bp.route('/read',methods=['POST','GET'])
def read():
    if request.method == 'GET':
        recipes = Recipe.query.all()
        print(recipes)
        return render_template('read.html', recipes=recipes)
    else:
        flash("Recipe Not Found","danger")
        return render_template('read.html')  


@main_bp.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST' or request.method == 'GET':
        title = request.form.get('title')
        description = request.form.get('descriptions')
        ingredients = request.form.get('ingredients')
        instructions = request.form.get('instruction')
        recipe = Recipe.query.filter_by(title=title).first()
        if recipe:
            if description:
                recipe.description=description
            if description:
                recipe.ingredients=ingredients
            if description:
                recipe.instructions=instructions   
            db.session.commit()  
            flash("Recipe Has Been Updated Successfully","success")         
        return render_template("update.html")
    return render_template("update.html")    


@main_bp.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        # Expecting the title to be sent in the form data
        title = request.form.get("title")
        if title:
            recipe = Recipe.query.filter_by(title=title).first()
            if recipe:
                # Delete the recipe from the database
                db.session.delete(recipe)
                db.session.commit()
                flash("Recipe has been deleted successfully", "success")
                return redirect(url_for("main.delete"))
            else:
                flash("Recipe not found", "danger")
        else:
            flash("No title provided", "warning")
        return redirect(url_for("main.delete"))
    else:  # For GET requests
        return render_template("delete.html")

                 
 

 
