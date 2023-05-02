from pickle import FALSE
import sys, Ice, os
import Demo
import vlc


import sqlite3

connectionDatabase = sqlite3.connect('DataBase.db', check_same_thread=False)
parcourirBDD = connectionDatabase.cursor()



instaciation = vlc.Instance()
start = instaciation.media_player_new()
current_musique=False
musique_tab=[]
title=''



class PrinterI(Demo.Printer):
    
    def GetNumberOfMusics(self,current=None):
        i=0
        parcourirBDD.execute("SELECT COUNT(*) FROM Musiques")
        for row in parcourirBDD:
            i+=row[0]
        return(i)



    def GetMusiques(self, i, current=None):

        bdd_musique_tab=[]
        parcourirBDD.execute("SELECT Titre, Artistes, Album, UrlStream FROM Musiques LIMIT 1 OFFSET " + str(i))
        for row in parcourirBDD:
            print(row[0], ' ', row[1],' ', row[2],' ', row[3])
            bdd_musique_tab.append(str(row[0]))
            #print(bdd_musique_tab[0])
            bdd_musique_tab.append(str(row[1]))
            #print(bdd_musique_tab[1])
            bdd_musique_tab.append(str(row[2]))
            bdd_musique_tab.append(str(row[3]))
            #print(bdd_musique_tab[0], ' ', bdd_musique_tab[1],' ', bdd_musique_tab[2],' ', bdd_musique_tab[3])
        return bdd_musique_tab



    def AjtMusique(self,offset,musique_tab:bytes, path, title, artistes, album, current=None):
        
        #Création du fichier sur le pc
        addmusique = open(path,'ab+')
        addmusique.seek(offset)
        addmusique.write(musique_tab)
        addmusique.close()

    def AjtMusiqueDatabase(self, title, artistes, album, current=None):
        #Création du fichier dans la bdd
        urlStream = "http://localhost:3000/getMusic/"+title.replace(" ",'')
        parcourirBDD.execute("INSERT INTO Musiques(Titre,Artistes,Album,UrlStream) VALUES(?,?,?,?) ", (title,artistes,album,urlStream))
        connectionDatabase.commit()
        print("Musique ajoutée !")

        #Modifier une music

    #def ModifyMusic(self,musiqueAModifier,  nouveauTitre,  nouveauxArtistes, nouvelAlbum, current=None):
    #    if nouveauTitre:
    #        parcourirBDD.execute("UPDATE Musiques SET Titre=? WHERE Titre=?", (nouveauTitre,musiqueAModifier))
    #        connectionDatabase.commit()
    #        old_file = os.path.join("/Users/ACER/Desktop/cours/Master/M1/S2/Architecture distributé/middlware/ice/Musiques/", musiqueAModifier+".mp3")
    #        new_file = os.path.join("/Users/ACER/Desktop/cours/Master/M1/S2/Architecture distributé/middlware/ice/Musiques/", nouveauTitre+".mp3")
    #        os.rename(old_file, new_file)
    #    if nouveauxArtistes:
    #        parcourirBDD.execute("UPDATE Musiques SET Artistes=? WHERE Titre=?", (nouveauxArtistes,musiqueAModifier))
    #        connectionDatabase.commit()
    #    if nouvelAlbum:
    #        parcourirBDD.execute("UPDATE Musiques SET Album=? WHERE Titre=?", (nouvelAlbum,musiqueAModifier))
    #        connectionDatabase.commit()    





    def ModifMusique(self, musiqueAModifier, nouveauTitre=None, nouveauxArtistes=None, nouvelAlbum=None, current=None):
        update_values = {}
        if nouveauTitre:
            update_values["Titre"] = nouveauTitre
        if nouveauxArtistes:
            update_values["Artistes"] = nouveauxArtistes
        if nouvelAlbum:
            update_values["Album"] = nouvelAlbum

        if update_values:
            update_query = "UPDATE Musiques SET " + ", ".join([f"{k} = ?" for k in update_values.keys()]) + " WHERE Titre = ?"
            update_params = list(update_values.values()) + [musiqueAModifier]
            parcourirBDD.execute(update_query, update_params)
            connectionDatabase.commit()

            # Renommer le fichier correspondant
            old_file = os.path.join("/Users/ACER/Desktop/cours/Master/M1/S2/Architecture distributé/middlware/ice/Musiques/", musiqueAModifier+".mp3")
            new_file = os.path.join("/Users/ACER/Desktop/cours/Master/M1/S2/Architecture distributé/middlware/ice/Musiques/", nouveauTitre+".mp3")
            os.rename(old_file, new_file)

            # Mettre à jour l'URL de streaming si nécessaire
        if nouveauTitre:
            urlStream = f"http://localhost:3000/getMusic/{nouveauTitre}"
            parcourirBDD.execute("UPDATE Musiques SET UrlStream = ? WHERE Titre = ?", (urlStream, nouveauTitre))
            connectionDatabase.commit()

        print("La musique a été modifiée avec succès.")




        # Delete Music


    def DeleteMusic(self, s, current=None):
        print("/Users/ACER/Desktop/cours/Master/M1/S2/Architecture distributé/middlware/ice/Musiques/"+s+".mp3")
        if os.path.exists("/Users/ACER/Desktop/cours/Master/M1/S2/Architecture distributé/middlware/ice/Musiques/"+s+".mp3"):
            parcourirBDD.execute("DELETE FROM Musiques WHERE Titre=?", (s,))
            connectionDatabase.commit()
            os.remove("/Users/ACER/Desktop/cours/Master/M1/S2/Architecture distributé/middlware/ice/Musiques/"+s+".mp3")
            print("Musique ", s+".mp3"," supprimée avec succees")


        # Recherche Artiste

    def SearchArtist(self, s, current=None):
        Artistes=[]
        parcourirBDD.execute("SELECT Titre, Artistes, Album FROM Musiques WHERE Artistes LIKE '%"+s+"%' ORDER BY Artistes")
        for row in parcourirBDD:
            print(row[0])
            Artistes.append("Titre : " +row[0] + " artiste(s) : " + row[1] + " album : "+ row[2])
            #Artistes.append(row[1])
            #Artistes.append(row[2])
        return Artistes

        # Recherche Titre 
    def SearchTitle(self, s ,current=None):
        Titres=[]
        parcourirBDD.execute("SELECT Titre, Artistes, Album FROM Musiques WHERE Titre LIKE '%"+s+"%' ORDER BY Titre")
        for row in parcourirBDD:
            print(row[0])
            Titres.append("Titre : " +row[0] + " artiste(s) : " + row[1] + " album : "+ row[2])
        return Titres

        #lancer music
    def Play(self, s, current=None): 
        global current_musique
        if current_musique:
            start.play()
        else:
            file_path = 'C:/Users/ACER/Desktop/cours/Master/M1/S2/Architecture distributé/middlware/ice/Musiques/'+s+'.mp3'
            if not os.path.isfile(file_path):
                print("Le fichier n'existe pas ou n'est pas accessible en lecture pour le serveur.")
                return False
            media = instaciation.media_new(file_path)
            # media.add_option("sout=#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100,scodec=none}:http{mux=mp3,dst=:3000/"+s.replace(".mp3",'').replace(" ",'')+"}")
            media.add_option(":sout=#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100,scodec=none}:http{mux=mp3,dst=:3000/}")
            media.add_option(":no-sout-all")
            media.add_option(":sout-keep")
            start.set_media(media)
            start.play()
            current_musique=True
            print(media.get_mrl())
            print("Musique en cours : "+s.replace(".mp3",''))
        return current_musique

        # mettre la music en pause 

    def Pause(self, current=None):
        start.pause()
        return ("La musique a été mise en pause ")

        #arreter la music

    def Stop(self, current=None):
        global current_musique
        start.stop()
        current_musique=False
        print("music arreter")
        return current_musique


with Ice.initialize(sys.argv) as communicator:
    # adapter = communicator.createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 10000")
    adapter = communicator.createObjectAdapterWithEndpoints("SimplePrinterAdapter", "tcp -h 10.126.2.115 -p 10000")
    object = PrinterI()
    adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
    adapter.activate()
    communicator.waitForShutdown()





