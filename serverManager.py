from experimental.StoneBoardPackagesexperimental.soundManager import *
from experimental.StoneBoardPackagesexperimental.home import *
from config import *
import shutil
import uuid
import os

def createServer():
    #delete old failed servers without error
    try:
        print('Deleting old failed server!')
        shutil.rmtree("storage/servers/createdServer")
    except:
        pass
    
    #create basic servcer file structure
    os.mkdir('storage/servers/createdServer')
    serveruuid = uuid.uuid4()
    serverPath = "storage/servers/" + str(serveruuid)
    os.renames("storage/servers/createdServer", serverPath)

