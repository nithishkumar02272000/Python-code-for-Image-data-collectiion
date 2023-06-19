import cv2
import os
import winsound
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    os.system('start output.mp3')

def capture_images(employee_name, num_images_per_angle):
    # Create a directory with the employee's name
    directory = employee_name.replace(" ", "_")
    os.makedirs(directory, exist_ok=True)

    # Initialize webcam
    capture = cv2.VideoCapture(0)

    # Set the width and height of the frame
    capture.set(3, 640)
    capture.set(4, 480)

    angles = ["face", "right", "left"]

    for angle in angles:
        speak(f"Please position your face towards the {angle}")
        winsound.Beep(500, 3000)

        for image_count in range(num_images_per_angle):
            # Read frame from webcam
            ret, frame = capture.read()

            if not ret:
                continue

            # Display the frame
            cv2.imshow('Capture Images', frame)

            # Press 'q' to exit
            if cv2.waitKey(1) == ord('q'):
                break

            # Save the captured image
            image_filename = f"{directory}/{employee_name.replace(' ', '_')}_{angle}_{image_count}.jpg"
            cv2.imwrite(image_filename, frame)

    # Release the webcam and close windows
    capture.release()
    cv2.destroyAllWindows()

# Usage example
employee_name = input("Enter the employee's name: ")
num_images_per_angle = 275

capture_images(employee_name, num_images_per_angle)
