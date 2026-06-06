import cv2
import os

def batch_debug(folder_path):
    # 获取文件夹里所有支持的图片格式
    extensions = ('.jpg', '.png', '.jpeg')
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(extensions)]
    
    if not images:
        print("文件夹里没有图片！")
        return

    for img_name in images:
        path = os.path.join(folder_path, img_name)
        img = cv2.imread(path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # 调试参数 (你可以在这里反复修改参数进行对比)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                       cv2.THRESH_BINARY_INV, 11, 2)
        
        print(f"正在分析: {img_name} (按任意键切换下一张，或按 ESC 退出)")
        cv2.imshow(f'Debugging: {img_name}', thresh)
        
        # 等待按键：按 ESC (27) 退出，按其他键切换
        key = cv2.waitKey(0)
        cv2.destroyAllWindows()
        if key == 27:
            break

if __name__ == "__main__":
    batch_debug('input')
