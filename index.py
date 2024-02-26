"""
Trieur de Fichiers © 2023 Marvideo est autorisé en vertu CC BY-NC-ND 4.0 
"""

import os
import shutil
from os import listdir
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import tkinter.filedialog
import json
import time

base_config = '''
{
    "version": "0.0.2",
    "title": "Trieur de fichiers",
    "author": "Marvideo",
    "dir_abslink": {
        "textes": "/Documents",
        "images": "/Images",
        "videos": "/Videos",
        "logiciels": "/Téléchargements",
        "archives": "/Documents/Archive",
        "musiques": "/Musique",
        "autres": "/Documents/Autre"
    },
    "ext_text": ["txt", "odt", "docx", "doc", "sh3d", "ods", "odg", "odb", "odp", "pdf", "pages", "wpd", "tex", "log", "markdown", "md", "csv", "json", "xml", "html", "rtf"],
    "ext_image": ["jpeg", "jpg", "png", "psd", "gif", "tif", "svg", "bmp", "ico", "raw", "webp", "exif", "ai", "eps", "rif", "riff"],
    "ext_video": ["mp4", "avi", "mov", "flv", "mkv", "wmv", "wmv", "mpeg", "mpg", "m4v", "webm", "3gp", "rmvb", "vob", "ts", "divx", "ogv"],
    "ext_logiciel": ["msi", "exe", "bat", "AppImage", "dmg", "app", "msi", "deb", "rpm", "jar", "apk", "run", "sh", "bin", "tar"],
    "ext_archive": ["zip", "rar", "iso", "7z", "gz", "bz2", "xz", "z", "arj", "lzh", "cab", "nrg", "pkg"],
    "ext_musique": ["flac", "wav", "mp3", "mscz", "aac", "wma", "ogg", "m4a", "ac3", "mid", "midi", "amr", "ape", "alac", "pcm", "au"],
    "msg": [{
        "success": "Votre dossier est bien rangé :D ",
        "whatdir": "Dans quel dossier voulez vous trier ?",
        "contentdir": "Voici le contenu du dossier %s :",
        "verify": "Etes vous sûr de ranger le dossier %s ???",
        "stopapp": "Le processus s'arrete."
    }]
}
'''

class config_class:
    def main_config(self):
        if(os.path.exists("config.json")):
            return config_class.load_config()
        else:
            config_class.create_config()

    def create_config(self):
        with open("config.json", "w", encoding ='utf8') as config_file:
            config_file.write(base_config)
            config_file.close()
            createconfig_window = Tk(className='Trieur de fichiers by Marvideo')
            messagebox.showinfo("Trieur de fichiers","La configuration a été creer !!\nRelance l'application pour que la nouvelle configuration soit prise en compte")
            exit()

    def load_config(self):
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
        return config

