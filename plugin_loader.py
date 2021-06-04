# -*- coding: utf-8 -*-

import os
import sys
from imp import find_module, load_module

from plugins_lib.plugin import Plugin
from plugins_lib.plugin_manager import PluginManager


class DirectoryPluginLoader(PluginManager):
    """
    从指定目录加载插件
    """
    name = "DirectoryPluginManager"

    def __init__(self, plugins=tuple(), config=dict()):
        default_directory = "".join([os.getcwd(), os.sep, "plugins"])
        self.directories = config.get("directories", (default_directory,))
        super(DirectoryPluginLoader, self).__init__(plugins=plugins, config=config)

    def load_plugins(self):
        """
        遍历文件目录加载插件
        """
        plugins = []
        for directory in self.directories:
            try:
                for file_name in os.listdir(directory):
                    if file_name.endswith(".py") and file_name != "__init__.py":
                        plugins.append((file_name[:-3], directory))
            except OSError:
                continue

        file = None
        mod = None
        for (name, path) in plugins:
            try:
                file, pathname, desc = find_module(name, [path])
                old = sys.modules.get(name)
                if old is not None:
                    del sys.modules[name]
                mod = load_module(name, file, pathname, desc)
            finally:
                if file:
                    file.close()
            if hasattr(mod, "__all__"):
                attrs = [getattr(mod, x) for x in mod.__all__]
                for plug in attrs:
                    if not issubclass(plug, Plugin):
                        continue
                    self._load_plugin(plug())