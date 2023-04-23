from flask import Blueprint, jsonify
import uuid

class Planet:
    def __init__(self, id = None, name = None, description = None):
        self.id = uuid.uuid4().int
        self.name = name
        self.description = description

planets = [
    Planet(None, "Mercury", "Fastest and smallest planet, slightly larger than Earth\'s moon."),
    Planet(None, "Venus", "Hottest planet that spins in opposite direction from most planets."),
    Planet(None, "Earth", "Only planet inhabited by living things and with liquid on the surface."),
    Planet(None, "Mars", "Dusty, cold, desert world. Mars used to be wetter and warmer billions of years ago."),
    Planet(None, "Jupiter", "Twice the size of other planets. The Great Red spot is a centuries-old storm larger than Earth."),
    Planet(None, "Saturn", "Complex system of dazzling, icy rings."),
    Planet(None, "Uranus", "Rotates at a nearly 90 degree angle making it appear to spin on its side."),
    Planet(None, "Neptune", "Most distant from the sun. Neptune is dark, cold, and whipped by supersonic winds. First planet located through mathematical calculations.")
]

planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")
@planets_bp.route("", methods = ["GET"])

def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
        }), 200

    return jsonify(planets_response)