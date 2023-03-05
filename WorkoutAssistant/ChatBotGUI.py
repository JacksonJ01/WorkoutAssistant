from speechFunct import analyzeResponse
from basicImportInfo import *


class ChatBotWindow(QWidget):
    switchToMenuWindow = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.CONTEXT = None

        self.setWindowTitle('ChatBot')
        self.setGeometry(winXPos, winYPos, winLength, winHeight)

        layout = QGridLayout()

        self.userMessageHistory1 = QLabel("_____")
        self.userMessageHistory2 = QLabel("_____")
        self.userMessageHistory3 = QLabel("_____")
        
        self.chatBotMessageHistory1 = QLabel("_____")
        self.chatBotMessageHistory2 = QLabel("_____")
        self.chatBotMessageHistory3 = QLabel("_____")

        self.userInput = QLineEdit()
        self.userInput.returnPressed.connect(self.goToAskChatBot)


        self.backButton = QPushButton('Back To Menu')
        self.backButton.clicked.connect(self.goToMenuWindow)
        self.enterButton = QPushButton('Enter')
        self.enterButton.clicked.connect(self.goToAskChatBot)
        
        self.borderLeft = QLabel("BderL")
        self.borderRight = QLabel("BderR")

        self.addToLayout = [(self.borderLeft, 0, 0, 3, 1), (self.borderRight, 0, 4, 3, 1), 
                            (self.userMessageHistory3, 0, 1, 1, 1), (self.chatBotMessageHistory3, 0, 2, 1, 1),
                            (self.userMessageHistory2, 1, 1, 1, 1), (self.chatBotMessageHistory2, 1, 2, 1, 1),
                            (self.userMessageHistory1, 2, 1, 1, 1), (self.chatBotMessageHistory1, 2, 2, 1, 1),
                            (self.backButton, 4, 0, 1, 1), (self.userInput, 4, 1, 1, 2), (self.enterButton, 4, 3, 1, 1)]

        for x in self.addToLayout:
            layout.addWidget(x[0], x[1], x[2], x[3], x[4])
        self.setLayout(layout)
        


        self.setLayout(layout)
    
    def goToMenuWindow(self):
        self.switchToMenuWindow.emit()

    def goToAskChatBot(self):
        self.userMessageHistory3.setText(self.userMessageHistory2.text())
        self.userMessageHistory2.setText(self.userMessageHistory1.text())
        
        self.chatBotMessageHistory3.setText(self.chatBotMessageHistory2.text())
        self.chatBotMessageHistory2.setText(self.chatBotMessageHistory1.text())
        
        self.userMessageHistory1.setText(self.userInput.text())
        response, self.CONTEXT = analyzeResponse(self.userInput.text(), self.CONTEXT)
        self.chatBotMessageHistory1.setText(response)

        self.userInput.clear()
