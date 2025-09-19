import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import requests
from io import BytesIO
from IPython.display import HTML

# Define the function f(x) and its derivative f'(x) - Change these as needed!
def f(x):
    return 10 * np.sin(x / 10) + x / 5  # Example function - you can change this

def f_prime(x):
    return np.cos(x / 10) + 0.2  # Derivative for slope - change if you change f(x)

# Download car image from URL (simple car icon with transparent background)
car_url = 'https://cdn-icons-png.flaticon.com/512/744/744465.png'  # Lightweight car icon
try:
    response = requests.get(car_url)
    response.raise_for_status()  # Check if request was successful
    image = Image.open(BytesIO(response.content))
except Exception as e:
    print(f"Error loading image: {e}")
    print("Please replace the car_url with a valid PNG image URL.")
    raise

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title('Car Moving Along the Curve y = f(x)')

# Generate x and y for the curve
x_vals = np.arange(0, 100.1, 0.1)
y_vals = f(x_vals)
ax.plot(x_vals, y_vals, lw=2, color='blue')

# Set limits
ax.set_xlim(0, 100)
ax.set_ylim(np.min(y_vals) - 10, np.max(y_vals) + 10)
ax.set_xlabel('x')
ax.set_ylabel('y = f(x)')

# Animation parameters
step = 0.1  # Increment x by 0.1 each frame
num_frames = int(100 / step) + 1  # From 0 to 100, ensures it goes to the end

# Init function for animation
def init():
    return []

# Update function for each frame
def update(frame):
    # Remove previous car if exists
    if hasattr(update, 'ab'):
        update.ab.remove()

    x = frame * step
    y = f(x)
    slope = f_prime(x)
    angle = np.arctan(slope) * 180 / np.pi  # Angle in degrees

    # Rotate the image (negative angle to point the car uphill correctly)
    rotated_image = image.rotate(-angle, resample=Image.BICUBIC, expand=True)

    # Create offset image with zoom for small size
    oi = OffsetImage(rotated_image, zoom=0.1)  # Adjust zoom (0.1 for smaller car)

    # Add to axis at (x, y)
    ab = AnnotationBbox(oi, (x, y), frameon=False)
    ax.add_artist(ab)

    # Save for next removal
    update.ab = ab

    return [ab]

ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=10)

HTML(ani.to_jshtml())