import farm2
from flask import Flask

import threading

import time

f = farm2.Farm2()

app = Flask(__name__)

@app.route('/')
def index():
	return f.state

def run_api():
	app.run()

if __name__ == '__main__' :
	# thread_1_t = threading.Thread(target = run_api)
	# thread_1_t.start()
	print("iniciado loop fsm")
	while True :
		f = farm2.Farm2()
		f.change_state("waiting")
		print("dormindo por 10s")
		time.sleep(10)
		print("end loop")

