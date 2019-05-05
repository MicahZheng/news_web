#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default Configurations.
'''

__author__ = 'micah'

configs = {
    'debug': True,
    'db': {
        'host': 'localhost',
        'port': '3306',
        'user': 'www',
        'password': 'www',
        'db': 'blogdb'
    },
    'session': {
        'secret': 'Awesome'
    }
}