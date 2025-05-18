""" Test pro třídu Planety"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from simulaceplanet import Planet
import numpy as np
import pytest


@pytest.fixture
def default_planet():
    return Planet("Test", np.array([0.0, 0.0]), np.array([1.0, 0.0]), 10.0)

def test_initialization(default_planet):
    assert default_planet.name == "Test"
    assert np.allclose(default_planet.position, [0.0, 0.0])
    assert np.allclose(default_planet.velocity, [1.0, 0.0])
    assert default_planet.mass == 10.0
    assert np.allclose(default_planet.acceleration, [0.0, 0.0])
    assert np.allclose(default_planet.force, [0.0, 0.0])
    assert len(default_planet.trajectory) == 1

def test_apply_force(default_planet):
    force = np.array([2.0, 4.0])
    default_planet.apply_force(force)
    assert np.allclose(default_planet.force, [2.0, 4.0])

def test_update_acceleration(default_planet):
    default_planet.apply_force(np.array([10.0, 0.0]))
    default_planet.update_acceleration()
    assert np.allclose(default_planet.acceleration, [1.0, 0.0])  # F=ma -> a=F/m

def test_reset_force(default_planet):
    default_planet.apply_force(np.array([3.0, 3.0]))
    default_planet.reset_force()
    assert np.allclose(default_planet.force, [0.0, 0.0])
    assert np.allclose(default_planet.acceleration, [0.0, 0.0])

def test_leapfrog_first_velocity(default_planet):
    default_planet.acceleration = np.array([1.0, 0.0])
    default_planet.leapfrog_update_first_velocity(dt=2.0)
    assert np.allclose(default_planet.velocity, [2.0, 0.0])  

def test_update_position(default_planet):
    default_planet.update_position(dt=2.0)
    assert np.allclose(default_planet.position, [2.0, 0.0])
    assert len(default_planet.trajectory) == 2

def test_leapfrog_second_velocity(default_planet):
    default_planet.acceleration = np.array([2.0, 0.0])
    default_planet.leapfrog_update_second_velocity(dt=1.0)
    assert np.allclose(default_planet.velocity, [2.0, 0.0])
