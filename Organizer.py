import os
import time

def organize():
    for directory in ('Imagenes', 'Documentos', 'Videos', 'Otros'):
        if not os.path.exists(directory):
            os.mkdir(directory)

    for file in ARCHIVOS:
        if file.endswith(('.jpg', '.png', '.jpeg', '.gif', '.webp', '.ico')):
            os.rename(file, 'Imagenes/' + file)
        elif file.endswith(('.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx')):
            os.rename(file, 'Documentos/' + file)	
        elif file.endswith(('.mp4', '.mkv')):
            os.rename(file, 'Videos/' + file)
        elif not os.path.isdir(file):
            os.rename(file, 'Otros/' + file)

def count(seconds):
    while seconds > 0:
        time.sleep(1)
        seconds-=1
    organize()

while(True):
    ruta = os.path.expanduser("~") + "/Downloads"

    ARCHIVOS = os.listdir(ruta)

    os.chdir(ruta)

    count(20)