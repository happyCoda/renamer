#!/usr/bin/env python

import os

def rename(prefix):
	cwd = os.getcwd()
	listdir = os.listdir(cwd)
	full_path = None
	for item in listdir:
		full_path = cwd + '\\' + item
		if os.path.isdir(full_path):
			os.rename(full_path, cwd + '\\' + prefix + item)