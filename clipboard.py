# -*- coding: utf-8 -*-
import os
import tempfile
import imghdr
import shutil

from AppKit import NSPasteboard, NSPasteboardTypePNG,\
        NSPasteboardTypeTIFF, NSPasteboardTypeString,\
        NSFilenamesPboardType

# image_file, need_format, need_compress
NONE_IMG = (None, False, None)

def _convert_to_png(from_path, to_path):
    # convert it to png file
    os.system('sips -s format png %s --out %s' % (from_path, to_path))

def get_paste_img_file():
    ''' get a img file from clipboard;
    the return object is a `tempfile.NamedTemporaryFile`
    you can use the name field to access the file path.
    the tmp file will be delete as soon as possible(when gc happened or close explicitly)
    you can not just return a path, must hold the reference'''

    pb = NSPasteboard.generalPasteboard()
    data_type = pb.types()

    supported_image_format = (NSPasteboardTypePNG, NSPasteboardTypeTIFF)
    if NSFilenamesPboardType in data_type:
        # file in clipboard
        img_path = pb.propertyListForType_(NSFilenamesPboardType)[0]
        img_type = imghdr.what(img_path)

        if not img_type:
            # not image file 
            return NONE_IMG

        if img_type not in ('png', 'jpeg', 'gif'):
            # now only support png & jpg & gif
            return NONE_IMG

        is_gif = img_type == 'gif'
        _file = tempfile.NamedTemporaryFile(suffix=img_type)
        tmp_clipboard_img_file = tempfile.NamedTemporaryFile()
        shutil.copy(img_path, tmp_clipboard_img_file.name)
        if not is_gif:
            _convert_to_png(tmp_clipboard_img_file.name, _file.name)
        else:
            shutil.copy(tmp_clipboard_img_file.name, _file.name)
        tmp_clipboard_img_file.close()
        return _file, False, 'gif' if is_gif else 'png'

    if NSPasteboardTypeString in data_type:
        # make this be first, because plain text may be TIFF format?
        # string todo, recognise url of png & jpg
        pass

    if any(filter(lambda f: f in data_type, supported_image_format)):
        # do not care which format it is, we convert it to png finally
        # system screen shotcut is png, QQ is tiff
        tmp_clipboard_img_file = tempfile.NamedTemporaryFile()
        print tmp_clipboard_img_file.name
        png_file = tempfile.NamedTemporaryFile(suffix='png')
        for fmt in supported_image_format:
            data = pb.dataForType_(fmt)
            if data: break
        ret = data.writeToFile_atomically_(tmp_clipboard_img_file.name, False)
        if not ret: return NONE_IMG

        _convert_to_png(tmp_clipboard_img_file.name, png_file.name)
        # close the file explicitly
        tmp_clipboard_img_file.close()
        return png_file, True, 'png'
        
if __name__ == '__main__':
    get_paste_img_file()
