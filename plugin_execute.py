# -*- coding: utf-8 -*-

import inspect

from plugins_lib.plugin_loader import DirectoryPluginLoader


class PluginExecute:

    def __init__(self, plugin_name: str, method_name: str):
        if not all([plugin_name, method_name]):
            raise KeyError('插件名称和方法名都是必要的!')
        self.plugin_mane = plugin_name
        self.method_name = method_name
        self.plugin_manager = DirectoryPluginLoader()
        self.plugin_manager.load_plugins()
        self.plugins = self.plugin_manager.get_plugins(plugin_name)

    @property
    def get_plugins(self):
        return self.plugins

    def excute_method(self):
        method_list = [func for func in dir(self.plugins[0]) if
                       callable(getattr(self.plugins[0], func)) and not func.startswith("__")]
        for method in method_list:
            if method != self.method_name.strip().lower():
                continue
            args = list(inspect.signature(self.plugins[0].method).parameters.keys())
            if 'self' in args:
                args.remove('self')
                result = self.plugins[0].method(args)
                return result
            elif len(args) == 0:
                result = self.plugins[0].method()
                return result
