# This class has all properties needed to download an individual file

class Track :
    def __init__(self) :
        self.mediaType = ".unspecified"
        self.mediaURL = "<URL empty>"
        self.title = "Unknown media"
        self.proceedToDownload = False
        self.downloadable = False
        self.downloaded = False
        
    def getMediaType(self) :
        return self.mediaType
    
    def getMediaURL(self) :
        return self.mediaURL
    
    def getTitle(self) :
        return self.title
    
    def getProceedToDownload(self) :
        return self.proceedToDownload
    
    def getDownloadable(self) :
        return self.downloadable
    
    def getDownloaded(self) :
        return self.downloaded
    
    def setMediaType(self, mediaType) :
        self.mediaType = mediaType
        
    def setMediaURL(self, mediaURL) :
        self.mediaURL = mediaURL
        
    def setTitle(self, title) :
        self.title = title
        
    def setProceedToDownload(self, proceedToDownload) :
        self.proceedToDownload = proceedToDownload
    
    def setDownloadable(self, downloadable) :
        self.downloadable = downloadable
    
    def setDownloaded(self, downloaded) :
        self.downloaded = downloaded