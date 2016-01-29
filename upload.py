# -*- coding: utf-8 -*-

import os
from qiniu import Auth, put_file
from util import read_config

config = read_config()

def upload_qiniu(path, upload_name):
    ''' upload file to qiniu'''
    q = Auth(config['ak'], config['sk'])
    key = '%s/%s' % (config['prefix'], upload_name) # upload to qiniu's markdown dir

    token = q.upload_token(config['bucket'], key)
    ret, info = put_file(token, key, path, check_crc=True)
    return ret != None and ret['key'] == key
