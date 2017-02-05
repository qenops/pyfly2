import time
import pyfly2

class SpeedTest(object):
    def __init__(self, camera):
        self.camera = camera
        self.count = 0
        self.update_rate = 1.0

    def Start(self):
        self.camera.connect()
        self.camera.start_capture()

        self.starttime = time.clock()

        try:
            while True:
                _ = self.camera.GrabPILImage()

                self.count += 1
                now = time.clock()
                elapsed = now - self.starttime
                if elapsed >= self.update_rate:
                    self.fps = self.count / elapsed
                    self.starttime = now
                    self.count = 0
                    print ("FPS =", self.fps)
        except:
            self.camera.stop_capture()
            raise


def main():
    context = pyfly2.Context()
    camera = context.get_camera(0)

    test = SpeedTest(camera)
    test.Start()

if __name__ == '__main__':    
    main()