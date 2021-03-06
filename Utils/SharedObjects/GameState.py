class GameState():
    def __init__(self):
        self.gameState = {}
        self.procRunning = False
        self.mapImages = {}
    def getGameState(self):
        return self.gameState
    def getGameStateValue(self,k):
        if k in self.gameState.keys():
            return self.gameState[k]
        else:
            return ""
    def setGameStateKeyValue(self,k,v):
        self.gameState[k] = v
    def setProcStatus(self,p):
        self.procRunning = p
    def getProcRunning(self):
        return self.procRunning
    def setMapImage(self, k, i):
        self.mapImages[k] = i 
    def getMapImage(self, k):
        return self.mapImages[k]
    def getMapImages(self):
        return self.mapImages
