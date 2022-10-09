class InitializeRepository:
    def __init__(self) :
        self.baseJSON = {}
        self.spotifySongURL = ""
        self.spotifyPlaylistURL = ""
        self.youtubeVideoURL = ""
        self.youtubePlaylistURL = ""
        self.downloadPath = ""
        self.listOfTrackObjects = []
        self.playlist = []
        
    def getBaseJSON(self):
        return self.baseJSON
    
    def getSpotifySongURL(self):
        return self.spotifySongURL
    
    def getSpotifyPlaylistURL(self) :
        return self.spotifyPlaylistURL
    
    def getYoutubeVideoURL(self):
        return self.youtubeVideoURL
    
    def getYoutubePlaylistURL(self) :
        return self.youtubePlaylistURL
    
    def getDownloadPath(self):
        return self.downloadPath
    
    def getPlaylist(self):
        return self.playlist
    
    def getListOfTrackObjects(self):
        return self.listOfTrackObjects
    
    def setBaseJSON(self, baseJSON) :
        self.baseJSON = baseJSON
        
    def setSpotifySongURL(self, spotifySongURL):
        self.spotifySongURL = spotifySongURL
    
    def setSpotifyPlaylistURL(self, spotifyPlaylistURL) :
        self.spotifyPlaylistURL = spotifyPlaylistURL
    
    def setYoutubeVideoURL(self, youtubeVideoURL):
        self.youtubeVideoURL = youtubeVideoURL
    
    def setYoutubePlaylistURL(self, youtubePlaylistURL) :
        self.youtubePlaylistURL = youtubePlaylistURL
        
    def setDownloadPath(self, downloadPath) :
        self.downloadPath = downloadPath
        
    def setPlaylist(self, playlist) :
        self.playlist = playlist
        
    def setListOfTrackObjects(self, listOfTrackObjects) :
        self.listOfTrackObjects = listOfTrackObjects