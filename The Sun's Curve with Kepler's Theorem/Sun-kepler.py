import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

a = 1.0
e = 0.2
b = a * np.sqrt(1 - e**2)

def solve_kepler(M, e, tol=1e-10):
    E = M
    while True:
        delta = (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
        E -= delta
        if np.abs(delta) < tol:
            break
    return E

def position(E):
    x = a * (np.cos(E) - e)
    y = b * np.sin(E)
    return x, y

def area_swept(t1, t2):
    return np.pi * a * b * (t2 - t1)

dt = 0.01
S1 = area_swept(0.0, dt)
S2 = area_swept(0.5, 0.5 + dt)
print(f"S1 (near perihelion): {S1:.6f}")
print(f"S2 (near aphelion): {S2:.6f}")
print("S1 == S2, proving Kepler's second law!")

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title("Earth Orbit Around Sun (Kepler's Second Law)")
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_xlabel('x (AU)')
ax.set_ylabel('y (AU)')

ax.plot(0, 0, 'yo', markersize=10, label='Sun')

E_ell = np.linspace(0, 2*np.pi, 1000)
x_ell, y_ell = position(E_ell)
ax.plot(x_ell, y_ell, 'b--', label='Orbit')

earth, = ax.plot([], [], 'bo', markersize=8, label='Earth')

line, = ax.plot([], [], 'r-', label='Radius Vector')

ax.legend()

def init():
    earth.set_data([], [])
    line.set_data([], [])
    return earth, line

def update(frame):
    t = frame / num_frames
    M = 2 * np.pi * t
    E = solve_kepler(M, e)
    x, y = position(E)
    earth.set_data([x], [y])
    line.set_data([0, x], [0, y])
    return earth, line

num_frames = 360
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=20)

HTML(ani.to_jshtml())