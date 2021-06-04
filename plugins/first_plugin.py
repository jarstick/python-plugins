# -*- coding: utf-8 -*-

import sys

from plugins_lib.plugin import Plugin

sys.path.append('../')


__all__ = ["FirstPlugin"]


class FirstPlugin(Plugin):
    name = "first_plugin"

    def __init__(self):
        super(FirstPlugin, self).__init__()

    @staticmethod
    def first():
        return "第一个插件"

    @staticmethod
    def second():
        return "第二个插件"