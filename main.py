import sys
import cv2
from cossim import topk
import numpy as np
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class GUI(QDialog):
    def __init__(self):
        super(GUI, self).__init__()
        loadUi('instamoji.ui', self)
        self.image = None
        self.canny = None
        self.prediction1 = None
        self.prediction2 = None
        self.prediciton3 = None


        self.emoji1 = cv2.imread('emojis\EMOJI\small\ok.jpg')
        self.emoji2 = cv2.imread('emojis\EMOJI\small\Smiling_Face_Emoji.jpg')
        self.emoji3 = cv2.imread('emojis\EMOJI\small\smiling-face-with-smiling-eyes-and-hand-covering-mouth.jpg')
        self.emoji4 = cv2.imread('emojis\EMOJI\small\humbs-up-sign.jpg')
        self.emoji5 = cv2.imread('emojis\EMOJI\small\ongue_Out_Emoji_with_Tightly_Closed_Eyes.jpg')
        self.emoji6 = cv2.imread('emojis\EMOJI\small\ictory-hand.jpg')

        self.dict = {}
        self.dict['OK'] = self.emoji1
        self.dict['grin'] = self.emoji2
        self.dict['hand'] = self.emoji3
        self.dict['thumbs'] = self.emoji4
        self.dict['tongue'] = self.emoji5
        self.dict['victory'] = self.emoji6


        self.startButton.clicked.connect(self.start_webcam)
        self.pauseButton.clicked.connect(self.pause_webcam)
        self.predictionButton.toggled.connect(self.predict_webcam)
        self.predictionButton.setCheckable(True)
        self.prediction_enabled = False

    def predict_webcam(self, status):
        if status:
            self.prediction_enabled = True
            self.predictionButton.setText('stop prediction')
        else:
            self.prediction_enabled = False
            self.predictionButton.setText('start prediction')

    def start_webcam(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)

    def update_frame(self):
        ret,self.image = self.capture.read()
        self.image = cv2.flip(self.image, 1)
        self.displayImage(self.image, 1)

        if(self.prediction_enabled):
            # gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY) if len(self.image.shape)>=3 else self.image
            # self.canny = cv2.Canny(gray, 100, 200)
            # self.displayImage(self.canny, 5)
            temp = topk(self.image, 3)
            # print(temp)
            self.prediction1 = self.dict[temp[0]]
            self.prediction2 = self.dict[temp[1]]
            self.prediction3 = self.dict[temp[2]]

            self.displayImage(self.prediction1, 2)
            self.displayImage(self.prediction2, 3)
            self.displayImage(self.prediction3, 4)
    def pause_webcam(self):
        self.timer.stop()

    def displayImage(self, img, window = 1):
        if (window == 1):
            qformat = QImage.Format_Indexed8
            if (len(img.shape) == 3):
                if (img.shape[2] == 4):
                    qformat = QImage.Format_RGBA8888
                else:
                    qformat = QImage.Format_RGB888
            outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)

            outImage = outImage.rgbSwapped()
            self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
            self.imgLabel.setScaledContents(True)
        if (window == 5):
            qformat = QImage.Format_Indexed8
            if (len(img.shape) == 3):
                if (img.shape[2] == 4):
                    qformat = QImage.Format_RGBA8888
                else:
                    qformat = QImage.Format_RGB888
            outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)

            outImage = outImage.rgbSwapped()
            self.cannyLabel.setPixmap(QPixmap.fromImage(outImage))
            self.cannyLabel.setScaledContents(True)
        if (window == 2):
            qformat = QImage.Format_RGB888
            outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
            outImage = outImage.rgbSwapped()
            self.outputLabel1.setPixmap(QPixmap.fromImage(outImage))
            self.outputLabel1.setScaledContents(True)
        if (window == 3):
            qformat = QImage.Format_RGB888
            outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
            outImage = outImage.rgbSwapped()
            self.outputLabel2.setPixmap(QPixmap.fromImage(outImage))
            self.outputLabel2.setScaledContents(True)
        if (window == 4):
            qformat = QImage.Format_RGB888
            outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
            outImage = outImage.rgbSwapped()
            self.outputLabel3.setPixmap(QPixmap.fromImage(outImage))
            self.outputLabel3.setScaledContents(True)


app = QApplication(sys.argv)
window = GUI()
window.setWindowTitle('instamoji')
window.show()
sys.exit(app.exec_())

