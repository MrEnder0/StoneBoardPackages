from experimental.StoneBoardPackagesexperimental.soundManager import *
from experimental.StoneBoardPackagesexperimental.home import *
from config import *
import shutil
import uuid
import os

def createServer():
    #delete failed server without error
    try:
        shutil.rmtree("storage/servers/createdServer")
        print("Deleting old failed server!")
    except:
        pass
    
    #create basic servcer file structure
    os.mkdir("storage/servers/createdServer")
    userFilePath = "storage/user.txt"
    with open(userFilePath, "r") as userId:
        userUuid = userId.read()
    with open("storage/servers/createdServer/serverOwner.txt", "w") as serverOwnerId:
        serverOwnerId.write(userUuid)

    #generate empty save file
    with open("storage/servers/createdServer/serverData.txt", "w") as serverData:
        serverData.write("#save data\nhi")
    
    #rename to randomly generated uuid
    serveruuid = uuid.uuid4()
    serverPath = "storage/servers/" + str(serveruuid)
    os.renames("storage/servers/createdServer", serverPath)

def loadServer():
    currentLine = 0
    with open('storage/selectedLine.txt', 'r') as selectedLineFile:
        selectedLine = selectedLineFile.read().rstrip('\n')

    serversListFile = open('storage/serversList.txt', 'r')
        
    while currentLine < int(selectedLine):
         serverName = serversListFile.readline().rstrip('\n')
         currentLine += 1
    print(serverName)
        
    serversFolder = "storage/servers/"
    openedServer = serversFolder + serverName
    serverDataFile = openedServer + "/serverData.txt"
    serverOwnerFile = openedServer + "/serverOwner.txt"

    with open("storage/openedServer.txt", "w") as serverOpen:
        serverOpen.write(openedServer)

def readServers():
    #Read all folder names and put in varible
    rootdir = 'storage/servers'
    dirD = 'storage/servers\\'
    final = ''
    for file in os.listdir(rootdir):
        before = os.path.join(rootdir, file)
        after = before.replace(dirD, "\n")
        final = (final + after)

    serversFilePath = "storage/serversList.txt"
    isServerList = os.path.isfile("storage/serversList.txt")
    final = final[1:]

    #Write as file
    if isServerList:
        os.remove(serversFilePath)
        with open(serversFilePath, "w") as serversList:
            serversList.write(str(final))
    else:
        with open(serversFilePath, "w") as serversList:
            serversList.write(str(final))
