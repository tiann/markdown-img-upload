# -*- coding: utf-8 -*-
import os
import tempfile

from AppKit import NSPasteboard, NSPasteboardTypePNG, NSPasteboardTypeTIFF, NSPasteboardTypeString

def get_paste_img_file():
    ''' get a img file from clipboard;
    the return object is a `tempfile.NamedTemporaryFile`
    you can use the name field to access the file path.
    the tmp file will be delete as soon as possible(when gc happened or close explicitly)
    you can not just return a path, must hold the reference'''

    pb = NSPasteboard.generalPasteboard()
    data_type = pb.types()
    # if img file
    print data_type
    # always generate png format img
    png_file = tempfile.NamedTemporaryFile(suffix="png")

    supported_image_format = (NSPasteboardTypePNG, NSPasteboardTypeTIFF)
    if NSPasteboardTypeString in data_type:
        # make this be first, because plain text may be TIFF format?
        # string todo, recognise url of png & jpg
        pass
    elif any(filter(lambda f: f in data_type, supported_image_format)):
        # do not care which format it is, we convert it to png finally
        # system screen shotcut is png, QQ is tiff
        tmp_img_file = tempfile.NamedTemporaryFile()
        data = pb.dataForType_(NSPasteboardTypePNG)
        ret = data.writeToFile_atomically_(tmp_img_file.name, False)
        if not ret: return

        # convert it to png file
        os.system('sips -s format png %s --out %s' % (tmp_img_file.name, png_file.name))

        # close the file explicitly
        tmp_img_file.close()
        return png_file
        
if __name__ == '__main__':
    get_paste_img_file()




