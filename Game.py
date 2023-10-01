import Window

class Game:

    def __init__(self):
        # Purpose of this class is to keep track of everything a single game
        # entails. Window, Score, PlayAgain, etc. 1 Game per AI Generation?
        
        self.score = 0
        self.birds = []
        self.pipes = []

        window = Window.Window()

        running = True
        while (running):
            running = False

        window.display(self.birds, self.pipes, self.score)