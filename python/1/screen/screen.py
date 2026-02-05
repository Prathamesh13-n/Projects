# importing the required packages
import pyautogui
import cv2
import numpy as np

# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
filename = "Recording.avi"

# Specify frames rate. We can choose any 
# value and experiment with it
import pyautogui
import cv2
import numpy as np

resolutions = (1920, 1080)

codec = cv2.VideoWriter_fourcc(*"XVID")

filename = "Recording.avi"

fps = 60

# Create VideoWriter (ensure correct class name and parameter order)
out = cv2.VideoWriter(filename, codec, fps, resolutions)

# Prepare a resizable window for preview
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 720)

try:
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)

        # pyautogui.screenshot() returns an RGB PIL image; convert to BGR for OpenCV
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Ensure frame size matches writer; resize if necessary
        h, w = frame.shape[:2]
        if (w, h) != resolutions:
            frame = cv2.resize(frame, resolutions)

        out.write(frame)

        # Display the recording preview
        cv2.imshow('Live', frame)

        # Stop recording when we press 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    pass
finally:
    out.release()
    cv2.destroyAllWindows()
