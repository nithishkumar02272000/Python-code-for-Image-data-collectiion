# Python-code-for-Image-data-collectiion
This Python script allows you to capture face images of an employee from different angles using a webcam. It automatically creates a directory for the employee's name and saves the captured images in separate folders for each angle.

## Prerequisites

- Python 3.x
- OpenCV (cv2) library
- GTTS (gTTS) library

## Installation

1. Clone the repository or download the `capture_images.py` file.

2. Install the required libraries using pip:

   ```shell
   pip install opencv-python gtts

##Usage
--Run the script by executing the following command:
data_collection_1.py
Enter the employee's name when prompted.

--The script will guide you to position your face towards different angles (face, right, left) by providing audio instructions and beeping sounds.

--For each angle, the script will capture a specified number of images from the webcam.

--Press 'q' to stop the image capture process.

--The captured images will be saved in a directory named after the employee's name. Each angle's images will be stored in separate subdirectories.

##Notes
--Make sure to have a webcam connected and properly configured.

--Adjust the num_images_per_angle variable in the code to control the number of images captured for each angle.

--The captured images will be saved in the same directory as the capture_images.py file.

--The images will be named following the format: employee_angle_imageIndex.jpg.

--Please ensure that you have the necessary permissions and legal rights to capture and store employee face images.
