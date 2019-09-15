import numpy as np
import cv2
import pickle
from tensorflow.python.keras.models import load_model
from mtcnn.mtcnn import MTCNN
from PIL import Image
from opponent import Opponent
from player import Player
from game import Game
import time


if __name__ == "__main__":
    model = load_model('../models/rps_v2.h5')
    hands_model = load_model('../models/detect_hands.h5')
    labels = ["...", "paper", "rock", "scissor"]
    
    print("Hey, What's Your Name?")
    name = input()

    p = Player(name)
    op = Opponent()
    game = Game(p, op)
    
    video_capture = cv2.VideoCapture(0)
    x, y = 320-150, 240-150
    w, h = 300, 300
    text_p = "..."
    text_o = "..."

    #shoot = False
    #wait = 5
    #intro = ""
    # for i in ["rock", "paper", "scissors", "shoot"]:
    #     intro = i
    #     ret, frame = video_capture.read()

    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     if(shoot == False):
    #         cv2.putText(frame, intro, (640//2, 480//2),
    #                     cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    #     intro = i
    #     time.sleep(1)
   # t_end = time.time() + 60 * 15
    #while time.time() < t_end:
    while True:
    #while text_p == "..." and text_o == "...":
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # if(shoot == False):
        # cv2.putText(frame, "Round 1", (640//2, 480//2),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        crop_frame = frame[y:y+h, x:x+w]
        crop = Image.fromarray(crop_frame)
        crop = cv2.resize(crop_frame, (150, 150)) 
        img = np.asarray(crop)
        img = np.expand_dims(img, 0)
        pred = model.predict(img)
        hand = hands_model.predict(img) 
        index = pred.argmax()
        if (pred[0][index] > 0.80): #and cv2.waitKey(1) & 0xFF == ord('x')):
            old = text_p
            text_p = labels[index]
            p.set_play(text_p)
            if (text_p != old):
                op.set_play()
                text_o = op.get_play()
        else:
            text_p = "..."
            text_o = "..."
        winner = game.decide_winner()
        cv2.putText(frame, p.get_name() + " played " + text_p, (10, 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        cv2.putText(frame, "Opponent played " + text_o, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        cv2.putText(frame, "winner:  " + winner, (400, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
