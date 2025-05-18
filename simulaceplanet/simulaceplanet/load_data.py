import json
import numpy as np
from .Planet import Planet


def load_planets_from_json(file_path:str) -> list[Planet]:
    """
    Načte seznam planet z JSON souboru.

    Args:
        file_path (str): Cesta k JSON souboru obsahujícímu informace o planetách.

    Returns:
        list[Planeta]: Seznam načtených planet.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    planets = []
    for name, atributs in data.items():
        position = np.array(atributs['position'], dtype=float)
        velocity = np.array(atributs['velocity'], dtype=float)
        mass = float(atributs['mass'])
        planet = Planet(name, position, velocity, mass)
        planets.append(planet)

    return planets

def generate_random_planets(n:int , position_range: float=1e11, velocity_range:float=1e4, mass_range:tuple[float, float]=(1e22, 1e28))-> list[Planet]:
    """
    Vytvoří několik náhodných planet.
    Args:
        n (int): Počet planet k vytvoření.
        position_range (float): Rozsah pro náhodné pozice planet.
        velocity_range (float): Rozsah pro náhodné rychlosti planet.
        mass_range (tuple[float, float]): Rozsah pro hmotnosti planet.
    Returns:
        list[Planeta]: Seznam náhodně vygenerovaných planet.
    """
    planets = []
    for i in range(n):
        name = f"Planet_{i+1}"
        position = np.random.uniform(-position_range, position_range, size=2)
        velocity = np.random.uniform(-velocity_range, velocity_range, size=2)
        mass = np.random.uniform(mass_range[0], mass_range[1])
        planet = Planet(name, position, velocity, mass)
        planets.append(planet)
    return planets
