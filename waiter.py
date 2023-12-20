import os
import time

class Waiter():

	def __init__(self, folder_to_watch):
		self.folder_to_watch = folder_to_watch

	def pre_run(self, machine):
		exists = os.path.exists(self.folder_to_watch)
		if not exists :
			machine.info["error"] = "'Watch folder' did not exist."
		machine.info["folder"] = self.folder_to_watch
		return exists

	def run(self, machine):
		l = os.listdir(self.folder_to_watch)
		if not l:
			machine.info["error"] = "'Watch folder' is empty"
			time.sleep(5)
			return False
		machine.info["task_file"] = l[0]
		return True
