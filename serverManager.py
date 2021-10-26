from experimental.StoneBoardPackagesexperimental.soundManager import *
from experimental.StoneBoardPackagesexperimental.home import *
from config import *
import shutil
import uuid
import os

userFilePath = 'storage/user.txt'
with open(userFilePath, 'r') as userId:
    useruuid = userId.read()

def createServer():
    #delete old failed servers without error
    try:
        print('Deleting old failed server!')
        shutil.rmtree("storage/servers/createdServer")
    except:
        pass
    #create basic servcer file structure
    os.mkdir('storage/servers/createdServer')
    with open('storage/servers/createdServer/serverOwner.txt', 'w') as serverOwnerId:
        serverOwnerId.write(useruuid)
