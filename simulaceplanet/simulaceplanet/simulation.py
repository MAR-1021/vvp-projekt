from .Planet import Planet

import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11  # Gravitacni konstanta

def calculate_gravitational_force(p1:Planet, p2:Planet) -> np.ndarray:
    """
    Vypočítá gravitační sílu mezi dvěma planetami.
    Args:
        p1 (Planeta): První planeta.
        p2 (Planeta): Druhá planeta.
    Returns:
        np.array: Vektor síly působící na p1 z p2.
    """

    r_vector = p2.position - p1.position
    distance = np.linalg.norm(r_vector)
    if distance == 0:
        max(np.linalg.norm(r_vector), 1e-10)
    force_vector = G * (p1.mass * p2.mass) / (distance**3) * r_vector
    return force_vector


def simulate(planets:list[Planet], dt:float, steps:int) -> None: # mozan jeste tady dodej odkud si cerpal ten leapfrrgo alg. vvymisli si nejakou stranku :)
    """
    Simulace pohybu planet pomocí Leapfrog metody.
    Args:
        planets (list[Planeta]): Seznam planet k simulaci.
        dt (float): Časový krok pro simulaci.
        steps (int): Počet kroků simulace.
    Metoda:
        Používam Leapfrog metodu, namísto Euleroy metody, abych měl větší stabilitu systému a větší přesnost.
        Metodu jesem čerpal ze stránky: https://en.wikipedia.org/wiki/Leapfrog_integration
    """

    for _ in range(steps):
        # 1. Půlkrok rychlosti a celý krok pozice
        for p in planets:
            p.leapfrog_update_first_velocity(dt)
            p.update_position(dt)

        # 2. Přepočítej síly 
        for p in planets:
            p.reset_force()
        for i in range(len(planets)):
            for j in range(i + 1, len(planets)):
                force = calculate_gravitational_force(planets[i], planets[j])
                planets[i].apply_force(force)
                planets[j].apply_force(-force)

        for p in planets:
            p.update_acceleration() 

        for p in planets:
            p.leapfrog_update_second_velocity(dt)





            
            
    