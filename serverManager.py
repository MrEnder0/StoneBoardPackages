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
    serversFolder = "storage/servers/createdServer/"
    serverName = "0"
    openedServer = serverFolder + serverName
    serverDataFile = openedServer + "/serverData.txt"
    serverOwnerFile = openedServer + "/serverOwner.txt"
    
    f = open(serverDataFile, "r")
    line = f.readline()
    print(line)
    f.close()

def readServers():
    rootdir = 'storage/servers'
    dirD = 'storage/servers\\'
    final = ''
    for file in os.listdir(rootdir):
        before = os.path.join(rootdir, file)
        after = before.replace(dirD, "\n")
        final = (final + after)
    print(final)

    serversFilePath = "storage/serversList.txt"
    isServerList = os.path.isfile("storage/serversList.txt")

    if isServerList:
        os.remove(serversFilePath)
        with open(serversFilePath, "w") as serversList:
            serversList.write(str(final))
    else:
        with open(serversFilePath, "w") as serversList:
            serversList.write(str(final))
