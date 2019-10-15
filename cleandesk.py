from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime
from pathlib import *

## Global variables: 
userdirectory = str(Path.home())
folder_to_track = '/Desktop'
folder_for_destination = '/Desktop/andy'
folder_destination = userdirectory + folder_for_destination
folder_to_track_path =  userdirectory + folder_to_track
##
class MyHandler(FileSystemEventHandler):
    
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track_path):
            i = 1
            # if is only needed when the destination folder is inside the folder to track
            if filename != 'kalle':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track_path + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" +year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track_path + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track_path + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track_path + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)


## TODO: redo all the directories and the extensions 

extensions_folders = {
#No name
    'noname' : folder_destination + "/Other/Uncategorized",
#Audio
    '.aif' : folder_destination + "/Media/Audio",
    '.cda' : folder_destination + "/Media/Audio",
    '.mid' : folder_destination + "/Media/Audio",
    '.midi' : folder_destination + "/Media/Audio",
    '.mp3' : folder_destination + "/Media/Audio",
    '.mpa' : folder_destination + "/Media/Audio",
    '.ogg' : folder_destination + "/Media/Audio",
    '.wav' : folder_destination + "/Media/Audio",
    '.wma' : folder_destination + "/Media/Audio",
    '.wpl' : folder_destination + "/Media/Audio",
    '.m3u' : folder_destination + "/Media/Audio",
#Text
    '.txt' : folder_destination + "/Text/TextFiles",
    '.doc' : folder_destination + "/Text/Microsoft/Word",
    '.docx' : folder_destination + "/Text/Microsoft/Word",
    '.odt ' : folder_destination + "/Text/TextFiles",
    '.pdf': folder_destination + "/Text/PDF",
    '.rtf': folder_destination + "/Text/TextFiles",
    '.tex': folder_destination + "/Text/TextFiles",
    '.wks ': folder_destination + "/Text/TextFiles",
    '.wps': folder_destination + "/Text/TextFiles",
    '.wpd': folder_destination + "/Text/TextFiles",
#Video
    '.3g2': folder_destination + "/Media/Video",
    '.3gp': folder_destination + "/Media/Video",
    '.avi': folder_destination + "/Media/Video",
    '.flv': folder_destination + "/Media/Video",
    '.h264': folder_destination + "/Media/Video",
    '.m4v': folder_destination + "/Media/Video",
    '.mkv': folder_destination + "/Media/Video",
    '.mov': folder_destination + "/Media/Video",
    '.mp4': folder_destination + "/Media/Video",
    '.mpg': folder_destination + "/Media/Video",
    '.mpeg': folder_destination + "/Media/Video",
    '.rm': folder_destination + "/Media/Video",
    '.swf': folder_destination + "/Media/Video",
    '.vob': folder_destination + "/Media/Video",
    '.wmv': folder_destination + "/Media/Video",
#Images
    '.ai': folder_destination + "/Media/Images",
    '.bmp': folder_destination + "/Media/Images",
    '.gif': folder_destination + "/Media/Images",
    '.ico': folder_destination + "/Media/Images",
    '.jpg': folder_destination + "/Media/Images",
    '.jpeg': folder_destination + "/Media/Images",
    '.png': folder_destination + "/Media/Images",
    '.ps': folder_destination + "/Media/Images",
    '.psd': folder_destination + "/Media/Images",
    '.svg': folder_destination + "/Media/Images",
    '.tif': folder_destination + "/Media/Images",
    '.tiff': folder_destination + "/Media/Images",
    '.CR2': folder_destination + "/Media/Images",
#Internet
    '.asp': folder_destination + "/Other/Internet",
    '.aspx': folder_destination + "/Other/Internet",
    '.cer': folder_destination + "/Other/Internet",
    '.cfm': folder_destination + "/Other/Internet",
    '.cgi': folder_destination + "/Other/Internet",
    '.pl': folder_destination + "/Other/Internet",
    '.css': folder_destination + "/Other/Internet",
    '.htm': folder_destination + "/Other/Internet",
    '.js': folder_destination + "/Other/Internet",
    '.jsp': folder_destination + "/Other/Internet",
    '.part': folder_destination + "/Other/Internet",
    '.php': folder_destination + "/Other/Internet",
    '.rss': folder_destination + "/Other/Internet",
    '.xhtml': folder_destination + "/Other/Internet",
#Compressed
    '.7z': folder_destination + "/Other/Compressed",
    '.arj': folder_destination + "/Other/Compressed",
    '.deb': folder_destination + "/Other/Compressed",
    '.pkg': folder_destination + "/Other/Compressed",
    '.rar': folder_destination + "/Other/Compressed",
    '.rpm': folder_destination + "/Other/Compressed",
    '.tar.gz': folder_destination + "/Other/Compressed",
    '.z': folder_destination + "/Other/Compressed",
    '.zip': folder_destination + "/Other/Compressed",
#Disc
    '.bin': folder_destination + "/Other/Disc",
    '.dmg': folder_destination + "/Other/Disc",
    '.iso': folder_destination + "/Other/Disc",
    '.toast': folder_destination + "/Other/Disc",
    '.vcd': folder_destination + "/Other/Disc",
#Data
    '.csv': folder_destination + "/Programming/Database",
    '.dat': folder_destination + "/Programming/Database",
    '.db': folder_destination + "/Programming/Database",
    '.dbf': folder_destination + "/Programming/Database",
    '.log': folder_destination + "/Programming/Database",
    '.mdb': folder_destination + "/Programming/Database",
    '.sav': folder_destination + "/Programming/Database",
    '.sql': folder_destination + "/Programming/Database",
    '.tar': folder_destination + "/Programming/Database",
    '.xml': folder_destination + "/Programming/Database",
    '.json': folder_destination + "/Programming/Database",
#Executables
    '.apk': folder_destination + "/Other/Executables",
    '.bat': folder_destination + "/Other/Executables",
    '.com': folder_destination + "/Other/Executables",
    '.exe': folder_destination + "/Other/Executables",
    '.gadget': folder_destination + "/Other/Executables",
    '.jar': folder_destination + "/Other/Executables",
    '.wsf': folder_destination + "/Other/Executables",
#Fonts
    '.fnt': folder_destination + "/Other/Fonts",
    '.fon': folder_destination + "/Other/Fonts",
    '.otf': folder_destination + "/Other/Fonts",
    '.ttf': folder_destination + "/Other/Fonts",
#Presentations
    '.key': folder_destination + "/Text/Presentations",
    '.odp': folder_destination + "/Text/Presentations",
    '.pps': folder_destination + "/Text/Presentations",
    '.ppt': folder_destination + "/Text/Presentations",
    '.pptx': folder_destination + "/Text/Presentations",
#Programming
    '.c': folder_destination + "/Programming/C&C++",
    '.class': folder_destination + "/Programming/Java",
    '.dart': folder_destination + "/Programming/Dart",
    '.py': folder_destination + "/Programming/Python",
    '.sh': folder_destination + "/Programming/Shell",
    '.swift': folder_destination + "/Programming/Swift",
    '.html': folder_destination + "/Programming/C&C++",
    '.h': folder_destination + "/Programming/C&C++",
#Spreadsheets
    '.ods' : folder_destination + "/Text/Microsoft/Excel",
    '.xlr' : folder_destination + "/Text/Microsoft/Excel",
    '.xls' : folder_destination + "/Text/Microsoft/Excel",
    '.xlsx' : folder_destination + "/Text/Microsoft/Excel",
#System
    '.bak' : folder_destination + "/Text/Other/System",
    '.cab' : folder_destination + "/Text/Other/System",
    '.cfg' : folder_destination + "/Text/Other/System",
    '.cpl' : folder_destination + "/Text/Other/System",
    '.cur' : folder_destination + "/Text/Other/System",
    '.dll' : folder_destination + "/Text/Other/System",
    '.dmp' : folder_destination + "/Text/Other/System",
    '.drv' : folder_destination + "/Text/Other/System",
    '.icns' : folder_destination + "/Text/Other/System",
    '.ico' : folder_destination + "/Text/Other/System",
    '.ini' : folder_destination + "/Text/Other/System",
    '.lnk' : folder_destination + "/Text/Other/System",
    '.msi' : folder_destination + "/Text/Other/System",
    '.sys' : folder_destination + "/Text/Other/System",
    '.tmp' : folder_destination + "/Text/Other/System",
}

    

if (not os.path.isdir(folder_destination)):
    print("Destination folder " + folder_destination + " doesn't exists")

for dir in extensions_folders:
    print(extensions_folders[dir])
    if not os.path.exists(extensions_folders[dir]):
        os.makedirs(extensions_folders[dir])
        


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track_path, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()