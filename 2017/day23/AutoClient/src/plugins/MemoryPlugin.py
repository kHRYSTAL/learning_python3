#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import subprocess
from lib import convert
from lib import log
from . import BasePlugin


class MemoryPlugin(BasePlugin.BasePlugin):
    def linux(self):
        result = {'status': 0, 'data': {}}
        try:
            # shell_command = "/usr/bin/sudo dmidecode -q -t 17 2>/dev/null"
            # shell_command = "sudo dmidecode  -q -t 17 2>/dev/null"
            # output = self.exec_shell_cmd(shell_command)
            from config.settings import BASEDIR
            output = open(os.path.join(BASEDIR,'files/memory.out'), 'r').read()

            result['data'] = self.parse(output)
            result['status'] = 1
        except Exception as e:
            result['error'] = e
        return result

    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        ram_dict = {}
        key_map = {
            'Size': 'capacity',
            'Locator': 'slot',
            'Type': 'model',
            'Speed': 'speed',
            'Manufacturer': 'manufactory',
            'Serial Number': 'sn',

        }
        devices = content.split('Memory Device')
        for item in devices:
            item = item.strip()
            if not item:
                continue
            if item.startswith('#'):
                continue
            segment = {}
            lines = item.split('\n\t')
            for line in lines:
                if len(line.split(':')) > 1:
                    key, value = line.split(':')
                else:
                    key = line.split(':')[0]
                    value = ""
                if key in key_map:
                    if key == 'Size':
                        segment[key_map['Size']] = convert.convert_mb_to_gb(value, 0)
                    else:
                        segment[key_map[key.strip()]] = value.strip()
            ram_dict[segment['slot']] = segment

        return ram_dict

