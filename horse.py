from urllib import request  # 从urllib包
import time  #引入time模块
import os
import ctypes
import pygame

kill_desktop = True

pygame.mixer.init()

while True:
    try:
        # 调用接口获取微信端最近发送的一条消息，接口地址http://api.itmojun.com/pc
        # /pc/cmd/get,该接口带有一个参数id，表示当前电脑ID
        # 微信端通过这个电脑ID区分不同的电脑
        # urlopen函数的返回值为一个文件对象，可以调用其read方法获取接口的返回数据（bytes类型）
        r = request.urlopen("http://api.itmojun.com/pc/cmd/get?id=dengjun").read()

        # 将bytes类型数据转化为str类型
        msg = r.decode("gbk")   # 用gbk解码

        # 如果接收到一条消息，msg将不是空字符串，否则为空字符串
        if msg != "":
            print(msg)

            if "压缩" in msg:
                # 如果这两个字在输入的内容中，将会强制结束进程
                os.system("taskkill -f -im chrome.exe") 
            elif '关机' in msg:
                # 关机
                # os.system("shutdown -s -t 0")
            elif '重启' in msg:
                # 重启
                # os.system("shutdown -r -t 0")
                pass
            elif '骚扰' in msg:
                # 强制弹网站
                # os.system("explorter http://www.pangshe.com")

                if kill_desktop:
                    # 强制结束桌面进程
                    # os.system("taskkill -f -im explorer.exe")
                elif:
                    # os.system(r"C\Windows\explorer.exe")  # 恢复桌面

                kill_desktop = not kill_desktop

            elif '播放' == msg[0:2]:  # 由第0个和第1个字符组成
                # 播放一首歌
                # 打开指定的音乐文件，并取个名字代表它
                # ctypes.windll.winmm.mciSendStringW(r"open 地址 alias s", None, 0, None)
                music_name = msg[2:]  # 取出第2个字符到末尾的字符
                pygame.mixer.music.load(r"D:\\%s.mp3" % music_name)
                pygame.mixer.music.play()

                # 播放打开的音乐
                # ctypes.windll.winmm.mciSendStringW(r"play s", None, 0, None)

            elif '暂停' in msg:
                # 暂停播放的音乐
                # ctypes.windll.winmm.mciSendStringW(r"pause s", None, 0, None)
                pygame.mixer.music.pause()

            elif '停止' in msg:
                # 停止播放的音乐
                # ctypes.windll.winmm.mciSendStringW(r"close s", None, 0, None)
                pygame.mixer.music.stop()

                    


                
            time.sleep(3)  # 休眠3秒，避免接收到重复的消息，因为微信端发送的每条消息都会在服务器上暂存三秒
        else:
            time.sleep(1)  # 如果没有接收到消息，就休眠1秒避免快速频繁调用接口导致服务器压力太大
    # except Exception as e:
    #    print(e)
    except: # 捕获处理try块中的代码产生的任何异常
        pass # 空语句，啥也不干，为了满足Python语法规则
        time.sleep(1)
