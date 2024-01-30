import socket
import platform
import os
import psutil

print("Exercice 1 : Socket")
def afficher_info_system():
    print(f"HostName: {socket.gethostname()}")
    print(f"Adresse ip : {socket.gethostbyname(socket.gethostname())}")    
    print(f"Architecture: {platform.architecture()}")
    print(f"Operating system: {platform.platform()}")
    return 1

afficher_info_system()

print("Exercice 2 : Os")

def afficher_infos_dossier(file=""):
    files = []
    for dir in os.listdir(file):
        full_path = os.path.join(file, dir)
        stats = os.stat(full_path)       
        details = (full_path, stats.st_size)
        files.append(details)
    return files

print(afficher_infos_dossier(r"C:\Users\itaka\Documents\CROCHEMORE_Johan"))

print("Exercice 3 : Psutil")

print(psutil.virtual_memory())