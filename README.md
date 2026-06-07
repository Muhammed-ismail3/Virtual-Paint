# 🎨 Virtual Painter (OpenCV)

A real-time computer vision application that detects colored objects through a webcam and uses them as virtual drawing tools. The system tracks predefined colors in real time and draws on a digital canvas by storing the detected object positions across frames.

---

## 🚀 Features

* **Real-Time Color Tracking:** Detects colored objects directly from a webcam feed.
* **Virtual Drawing Canvas:** Draws and stores points permanently while the object moves.
* **Multi-Color Support:** Supports Blue, Green, and Red drawing tools simultaneously.
* **HSV Color Segmentation:** Uses HSV color space for robust color detection under varying lighting conditions.
* **Contour-Based Object Detection:** Locates colored objects using contour extraction and bounding boxes.
* **Persistent Drawing:** Maintains all previously detected points until the application is closed.

---

## 🛠 Computer Vision Pipeline

The project follows a real-time computer vision workflow:

### 1. Frame Acquisition

* Initializes the webcam using OpenCV.
* Captures live video frames continuously.
* Horizontally flips frames to create a natural mirror effect.

### 2. Color Space Conversion

* Converts each frame from **BGR** to **HSV** color space.
* HSV provides better color separation and is less sensitive to lighting changes.

### 3. Color Segmentation

Creates individual masks for:

* **Blue Objects**
* **Green Objects**
* **Red Objects**

The red color is detected using two HSV ranges because red spans both ends of the HSV hue spectrum.

### 4. Contour Detection

* Finds contours in each color mask.
* Filters contours using an area threshold to eliminate noise.
* Computes bounding rectangles around valid objects.

### 5. Position Extraction

* Calculates the top-center point of the detected object's bounding box.
* Uses this point as the virtual brush position.

### 6. Virtual Canvas Rendering

* Stores detected points in memory.
* Draws circles at all stored locations.
* Uses different drawing colors depending on the detected object.

---

## 🧠 Detection Logic

Each stored point follows the structure:

```python
[x, y, colorID]
```

Where:

* `x` = Horizontal position
* `y` = Vertical position
* `colorID` = Associated drawing color

Example:

```python
[320, 150, 0]
```

Represents a blue point located at `(320, 150)`.

---

## 💻 How to Run

### Prerequisites

Ensure Python is installed along with the required libraries:

```bash
pip install opencv-python
pip install numpy
```

Or install everything at once:

```bash
pip install opencv-python numpy
```

---

### Execution

1. Download the project files.
2. Connect a webcam.
3. Run the script:

```bash
python main.py
```

4. Hold a blue, green, or red object in front of the camera.
5. Move the object to draw on the virtual canvas.
6. Press **ESC** to exit.

---

## 📂 Project Structure

```text
Virtual-Painter/
│
├── main.py
├── README.md
└── assets/
```

---

## 🔧 Technologies Used

* **Python**
* **OpenCV**
* **NumPy**

---

## 📸 Example Use Cases

* Interactive drawing applications
* Gesture-based interfaces
* Computer vision learning projects
* Real-time object tracking demonstrations
* Human-computer interaction experiments

---

## 🎯 Future Improvements

* Add an eraser tool.
* Save drawings as image files.
* Support additional colors.
* Implement brush size control.
* Add a dedicated virtual canvas window.
* Improve tracking robustness with morphological operations.
