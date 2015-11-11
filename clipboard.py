# -*- coding: utf-8 -*-
import time
from AppKit import NSPasteboard, NSPasteboardTypePNG, NSPasteboardTypeTIFF, NSPasteboardTypeString

def get_paste_img_file():
    pb = NSPasteboard.generalPasteboard()
    data_type = pb.types()
    # if img file
    print data_type
    now = int(time.time() * 1000) # used for filename
    if NSPasteboardTypePNG in data_type:
        # png
        data = pb.dataForType_(NSPasteboardTypePNG)
        filename = '%s.png' % now
        filepath = '/tmp/%s' % filename
        ret = data.writeToFile_atomically_(filepath, False)
        if ret:
            return filepath
    elif NSPasteboardTypeTIFF in data_type:
        # tiff
        data = pb.dataForType_(NSPasteboardTypeTIFF)
        filename = '%s.tiff' % now
        filepath = '/tmp/%s' % filename
        ret = data.writeToFile_atomically_(filepath, False)
        if ret:
            return filepath
    elif NSPasteboardTypeString in data_type:
        # string todo, recognise url of png & jpg
        pass





