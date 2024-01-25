# InteractiveHologram

## Basic Overview

The interactive hologram is a platform that enables objects to be viewed with an illusion of depth and interacted with in real time using hand detection. 

Thanks to this platform, it is possible to visualize complex objects and learn more about their various characteristics, as well as adding information to a tangible object placed at the center of the pyramid.

Get to know more about the interactive hologram project on DVIC website (link of the page soon…)<br><br><br><br><br>


## Clone the Code 

To clone the project:

1. Clone the repository: `git clone https://github.com/GaetanCrd/InteractiveHologram/tree/main`
   
2. Install the required libraries (`cv2`, `mediapipe`, `pyautogui`, `tensorflow`, `audioop`, `pyaudio`)
   
3. Adjust thresholds to suit your hardware (seuil de déclenchement du clic pouce/index, seuil de déclenchement du clic avec l’audio => voir les commentaires du code)<br><br>

Note that this Python code is designed to work with a specific Figma file:
- For example, during an audio peak, the `InteractiveHolo.py` code triggers a click on the coordinates x,y=90,990
- So, a button has been placed on these coordinates in the Figma file to trigger an action<br><br><br><br><br>


## Files Provided in the GitHub

- `InteractiveHolo.py`: Main Python file used to run the interactive hologram. In practical terms, it allows you to:
  - Control the computer mouse using the hand detected by the webcam.
  - Click by pinching the thumb and index finger.
  - Trigger a click by creating a sound peak on the webcam microphone.<br><br>
 
- `AudioID`: Python file used to detect all the audio devices connected to your computer and their IDs, useful for setting up the `InteractiveHolo.py` code with your variables.<br><br>

- `AfterEffect_Github`: The AfterEffect files used to create the videos used on Figma + the source media used in the AfterEffect files.<br><br>

- `Figma_Github`: .mp4 videos exported from AfterEffect and used in the Figma.<br><br><br><br><br>


## Hardware: A Webcam + Screen System

The interactive hologram function thanks to 1 webcam, 1 displaying screen and 1 control monitor :
- One webcam to capture the video stream of hands and sound peaks.
- One displaying screen directly implemented in the hologram.
- One control monitor allowing you to run the Python code and the Figma file.

<p style="text-align:center;"><img src="(https://github.com/GaetanCrd/InteractiveHologram/blob/main/images/sche%CC%81ma_github.png)" alt="Interactive Hologram Hardware" width="320" height="180" title="Interactive Hologram Hardware"></p>


## Launch the Interactive Hologram

  ### 1. Wiring

Make sure that when the Python code is launched it detects the webcam and the webcam microphone.

  #### 1.1 Webcam

  Line 59 of the code `InteractiveHolo.py`: 
  Modify the variable to find your webcam; a window with a video stream should open if the webcam is correctly detected.

  #### 1.2 Micro

  Line 14 of the code `InteractiveHolo.py`: 
  Modify the variable to find your webcam's microphone; use the `audioID.py` code provided in the GitHub repo to identify all your audio devices and their IDs.

### 2. Control Monitor

#### 2.1 Figma

  Get the file from this public link (you'll need a Figma account). Normally, the file is published, so it's public. If you can't get it, you can send me a request on gaetan.carrade@gmail.com
  
  link -> [InteractiveHologramV2-(Community)](https://www.figma.com/file/djTwNBUoWC2nPRA5BrAYd0/InteractiveHologramV2-(Community)?type=design&mode=design&t=z7bf9A173N1yEMxa-1)

#### 2.2 Python

  Make sure that you have correctly imported all the necessary libraries and that you can run the `InteractiveHolo.py` code without error. Run it from a code editor or directly from the terminal.
  
  Launch the Figma model using the play button at the top right of the window, uncheck "hotspot hints on click" and "Figma UI" in the options, and set it to full screen by clicking F.
  
  You can now control the Figma model using your hand.

