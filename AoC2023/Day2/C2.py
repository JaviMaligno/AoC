import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_data import get_input
text = get_input(2)

def check_games(text):
    games = text.splitlines()
    # Initial number of cubes
    
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14

    # Variable to store the sum of the IDs of the possible games
    possible_game_ids = 0

    for game in games:
        # Split the game string into ID and rounds
        game_id, rounds = game.split(":")
        game_id = int(game_id.strip("Game "))

        # Split the rounds string into individual rounds
        rounds = rounds.split(";")

        # Variable to check if the game is possible
        is_possible = True

        for round in rounds:
            # Variables to store the number of cubes shown in this round
            red_shown = 0
            green_shown = 0
            blue_shown = 0

            # Split the round string into individual cube counts
            cube_counts = round.split(",")

            for cube_count in cube_counts:
                # Split the cube count string into number and color
                number, color = cube_count.split()
                number = int(number)

                # Update the number of cubes shown based on the color
                if color == "red":
                    red_shown += number
                elif color == "green":
                    green_shown += number
                elif color == "blue":
                    blue_shown += number

            # Check if the round is possible
            if red_shown > red_cubes or green_shown > green_cubes or blue_shown > blue_cubes:
                is_possible = False
                break

        # If all rounds are possible, add the game ID to the sum
        if is_possible:
            possible_game_ids += game_id

    return possible_game_ids

def calculate_cubes(text):
    # Variable to store the total sum
    games = text.splitlines()
    total_sum = 0

    for game in games:
        # Split the game string into ID and rounds
        game_id, rounds = game.split(":")
        game_id = int(game_id.strip("Game "))

        # Variables to store the maximum number of cubes shown in each round
        max_red = 0
        max_green = 0
        max_blue = 0

        # Split the rounds string into individual rounds
        rounds = rounds.split(";")

        for round in rounds:
            # Variables to store the number of cubes shown in this round
            red_shown = 0
            green_shown = 0
            blue_shown = 0

            # Split the round string into individual cube counts
            cube_counts = round.split(",")

            for cube_count in cube_counts:
                # Split the cube count string into number and color
                number, color = cube_count.split()
                number = int(number)

                # Update the number of cubes shown based on the color
                if color == "red":
                    red_shown = max(red_shown, number)
                elif color == "green":
                    green_shown = max(green_shown, number)
                elif color == "blue":
                    blue_shown = max(blue_shown, number)

            # Update the maximum number of cubes shown if necessary
            max_red = max(max_red, red_shown)
            max_green = max(max_green, green_shown)
            max_blue = max(max_blue, blue_shown)

        # Add the product of the maximum number of cubes shown to the total sum
        total_sum += max_red * max_green * max_blue

    return total_sum