class DirCleaner:
    def cleaner(self, path):
        os.chdir(path)
        get_dir = os.getcwd()   #Avoir le chemin du "current directory"
        #création des dossiers
        textes = os.getcwd() + config["dir_abslink"]["textes"]
        images = os.getcwd() + config["dir_abslink"]["images"]
        videos = os.getcwd() + config["dir_abslink"]["videos"]
        logiciels = os.getcwd() + config["dir_abslink"]["logiciels"]
        archives = os.getcwd() + config["dir_abslink"]["archives"]
        musiques = os.getcwd() + config["dir_abslink"]["musiques"]
        autres = os.getcwd() + config["dir_abslink"]["autres"]

        texte = config["ext_text"]
        moveintext = []
        image = config["ext_image"]
        moveinimage = []
        video = config["ext_video"]
        moveinvideo = []
        logiciel = config["ext_logiciel"]
        moveinlogiciel = []
        archive = config["ext_archive"]
        moveinarchive = []
        musique = config["ext_musique"]
        moveinmusique = []
        moveinother = []
        #shutil.move(new_path,pdfs)
        #Ici nous allons parcourir les fichiers qui sont dans le dossier et les sous-dossiers du répértoir actuel
        for chemin, sous_rep, fichiers in os.walk(get_dir):
            for fichier in fichiers :
                new_path = os.path.join(chemin, fichier)
                if(new_path == os.path.abspath(__file__) or new_path == os.path.abspath("config.json")):
                    continue
                #Selon l'extention du fichier, nous allons le placer dans le dossier approprié
                succes = False
                for extension in texte:
                    if new_path.endswith(extension):
                        moveintext.append(new_path)
                        succes = True
                    else:
                        continue

                for extension in image:
                    if new_path.endswith(extension):
                        moveinimage.append(new_path)
                        succes = True
                    else:
                        continue

                for extension in video:
                    if new_path.endswith(extension):
                        moveinvideo.append(new_path)
                        succes = True
                    else:
                        continue

                for extension in logiciel:
                    if new_path.endswith(extension):
                        moveinlogiciel.append(new_path)
                        succes = True
                    else:
                        continue

                for extension in archive:
                    if new_path.endswith(extension):
                        moveinarchive.append(new_path)
                        succes = True
                    else:
                        continue

                for extension in musique:
                    if new_path.endswith(extension):
                        moveinmusique.append(new_path)
                        succes = True
                    else:
                        continue
                if(succes == False):
                    moveinother.append(new_path)
            for dossier  in sous_rep:
                #print("nous cherchons dans le dossier : ", dossier + " ... \n ")
                continue
        if(len(moveinvideo) == 0):
            print("")
        else:
            try:
                os.mkdir(videos)
            except: pass

        if(len(moveintext) == 0):
            pass
        else:
            try:
                os.mkdir(textes)
            except: pass

        if(len(moveinlogiciel) == 0):
            pass
        else:
            try:
                os.mkdir(logiciels)
            except: pass

        if(len(moveinimage) == 0):
            pass
        else:
            try:
                os.mkdir(images)
            except: pass

        if(len(moveinarchive) == 0):
            pass
        else:
            try:
                os.mkdir(archives)
            except: pass

        if(len(moveinmusique) == 0):
            pass
        else:
            try:
                os.mkdir(musiques)
            except: pass

        if(len(moveinother) == 0):
            pass
        else:
            try:
                os.mkdir(autres)
            except: pass

        for file in moveintext:
            shutil.move(file,textes)

        for file in moveinimage:
            shutil.move(file, images)

        for file in moveinvideo:
            shutil.move(file, videos)

        for file in moveinlogiciel:
            shutil.move(file, logiciels)

        for file in moveinarchive:
            shutil.move(file, archives)

        for file in moveinmusique:
            shutil.move(file, musiques)

        for file in moveinother:
            shutil.move(file, autres)

        #print("Votre dossier est bien ranger :D ")
        #print("Code by Marvideo")
        messagebox.showinfo(config["title"],config["msg"][0]["success"]+"\n  Code by %s" % config["author"])
        exit()

if __name__ == "__main__":
    config_class = config_class()
    config = config_class.main_config()
    InstanceOfCleaner = DirCleaner()
    window = Tk(className='%s by %s' % (config["title"], config["author"]))
    chemin = os.getcwd()
    #dir = input("Dans quelle dossier voulez vous triez ? (Laisser vide si : '%s' est le bon dossier) \n" % chemin)

    #dir = simpledialog.askstring("Trieur de fichiers", "Dans quelle dossier voulez vous triez ?",parent=window)

    dir = tkinter.filedialog.askdirectory(parent=window,initialdir="/",title=config["msg"][0]["whatdir"])
    if dir == "":
        chemin = os.getcwd()
    else:
        chemin = dir

    listfichier = ""

    for file in listdir(chemin):
        if(file == "prod.py"):
            pass
        else:
            if(len(file) > 35):
                fichier = os.path.splitext(file)
                nom_fichier = fichier[0]
                ext_fichier = fichier[1]
                file = nom_fichier[0:20] + "... " + ext_fichier
            listfichier = "%s- %s \n" % (listfichier, file)
    messagebox.showinfo(config["title"],config["msg"][0]["contentdir"] % chemin+"\n%s" % listfichier)
    verify = messagebox.askyesno(config["title"], config["msg"][0]["verify"] % chemin)
    if verify == True:
        #messagebox.showinfo('Trieur de fichiers',)
        InstanceOfCleaner.cleaner(chemin)
    else:
        messagebox.showinfo(config["title"], config["msg"][0]["stopapp"])
        exit()

    #print("Voici le contenu du dossier %s : \n     %s \n" % (chemin,listdir(chemin)))
    #verify = input("Etes vous sur de ranger le dossier %s ??? (O/N) : " % chemin)

    #if(verify == "N" or verify == "n"):
        #print("Le processus s'arrete.")
        #exit()
    #elif(verify == "O" or verify == "o"):
        #if(dir == ""):
            #InstanceOfCleaner.cleaner(os.getcwd())
        #else:
            #InstanceOfCleaner.cleaner(dir)
    #else:
        #print("Veuillez rentrez O ou N et non %s" % verify)
        #print("Tu dois reouvrir le programme pour recommencer.")
    window.mainloop()