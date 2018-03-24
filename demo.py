from templatematc import *
from Mousecon import *
import time
class Main:
    def __init__(self):
        self.matc = img_jeg()
        self.worker=Worker()
    def run(self):
        for i in range(100):
            time.sleep(1)
            path='len.png'
            req=self.matc.mathc_img(path)
            if req[0]:
                self.worker.move(req[1],req[2])

if __name__ == '__main__':
    mian=Main()
    mian.run()