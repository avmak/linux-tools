#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
import tarfile

DIR_BASE = "/ARCHIVE/collog"
DIR_BASE_ES_LOG = "/ARCHIVE/logs/elasticsearch"

class Archlog(object):
	SUF = ".log.tar.gz"
	def __init__(self, sour, dest):
		self.dir_sour = sour
		self.dir_dest = dest

	def archive_creating(self):
		print "Создается архив логов..."
		if os.path.isfile(self.dir_sour + self.SUF):
			os.remove(self.dir_sour + self.SUF)

		tar = tarfile.open(self.dir_sour + self.SUF, "w|gz")
		tar.add(self.dir_dest, arcname="log")
		tar.close()
		print "Архив логов создан!"

if __name__ == "__main__":
	Archlog(DIR_BASE, DIR_BASE_ES_LOG).archive_creating()
