from datetime import datetime


def current_timestamp():  # Define a function
    timestamp = datetime.now().strftime('%d_%h_%Y %H-%M-%S') # 24 hrs format
    # timestamp = datetime.now().strftime('%d_%h_%Y %I-%M-%S %p')  # 12 hrs format
    file_name = f"{timestamp}.txt"  # Filename
    with open(file_name, 'w') as file:  # Write permission to the file
        file.write(f"Current Timestamp: {timestamp}")  # Write the content in a file
    print(f"Timestamp file {timestamp} created successfully")  # Print the successful message


current_timestamp()  # Call the function
