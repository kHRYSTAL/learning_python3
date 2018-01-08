#!/usr/bin/env python
# -*- coding:utf-8 -*-
import paramiko
import config


class BasePlugin(object):
    def __init__(self):
        pass

    def os_platform(self):
        output = self.exec_shell_cmd('uname')
        return output.strip()

    def os_version(self):

        try:
            # output = self.exec_shell_cmd('cat /etc/issue')
            output = """CentOS release 6.6 (Final)
                    Kernel \r on an \m
                    """
            result = output.strip().split('\n')[0]
        except Exception as  e:
            result = " "
        return result

    def os_hostname(self):
        output = self.exec_shell_cmd('hostname')
        return output.strip()

    def exec_shell_cmd(self, cmd):
        # private_key_path = config.configration['key_path']
        # key = paramiko.RSAKey.from_private_key_file(private_key_path)
        # ssh = paramiko.SSHClient()
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh.connect(hostname=self.hostname, port=self.port, username=self.username, pkey=key)
        # stdin,stdout,stderr = ssh.exec_command(cmd)
        # result = stdout.read()
        # ssh.close()
        import subprocess
        status, output = subprocess.getstatusoutput(cmd)
        return output

    def execute(self):
        return self.linux()

    def linux(self):
        raise Exception('You must implement Linux method.')

    def windows(self):
        raise Exception('You must implement Linux method.')

# class NicPlugin(BasePlugin):
#     def linux(self):
#         self.exec_shell_cmd('cmd')
#
# obj = NicPlugin()
# obj.execute()