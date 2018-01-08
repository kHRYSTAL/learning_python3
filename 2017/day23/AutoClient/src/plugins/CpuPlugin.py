#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import re
from . import BasePlugin


class CpuPlugin(BasePlugin.BasePlugin):
    def linux(self):

        try:
            # shell_command = "cat /proc/cpuinfo"
            # output = self.exec_shell_cmd(shell_command)
            from config.settings import BASEDIR
            output = open(os.path.join(BASEDIR,'files/cpuinfo.out'), 'r').read()
            return self.parse(output)
        except Exception as e:
            raise Exception('linux cpu command is exception')

    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        response = {'cpu_count': 0, 'cpu_physical_count': 0, 'cpu_model': ''}

        cpu_physical_set = set()

        content = content.strip()
        for item in content.split('\n\n'):
            for row_line in item.split('\n'):
                key, value = row_line.split(':')
                key = key.strip()
                if key == 'processor':
                    response['cpu_count'] += 1
                elif key == 'physical id':
                    cpu_physical_set.add(value)
                elif key == 'model name':
                    if not response['cpu_model']:
                        response['cpu_model'] = value
        response['cpu_physical_count'] = len(cpu_physical_set)

        return response

