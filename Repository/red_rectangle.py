import cv2
import numpy as np

# === POSTAVKE ===
rel_path = "../room-dataset/"
image_path = rel_path + "kitchen/kitchen_284.jpg"
scale = 0.5  # omjer prikaza
thickness = 5   # debljina crvenog pravokutnika 

# Točke u postocima slike (0,0 dolje lijevo → 100,100 gore desno)
percent_points = [
# ====== Ovdje upisati svoje koordinate u ovom obliku ============== 
(10, 10), (40, 10), (40, 50), (10, 50) 
# ============================================================
]

# === UČITAJ SLIKU ===
img = cv2.imread(image_path)
if img is None:
    raise FileNotFoundError("Kriva putanja: " + image_path)

h, w = img.shape[:2]

# === PRETVORI POSTOTKE U PIXELE ===
def percent_to_pixel(x_percent, y_percent):
    px = int((x_percent / 100) * w)
    py = int((1 - y_percent / 100) * h)  # y raste prema gore
    return (px, py)

pixel_points = [percent_to_pixel(x, y) for (x, y) in percent_points]

# === NACRTAJ PRAVOKUTNIK ===
pts = np.array(pixel_points, np.int32).reshape((-1, 1, 2))
cv2.polylines(img, [pts], isClosed=True, color=(0, 0, 255), thickness=thickness)

# === PRIKAZI SLIKU ===
resized_img = cv2.resize(img, (0, 0), fx=scale, fy=scale)
cv2.imshow('Smanjena slika', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
