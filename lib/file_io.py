def write_file(file_name, file_content):
    file_name_with_extension = file_name + ".txt"
    with open(file_name_with_extension, "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_name_with_extension = file_name + ".txt"
    with open(file_name_with_extension, "a") as file:
        file.write("\n" + append_content)

def read_file(file_name):
    file_name_with_extension = file_name + ".txt"
    try:
        with open(file_name_with_extension, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found"
# test
write_file(file_name="logfile", file_content="Log 1: 5 bananas added")
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

# Read the file
log_content = read_file(file_name="logfile")
print(log_content)
# Log 1: 5 bananas added
# Log 2: 3 bananas subtracted
