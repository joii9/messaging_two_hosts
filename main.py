import time
from watchdog.observers import Observer

from observer import MyEventHandler
from messaging_two_hosts import MainWindow


main_window = MainWindow()
main_window.create_greeting("Iniciaste un chat con ... por favor saluda")
main_window.create_inbox_message()
main_window.create_viewer_text()



observer = Observer() 
observer.schedule(MyEventHandler(main_window), "X:/test_messaging/", recursive=True) #Directorio monitoreado
observer.start()
main_window.show()
while observer.is_alive():
    time.sleep(1)
    observer.join(1)
observer.stop()
observer.join()

