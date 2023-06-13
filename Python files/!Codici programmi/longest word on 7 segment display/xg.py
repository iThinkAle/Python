# Open the text file in read mode
file_path = "E:\!PERSONALE\Programming\Python\Python files\!Codici programmi\longest word on 7 segment display\dictionary.txt"
file = open(file_path, "r")

# Read the contents of the file
file_contents = file.read()

# Close the file
file.close()

# Print the file contents
print(file_contents)
