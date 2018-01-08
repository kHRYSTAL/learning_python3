#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.path.join(BASEDIR)

from src.plugins import PluginApi
from src.plugins import CpuPlugin
v = PluginApi.get_server_info()
for k,v in v.__dict__['data'].items():
    print(k,v)
