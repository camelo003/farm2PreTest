import os

class Runner():

	def pre_run(self, machine):
		file = machine.info["folder"] + "/" + machine.info["task_file"]
		exists = os.path.exists(file)
		if exists :
			machine.info["task_full_path"] = file
		else :
			machine.info["error"] = "Task file do not fond."
		return exists

	def run(self, machine):
		task_file = open(machine.info["task_full_path"], "a")
		if task_file :
			task_file.write("\n=====\n")
			task_file.write("Trecho adicionado pela classe 'runner'.")
			task_file.close()
			return True
		task_file.close()
		machine.info["error"] = "Could not open the task file."
		return False
