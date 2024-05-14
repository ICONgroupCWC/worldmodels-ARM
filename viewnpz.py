from numpy import load
from matplotlib import pyplot as plt
import cv2
import numpy as np

def showimgObservation(np3DArray):
    
    plt.imshow(np3DArray, interpolation='nearest')
    plt.show()
    return


def createMovie(data,item):
    output_video = 'output_video.mp4'

    # Define the dimensions of the images
    image_width = 64
    image_height = 64

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec
    fps = 30  # Frames per second
    video_writer = cv2.VideoWriter(output_video, fourcc, fps, (image_width, image_height))

    # Loop through each image array and write it to the video
    for img_array in data[item]:
        # Convert the NumPy array to uint8 format (assuming pixel values are in the range [0, 255])
        img_uint8 = np.uint8(img_array)
        
        # Resize the image to fit the video dimensions (if needed)
        # img_resized = cv2.resize(img_uint8, (image_width, image_height))
        
        # Write the frame to the video
        video_writer.write(img_uint8)

    # Release the VideoWriter object
    video_writer.release()

    print("Video creation completed.")




data = load('/Users/athmajanvivekananthan/WCE/JEPA - MARL/World Models/world-models/datasets/carracing/thread_1/rollout_0.npz')
lst = data.files

item = lst[0] # observations

print(item)
print(len(data[item]))
obs0 = data[item][500]


#createMovie(data,item)
#showimgObservation(obs0)




