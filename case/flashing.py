#!/usr/bin/env python
# encoding: utf-8

"""
@version: 0.1
@author: liuzhangpei
@contact: liuzhangpei@126.com
@site: http://www.livenowhy.com
@time: 17/2/26 12:36
"""



from flask import Flask, render_template
import time
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()

def calculate_value():
    return time.time()

def get_my_item(key):
    rv = cache.get(key=key)
    if rv is None:
        rv = calculate_value()
        cache.set(key=key, value=rv, timeout=5 * 60)
    return rv


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return 'page_not_found'
    # return render_template('404.html'), 404





if __name__ == '__main__':

    # for x in range(1, 40):
    #     print get_my_item(key='sss')
    app.run(debug=False, port=8099, host='0.0.0.0', threaded=True)