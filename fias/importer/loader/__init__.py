#coding: utf-8
from __future__ import unicode_literals, absolute_import

from fias.config import FIAS_LOADERS_PATH
from importlib import import_module

DEFAULT_LOADERS_PATH = 'fias.importer.loader'


class UnknownTableError(Exception):
    pass


def _import(path, name):
    return import_module('{0}.{1}'.format(path, name))


def loader(table):
    loader_module = None
    if FIAS_LOADERS_PATH: #  try custom
        try:
            loader_module = _import(FIAS_LOADERS_PATH, table.full_name)
        except ImportError:
            pass

    if not loader_module: #  load default
        try:
            loader_module = _import(DEFAULT_LOADERS_PATH, table.full_name)
        except ImportError:
            raise UnknownTableError(table.full_name)

    return loader_module.Loader(table)
