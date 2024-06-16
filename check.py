import os

def find_missing_files(directory):
    print(f"Listing files in directory: {directory}")
    
    # List all files in the directory
    all_files = os.listdir(directory)
    print(f"Found {len(all_files)} files.")

    # Extract numerical part from file names, filter for valid 6-digit .json files
    file_numbers = set()
    print("Processing file names and extracting numbers...")
    for f in all_files:
        if f.endswith('.json') and f[:-5].isdigit() and len(f[:-5]) == 6:
            file_number = int(f[:-5])
            file_numbers.add(file_number)
            if len(file_numbers) % 10000 == 0:
                print(f"Processed {len(file_numbers)} files...")

    print(f"Total valid files found: {len(file_numbers)}")

    if file_numbers:
        min_number = min(file_numbers)
        max_number = max(file_numbers)
        print(f"File numbers range from {min_number} to {max_number}.")

        print("Generating the full expected range of file numbers...")
        full_range = set(range(min_number, max_number + 1))
        
        print("Identifying missing file numbers...")
        missing_numbers = sorted(full_range - file_numbers)
        
        print(f"Missing file numbers: {missing_numbers}")
        return missing_numbers
    else:
        print("No valid .json files found.")
        return []

# Replace 'your_directory_path' with the path to your JSON files directory
directory_path = 'raw'
missing_files = find_missing_files(directory_path)

if missing_files:
    print(f"Missing file numbers: {missing_files}")
    print(f"There are {len(missing_files)} deleted mangas")
else:
    print("No missing files.")

