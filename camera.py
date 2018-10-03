import cv2
import keyboard
from sightengine.client import SightengineClient
import paralleldots
from paralleldots import set_api_key

capit = "press SPACEBAR to capture the image"
exit = "press ESC to EXIT"
print(capit)
print(exit)
class VideoCamera(object):
    def get_frame(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        
        
        self.video = cv2.VideoCapture(0)

        img_counter = 0
        
        while True:
            ret, frame = self.video.read()
            #cv2.imshow("test", frame)
            if not ret:
                break
            k = cv2.waitKey(1)
    
            if k%256 == 27:
        # ESC pressed
                print("Escape hit, closing...")
                break
            elif keyboard.is_pressed('space'):
        # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))

                client = SightengineClient('523702522', 'SoMh4T2mBCTB848RmhqS')
                output = client.check('celebrities').set_file('/Users/jeffrosal1/Desktop/NUhomework/project3/combined/flasktest/opencv_frame_0.png')
                print(output)
                set_api_key("i0bqh0wRTlMqHMTHXZPxXFumRAcETw698GaIqBN9vuM")

# when sending a image file

                path = "/Users/jeffrosal1/Desktop/NUhomework/project3/combined/flasktest/opencv_frame_0.png"
                emoout = paralleldots.facial_emotion(path)         
                print(emoout)
            rete, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()

    def __del__(self):
        self.video.release()

        #cv2.destroyAllWindows()


         
