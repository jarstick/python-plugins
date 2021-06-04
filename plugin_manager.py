# -*- coding: utf-8 -*-


class PluginManager:
    """
    基础的插件管理类
    """
    name = "PluginManager"

    def __init__(self, plugins=tuple(), config=dict()):
        self.__plugins = []
        if plugins:
            self.add_plugins(plugins)

    def __iter__(self):
        return iter(self.plugins)

    def add_plugin(self, plug):
        self.__plugins.append(plug)

    def add_plugins(self, plugins):
        for plug in plugins:
            self.add_plugin(plug)

    def del_plugin(self, plug):
        if plug in self.__plugins:
            self.__plugins.remove(plug)

    def del_plugins(self, plugins):
        for plug in plugins:
            self.del_plugin(plug)

    def get_plugins(self, name=None):
        plugins = []
        for plugin in self.__plugins:
            if name is None or plugin.name == name:
                plugins.append(plugin)
        return plugins

    def _load_plugin(self, plug):
        loaded = False
        for p in self.plugins:
            if p.name == plug.name:
                loaded = True
                break
        if not loaded:
            self.add_plugin(plug)

    def load_plugins(self):
        pass

    def _get_plugins(self):
        return self.__plugins

    def _set_plugins(self, plugins):
        self.add_plugins(plugins)

    plugins = property(_get_plugins, _set_plugins, None,
                       """可以批量操作插件!""")


