import cv2
vc = cv2.VideoCapture(r'D:\test01\video-1.mp4')  # 读入视频文件，命名cv
n = 1  # 计数
rval,frame = vc.read()

timeF = 10  # 视频帧计数间隔频率

i = 0
while rval:  # 循环读取视频帧
    rval, frame = vc.read()
    if (n % timeF == 0):  # 每隔timeF帧进行存储操作
        i += 1
        print(i)
        cv2.imwrite(r'D:\test01\{}.jpg'.format(i), frame)  # 存储为图像
    n = n + 1
    cv2.waitKey(1)
vc.release()