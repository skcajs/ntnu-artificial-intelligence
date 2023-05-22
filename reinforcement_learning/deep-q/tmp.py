import cv2
import os

image_folder = './screens'
video_name = 'video.avi'

images = []
for i in range(1, 31640):
    images.append(f"image_{i}.jpg")

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 120, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()