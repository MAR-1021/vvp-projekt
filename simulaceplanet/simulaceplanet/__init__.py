"""
Toto je balíček simulace planet

Obsahuje moduly:
- Planet.py - definice třídy Planet
- simulation.py - funkce pro simulaci pohybu planet
- visualization.py - funkce pro vizualizaci trajektorií planet
- load_data.py - funkce pro načítání dat planet z JSON souboru a generování náhodných planet

Pro použití v hlavním skriptu použijte přímo třídy a funkce:
- simulate – spuštění simulace pohybu planet
- load_planets_from_json – načítání počátečních podmínek z JSON
- generate_random_planets – generování náhodných počátečních podmínek
- plot_trajectories – vykreslení trajektorií planet
- create_animation – vytvoření animace trajektorií planet
- save_animation – uložení animace do souboru
"""

from .Planet import Planet
from .simulation import simulate
from .load_data import load_planets_from_json, generate_random_planets
from .visualization import plot_trajectories, create_animation, save_animation

__all__ : list[str] = [
    "Planet",
    "simulate",
    "load_planets_from_json",
    "generate_random_planets",
    "plot_trajectories",
    "save_animation",
    "create_animation",
]
