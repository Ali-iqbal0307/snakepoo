class Player:
    def __init__(self, name):
        self.name = name
        self.position = 1  # Départ à la position 1

    def move(self, steps):
        self.position += steps
        if self.position < 1:
            self.position = 1  # Ne pas descendre en dessous de la position 1

    def reset_position(self):
        self.position = 1
