#!/usr/bin/env python
# encoding: utf-8

"""
@version: 0.1
@author: liuzhangpei
@contact: liuzhangpei@126.com
@site: http://www.livenowhy.com
@time: 17/3/16 09:21

    flask.__main__
    ~~~~~~~~~~~~~~

    Alias for flask.run for the command line.
"""

if __name__ == '__main__':
    from .cli import main
    main(as_module=True)


# 20170321