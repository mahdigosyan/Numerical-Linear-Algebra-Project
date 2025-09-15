import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def householder_matrix(v):
    v = np.array(v)
    norm_v = np.linalg.norm(v)
    if norm_v == 0:
        raise ValueError("Vector v cannot be zero!")
    v = v / norm_v  # Normalize v
    H = np.eye(3) - 2 * np.outer(v, v)
    return H

v_input = input("Enter vector v")
v = list(map(float, v_input.split()))
if len(v) != 3:
    raise ValueError("Vector v have 3")

H = householder_matrix(v)

p_input = input("Enter point p")
p = list(map(float, p_input.split()))
if len(p) != 3:
    raise ValueError("Point p have 3!")
p = np.array(p)

p_prime = H @ p

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Householder Reflection in R^3')

ax.scatter(p[0], p[1], p[2], color='blue', s=50, label='p')
ax.scatter(p_prime[0], p_prime[1], p_prime[2], color='red', s=50, label="p' = H p")

ax.plot([p[0], p_prime[0]], [p[1], p_prime[1]], [p[2], p_prime[2]], color='green', linewidth=2, label='Line connecting p and p\'')

v_norm = np.array(v) / np.linalg.norm(v)

if np.abs(v_norm[0]) > 1e-6 or np.abs(v_norm[1]) > 1e-6:
    u1 = np.array([-v_norm[1], v_norm[0], 0])
else:
    u1 = np.array([0, -v_norm[2], v_norm[1]])
u1 /= np.linalg.norm(u1)
u2 = np.cross(v_norm, u1)
u2 /= np.linalg.norm(u2)

s, t = np.meshgrid(np.linspace(-5, 5, 10), np.linspace(-5, 5, 10))
plane_points = s[..., np.newaxis] * u1 + t[..., np.newaxis] * u2

xx = plane_points[..., 0]
yy = plane_points[..., 1]
zz = plane_points[..., 2]

ax.plot_surface(xx, yy, zz, alpha=0.5, color='yellow', label='Reflection Plane')

ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()