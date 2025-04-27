import numpy as np
import plotly.graph_objects as go

# --- کره زمین ---
R = 1
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 50)
x = R * np.outer(np.cos(u), np.sin(v))
y = R * np.outer(np.sin(u), np.sin(v))
z = R * np.outer(np.ones(np.size(u)), np.cos(v))

# --- شهرها ---
cities = {
    "قم": (34.64, 50.88),
    "تورنتو": (51.5072, 0.1276)
}

def geo_to_cart(lat, lon):
    lat_rad = np.radians(lat)
    lon_rad = np.radians(lon)
    x = R * np.cos(lat_rad) * np.cos(lon_rad)
    y = R * np.cos(lat_rad) * np.sin(lon_rad)
    z = R * np.sin(lat_rad)
    return np.array([x, y, z])

qom = geo_to_cart(*cities["قم"])
toronto = geo_to_cart(*cities["تورنتو"])

# --- بدست آوردن بردار نرمال صفحه ---
n = np.cross(qom, toronto)
n = n / np.linalg.norm(n)

# --- زاویه و محور دوران  ---
z_axis = np.array([0, 0, 1])
theta = np.arccos(np.dot(z_axis, n))
rotation_axis = np.cross(z_axis, n)
rotation_axis = rotation_axis / np.linalg.norm(rotation_axis)

# --- فرمول ماتریس دوران (Rodrigues) ---
def rotation_matrix(axis, theta):
    x, y, z = axis
    c = np.cos(theta)
    s = np.sin(theta)
    C = 1 - c
    return np.array([
        [x*x*C + c,   x*y*C - z*s, x*z*C + y*s],
        [y*x*C + z*s, y*y*C + c,   y*z*C - x*s],
        [z*x*C - y*s, z*y*C + x*s, z*z*C + c  ]
    ])

rot_mat = rotation_matrix(rotation_axis, theta)

# --- ساخت نقاط روی دایره استوا و چرخش آن ---
t = np.linspace(0, 2*np.pi, 200)
circle = np.array([np.cos(t), np.sin(t), np.zeros_like(t)])
rotated_circle = rot_mat @ circle  # (3, N)

# --- رسم کره و مسیر ---
fig = go.Figure()

fig.add_trace(go.Surface(
    x=x, y=y, z=z,
    surfacecolor=z,
    colorscale=[
        [0, 'rgb(0, 100, 200)'],
        [0.5, 'rgb(0, 150, 250)'],
        [0.5001, 'rgb(50, 180, 80)'],
        [1, 'rgb(50, 150, 50)']
    ],
    showscale=False,
    opacity=0.9
))

fig.add_trace(go.Scatter3d(
    x=rotated_circle[0], y=rotated_circle[1], z=rotated_circle[2],
    mode='lines',
    line=dict(color='red', width=6),
    name='مسیر هوایی عظیم‌الدایره'
))

# --- نشان دادن شهرها ---
for name, coords in cities.items():
    point = geo_to_cart(*coords)
    fig.add_trace(go.Scatter3d(
        x=[point[0]], y=[point[1]], z=[point[2]],
        mode='markers+text',
        marker=dict(size=6, color='yellow'),
        text=name,
        textposition="top center",
        name=name
    ))

# --- تنظیمات نهایی ---
fig.update_layout(
    title='مسیر کوتاه هوایی  بین قم و تورنتو',
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode='manual',
        aspectratio=dict(x=1, y=1, z=1),
        camera=dict(eye=dict(x=1.5, y=-1.5, z=1))
    ),
    margin=dict(l=0, r=0, b=0, t=40),
    paper_bgcolor='black',
    font=dict(color='white', size=12)
)

fig.show()
