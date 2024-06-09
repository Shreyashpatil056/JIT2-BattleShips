import os
import sys

# Path to one.txt and two.txt files
one_txt_path = os.path.join('folder1', 'one.txt')
two_txt_path = os.path.join('folder1', 'two.txt')

# Function to read the printed pairs from one.txt
def read_printed_pairs(file_path):
    if not os.path.exists(file_path):
        return set()
    with open(file_path, 'r') as file:
        lines = file.readlines()
    printed_pairs = set()
    for line in lines:
        x, y = map(int, line.strip().split())
        printed_pairs.add((x, y))
    return printed_pairs

# Function to write the new pair to one.txt
def write_pair(file_path, pair):
    with open(file_path, 'a') as file:
        file.write(f"{pair[0]} {pair[1]}\n")

# Function to append ship info to two.txt
def append_ship_info(file_path, info):
    with open(file_path, 'a') as file:
        file.write(f"{info}\n")

# Function to reset one.txt and two.txt
def reset_files(one_path, two_path):
    with open(one_path, 'w') as file:
        file.write('')
    with open(two_path, 'w') as file:
        file.write('')

# Read command-line arguments
if len(sys.argv) != 3:
    sys.exit("Usage: python main.py <ACKNOWLEDGEMENT> <SHIP_INFO>")

acknowledgement = sys.argv[1]
ship_info = sys.argv[2]

# Read previously printed pairs
printed_pairs = read_printed_pairs(one_txt_path)

# Find the next pair to print
next_pair = None
for i in range(1, 11):
    for j in range(1, 11):
        if (i, j) not in printed_pairs:
            next_pair = (i, j)
            break
    if next_pair:
        break

# Print the next pair and update one.txt
if next_pair:
    print(f"{next_pair[0]} {next_pair[1]}")
    write_pair(one_txt_path, next_pair)
    
    # If the pair is (10, 10), reset the files
    if next_pair == (10, 10):
        reset_files(one_txt_path, two_txt_path)
else:
    print("All pairs have been printed.")

# Process the acknowledgement and ship info
if acknowledgement not in ["HIT", "MISS", "NONE"]:
    sys.exit("Invalid ACKNOWLEDGEMENT value. It should be 'HIT', 'MISS', or 'NONE'.")

if ship_info not in ["2", "3", "4", "5", "NONE"]:
    sys.exit("Invalid SHIP_INFO value. It should be '2', '3', '4', '5', or 'NONE'.")

# Append ship info to two.txt if a ship is destroyed
if ship_info != "NONE":
    append_ship_info(two_txt_path, ship_info)
