import random
from medications import medications
from clues import clues

# Define the clues for each round as a list of strings with placeholders for values
round_clues = [
    'Clue 1: {}, | {}',
    'Clue 2: {}',
    'Clue 3: {}, {}, and {}',
    'Clue 4: {}, {}, and {}',
    'Clue 5: {}, {}, and {}'
]

# Define a function to generate clues for a given medication
def generate_clues(medication):
    medication_clues = clues[medication]
    return random.sample(medication_clues, len(medication_clues))

# Generate a list of clues for all medications in the medications list
medication_clues = [random.choice(round_clues).format(medication, *generate_clues(medication)) for medication in medications]

# Shuffle the order of the medications and clues
zipped = list(zip(medications, medication_clues))
random.shuffle(zipped)
medications, medication_clues = zip(*zipped)

# Define the number of rounds and guesses
num_rounds = 10  # set the number of rounds to 10
num_guesses = 1  # set the number of guesses per round to 3

def play_round(medication):
    round_num = medications.index(medication) + 1
    print('\nRound {}:'.format(round_num))

    # Print the clues for the current round
    for i, clue in enumerate(medication_clues[round_num - 1].split("|")):
        print('Clue {}: {}'.format(i+1, clue))

    # Prompt the player to make a guess
    print('\nGuess the medication ({} guesses remaining):'.format(num_guesses))
    guess = input().lower()

    # Check if the guess is correct and respond appropriately
    if guess == medication.lower():
        print('Correct! The medication was {}.'.format(medication))
        return True
    else:
        print('Nope!')
        return False

# Main game loop
print('Welcome to Medication Mastermind!')

for i in range(num_rounds):
    medication = medications[i]
    play_round(medication)

print('\nCongratulations! You have completed all rounds.')
