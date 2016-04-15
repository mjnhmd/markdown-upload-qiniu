# -*- coding: utf-8 -*-

import os
import sys
import win32clipboard as w

reload(sys)
sys.setdefaultencoding('utf-8')
from qiniu import Auth, put_file

import ConfigParser
from datetime import datetime


cf = ConfigParser.ConfigParser()
cf.read('config.ini')
access_key = cf.get('qiniu', 'ak') # AK
secret_key = cf.get('qiniu', 'sk') # SK
bucket_name = cf.get('qiniu', 'bucket') # 七牛空间名
url = cf.get('qiniu', 'url') # url

q = Auth(access_key, secret_key)

mime_type = "image/jpeg"
params = {'x:a': 'a'}

prefix = datetime.now().strftime('%Y_%m_%d')

def upload_qiniu(path, prefix):
    ''' upload file to qiniu '''
    dirname, filename = os.path.split(path)
    key = '%s_%s' % (prefix, filename) # upload to qiniu's dir
    key = key.decode('gbk').encode('utf8')

    token = q.upload_token(bucket_name, key)
    progress_handler = lambda progress, total: progress

    ret, info = put_file(token, key, path, params, mime_type, progress_handler=progress_handler)
    return ret != None and ret['key'] == key

def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardText(aString)
    w.CloseClipboard()

if __name__ == '__main__':
    path = sys.argv[1]
    ret = upload_qiniu(path, prefix)
    if ret:
        # upload success
        name = os.path.split(path)[1]
        alt = name.split('.', 1)
        markdown_url = "![%s](%s/%s_%s \"%s\")" % (alt[0], url, prefix, name, alt[0])
        # make it to clipboard
        setText(markdown_url)
    else:
        print "upload_failed"

