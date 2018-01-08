#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from . import BasePlugin


class MotherboardPlugin(BasePlugin.BasePlugin):

    def linux(self):
        try:
            # shell_command = "sudo dmidecode -t1"
            # output = self.exec_shell_cmd(shell_command)
            from config.settings import BASEDIR
            output = open(os.path.join(BASEDIR,'files/board.out'), 'r').read()
            return self.parse(output)
        except Exception as e:
            raise Exception('linux motherboard command is exception')

    def parse(self,content):

        result = {}
        key_map = {
            'Manufacturer': 'manufactory',
            'Product Name': 'model',
            'Serial Number': 'sn',
        }

        for item in content.split('\n'):
            row_data = item.strip().split(':')
            if len(row_data) == 2:
                if row_data[0] in key_map:
                    result[key_map[row_data[0]]] = row_data[1].strip() if row_data[1] else row_data[1]

        return result