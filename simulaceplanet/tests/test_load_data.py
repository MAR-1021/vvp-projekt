import pytest
import numpy as np
import json
import os
from simulaceplanet.load_data import load_planets_from_json, generate_random_planets
from simulaceplanet.Planet import Planet


def test_generate_random_planets_count():
    planets = generate_random_planets(5)
    assert len(planets) == 5
    assert all(isinstance(p, Planet) for p in planets)


def test_generate_random_planets_attributes():
    planets = generate_random_planets(3)
    for planet in planets:
        assert planet.position.shape == (2,)
        assert planet.velocity.shape == (2,)
        assert isinstance(planet.mass, float)
        assert planet.mass >= 1e22 and planet.mass <= 1e28


def test_load_planets_from_json(tmp_path):
    data = {
        "Earth": {
            "position": [1.0e11, 0.0],
            "velocity": [0.0, 3e4],
            "mass": 5.972e24
        },
        "Mars": {
            "position": [1.5e11, 0.0],
            "velocity": [0.0, 2.4e4],
            "mass": 6.39e23
        }
    }

    json_file = tmp_path / "planets.json"
    with open(json_file, "w") as f:
        json.dump(data, f)

    planets = load_planets_from_json(str(json_file))

    assert len(planets) == 2
    names = [planet.name for planet in planets]
    assert "Earth" in names and "Mars" in names
    assert np.allclose(planets[0].position, np.array([1.0e11, 0.0]))
    assert np.allclose(planets[1].velocity, np.array([0.0, 2.4e4]))
