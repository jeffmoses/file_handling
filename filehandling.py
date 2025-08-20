# Create a program that reads a file and writes a modified version to a new file.
# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read. 



# Prompt the user to enter a filename
filename = input("Enter the filename: ")

try:
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read the entire content of the file
        data = file.read()
        print("File content read successfully.")

    # Create a new filename by replacing the original extension with "_modified."
    new_filename = filename.replace(".", "_modified.", 1)
    # Open the new file in write mode
    with open(new_filename, 'w') as new_file:
        # Write the uppercase version of the content to the new file
        new_file.write(data.upper())
    print(f"File written successfully to {new_filename}")
except FileNotFoundError:
    # Handle the case where the file is not found
    print("Error: File not found.")
except Exception as e:
    # Handle other potential errors during file reading
    print(f"Error: Could not read file: {e}")
