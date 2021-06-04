# -*- coding: utf-8 -*-

class Plugin(object):
    """定义一个接口，其他 插件必须实现这个接口，name属性必须赋值"""
    name = ''

    def __init__(self):
        pass