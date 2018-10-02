import numpy as np
import cv2
from skimage.measure import compare_ssim

# grin1 = cv2.resize(cv2.imread("images/grin1.jpg", 0), (640, 480))
# grin2 = cv2.resize(cv2.imread("images/grin2.jpg", 0), (640, 480))
# hand1 = cv2.resize(cv2.imread("images/hand1.jpg", 0), (640, 480))
# hand2 = cv2.resize(cv2.imread("images/hand2.jpg", 0), (640, 480))
# shush1 = cv2.resize(cv2.imread("images/shush1.jpg", 0), (640, 480))
# shush2 = cv2.resize(cv2.imread("images/shush2.jpg", 0), (640, 480))
# think1 = cv2.resize(cv2.imread("images/think1.jpg", 0), (640, 480))
# think2 = cv2.resize(cv2.imread("images/think2.jpg", 0), (640, 480))
# tongue1 = cv2.resize(cv2.imread("images/tongue1.jpg", 0), (640, 480))
# tongue2 = cv2.resize(cv2.imread("images/tongue2.jpg", 0), (640, 480))
grin1 = cv2.resize(cv2.imread("images/grin.jpg", 0), (640, 480))
hand1 = cv2.resize(cv2.imread("images/hand.jpg", 0), (640, 480))
tongue1 = cv2.resize(cv2.imread("images/tongue.jpg", 0), (640, 480))
thumbs1 = cv2.resize(cv2.imread("images/thumbs.jpg", 0), (640, 480))
victory1 = cv2.resize(cv2.imread("images/victory.jpg", 0), (640, 480))
OK1 = cv2.resize(cv2.imread("images/OK.jpg", 0), (640, 480))

emoji_list = ['grin', 'hand', 'tongue', 'thumbs', 'victory', 'OK']

def topk(img, k):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print(img.shape)
    # print(grin1.shape)
    sim = np.zeros(6)
    sim[0], _ = compare_ssim(grin1, img, full=True)
    sim[1], _ = compare_ssim(hand1, img, full=True)
    sim[2], _ = compare_ssim(tongue1, img, full=True)
    sim[3], _ = compare_ssim(thumbs1, img, full=True)
    sim[4], _ = compare_ssim(victory1, img, full=True)
    sim[5], _ = compare_ssim(OK1, img, full=True)
    top = sorted(range(len(sim)), key=lambda i: sim[i])[-k:]
    return list(map(lambda i: emoji_list[i], top))#emoji_list[np.argmax(sim)]

# print(top(tongue2))