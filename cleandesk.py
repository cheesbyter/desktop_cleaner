from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime
from pathlib import *

global_userdirectory = str(Path.home())

class MyHandler(FileSystemEventHandler):
    
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'kalle':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
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
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)


## TODO: redo all the directories and the extensions 

extensions_folders = {
#No name
    'noname' : str(global_userdirectory) + "/Desktop/kalle/Other/Uncategorized",
#Audio
    '.aif' : str(global_userdirectory) + "/Desktop/kalle/Media/Audio",
    '.cda' : str(global_userdirectory) + "/Desktop/kalle/Media/Audio",
    '.mid' : str(global_userdirectory) + "/Desktop/kalle/Media/Audio",
    '.midi' : str(global_userdirectory) + "/Desktop/kalle/Media/Audio",
    '.mp3' : str(global_userdirectory) + "/Desktop/kalle/Media/Audio",
    '.mpa' : str(global_userdirectory) + "/Desktop/kalle/Media/Audio",
    '.ogg' : str(global_userdirectory) + "/Desktop/kalle/Media/Audio",
    '.wav' : str(global_userdirectory) + "/Desktop/kalle/Media/Audio",
    '.wma' : str(global_userdirectory) + "/Desktop/kalle/Media/Audio",
    '.wpl' : str(global_userdirectory) + "/Desktop/kalle/Media/Audio",
    '.m3u' : str(global_userdirectory) + "/Desktop/kalle/Media/Audio",
#Text
    '.txt' : str(global_userdirectory) + "/Desktop/kalle/Text/TextFiles",
    '.doc' : str(global_userdirectory) + "/Desktop/kalle/Text/Microsoft/Word",
    '.docx' : str(global_userdirectory) + "/Desktop/kalle/Text/Microsoft/Word",
    '.odt ' : str(global_userdirectory) + "/Desktop/kalle/Text/TextFiles",
    '.pdf': str(global_userdirectory) + "/Desktop/kalle/Text/PDF",
    '.rtf': str(global_userdirectory) + "/Desktop/kalle/Text/TextFiles",
    '.tex': str(global_userdirectory) + "/Desktop/kalle/Text/TextFiles",
    '.wks ': str(global_userdirectory) + "/Desktop/kalle/Text/TextFiles",
    '.wps': str(global_userdirectory) + "/Desktop/kalle/Text/TextFiles",
    '.wpd': str(global_userdirectory) + "/Desktop/kalle/Text/TextFiles",
#Video
    '.3g2': str(global_userdirectory) + "/Desktop/kalle/Media/Video",
    '.3gp': str(global_userdirectory) + "/Desktop/kalle/Media/Video",
    '.avi': str(global_userdirectory) + "/Desktop/kalle/Media/Video",
    '.flv': str(global_userdirectory) + "/Desktop/kalle/Media/Video",
    '.h264': str(global_userdirectory) + "/Desktop/kalle/Media/Video",
    '.m4v': str(global_userdirectory) + "/Desktop/kalle/Media/Video",
    '.mkv': str(global_userdirectory) + "/Desktop/kalle/Media/Video",
    '.mov': str(global_userdirectory) + "/Desktop/kalle/Media/Video",
    '.mp4': str(global_userdirectory) + "/Desktop/kalle/Media/Video",
    '.mpg': str(global_userdirectory) + "/Desktop/kalle/Media/Video",
    '.mpeg': str(global_userdirectory) + "/Desktop/kalle/Media/Video",
    '.rm': str(global_userdirectory) + "/Desktop/kalle/Media/Video",
    '.swf': str(global_userdirectory) + "/Desktop/kalle/Media/Video",
    '.vob': str(global_userdirectory) + "/Desktop/kalle/Media/Video",
    '.wmv': str(global_userdirectory) + "/Desktop/kalle/Media/Video",
#Images
    '.ai': str(global_userdirectory) + "/Desktop/kalle/Media/Images",
    '.bmp': str(global_userdirectory) + "/Desktop/kalle/Media/Images",
    '.gif': str(global_userdirectory) + "/Desktop/kalle/Media/Images",
    '.ico': str(global_userdirectory) + "/Desktop/kalle/Media/Images",
    '.jpg': str(global_userdirectory) + "/Desktop/kalle/Media/Images",
    '.jpeg': str(global_userdirectory) + "/Desktop/kalle/Media/Images",
    '.png': str(global_userdirectory) + "/Desktop/kalle/Media/Images",
    '.ps': str(global_userdirectory) + "/Desktop/kalle/Media/Images",
    '.psd': str(global_userdirectory) + "/Desktop/kalle/Media/Images",
    '.svg': str(global_userdirectory) + "/Desktop/kalle/Media/Images",
    '.tif': str(global_userdirectory) + "/Desktop/kalle/Media/Images",
    '.tiff': str(global_userdirectory) + "/Desktop/kalle/Media/Images",
    '.CR2': str(global_userdirectory) + "/Desktop/kalle/Media/Images",
#Internet
    '.asp': str(global_userdirectory) + "/Desktop/kalle/Other/Internet",
    '.aspx': str(global_userdirectory) + "/Desktop/kalle/Other/Internet",
    '.cer': str(global_userdirectory) + "/Desktop/kalle/Other/Internet",
    '.cfm': str(global_userdirectory) + "/Desktop/kalle/Other/Internet",
    '.cgi': str(global_userdirectory) + "/Desktop/kalle/Other/Internet",
    '.pl': str(global_userdirectory) + "/Desktop/kalle/Other/Internet",
    '.css': str(global_userdirectory) + "/Desktop/kalle/Other/Internet",
    '.htm': str(global_userdirectory) + "/Desktop/kalle/Other/Internet",
    '.js': str(global_userdirectory) + "/Desktop/kalle/Other/Internet",
    '.jsp': str(global_userdirectory) + "/Desktop/kalle/Other/Internet",
    '.part': str(global_userdirectory) + "/Desktop/kalle/Other/Internet",
    '.php': str(global_userdirectory) + "/Desktop/kalle/Other/Internet",
    '.rss': str(global_userdirectory) + "/Desktop/kalle/Other/Internet",
    '.xhtml': str(global_userdirectory) + "/Desktop/kalle/Other/Internet",
#Compressed
    '.7z': str(global_userdirectory) + "/Desktop/kalle/Other/Compressed",
    '.arj': str(global_userdirectory) + "/Desktop/kalle/Other/Compressed",
    '.deb': str(global_userdirectory) + "/Desktop/kalle/Other/Compressed",
    '.pkg': str(global_userdirectory) + "/Desktop/kalle/Other/Compressed",
    '.rar': str(global_userdirectory) + "/Desktop/kalle/Other/Compressed",
    '.rpm': str(global_userdirectory) + "/Desktop/kalle/Other/Compressed",
    '.tar.gz': str(global_userdirectory) + "/Desktop/kalle/Other/Compressed",
    '.z': str(global_userdirectory) + "/Desktop/kalle/Other/Compressed",
    '.zip': str(global_userdirectory) + "/Desktop/kalle/Other/Compressed",
#Disc
    '.bin': str(global_userdirectory) + "/Desktop/kalle/Other/Disc",
    '.dmg': str(global_userdirectory) + "/Desktop/kalle/Other/Disc",
    '.iso': str(global_userdirectory) + "/Desktop/kalle/Other/Disc",
    '.toast': str(global_userdirectory) + "/Desktop/kalle/Other/Disc",
    '.vcd': str(global_userdirectory) + "/Desktop/kalle/Other/Disc",
#Data
    '.csv': str(global_userdirectory) + "/Desktop/kalle/Programming/Database",
    '.dat': str(global_userdirectory) + "/Desktop/kalle/Programming/Database",
    '.db': str(global_userdirectory) + "/Desktop/kalle/Programming/Database",
    '.dbf': str(global_userdirectory) + "/Desktop/kalle/Programming/Database",
    '.log': str(global_userdirectory) + "/Desktop/kalle/Programming/Database",
    '.mdb': str(global_userdirectory) + "/Desktop/kalle/Programming/Database",
    '.sav': str(global_userdirectory) + "/Desktop/kalle/Programming/Database",
    '.sql': str(global_userdirectory) + "/Desktop/kalle/Programming/Database",
    '.tar': str(global_userdirectory) + "/Desktop/kalle/Programming/Database",
    '.xml': str(global_userdirectory) + "/Desktop/kalle/Programming/Database",
    '.json': str(global_userdirectory) + "/Desktop/kalle/Programming/Database",
#Executables
    '.apk': str(global_userdirectory) + "/Desktop/kalle/Other/Executables",
    '.bat': str(global_userdirectory) + "/Desktop/kalle/Other/Executables",
    '.com': str(global_userdirectory) + "/Desktop/kalle/Other/Executables",
    '.exe': str(global_userdirectory) + "/Desktop/kalle/Other/Executables",
    '.gadget': global_userdirectory + "/Desktop/kalle/Other/Executables",
    '.jar': str(global_userdirectory) + "/Desktop/kalle/Other/Executables",
    '.wsf': str(global_userdirectory) + "/Desktop/kalle/Other/Executables",
#Fonts
    '.fnt': str(global_userdirectory) + "/Desktop/kalle/Other/Fonts",
    '.fon': str(global_userdirectory) + "/Desktop/kalle/Other/Fonts",
    '.otf': str(global_userdirectory) + "/Desktop/kalle/Other/Fonts",
    '.ttf': str(global_userdirectory) + "/Desktop/kalle/Other/Fonts",
#Presentations
    '.key': str(global_userdirectory) + "/Desktop/kalle/Text/Presentations",
    '.odp': str(global_userdirectory) + "/Desktop/kalle/Text/Presentations",
    '.pps': str(global_userdirectory) + "/Desktop/kalle/Text/Presentations",
    '.ppt': str(global_userdirectory) + "/Desktop/kalle/Text/Presentations",
    '.pptx': str(global_userdirectory) + "/Desktop/kalle/Text/Presentations",
#Programming
    '.c': str(global_userdirectory) + "/Desktop/kalle/Programming/C&C++",
    '.class': str(global_userdirectory) + "/Desktop/kalle/Programming/Java",
    '.dart': str(global_userdirectory) + "/Desktop/kalle/Programming/Dart",
    '.py': str(global_userdirectory) + "/Desktop/kalle/Programming/Python",
    '.sh': str(global_userdirectory) + "/Desktop/kalle/Programming/Shell",
    '.swift': str(global_userdirectory) + "/Desktop/kalle/Programming/Swift",
    '.html': str(global_userdirectory) + "/Desktop/kalle/Programming/C&C++",
    '.h': str(global_userdirectory) + "/Desktop/kalle/Programming/C&C++",
#Spreadsheets
    '.ods' : str(global_userdirectory) + "/Desktop/kalle/Text/Microsoft/Excel",
    '.xlr' : str(global_userdirectory) + "/Desktop/kalle/Text/Microsoft/Excel",
    '.xls' : str(global_userdirectory) + "/Desktop/kalle/Text/Microsoft/Excel",
    '.xlsx' : str(global_userdirectory) + "/Desktop/kalle/Text/Microsoft/Excel",
#System
    '.bak' : str(global_userdirectory) + "/Desktop/kalle/Text/Other/System",
    '.cab' : str(global_userdirectory) + "/Desktop/kalle/Text/Other/System",
    '.cfg' : str(global_userdirectory) + "/Desktop/kalle/Text/Other/System",
    '.cpl' : str(global_userdirectory) + "/Desktop/kalle/Text/Other/System",
    '.cur' : str(global_userdirectory) + "/Desktop/kalle/Text/Other/System",
    '.dll' : str(global_userdirectory) + "/Desktop/kalle/Text/Other/System",
    '.dmp' : str(global_userdirectory) + "/Desktop/kalle/Text/Other/System",
    '.drv' : str(global_userdirectory) + "/Desktop/kalle/Text/Other/System",
    '.icns' : str(global_userdirectory) + "/Desktop/kalle/Text/Other/System",
    '.ico' : str(global_userdirectory) + "/Desktop/kalle/Text/Other/System",
    '.ini' : str(global_userdirectory) + "/Desktop/kalle/Text/Other/System",
    '.lnk' : str(global_userdirectory) + "/Desktop/kalle/Text/Other/System",
    '.msi' : str(global_userdirectory) + "/Desktop/kalle/Text/Other/System",
    '.sys' : str(global_userdirectory) + "/Desktop/kalle/Text/Other/System",
    '.tmp' : str(global_userdirectory) + "/Desktop/kalle/Text/Other/System",
}

    
folder_to_track = global_userdirectory + '/Desktop'
folder_destination = global_userdirectory + '/Desktop/kalle'

if (not os.path.isdir(folder_destination)):
    print(folder_destination + " to observe doesn't exists")

for dir in extensions_folders:
    print(extensions_folders[dir])
    if not os.path.exists(extensions_folders[dir]):
        os.makedirs(extensions_folders[dir])
        


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()