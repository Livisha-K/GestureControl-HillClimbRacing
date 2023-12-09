<!DOCTYPE html>
<html>

<body>

  <h1>Hill Climb Racing Hand Gesture Control</h1>

  <p>This Python script utilizes the OpenCV and MediaPipe libraries to control the Hill Climb Racing game using hand gestures. The program captures the video feed from the default camera, tracks hand movements, and interprets specific gestures to generate commands for controlling the game.</p>

  <h2>Requirements</h2>
  <ul>
      <li>Python</li>
      <li>OpenCV</li>
      <li>MediaPipe</li>
      <li>PyAutoGUI</li>
  </ul>

  <h2>Code Overview</h2>
  <p>The script consists of the following key components:</p>

  <ol>
      <li>Import necessary libraries:
          <ul>
              <li>cv2 (OpenCV)</li>
              <li>mediapipe</li>
              <li>pyautogui</li>
              <li>time</li>
          </ul>
      </li>
      <li>Initialize video capture from the default camera.</li>
      <li>Create instances for hand tracking using MediaPipe and initialize drawing utilities.</li>
      <li>Define functions for finding commands based on hand landmarks and for tracing hand movements.</li>
      <li>Inside the main loop:
          <ul>
              <li>Read frames from the camera.</li>
              <li>Flip the frame horizontally for better user experience.</li>
              <li>Process the frame to detect hand landmarks and draw connections.</li>
              <li>Identify commands based on hand gestures.</li>
              <li>Control the Hill Climb Racing game using PyAutoGUI based on detected commands.</li>
              <li>Show the processed frame with hand landmarks on a window.</li>
              <li>Exit the loop if the 'q' key is pressed.</li>
          </ul>
      </li>
  </ol>

  <h2>Hand Gesture Commands</h2>
  <ul>
      <li><strong>Command 1:</strong> Move the vehicle by pressing gas.</li>
      <li><strong>Command 2:</strong> Stop the vehicle by applyinig brakes.</li>
      <li><strong>No Command:</strong> No vehicle movement.</li>
  </ul>

  <h2>Usage</h2>
  <p>Ensure that the required libraries are installed before running the script. The program captures your hand gestures through the camera and translates them into commands for controlling the Hill Climb Racing game.</p>

  <h2>Important Notes</h2>
  <ul>
      <li>This script assumes that the Hill Climb Racing game is running and active.</li>
      <li>Adjustments may be needed for optimal hand gesture detection based on environmental conditions and camera placement.</li>
      <li>Exit the program by pressing the 'q' key in the output window.</li>
  </ul>

  <h2>Author</h2>
  <p>Author: Livisha K</p>

</body>

</html>
