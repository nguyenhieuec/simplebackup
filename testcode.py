from shutil import copytree
from datetime import datetime
import os

path = '/Users/hieuqcf/PycharmProjects/BACKUP/' + str(datetime.now())

copytree(os.getcwd(), path)