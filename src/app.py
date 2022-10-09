import sys

sys.path.insert(0, "./src/helpers/Data")
sys.path.insert(0, "./src/helpers/Downloader")
sys.path.insert(0, "./src/helpers/Extractor")
sys.path.insert(0, "./src/UI")

import tabulate
import json
import Repository
import CompilePlaylist
import SpotifyDownloader
import Display

#This program takes playlist object as input and downloads the playlist

Display.Show.welcome()

downloadPath = "C:\\Users\\Vasu\\Desktop\\Spotify downloader\\Downloads"
with open("C:\\Users\\Vasu\\Desktop\\Spotify downloader\\Downloads\\base.json", encoding="utf-8") as JSONFile :
  baseJSON = json.load(JSONFile)

# Creating instance of Repository which stores major data
repository = Repository.InitializeRepository()
# Configuring necessary data to Repository
repository.setBaseJSON(baseJSON)
repository.setDownloadPath(downloadPath)

# Setting up Compiler for extracting the downloadable playlist
playlistCompiler = CompilePlaylist.Compiler()
# Call to compile from base object
playlistCompiler.extractIndividualFileData(repository)

# Setting up the downloader
downloader = SpotifyDownloader.Downloader()
downloader.download(repository)

# Displays the formatted playlist is created correctly
header = repository.playlist[0].keys()
rows =  [x.values() for x in repository.getPlaylist()]
# print(tabulate.tabulate(rows, header, tablefmt="fancy_grid", showindex="always", maxcolwidths=[None, 50]))