from libs.qtSingleton import QtSingleton
import json

macroActions = ["capture", "delay", "crop", "key"]


class mainCore(QtSingleton):
    def __init__(self):
        super().__init__()
        self.capturePath = './capture'
        self.macro = []
        self.configPath = './default.json'
        self.loadMacro()

    def loadMacro(self):
        """
        json의 데이터를 로딩하기
        """
        try:
            print(self.configPath)
            with open(self.configPath, encoding='utf8') as jsonFile:
                self.macro = json.load(jsonFile)
        except Exception as e:
            print(e)
            self.macro = []

    def saveMacro(self):
        try:
            with open(self.configPath, 'w', encoding='utf8') as jsonFile:
                json.dump(self.macro, jsonFile)
        except IOError:
            print(IOError)
