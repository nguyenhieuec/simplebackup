
import os
import time
from shutil import copyfile
from shutil import copytree
from datetime import datetime, timedelta
from watchdog.events import FileSystemEventHandler

from PIL import Image
from PIL.ImageOps import grayscale
from watchdog.events import RegexMatchingEventHandler


class Backup(FileSystemEventHandler):
    FILE_REGEX = [r".*.xml$"]
    BACKUP_PATH = '..' + '/BACKUP'
    SNAPSHOT_PATH = ''
    # change the source when deploy
    SOURCE_PATH = ''



    
    def __init__(self):

        # super().__init__()

        self.__checkpoint_daily = str(datetime.now())
        self.SNAPSHOT_PATH = '..' + str(datetime.now())
        self.snapshot()

    def on_created(self, event):
        print("file created")
        file_size = -1
        while file_size != os.path.getsize(event.src_path):
            file_size = os.path.getsize(event.src_path)
            time.sleep(1)

        self.process(event)

    def on_modified(self, event):
        print("file modified")
        file_size = -1
        while file_size != os.path.getsize(event.src_path):
            file_size = os.path.getsize(event.src_path)
            time.sleep(1)

        self.process(event)

    def process(self, event):
        print('backup file')
        print(event.src_path)
        print(self.BACKUP_PATH)
        _, ext = os.path.splitext(event.src_path)
        print(_, ext)
        if not os.path.exists(self.BACKUP_PATH):
            os.makedirs(self.BACKUP_PATH)
        if ext == '.xml':
            print('copy file')
            _ = _.replace('.','')
            dst = os.path.join(os.path.abspath(os.path.join('.', '..')), 'BACKUP') + _ + str(datetime.now()) + ext
            copyfile(event.src_path, dst)

    def snapshot(self): 
        SNAPSHOT_PATH = os.path.join(os.path.abspath(os.path.join('.', '..')), 'BACKUP') + str(datetime.now())
        ### deploy please comment this section
        self.SOURCE_PATH = os.getcwd()
        ###
        copytree(self.SOURCE_PATH, SNAPSHOT_PATH) 
