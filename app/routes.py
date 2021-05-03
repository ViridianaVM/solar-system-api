from app import db
from flask import Blueprint
from flask import request, Blueprint, make_response
from .models.planet import Planet


planets_bp = Blueprint("planet", __name__, url_prefix="/planet")

@planets_bp.route("/planet", methods=["GET"])
def get_all_planets():
    planet = Planet.query.all()
    my_beautiful_response_body = planet
    return my_beautiful_response_body

@planets_bp.route("/planet/<id>", methods=["GET"])
def get_one_planet():
    planet = Planet.query.get(id)
    my_beautiful_response_body = planet
    return my_beautiful_response_body

@planets_bp.route("", methods=["POST"])
def make_new_planet():
    req_body = request.get_json()
    new_planet = Planet(name = req_body["name"], description = req_body["description"])
    db.session.add(new_planet)
    db.session.commit()
    my_beautiful_response_body = {
        "success": True,
        "message": f"Planet {new_planet.name} has been created"
    }, 201
    return my_beautiful_response_body

@planets_bp.route("/<id>", methods=["GET", "PUT"])
def update_planet(id):
    old_planet = Planet.query.get(id)

    if request.method == "GET":
        return old_planet.to_json(), 200

    elif request.method == "PUT":
        from_data = request.get_json()

        planet.name = from_data["name"]
        planet.description = from_data["description"]

        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully updated"), 200