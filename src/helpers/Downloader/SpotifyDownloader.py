import certifi
import ssl
import urllib
import urllib.request

context = ssl.create_default_context(cafile=certifi.where())

class Downloader :
    def __init__(self) :
        pass
    
    def formatTitle(self, title) :
        title = title.replace("\"", "")
        title = title.replace("-", "")
        return title
        
    def download(self, repository) :
        for i in range(len(repository.playlist)) :
            title = repository.playlist[i]["title"]
            title = self.formatTitle(title)
            title += repository.playlist[i]["mediaType"]
            print("\n[--------++++-------->>>> Downloading :" + title + "...")
            pathToDownloadFile = repository.getDownloadPath() + "\\" + title
            # file = urllib.request.urlopen(repository.playlist[i]["mediaURL"], context=context)
            # with open(pathToDownloadFile,'wb') as output:
            #     output.write(file.read())
            print("[--------++++-------->>>> Downloaded : " + title + "--------++++--------")
            repository.playlist[i]["downloaded"] = True
            
            