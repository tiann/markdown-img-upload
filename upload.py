# -*- coding: utf-8 -*-

import os
from qiniu import Auth, put_file

access_key = '' # AK
secret_key = '' # SK

bucket_name = 'booluimg' # 七牛空间名

q = Auth(access_key, secret_key)

def upload_qiniu(path):
    ''' upload file to qiniu'''
    dirname, filename = os.path.split(path)
    key = 'markdown/%s' % filename # upload to qiniu's markdown dir

    token = q.upload_token(bucket_name, key)
    ret, info = put_file(token, key, path, check_crc=True)
    return ret != None and ret['key'] == key
