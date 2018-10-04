import os
import cv2
import keyboard
from sightengine.client import SightengineClient
import paralleldots
from paralleldots import set_api_key
import requests
import matplotlib.pyplot as plt
from matplotlib import figure
import numpy as np

capit = "press SPACEBAR to capture the image"
print(capit)
print(exit)

class VideoCamera(object):
    def get_frame(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        
        from app import buttons
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
                path_img = "/Users/jeffrosal1/Desktop/NUhomework/project3/Project3/dopple/static/img/"
                img_name = "dopplegang.png"
                #cv2.imwrite(img_name, frame)
                
                cv2.imwrite(str(path_img) + 'dopplegang.png', frame)
                print("{} written!".format(img_name))

                client = SightengineClient('523702522', 'SoMh4T2mBCTB848RmhqS')
                output = client.check('celebrities').set_file('/Users/jeffrosal1/Desktop/NUhomework/project3/Project3/dopple/static/img/dopplegang.png')
                print(output)
                set_api_key("i0bqh0wRTlMqHMTHXZPxXFumRAcETw698GaIqBN9vuM")

# when sending a image file

                path = "/Users/jeffrosal1/Desktop/NUhomework/project3/Project3/dopple/static/img/dopplegang.png"
                emoout = paralleldots.facial_emotion(path)         
                print(emoout)

                #start matplotlib
                faces = output["faces"]
                celebrity = faces[0]
                name_set= celebrity["celebrity"]
                index = 0
                totalprob = 0
                names = []
                probability = []
                while index < len(name_set):
                    x = name_set[index]
                    name = x['name']
                    names.append(name)

                    prob = x['prob']
                    probability.append(prob)
    
                    index = index + 1
                print(names)
                print(probability)
                from matplotlib import rcParams
                rcParams.update({'figure.autolayout': True})
                plt.bar(names, probability, color='yellow', alpha=0.5, align="center", edgecolor = "black")
                plt.xticks(rotation=45)
                plt.ylim(0, 1)
                plt.title("Celebrity Doppelganger")
                plt.xlabel("Celebrity Name")
                plt.ylabel("Probability")                             
                
                plt.savefig(str(path_img) + "prob_bar_graph.png")
                plt.close()
                #end matplotlib








            rete, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()

     
    def __del__(self):
        self.video.release()

        #cv2.destroyAllWindows()


         
