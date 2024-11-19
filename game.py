import random
from player import Player

class Game:
    def __init__(self):
        self.board_size = 0
        self.players = []
        self.traps = []
        self.bonuses = []
        self.is_game_over = False
        self.initialize_game()

    def start(self):
        while not self.is_game_over:
            self.play_turn()

    def initialize_game(self):
        # Choix de la taille du plateau
        while True:
            try:
                size = int(input("Choisissez la taille du plateau (50, 100, 200) : "))
                if size in [50, 100, 200]:
                    self.board_size = size
                    break
                else:
                    print("Entrée invalide. Veuillez entrer 50, 100 ou 200.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")

        # Choix du nombre de joueurs
        while True:
            try:
                num_players = int(input("Entrez le nombre de joueurs (2 à 4) : "))
                if 2 <= num_players <= 4:
                    break
                else:
                    print("Entrée invalide. Veuillez entrer un nombre entre 2 et 4.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")

        # Initialisation des joueurs
        for i in range(1, num_players + 1):
            name = input(f"Entrez le nom du joueur {i} : ")
            self.players.append(Player(name))

        # Initialisation des pièges et bonus
        num_traps = self.board_size // 10

        num_bonuses = self.board_size // 10
        self.traps = self.generate_special_positions(num_traps)
        self.bonuses = self.generate_special_positions(num_bonuses, exclude=self.traps)

    def generate_special_positions(self, count, exclude=[]):
        positions = []
        while len(positions) < count:
            pos = random.randint(2, self.board_size - 1)
            if pos not in positions and pos not in exclude:
                positions.append(pos)
        return positions

    def play_turn(self):
        for player in self.players:
            input(f"\nC'est le tour de {player.name}. Appuyez sur Entrée pour lancer le dé.")
            dice = self.roll_dice()
            print(f"{player.name} a lancé un {dice}.")
            player.move(dice)

            # Vérification des limites
            if player.position > self.board_size:
                player.position = self.board_size - (player.position - self.board_size)
                print(f"{player.name} dépasse la limite ! Retour à la position {player.position}.")

            # Vérification des pièges
            if player.position in self.traps:
                print(f"{player.name} est tombé dans un piège ! Retour de 5 cases.")
                player.move(-5)

            # Vérification des bonus
            if player.position in self.bonuses:
                print(f"{player.name} a trouvé un bonus ! Avance de 5 cases.")
                player.move(5)

            # Vérification de la victoire
            if player.position == self.board_size:
                print(f"\nFélicitations {player.name} ! Vous avez gagné !")
                self.is_game_over = True
                break

            print(f"{player.name} est maintenant à la position {player.position}.")

        self.display_board()

    def roll_dice(self):
        return random.randint(1, 6)

    def display_board(self):
        print("\n--- État du Plateau ---")
        for player in self.players:
            print(f"{player.name} : Position {player.position}")
        print("-----------------------\n")
