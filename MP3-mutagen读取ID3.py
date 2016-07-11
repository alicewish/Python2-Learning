# -*- coding: utf-8 -*-
import time

start_time = time.time()  # 初始时间戳
from mutagen.id3 import ID3

#----------------------------------------------------------------------
def getMutagenTags(path):
    """"""
    audio = ID3(path)

    print "Artist: %s" % audio['TPE1'].text[0]
    print "Track: %s" % audio["TIT2"].text[0]
    print "Release Year: %s" % audio["TDRC"].text[0]

getMutagenTags("/Users/alicewish/Desktop/Miranda Cosgrove - Sparks Fly 05 - Hey You (2010).mp3")
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
