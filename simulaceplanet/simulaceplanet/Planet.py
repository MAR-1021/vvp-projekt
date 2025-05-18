import numpy as np
class Planet:
    """
    Třída reprezentující planetu v simulaci.
    
    Atributy:
        name (str): Název planety.
        position (np.array): Pozice planety v prostoru.
        velocity (np.array): Rychlost planety.
        mass (float): Hmotnost planety.
        acceleration (np.array): Zrychlení planety.
        force (np.array): Gravitační síla působící na planetu.
        trajectory (list): Trajektorie pohybu planety.
    """
    def __init__(self, name:str, position:np.array, velocity:np.array, mass:float)-> None:
        """
        Inicializuje planetu s danými atributy.
        Args:
            name (str): Název planety.
            position (np.array): Pozice planety v prostoru.
            velocity (np.array): Rychlost planety.
            mass (float): Hmotnost planety.
        """
        self.name = name
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.acceleration = np.array([0.0, 0.0])
        self.force = np.array([0.0, 0.0])
        self.trajectory = [position.copy()]

    def apply_force(self, force:np.array)->None:
        """
        Aplikuje sílu na planetu.
        Args:
            force (np.array): Síla, kterou chceme aplikovat na planetu.
        """
        self.force += force

    def update_acceleration(self)-> None:
        """
        Aktualizuje zrychlení planety na základě aplikované síly a hmotnosti.
        """
        self.acceleration = self.force / self.mass

    def reset_force(self)-> None:
        """
        Resetuje sílu na nulu.
        """
        self.force[:] = 0.0
        self.acceleration[:] = 0.0

    def leapfrog_update_first_velocity(self, dt:float)-> None:
        """
        Provádí aktualizaci pozice planety pomocí Leapfrog metody.
        Args:
            dt (float): Časový krok pro aktualizaci.
        """
        self.velocity += 0.5 * self.acceleration * dt

    def update_position(self, dt:float)-> None:
        """
        Aktualizuje pozici planety.
        Args:
            dt (float): Časový krok pro aktualizaci.
        """
        
        self.position += self.velocity * dt
        self.trajectory.append(self.position.copy())
        
        
    def leapfrog_update_second_velocity(self, dt:float)-> None:
        """
        Provádí aktualizaci rychlosti planety pomocí Leapfrog metody.
        Args:
            dt (float): Časový krok pro aktualizaci.
        """
        self.velocity += 0.5 * self.acceleration * dt


