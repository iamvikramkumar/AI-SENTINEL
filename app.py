from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, from Flask!"



# import cv2

# # Open the default camera (usually the built-in webcam)
# cap = cv2.VideoCapture(0)

# # Check if the camera is opened successfully
# if not cap.isOpened():
#     print("Error: Could not open webcam.")
#     exit()

# while True:
#     # Read a frame from the webcam
#     success, img = cap.read()

#     # Check if the frame is read successfully
#     if not success:
#         print("Error: Failed to read frame from webcam.")
#         break
        

#     # Display the frame
#     cv2.imshow("Webcam", img)

#     # Exit the loop if 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close all OpenCV windows
# cap.release()
# cv2.destroyAllWindows()



