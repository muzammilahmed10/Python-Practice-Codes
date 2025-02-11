import threading
import time

def background_task():
    while True:
        time.sleep(1)
        print("Background task running")
        

thread = threading.Thread(target=background_task)
thread.daemon = True
thread.start()

time.sleep(4)
print("Main program ends.")