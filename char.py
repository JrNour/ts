import random

def generate_random_string():
    # Define the character sets for each position
    first_char_set = '456789'  # Digits 4 through 9
    second_char_set = 'kmnpqrstuvwxyz'  # Characters from k to z
    base58_chars = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
    third_char_set = base58_chars
    fourth_char_set = base58_chars
    fifth_char_set = base58_chars
    sixth_char_set = base58_chars
    seventh_char_set = base58_chars
    eighth_char_set = base58_chars
    ninth_char_set = base58_chars + '123456789'
    last_char_set = base58_chars

    # Generate each character based on the respective character set
    first_char = random.choice(first_char_set)
    second_char = random.choice(second_char_set)
    third_char = random.choice(third_char_set)
    fourth_char = random.choice(fourth_char_set)
    fifth_char = random.choice(fifth_char_set)
    sixth_char = random.choice(sixth_char_set)
    seventh_char = random.choice(seventh_char_set)
    eighth_char = random.choice(eighth_char_set)
    ninth_char = random.choice(ninth_char_set)
    last_char = random.choice(last_char_set)

    # Concatenate the characters to form the final string
    result = (first_char + second_char + third_char + fourth_char + fifth_char + sixth_char +
              seventh_char + eighth_char + ninth_char + last_char)
    return result

# Number of random strings to generate
num_strings = 10000  # Change this to the desired number of strings

# Write random combinations to a file
with open('random_output.txt', 'w') as file:
    for _ in range(num_strings):
        file.write(generate_random_string() + '\n')
