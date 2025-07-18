import random


class Game:
    def __init__(self):
        self.player_points, self.computer_points = 0, 0
        self.rounds_nb = self.start_game()

    @staticmethod
    def start_game():
        while True:
            print("--- Rock Paper Scissors Game ---")
            rounds_nb = input("How many rounds would you like to play? ")
            if rounds_nb.isnumeric():
                return int(rounds_nb)
            else:
                print("\nPlease enter a valid number.")

    def get_player_move(self):
        while True:
            move = input("Rock, paper or scissors [r/p/s]? ").strip().lower()
            if move in ("r", "p", "s"):
                return move

    @staticmethod
    def get_winner(player_move, computer_move):
        if player_move == computer_move:
            return "tie"
        elif player_move == "r" and computer_move == "p":
            return "computer"
        elif player_move == "r" and computer_move == "s":
            return "player"
        elif player_move == "p" and computer_move == "r":
            return "player"
        elif player_move == "p" and computer_move == "s":
            return "computer"
        elif player_move == "s" and computer_move == "r":
            return "computer"
        elif player_move == "s" and computer_move == "p":
            return "player"
        return None

    def launch_game(self):
        for _ in range(self.rounds_nb):
            player_move = self.get_player_move()
            computer_move = random.choice(["r", "p", "s"])
            print("You:", player_move, "| Computer:", computer_move)
            winner = self.get_winner(player_move, computer_move)
            if winner == "tie":
                print("This round is a tie\n")
            elif winner == "player":
                print("You won this round!\n")
                self.player_points += 1
            elif winner == "computer":
                print("You lost this round!\n")
                self.computer_points += 1

        print(
            "[Game Summary] Your points:",
            self.player_points,
            "| Computer points:",
            self.computer_points,
        )

        if self.player_points == self.computer_points:
            print("It was a tie.")
        elif self.player_points > self.computer_points:
            print("You won.")
        else:
            print("Computer won.")


if __name__ == "__main__":
    game = Game()
    game.launch_game()
