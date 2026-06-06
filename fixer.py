import cv2
import numpy as np
import os

def auto_remove_watermark(image_path, output_path):
    img = cv2.imread(image_path)
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]

    # 1. 智能检测：聚焦右下角区域 (比如图片右下角的 1/4 区域)
    roi = gray[h//2:, w//2:]
    
    # 2. 二值化处理：寻找水印颜色（假设水印较深，通过阈值提取）
    # 如果水印是黑色的，用 THRESH_BINARY_INV，若是白色的，用 THRESH_BINARY
    _, thresh = cv2.threshold(roi, 50, 255, cv2.THRESH_BINARY_INV)

    # 3. 寻找水印轮廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    mask = np.zeros((h, w), np.uint8)
    for cnt in contours:
        # 获取轮廓的矩形边界
        x, y, bw, bh = cv2.boundingRect(cnt)
        # 过滤掉太小的噪点
        if bw > 10 and bh > 10:
            # 在全图对应的位置画出 mask
            mask[h//2 + y : h//2 + y + bh, w//2 + x : w//2 + x + bw] = 255

    # 4. 修复
    result = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
    cv2.imwrite(output_path, result)

# 遍历文件夹... (保持之前的逻辑)
