import fsm

import waiter
import runner
import rester

import os
import time

class Farm2(fsm.FiniteStateMachineMixin):

	state_machine = {
		'init': ('waiting',),
		'waiting': ('error', 'running'),
		'running': ('error', 'resting'),
		'resting': ('error', 'end'),
		'error': ('end',),
		'end': None
	}

	waiter = waiter.Waiter("folder") #FIXME
	runner = runner.Runner()
	rester = rester.Rester("logs") #FIXME

	# info = {}

	def __init__(self):
		self.state = 'init'
		self.info = {}

	def pre_waiting(self):
		if not self.waiter.pre_run(self):
			self.change_state("error")

	def post_waiting(self):
		if not self.waiter.run(self):
			self.change_state("error")
		else :
			self.change_state("running")

	def pre_running(self):
		if not self.runner.pre_run(self):
			self.change_state("error")

	def post_running(self):
		if not self.runner.run(self):
			self.change_state("error")
		else :
			self.change_state("resting")

	def pre_resting(self):
		if not self.rester.pre_run(self):
			self.change_state("error")

	def post_resting(self):
		if not self.rester.run(self):
			self.change_state("error")
		else :
			self.change_state("end")
