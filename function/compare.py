import paddleocr

def sanity_ocr ():
    import subprocess
    from paddleocr import PaddleOCR
    import re
    resul_t = []
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
    img_path = "./picture/screenshot/screen.png"
    result = ocr.ocr(img_path, cls=True)
    for coordinates in result:

        try:
            if float(coordinates[0][0][0]) > 1072 and float(coordinates[0][0][1]) > 180 and float(coordinates[0][2][0]) < 1346 and float(coordinates[0][2][1]) < 408:
                print(coordinates[1])
                resul_t.append(re.findall("\d+\.?\d*", coordinates[1][0])[0])
        except:
            pass
    return resul_t
def compare (flies):
    import cv2
    # 读入图像，截图部分作为模板图片
    img_src = cv2.imread('./picture/screenshot/screen.png')
    img_templ = cv2.imread(flies)

    # 模板匹配
    result = cv2.matchTemplate(img_src, img_templ, 0)
    # 计算匹配位置
    min_max = cv2.minMaxLoc(result)
    min_loc = min_max[2]
    return min_loc
        #print(coordinates)
#1095,191
#1346,408

#maa_ocr()