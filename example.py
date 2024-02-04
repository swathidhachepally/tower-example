# create_file.py
file_content = "This is the content of the file."

with open("example_file.txt", "w") as file:
    file.write(file_content)

print("File 'example_file.txt' created with contents:", file_content)

