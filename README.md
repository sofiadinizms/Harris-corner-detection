# Corner Detection Application

## Overview
This project is a Python-based application that uses the Harris Corner Detection algorithm to detect and highlight corners in a live camera feed. It was created by Sofia Diniz for the Advanced Topics in Media and Interaction subject.

## Features
- Detects corners in real-time using a custom implementation of the Harris Corner Detection algorithm.
- Highlights detected corners with rectangles of consistent colors.
- Limits the number of displayed corners to a maximum of 15, selected randomly for each frame.
- Simple home screen with a title and a button to launch the camera feed.

## Requirements
- Python 3.7+
- Required libraries:
  - `opencv-python`
  - `numpy`
  - `tkinter` (built-in with most Python distributions)

## Installation
1. Clone or download this repository to your local machine.
2. Install the required libraries:
   ```bash
   pip install opencv-python numpy
   ```

## Usage
1. Run the application:
   ```bash
   python scratch.py
   ```
2. The home screen will appear with a title "Corner Detection Application" and a button labeled "Start Camera Feed."
3. Click the button to open the live camera feed.
4. Press the `q` key to exit the live feed.

## How It Works
1. **Harris Corner Detection Algorithm**:
   - Computes image gradients using Sobel filters.
   - Applies a Gaussian filter to smooth the gradient products.
   - Calculates the Harris response matrix to identify corners.
2. **Corner Highlighting**:
   - Detected corners are drawn with rectangles in consistent colors.
   - Colors remain constant across frames for each corner.
3. **Home Screen**:
   - Built with Tkinter.
   - Provides an intuitive interface to launch the corner detection.

## Example Output
When running, the application will:
- Display live camera feed.
- Highlight detected corners in real time with small rectangles of varying colors.

## Limitations
- Requires a functional webcam to run.
- May not work with certain integrated cameras or virtual environments.

## Contact
For any issues or questions, please reach out to my email: sofiadinizms@gmail.com.

