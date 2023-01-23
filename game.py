import random


class Game:
    def __init__(self):
        self.player1_count = 0
        self.player2_count = 0
        self.tries = 0
        self.player1 = self.get_player1_name()
        self.player2 = "computer"

    # TODO function that asks for player1's name

    def get_player1_name(self):
        player1_name = input("Enter Player1's name: ")
        return player1_name

    # # user
    # player1_count = 0
    # # computer
    # player2_count = 0
    # tries = 0

    def player_choice(self):
        print(
            f"choice for player1: {self.player1} is {self.player1_choice} | choice for player2: {self.player2} is {self.player2_choice}")

    def the_game(self):
        # rules of the game
        print()
        print("----------- R U L E S  O F  T H E  G A M E: ----------------")
        print("1. Rock beats scissors")
        print("2. Paper beats rock")
        print("3. Scissors beats paper")
        print()

        print("Your choices are: \n")
        game_options = ["rock", "paper", "scissors"]

        while self.tries < 3:
            print()
            print(game_options)
            print()
            self.player1_choice = input("Please pick a choice: ").lower()
            self.player2_choice = random.choice(game_options)
            if self.player1_choice == self.player2_choice:
                print("it's a tie")
                self.player_choice()
                self.win()
                self.player1_count += 1
                self.player2_count += 1
                self.tries += 1
            elif self.player1_choice == "rock" and self.player2_choice == "paper":
                print(f"1 point for {self.player2}")
                self.player_choice()
                self.win()
                self.player2_count += 1
                self.tries += 1
            elif self.player1_choice == "rock" and self.player2_choice == "scissors":
                print(f"1 point for {self.player1}")
                self.player_choice()
                self.win()
                self.player1_count += 1
                self.tries += 1
            elif self.player1_choice == "scissors" and self.player2_choice == "paper":
                print(f"1 point for {self.player1}")
                self.player_choice()
                self.win()
                self.player1_count += 1
                self.tries += 1
            else:
                print("try again")
            # or you can break here with tries like:
            # if tries == 3: then break

            # don't forget the parameters aren't the same as attributes in main class

    def win(self):
        if self.player1_count > self.player2_count:
            # TODO try to change every player 1 to the name
            print(f"{self.player1} won this game")
        elif self.player1_count == self.player2_count:
            print("You tied!")
        elif self.player1_count < self.player2_count:
            print(f"{self.player2} won this game")
        else:
            print("try again.")

    def count_points(self):
        player1_points = self.player1_count
        player2_points = self.player2_count
        total_points = player1_points + player2_points
        print(f"Points for {self.player1}  are {player1_points}")
        print(f"Points for {self.player2} are {player2_points}")
        print(f"Total points: {total_points}")


# function calls
user1 = Game()
user1.the_game()
user1.win()
user1.count_points()
