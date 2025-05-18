import matplotlib.pyplot as plt
import numpy as np
from .Planet import Planet

from matplotlib.animation import FuncAnimation

def plot_trajectories(planets:list[Planet])-> None:
    """
    Vykreslí trajektorie planet do grafu.
    Args:
        planets (list[Planeta]): Seznam planet k vykreslení.
    """
    for p in planets:
        traj = np.array(p.trajectory)
        plt.plot(traj[:, 0], traj[:, 1], label=p.name)
        plt.scatter(traj[-1, 0], traj[-1, 1], s=20) 
    
    plt.legend()
    plt.axis("equal")
    plt.title("Trajektorie planet")
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.grid(True)

    plt.show()


def create_animation(planets:list[Planet], interval:float=100, kazdy_krok:int=100)-> FuncAnimation:
    """
    Vytvoří animaci trajektorií planet.
    Args:
        planety (list[Planeta]): Seznam planet k animaci.
        interval (float): Interval mezi snímky v milisekundách.
        kazdy_krok (int): Kolik kroků simulace se má přeskočit mezi snímky.
    Returns:
        FuncAnimation: Animace trajektorií planet.
    """
    num_planet = len(planets)
    num_frames = len(planets[0].trajectory) // kazdy_krok

    traj_x = np.array([[p.trajectory[i * kazdy_krok][0] for i in range(num_frames)] for p in planets])
    traj_y = np.array([[p.trajectory[i * kazdy_krok][1] for i in range(num_frames)] for p in planets])

    trajectories = [np.array(p.trajectory) for p in planets]

    fig, ax = plt.subplots()
    all_x = np.concatenate([traj[:, 0] for traj in trajectories])
    all_y = np.concatenate([traj[:, 1] for traj in trajectories])
    margin_x = (all_x.max() - all_x.min()) * 0.1
    margin_y = (all_y.max() - all_y.min()) * 0.1
    ax.set_xlim(all_x.min() - margin_x, all_x.max() + margin_x)
    ax.set_ylim(all_y.min() - margin_y, all_y.max() + margin_y)

    # barvy
    colors = plt.colormaps.get_cmap("tab10").resampled(num_planet)


    body = [ax.plot([], [], 'o', color=colors(i), label=p.name)[0] for i, p in enumerate(planets)]
    trails = [ax.plot([], [], '-', lw=1, color=colors(i))[0] for i in range(num_planet)]

    ax.legend()

    def init():
        for b, t in zip(body, trails):
            b.set_data([], [])
            t.set_data([], [])
        return body + trails

    def update(frame):
        for i in range(num_planet):
            body[i].set_data(traj_x[i, frame], traj_y[i, frame])
            trails[i].set_data(traj_x[i, :frame+1], traj_y[i, :frame+1])
        return body + trails

    print(f"animuj_planety: {num_frames} frames")
    ani = FuncAnimation(fig, update, frames=num_frames, init_func=init,
                        interval=interval, blit=True)
    return ani
   
def save_animation(animation:FuncAnimation, filename:str="simulation.mp4", fps:int=10, dpi:int=10)-> None:
    """
    Uloží animaci do souboru.
    Args:
        animation (FuncAnimation): Animace k uložení.
        filename (str): Název souboru pro uložení animace.
        fps (int): Počet snímků za sekundu.
        dpi (int): Rozlišení DPI pro uložení animace.
    """
    animation.save(
    filename,
    fps=fps,
    dpi=dpi,
    writer="ffmpeg",
    extra_args=["-preset", "ultrafast"]
    )



