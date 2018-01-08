#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import logging
from config import settings


def check_path_exist(log_abs_file):
    log_path = os.path.split(log_abs_file)[0]
    if not os.path.exists(log_path):
        os.mkdir(log_path)


def write_error_log(message):
    error_log_path = settings.ERROR_LOG_FILE

    file_1_1 = logging.FileHandler(error_log_path, 'a', encoding='utf-8')
    fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
    file_1_1.setFormatter(fmt)
    logger1 = logging.Logger('error_log', level=logging.ERROR)
    logger1.addHandler(file_1_1)

    check_path_exist(error_log_path)

    logger1.error(message)


def write_run_log(message):
    error_log_path = settings.ERROR_LOG_FILE

    file_1_1 = logging.FileHandler(error_log_path, 'a', encoding='utf-8')
    fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
    file_1_1.setFormatter(fmt)
    logger1 = logging.Logger('error_log', level=logging.INFO)
    logger1.addHandler(file_1_1)

    check_path_exist(error_log_path)

    logger1.info(message)