from time import time
import os

class Rester():

	def __init__(self, folder_to_log):
		self.folder_to_log = folder_to_log

	def pre_run(self, machine):
		exists = os.path.exists(self.folder_to_log)
		if not exists :
			machine.info["error"] = "'Log folder' did not exist."
		machine.info["log"] = self.folder_to_log
		return exists

	def run(self, machine):
		timestamp = str(time()).split('.')[0]
		task_log_full_path = os.path.join(self.folder_to_log, timestamp)
		os.mkdir(task_log_full_path)
		if not os.path.exists(task_log_full_path):
			machine.info["error"] = "Unable to create task log."
			return False
		task_log_file_path = os.path.join(task_log_full_path, "rester_log.txt")
		task_log_file = open(task_log_file_path, "w")
		if not task_log_file :
			machine.info["error"] = "Unable to create task log file."
			task_log_file.close()
			return False
		task_log_file.write("log criado pelo rester.")
		return True
