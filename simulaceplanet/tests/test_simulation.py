import numpy as np
import pytest
from simulaceplanet.simulation import calculate_gravitational_force, simulate
from simulaceplanet.Planet import Planet


def test_gravitational_force_symmetric():
    p1 = Planet("Earth", np.array([0.0, 0.0]), np.array([0.0, 0.0]), 5.972e24)
    p2 = Planet("Moon", np.array([384400000.0, 0.0]), np.array([0.0, 0.0]), 7.34767309e22)

    f1 = calculate_gravitational_force(p1, p2)
    f2 = calculate_gravitational_force(p2, p1)

    np.testing.assert_allclose(f1, -f2, rtol=1e-5)


def test_simulation_conservation_of_momentum():
    p1 = Planet("A", np.array([0.0, 0.0]), np.array([1.0, 0.0]), 1e5)
    p2 = Planet("B", np.array([1.0, 0.0]), np.array([-1.0, 0.0]), 1e5)
    
    initial_momentum = p1.mass * p1.velocity + p2.mass * p2.velocity
    simulate([p1, p2], dt=0.01, steps=10)
    final_momentum = p1.mass * p1.velocity + p2.mass * p2.velocity

    np.testing.assert_allclose(final_momentum, initial_momentum, rtol=1e-3)


def test_simulate_updates_positions():
    p1 = Planet("Test", np.array([0.0, 0.0]), np.array([1.0, 0.0]), 1.0)
    simulate([p1], dt=1.0, steps=5)
    assert not np.allclose(p1.position, np.array([0.0, 0.0]))
