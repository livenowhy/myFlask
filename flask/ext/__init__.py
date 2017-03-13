#!/usr/bin/env python
# encoding: utf-8

"""
@version: 0.1
@author: liuzhangpei
@contact: liuzhangpei@126.com
@site: http://www.livenowhy.com
@time: 17/2/26 14:15

    flask.ext

    Redirect imports for extensions.
    This module basically makes it possible for us to transition from flaskext.foo to flask_foo without having to
    force all extensions to upgrade at the same time.

    When a user does ``from flask.ext.foo import bar`` it will attempt to import ``from flask_foo import bar`` first
    and when that fails it will try to import ``from flaskext.foo import bar``.

    We're switching from namespace packages because it was just too painful for everybody involved.
"""

def setup():
    from ..exthook import ExtensionImporter
    importer = ExtensionImporter(['flask_%s', 'flaskext.%s'], __name__)
    importer.install()

setup()
del setup
