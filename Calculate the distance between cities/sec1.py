# Calculate the distance between cities
import math
R = 6371
def deg_to_rad(deg):
    return deg * (math.pi / 180)
def spherical_coordinates(lat, lon):
    lat_rad = deg_to_rad(lat)
    lon_rad = deg_to_rad(lon)

    x = R * math.cos(lat_rad) * math.cos(lon_rad)
    y = R * math.cos(lat_rad) * math.sin(lon_rad)
    z = R * math.sin(lat_rad)
    return x, y, z
def angle_between_vectors(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a ** 2 for a in vec1))
    magnitude2 = math.sqrt(sum(a ** 2 for a in vec2))
    cos_alpha = dot_product / (magnitude1 * magnitude2)
    alpha = math.acos(cos_alpha)
    return alpha
def arc_distance(alpha):
    return R * alpha
lat_qom = 34.64
lon_qom = 50.88
lat_toronto = 43.70
lon_toronto = -79.42
qom_x, qom_y, qom_z = spherical_coordinates(lat_qom, lon_qom)
toronto_x, toronto_y, toronto_z = spherical_coordinates(lat_toronto, lon_toronto)
alpha = angle_between_vectors((qom_x, qom_y, qom_z), (toronto_x, toronto_y, toronto_z))
distance = arc_distance(alpha)
print(f"فاصله بین قم و تورنتو: {distance:.2f} کیلومتر")