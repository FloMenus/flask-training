from flask import Flask, request
import json
from cat_data import cats
from cat_model import Cat
from markupsafe import escape

app= Flask(__name__)

#Get all cats
@app.get("/")
def getCats():
    cats_list = [cat.__dict__ for cat in cats]
    return json.dumps(cats_list), 200

#Get a specific cat by name
@app.get("/cat/<string:name>")
def getCat(name):
    for cat in cats:
        if cat.name == name:
            return json.dumps(cat.__dict__)
    return "Cat not found", 404

#Create a new cat
@app.post("/cat")
def postCat():
    name = request.json["name"]
    color = request.json["color"]
    age = request.json["age"]
    new_cat = Cat(name, color, age)
    cats.append(new_cat)
    return json.dumps(new_cat.__dict__), 201

#Update a cat
@app.put("/cat/<string:name>")
def putCat(name):
    for cat in cats:
        if cat.name == name:
            cat.name = request.json["name"]
            cat.color = request.json["color"]
            cat.age = request.json["age"]
            """ Other method: 
            for (key, value) in request.json.items():
            setattr(cat, key, value)
            """
            return json.dumps(cat.__dict__), 200
    return "Cat not found", 404

#Delete a cat
@app.delete("/cat/<string:name>")
def deleteCat(name):
    for cat in cats:
        if cat.name == name:
            cats.remove(cat)
            return json.dumps(cat.__dict__), 200
    return "Cat not found", 404