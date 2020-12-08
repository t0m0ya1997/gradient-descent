#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 23:38:44 2020

@author: t_hirakawa
"""

from tqdm import tqdm
import numpy as np
import cv2

target = np.float32(cv2.imread("../img/demo.jpg"))
start = np.float32(np.random.rand(target.shape[0], target.shape[1], target.shape[2])) * 255

lr = 0.005

frame_rate = 24.0
size = (start.shape[0], start.shape[1])
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter('../result/output.mp4', fmt, frame_rate, size)

for i in tqdm(range(10000)):
    start = start + lr * (target - start)
    psnr = cv2.PSNR(start, target)
    writer.write(np.uint8(start))
    if psnr > 35.0:
        break

writer.release()
cv2.destroyAllWindows()
