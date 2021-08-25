import cv2 as cv
import argparse
import sys
import numpy as np

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_width', type=int, help="image width")
    parser.add_argument("--img_height", type=int, help='image height')
    parser.add_argument("--num_imgs", type=int, help="how many images used for calibration")
    parser.add_argument("--square_size",type=float,help="square size of chessboard")
    parser.add_argument("--board_width",type=int,help='inner corner points in row')
    parser.add_argument("--board_height",type=int,help="inner corner points in column")
    args = parser.parse_args()
    #   load camera

    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, args.img_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, args.img_height)
    vet, img = cap.read()
    if not vet:
        print('-----\ncheck your camera, it can not be loaded,\n-----')
        sys.exit()

    pos_lib = []
    objp = np.zeros((args.board_height * args.board_width, 3), dtype=np.float32)
    objp[:, :2] = np.mgrid[0:args.board_height, 0:args.board_width].T.reshape(-1, 2)
    while True:
        # obtain image
        # vet,img = cap.read()
        img=cv.imread('1.bmp')
        # corner points
        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        vet,corners=cv.findChessboardCornersSB(gray,patternSize=(args.board_width,args.board_height))



    print(1)
