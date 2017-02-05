"""
   pyfly2
   
   example_opencv_integration

   continually grab images from a camera and display them using OpenCV's
   HighGui module, until the user presses a key
"""

import pyfly2
import cv2


def main(cameraIndex=0, format='bgr', scale=1.0, windowName='Live Video'):
    context = pyfly2.Context()
    if context.num_cameras < 1:
        raise ValueError('No cameras found')
    camera = context.get_camera(cameraIndex)
    camera.connect()
    camera.start_capture()
    while cv2.waitKey(1) == -1:
        image = camera.grab_numpy_image(format)
        if scale != 1.0:
            image = cv2.resize(image, (0, 0), fx=scale, fy=scale)
        cv2.imshow(windowName, image)
    camera.stop_capture()


if __name__ == "__main__":
    main()
