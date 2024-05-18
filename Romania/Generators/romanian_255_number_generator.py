import os
import json
import zipfile
from tqdm import tqdm

# Define the starting and ending numbers
START_NUMBER = 1000000
END_NUMBER = 9999999

# Define the number of numbers to be included in each archive
NUMBERS_PER_ARCHIVE = 1000000

# Define the chunk size for generating numbers
CHUNK_SIZE = 100000

# Define the base folder for the archives
BASE_FOLDER = os.path.join("..", "255_NUMBERS")

# Create the base folder if it doesn't exist
os.makedirs(BASE_FOLDER, exist_ok=True)


# Function to generate numbers
def generate_numbers(start, end):
    for num in range(start, end + 1):
        yield f"+4255 {num:07d}"


# Function to create an archive
def create_archive(start, end):
    archive_name = f"NUMBERS_255{start}_255{end}.zip"
    archive_path = os.path.join(BASE_FOLDER, archive_name)
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zip_file:
        json_filename = f"255{start}_255{end}.json"
        with zip_file.open(json_filename, "w") as json_file:
            for chunk_start in tqdm(range(start, end + 1, CHUNK_SIZE), total=(end - start + 1) // CHUNK_SIZE, desc=f"Generating archive for numbers {start} to {end}"):
                chunk_end = min(chunk_start + CHUNK_SIZE, end + 1)
                numbers = generate_numbers(chunk_start, chunk_end - 1)
                json_bytes = '\n'.join(numbers).encode('utf-8')
                json_file.write(json_bytes)


# Function to generate and create archives
def generate_archives(num_sets):
    total_sets = (END_NUMBER - START_NUMBER + 1) // NUMBERS_PER_ARCHIVE

    if num_sets > total_sets:
        print(f"Maximum number of sets that can be generated is {total_sets}. Limiting to {total_sets} sets.")
        num_sets = total_sets

    remaining_sets = num_sets
    generated_sets = 0

    with open(os.path.join(BASE_FOLDER, "log.txt"), "w") as log_file:
        start = START_NUMBER
        while remaining_sets > 0:
            end = start + NUMBERS_PER_ARCHIVE - 1
            create_archive(start, end)
            log_file.write(f"Generated archive for numbers {start} to {end}\n")
            start = end + 1
            remaining_sets -= 1
            generated_sets += 1
            print(f"Generated set {generated_sets}/{num_sets} ({total_sets - remaining_sets}/{total_sets})")


# Prompt the user for the number of sets to generate
num_sets = int(input("Enter the number of sets to generate: "))

# Generate the archives
generate_archives(num_sets)