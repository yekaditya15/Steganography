import cv2
import os

folder_path = "images/"
file_list = []
for file in os.listdir(folder_path):
    if file.endswith(".jpg"):
        img_path = os.path.join(folder_path, file)
        img = cv2.imread(img_path)
        total_pixels = img.shape[0] * img.shape[1]
        file_list.append((file, total_pixels))

for i, (file, total_pixels) in enumerate(sorted(file_list, key=lambda x: x[1])):
    new_file = f"c{str(i).rjust(2,'0')}_{total_pixels}.jpg"
    old_path = os.path.join(folder_path, file)
    new_path = os.path.join(folder_path, new_file)
    os.rename(old_path, new_path)