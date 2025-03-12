
import os

#from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from messaging_two_hosts import *

global current_size

file_name="X:\\test_messaging\\logs_messages.txt"
file_stats = os.stat(file_name)
current_size=file_stats.st_size #/ (1024 * 1024)
print(f'1. File Size in Bytes is {current_size}')

class MyEventHandler(FileSystemEventHandler):
    def __init__(self, main_window):
        self.main_window=main_window
    def on_modified(self, event): #self.main_window=main_window
        global current_size
        file_name_modified="X:/test_messaging/logs_messages.txt"
        file_stats_wd = os.stat(file_name_modified)
        new_size= file_stats_wd.st_size
        print(f'New size: {new_size}')
        if file_name_modified:
            if new_size > current_size:
                print("Estas dentro del IF")
                current_size=new_size
                self.main_window.viewer_text.destroy()
                self.main_window.create_viewer_text()
                print("Lo hizo")


#observer = Observer() 
#observer.schedule(MyEventHandler(), "X:/test_messaging/", recursive=True) #Directorio monitoreado
#observer.start()
#while observer.is_alive():
#    observer.join(1)
#observer.stop()
#observer.join()
