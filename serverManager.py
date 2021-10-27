from experimental.StoneBoardPackagesexperimental.soundManager import *
from experimental.StoneBoardPackagesexperimental.home import *
from config import *
import shutil
import uuid
import os

def createServer():
    #delete old failed servers without error
    try:
        shutil.rmtree("storage/servers/createdServer")
        print('Deleting old failed server!')
    except:
        pass
    
    #create basic servcer file structure
    os.mkdir('storage/servers/createdServer')
    userFilePath = 'storage/user.txt'
    with open(userFilePath, 'r') as userId:
        userUuid = userId.read()
    with open('storage/servers/createdServer/serverOwner.txt', 'w') as serverOwnerId:
        serverOwnerId.write(userUuid)
        
    serveruuid = uuid.uuid4()
    serverPath = "storage/servers/" + str(serveruuid)
    os.renames("storage/servers/createdServer", serverPath)
