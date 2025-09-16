import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
shoa_zamin = 6371
def daraj_be_radian(daraj):
    return daraj * (np.pi / 180)
def arz_be_phi(arz):
    if arz >= 0:  # شمالی
        return 90 - arz
    else:  # جنوبی
        return 90 + abs(arz)
def tool_be_theta(tool):
    if tool >= 0:  # شرقی
        return tool
    else:  # غربی
        return 360 + tool
def mohasebe_mokhtasat_koore(arz, tool):
    phi = daraj_be_radian(arz_be_phi(arz))
    theta = daraj_be_radian(tool_be_theta(tool))
    x = shoa_zamin * np.sin(phi) * np.cos(theta)
    y = shoa_zamin * np.sin(phi) * np.sin(theta)
    z = shoa_zamin * np.cos(phi)
    return x, y, z
def rass_kore(ax):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = shoa_zamin * np.outer(np.cos(u), np.sin(v))
    y = shoa_zamin * np.outer(np.sin(u), np.sin(v))
    z = shoa_zamin * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='b', alpha=0.1)
def matris_dorani(mehvar, theta):
    mehvar = mehvar / np.linalg.norm(mehvar)
    a = np.cos(theta / 2)
    b, c, d = -mehvar * np.sin(theta / 2)
    return np.array([
        [a*a + b*b - c*c - d*d, 2*(b*c - a*d), 2*(b*d + a*c)],
        [2*(b*c + a*d), a*a + c*c - b*b - d*d, 2*(c*d - a*b)],
        [2*(b*d - a*c), 2*(c*d + a*b), a*a + d*d - b*b - c*c]
    ])
def rass_dayere_bozorg(ax, vec1, vec2):
    normal_vector = np.cross(vec1, vec2)
    normal_vector = normal_vector / np.linalg.norm(normal_vector)
    mehvar = np.cross([0, 0, 1], normal_vector)
    mehvar = mehvar / np.linalg.norm(mehvar)
    theta = np.arccos(np.dot([0, 0, 1], normal_vector))
    rot_matrix = matris_dorani(mehvar, theta)
    t = np.linspace(0, 2 * np.pi, 100)
    noghat_dayere = np.array([shoa_zamin * np.cos(t), shoa_zamin * np.sin(t), np.zeros_like(t)])

    noghat_rot = np.dot(rot_matrix, noghat_dayere)

    ax.plot(noghat_rot[0], noghat_rot[1], noghat_rot[2], color='r', linewidth=2)

arz_qom, tool_qom = 34.64, 50.88
arz_toronto, tool_toronto = 43.70, -79.42
qom_x, qom_y, qom_z = mohasebe_mokhtasat_koore(arz_qom, tool_qom)
toronto_x, toronto_y, toronto_z = mohasebe_mokhtasat_koore(arz_toronto, tool_toronto)
qom_vec = np.array([qom_x, qom_y, qom_z])
toronto_vec = np.array([toronto_x, toronto_y, toronto_z])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
rass_kore(ax)
ax.scatter(qom_vec[0], qom_vec[1], qom_vec[2], color='g', s=100, label='Qom')
ax.scatter(toronto_vec[0], toronto_vec[1], toronto_vec[2], color='r', s=100, label='Toronto')
rass_dayere_bozorg(ax, qom_vec, toronto_vec)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()