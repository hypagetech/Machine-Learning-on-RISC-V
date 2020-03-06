# Untitled - By: pmbehera - Mi. März 4 2020

import sensor, image, lcd, time
import KPU as kpu
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.set_vflip(1)
lcd.clear()
lcd.draw_string(100,96,"MobileNet Demo")
lcd.draw_string(100,112,"Loading labels...")
f=open('labels.txt','r')
labels=f.readlines()
f.close()
task = kpu.load("/sd/model.kmodel")
while(True):
    img = sensor.snapshot()
    fmap = kpu.forward(task, img)
    plist=fmap[:]
    pmax=max(plist)
    max_index=plist.index(pmax)
    #lcd.draw_string(0, 224, "%.2f:%s                            "%(pmax, labels[max_index].strip()))
    a = img.draw_string(0,0, str(labels[max_index].strip()), color=(255,0,0), scale=2)
    a = img.draw_string(0,20, str(pmax), color=(255,0,0), scale=2)
    print((pmax, labels[max_index].strip()))
    a = lcd.display(img)
a = kpu.deinit(task)