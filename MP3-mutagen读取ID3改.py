# -*- coding: utf-8 -*-
import time

start_time = time.time()  # 初始时间戳
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

#----------------------------------------------------------------------
def getTags(path):
    """"""
    m = MP3(path, id3=EasyID3)

    print "Artist: %s" % m['artist'][0]
    print "Album: %s" % m['album'][0]
    print "Track: %s" % m['title'][0]
    print "Release Year: %s" % m['date'][0]

getTags("/Users/alicewish/Desktop/Miranda Cosgrove - Sparks Fly 05 - Hey You (2010).mp3")
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
