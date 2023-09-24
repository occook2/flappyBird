import Window

class Game:

    def __init__(self):
        # Purpose of this class is to keep track of everything a single game
        # entails. Window, Score, PlayAgain, etc.
        
        self.score = 0
        window = Window.Window()

        window.display()