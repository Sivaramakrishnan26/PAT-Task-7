print("Write Content in a file:")


def write_to_file(file_name, content):  # Define a function with 2 arguments
    with open(file_name, 'w') as file:  # Write permission to the file
        file.write(content)  # Write the content in a file
    print(f"The content was successfully written to {file_name}")  # Print the successful message


file_name = "Demo.txt"  # File Name
content = "Hello!\nWelcome to File Handling"  # Content
write_to_file(file_name, content)  # Call the function

print("\nRead from file:\n")


def read_from_file(file_name):  # Define a function
    with open(file_name, 'r') as file:  # Read permission to the file
        content = file.read()  # Read the content in the file
    print(content)  # Display the content into the console
    print(f"\nThe file {file_name} was read successfully")  # Print the successful message


file_name = "Demo.txt"  # File Name
read_from_file(file_name)  # Call the function
