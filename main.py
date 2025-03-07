from watchdog.observers import Observer
import time
from messaging_two_hosts import MainWindow
from observer import MyEventHandler

global current_size


observer =Observer()
observer.schedule(MyEventHandler(), "X:/test_messaging/", recursive=False) #Directorio monitoreado, MyEventHandler(main_window) 
observer.start()

try:
    while True:
            # Set the thread sleep time
            time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    observer.join()


#main_window = MainWindow()
#main_window.create_greeting("Iniciaste un chat con ... por favor saluda")
#main_window.create_inbox_message()
#main_window.create_viewer_text()
#main_window.show()