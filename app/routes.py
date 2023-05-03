from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request
import uuid


# class Planet:
#     def __init__(self, id = None, name = None, description = None):
#         self.id = uuid.uuid4().int
#         self.name = name
#         self.description = description

# planets = [
#     Planet(None, "Mercury", "Fastest and smallest planet, slightly larger than Earth\'s moon."),
#     Planet(None, "Venus", "Hottest planet that spins in opposite direction from most planets."),
#     Planet(None, "Earth", "Only planet inhabited by living things and with liquid on the surface."),
#     Planet(None, "Mars", "Dusty, cold, desert world. Mars used to be wetter and warmer billions of years ago."),
#     Planet(None, "Jupiter", "Twice the size of other planets. The Great Red spot is a centuries-old storm larger than Earth."),
#     Planet(None, "Saturn", "Complex system of dazzling, icy rings."),
#     Planet(None, "Uranus", "Rotates at a nearly 90 degree angle making it appear to spin on its side."),
#     Planet(None, "Neptune", "Most distant from the sun. Neptune is dark, cold, and whipped by supersonic winds. First planet located through mathematical calculations.")
# ]

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet id is invalid. {planet_id} is {type(planet_id)}"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"Planet id {planet_id} not found"}, 404))
    
    return planet


planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")

@planets_bp.route("", methods = ["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"]
    )


    db.session.add(new_planet)
    db.session.commit()

    return make_response(
        f'Planet {new_planet.name} successfully created', 201
    )

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]

    db.session.commit()

    return make_response(f'Planet #{planet.id} sucessfully updated', 200)


@planets_bp.route("", methods = ["GET"])
def retrieve_planet():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name = name_query)
    else:
        planets = Planet.query.all()

    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
        })

    return jsonify(planets_response, 200)

@planets_bp.route("/<planet_id>", methods = ["GET"])
def read_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
    }

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")