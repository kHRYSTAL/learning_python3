#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

from src.plugins.DiskPlugin import DiskPlugin
from src.plugins.MemoryPlugin import MemoryPlugin
from src.plugins.MotherboardPlugin import MotherboardPlugin
from src.plugins.NicPlugin import NicPlugin
from src.plugins.CpuPlugin import CpuPlugin
from lib import log
from lib.response import BaseResponse


def get_server_info():
    response = BaseResponse()
    try:
        server_info = {}

        diskObj = DiskPlugin()
        memObj = MemoryPlugin()
        boardObj = MotherboardPlugin()
        nicObj = NicPlugin()
        cpuObj = CpuPlugin()

        collect_hostname = boardObj.os_hostname()
        hostname = collect_hostname
        # if hostname != collect_hostname:
        #     raise Exception(
        #         'hostname inconformity :task hostname is %s,collect hostname is %s' % (hostname, collect_hostname))

        server_info['os_platform'] = boardObj.os_platform()
        server_info['os_version'] = boardObj.os_version()

        board_info = boardObj.execute()
        server_info.update(board_info)

        cpu_info = cpuObj.execute()
        server_info.update(cpu_info)

        server_info['disk'] = diskObj.execute()
        if not server_info['disk']['status']:
            log.write_error_log('[%s][disk],%s' % (hostname, server_info['disk']['error']))
            del server_info['disk']['error']

        server_info['memory'] = memObj.execute()
        if not server_info['memory']['status']:
            log.write_error_log('[%s][memory],%s' % (hostname, server_info['memory']['error']))
            del server_info['memory']['error']

        server_info['nic'] = nicObj.execute()
        if not server_info['nic']['status']:
            log.write_error_log('[%s][nic],%s' % (hostname, server_info['nic']['error']))
            del server_info['nic']['error']

        response.data = server_info
        response.status = True
    except Exception as e:
        response.message = str(e)
    return response


if __name__ == '__main__':
    ret = get_server_info()
    print(ret.__dict__)
    for k,v in ret.data.items():
        print(k,v)