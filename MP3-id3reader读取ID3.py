# -*- coding: utf-8 -*-
import time

start_time = time.time()  # 初始时间戳
import id3reader

#----------------------------------------------------------------------
def getTags(path):
    """"""
    id3r = id3reader.Reader(path)

    print "Artist: %s" % id3r.getValue('performer')
    print "Album: %s" % id3r.getValue('album')
    print "Track: %s" % id3r.getValue('title')
    print "Release Year: %s" % id3r.getValue('year')
getTags("/Users/alicewish/Desktop/Miranda Cosgrove - Sparks Fly 05 - Hey You (2010).mp3")
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
