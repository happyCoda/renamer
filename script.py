#!/usr/bin/env python

import os

def rename(prefix, flag, dir=None):
	target_dir = os.getcwd() if dir is None else dir

	listdir = os.listdir(target_dir)
	full_path = None
	for item in listdir:
		full_path = target_dir + '\\' + item
		if os.path.isdir(full_path):
			if flag == 'add':
				os.rename(full_path, target_dir + '\\' + prefix + item)
			elif flag == 'remove':
				os.rename(full_path, target_dir + '\\' + item[len(prefix):])