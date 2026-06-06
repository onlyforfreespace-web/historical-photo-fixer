import cv2
import sys

def run_debug(image_path):
    if not os.path.exists(image_path):
        print(f"找不到文件: {image_path}")
        return

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 这一步是核心：通过高斯模糊和自适应阈值，让背景“消失”，只留下水印轮廓
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 2)
    
    print("正在显示调试窗口，请查看是否能清晰辨认出水印形状...")
    print("按键盘上的任意键即可关闭窗口。")
    
    cv2.imshow('Debug View (White = Detected Watermark)', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import os
    # 替换为你 input 文件夹下的一张图片名
    img_name = 'test.jpg' 
    run_debug(f'input/{img_name}')
