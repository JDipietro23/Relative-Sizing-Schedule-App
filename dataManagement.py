import pickle
import os
from week import week

def saveData(weekObj:week)->None:
    objFile = open('saveData.txt', 'wb')
    pickle.dump(weekObj,objFile)
    objFile.close()

def loadData()->week:

    if os.path.getsize('saveData.txt')==0:
        return None
    
    loadFile = open('saveData.txt', 'rb')
    loadedData = pickle.load(loadFile)
    loadFile.close()
    return loadedData

def clearFile()->None:
    objFile = open('saveData.txt', 'wb')
    objFile.close()