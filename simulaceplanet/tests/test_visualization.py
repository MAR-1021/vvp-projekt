import pytest
import numpy as np
import matplotlib
matplotlib.use("Agg")  # Nepotřebujeme zobrazovat grafy (pro testy)

from simulaceplanet.Planet import Planet
from simulaceplanet.visualization import plot_trajectories, create_animation, save_animation


@pytest.fixture
def sample_planets():
    p1 = Planet("A", np.array([0.0, 0.0]), np.array([0.0, 0.0]), 1e24)
    p2 = Planet("B", np.array([1.0, 0.0]), np.array([0.0, 0.0]), 1e24)

    for _ in range(10):
        p1.trajectory.append(p1.position + np.random.rand(2))
        p2.trajectory.append(p2.position + np.random.rand(2))

    return [p1, p2]


def test_plot_trajectories_runs_without_error(sample_planets):
    # Jen ověřujeme, že funkce doběhne bez výjimky
    plot_trajectories(sample_planets)


def test_create_animation_returns_animation(sample_planets):
    ani = create_animation(sample_planets, interval=100, kazdy_krok=1)
    assert ani is not None
    assert hasattr(ani, "save")


def test_save_animation_creates_file(tmp_path, sample_planets):
    ani = create_animation(sample_planets, interval=100, kazdy_krok=1)
    output_file = tmp_path / "test_anim.mp4"
    save_animation(ani, filename=str(output_file), fps=5, dpi=100)
    assert output_file.exists()
    assert output_file.stat().st_size > 0
