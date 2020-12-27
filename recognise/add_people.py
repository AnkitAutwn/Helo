from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os
import json
import pathlib

def encode(urls,name):
    abspath = pathlib.Path('media/encodings.pickle').absolute()
    with open(abspath,'rb') as input:
            data = pickle.load(input)

    knownEncodings = data["encodings"]
    knownNames = data["names"]

    for imagePath in urls:
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb,
            model="cnn")

        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
           #if encoding not in knownEncodings:
            knownEncodings.append(encoding)
            knownNames.append(name)

    print("[INFO] serializing encodings...")
    data = {"encodings": knownEncodings, "names": knownNames}

    #print(data)

    f = open(abspath, "wb")
    f.write(pickle.dumps(data))
    f.close()