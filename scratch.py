import cv2
import numpy as np
import random
import tkinter as tk
from tkinter import messagebox

# Global dictionary to store colors for consistent corner coloring
corner_colors = {}

def harris_corner_detector(image, k=0.04, threshold=0.01):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate gradients using Sobel filter
    Ix = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    Iy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)

    # Calculate products of gradients
    Ixx = Ix * Ix
    Iyy = Iy * Iy
    Ixy = Ix * Iy

    # Apply a Gaussian filter to the products of gradients
    sigma = 1
    Ixx = cv2.GaussianBlur(Ixx, (5, 5), sigma)
    Iyy = cv2.GaussianBlur(Iyy, (5, 5), sigma)
    Ixy = cv2.GaussianBlur(Ixy, (5, 5), sigma)

    # Compute Harris corner response
    det = (Ixx * Iyy) - (Ixy ** 2)
    trace = Ixx + Iyy
    R = det - k * (trace ** 2)

    # Threshold for corner detection
    corners = np.zeros_like(R)
    corners[R > threshold * R.max()] = 255

    return corners

def assign_color_to_corner(corner):
    """Assign a consistent color to each corner."""
    global corner_colors
    if corner not in corner_colors:
        corner_colors[corner] = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
    return corner_colors[corner]

def camera_feed():
    # Initialize webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Detect corners using custom Harris Corner Detector
        corners = harris_corner_detector(frame)

        # Find corner locations and limit to 15 randomly selected corners
        corner_locations = np.argwhere(corners == 255)
        if len(corner_locations) > 15:
            corner_locations = corner_locations[np.random.choice(len(corner_locations), 15, replace=False)]

        # Draw rectangles with consistent colors
        for corner in corner_locations:
            y, x = corner  # Note: OpenCV uses (y, x) format
            color = assign_color_to_corner((x, y))
            cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), color, 1)

        # Display the resulting frame
        cv2.imshow('Live Camera with Corners', frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

def main():
    def start_camera():
        root.destroy()
        camera_feed()

    root = tk.Tk()
    root.title("Corner Detection Application")

    # Set the size of the window
    root.geometry("600x400")

    tk.Label(root, text="Corner Detection Application", font=("Arial", 24)).pack(pady=20)
    tk.Button(root, text="Start Camera Feed", font=("Arial", 16), command=start_camera).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()