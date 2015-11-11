# -*- coding: utf-8
import os, re
import ConfigParser

CONFIG_FILE = 'config.ini'

def notice(msg, title="notice"): 
    ''' notoce message in notification center'''
    os.system('osascript -e \'display notification "%s" with title "%s"\'' % (msg, title))

def read_config():
    ''' read congig from config.ini, return a five tuple'''
    if not os.path.exists(CONFIG_FILE):
        return
    cf = ConfigParser.ConfigParser()
    cf.read(CONFIG_FILE)

    qiniu_section = 'qiniu'
    try:
        ak = cf.get(qiniu_section, 'ak')
        sk = cf.get(qiniu_section, 'sk')
        url = cf.get(qiniu_section, 'url')
        bucket = cf.get(qiniu_section, 'bucket')
        prefix = cf.get(qiniu_section, 'prefix')
    except ConfigParser.NoOptionError:
        return
    
    keys = ('ak', 'sk', 'url', 'bucket', 'prefix')
    res = (ak, sk, url, bucket, prefix)
    if not all(map(lambda x: re.match(r'\w+', x), res)):
        return
    return dict(zip(keys, res))

def open_with_editor(filepath):
    ''' open file with apple's text editor'''
    os.system('open -b "com.apple.TextEdit" "./%s"' % CONFIG_FILE)

def generate_config_file():
    import textwrap
    config_file_init_content = '''\
    [qiniu]
    ak=七牛图床的Access Key
    sl=七牛图床的Secret Key
    url=七牛图床地址
    bucket=七牛图床空间名
    prefix=七牛图床资源前缀名'''
    with open(CONFIG_FILE, 'w') as fp:
        fp.write(textwrap.dedent(config_file_init_content))
