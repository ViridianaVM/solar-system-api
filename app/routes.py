from flask import Blueprint

planets_bp = Blueprint("planet", __name__, url_prefix="/planet")

@planet_bp.route("/planet", methods=["GET"])
def planet():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body

@planet_bp.route("/planet/<id>", methods=["GET"])
def planet():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body

@planet_bp.route("", methods=["POST"])
def planet():
    new_planet = Planet(name = request.get_json(["name"]), description = request.get_json(["description"]))
    db.session.add(new_planet)
    db.session.commit()
    my_beautiful_response_body = {
        "success": True,
        "message": f"Planet {new_planet.name} has been created"
    }, 201
    return my_beautiful_response_body