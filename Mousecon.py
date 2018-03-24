import pyautogui
import time
'''
鼠标操作类，pyautogui库的简单封装
'''
class Worker:
    def click_left(self,x,y):#鼠标左键点击
        self.move(x, y)
        pyautogui.click(x,y)
    def click_right(self,x,y):#鼠标右键点击
        self.move(x,y)
        pyautogui.rightClick(x,y)
    def move(self,x,y):#鼠标移动
        pyautogui.moveTo(x,y,duration=0.25)
    def click_middle(self,x,y): #鼠标滑轮点击
        self.move(x, y)
        pyautogui.middleClick(x,y)
    def drag(self,x,y):#拖拽
        pyautogui.dragTo(x,y,duration=0.25)
    def typewrite(self,value):#输入
        pyautogui.typewrite(value)
    def keyDown(self,key,times):#按下一个键
        pyautogui.keyDown(key) #按下
        time.sleep(times) #按下之后释放的时间
        pyautogui.keyUp(key)#松开这个键
    def hotkey(self,*args):#组合按键，接受多个参数
        pyautogui.hotkey(*args)
