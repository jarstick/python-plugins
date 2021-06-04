# -*- coding: utf-8 -*-

import sys

from plugins_lib.plugin import Plugin

sys.path.append('../')

__all__ = ["SecondPlugin"]


class SecondPlugin(Plugin):
    name = "second_plugin"

    def __init__(self):
        super(SecondPlugin, self).__init__()

    @staticmethod
    def first_1():
        return "第一个插件"

    @staticmethod
    def second_2():
        return "第二个插件"