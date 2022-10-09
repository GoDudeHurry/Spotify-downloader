# This class extracts the links, titles and all necessary parameters required 
# to download files

import sys

sys.path.insert(0, "../Data")

import IndividualFile

class Compiler :
    def __init__(self) :
        self.playlist = []
        
    def getPlaylist(self) :
        return self.playlist
    
    def setPlaylist(self, playlist) :
        self.playlist = playlist
        
    def extractIndividualFileData(self, repository) :
        base = repository.getBaseJSON()
        if base != {} :
            for i in range(len(base)) :
                eachTrack = IndividualFile.Track()
                eachTrack.setMediaURL(base[i]["track"]["external_playback_url"])
                eachTrack.setMediaType(".mp3")
                eachTrack.setTitle(base[i]["track"]["name"])
                repository.playlist.append(eachTrack.__dict__)
            
        else :
            print("\nErr : BaseJSON is empty !!!")
            
        