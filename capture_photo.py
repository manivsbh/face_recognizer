import cv2
import os
import time


class capturePhoto:
    def capture_photo_from_camera():
        # Create a directory to store the captured photos
        output_folder = 'captured_photos'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Create a VideoCapture object to access the webcam
        cap = cv2.VideoCapture(0)  # 0 for the default camera, you can change it if you have multiple cameras

        # Load the Haar Cascade Classifier for face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        if not cap.isOpened():
            print("Error: Could not access the camera.")
        else:
            # Display the camera feed for 3 seconds
            start_time = time.time()
            while time.time() - start_time < 3:
                ret, frame = cap.read()
                if not ret:
                    print("Error: Could not capture a frame.")
                    break

                # Detect faces in the frame
                faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                # Draw blue rectangles around detected faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue rectangle

                cv2.imshow("Camera Feed with Face Detection", frame)
                cv2.waitKey(1)  # Display each frame for 1 millisecond

            if len(faces) == 0:
                print("No face detected.")
            else:
                # Capture a single frame
                ret, frame = cap.read()

                if ret:
                    # Save the captured photo to the specified folder
                    photo_path = os.path.join(output_folder, "captured_photo_with_face.jpg")
                    cv2.imwrite(photo_path, frame)
                    print(f"Photo saved to {photo_path}")
                else:
                    print("Error: Could not capture a frame.")

            # Release the camera and close the OpenCV windows
            cap.release()
            cv2.destroyAllWindows()
