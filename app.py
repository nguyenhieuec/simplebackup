import sys
import time
import logging

from datetime import datetime, timedelta
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from events import Backup

class Monitor():
    def __init__(self, src_path):
        self.__src_path = src_path
        super().__init__()
        self.__event_handler = Backup()
        self.__event_observer = Observer()
        self.check_point = datetime.now()
        
    def run(self):
        self.start()
        try:
            while True:
                time.sleep(1)
                now = datetime.now()
                if now-timedelta(hours=24) == self.check_point:
                    self.__event_handler.snapshot()
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()


    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__src_path,
            recursive=True
        )

    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # Source is the path of the folder you want to backup
    # dst is the path to backup
    # snapshot is entire folder backup
    source = '.'
    bk = Monitor(source)
    bk.run()
    