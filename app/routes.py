from flask import Blueprint

class Planet:
    def __init__(self, id = None, name = None, description = None, moons = None):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons or []

mercury = Planet(self, id, "Mercury", description, moons)