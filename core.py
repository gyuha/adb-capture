from libs.qtSingleton import QtSingleton
import json

macroActions = ["capture", "delay", "crop", "key"]


class mainCore(QtSingleton):
    def __init__(self):
        super().__init__()
        self.capturePath = './capture'
        self.macro = []
        self.loadMacro('default.json')

    def loadMacro(self, filePath):
        """
        json의 데이터를 로딩하기
        """
        try:
            with open(filePath, encoding='utf8') as jsonFile:
                print(jsonFile)
                self.macro = json.load(jsonFile)
        except IOError:
            print(IOError)
            self.macro = []
