
# Reading the file

with open("../../Desktop/my_file.txt") as file:  # with keyword will manage the file once it is done using it
    content = file.read()  # take up some computer resource
    print(content)

# Writing to a file
# w is write
# a is append
# if in write mode but file dont exist, will start a new file

with open("../day_24/venv/Lib/test.txt", mode="w") as file:
    file.write("New Text")
