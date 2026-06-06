import cv2
import os

# 配置区域
INPUT_DIR = 'input'
OUTPUT_DIR = 'output'

def process_images():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.jpg', '.png')):
            img = cv2.imread(os.path.join(INPUT_DIR, filename))
            h, w = img.shape[:2]
            
            # 针对图片右下角水印的区域设置 (根据图片比例动态计算)
            # 假设水印位于右下角，宽占15%，高占8%
            mask = np.zeros((h, w), np.uint8)
            mask[h-int(h*0.08):h, w-int(w*0.15):w] = 255
            
            # 使用 NS 算法，这是处理复杂纹理效果较好的算法
            result = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)
            
            cv2.imwrite(os.path.join(OUTPUT_DIR, filename), result)
            print(f"完成: {filename}")

import numpy as np
if __name__ == "__main__":
    process_images()
