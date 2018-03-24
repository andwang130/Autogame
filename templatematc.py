import cv2
import numpy as np
from PIL import ImageGrab
'''图片对比类'''
class img_jeg:
    def mathc_img(self,Target,value=None,image=None):
        if not image:
            image=self.screenshot()
        if not value:
            value=0.9
        img_rgb = cv2.imread(image)  #打开对比图片
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)#颜色空间转换
        template = cv2.imread(Target,0)#  打开模板图片
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) #两张图片进行对比，cv2.TM_CCOEFF_NORMED对比类型
        tutp=cv2.minMaxLoc(res)
        similar=tutp[1]  #相似度
        x,y=tutp[3]     #坐标
        if similar>value:
            return (True,x,y)
        else:
            return (False,None,None)

        # threshold = value  #传入的对比阀值
        # loc = np.where( res >= threshold)
        # for pt in zip(*loc[::-1]):
        #     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)
        #     print(pt)
        # cv2.imshow('Detected',img_rgb)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    def screenshot(self,path='temlpath.jpg'):
        im=ImageGrab.grab()#截取当前屏幕。不加参数默认截取全屏
        im.save(path)
        return path
if __name__ == '__main__':
    image=("temlpath.png")#模板图片
    Target=('len.png')#对比的图片
    value=0.9  #相似度
    myimg_jeg=img_jeg()
    image_tupe=myimg_jeg.mathc_img(image,Target,value)
    print(image_tupe)