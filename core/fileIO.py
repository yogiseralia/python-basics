# writing text (wt) mode
file = open("wasteland.txt", mode="wt", encoding="utf-8")
file.write("What are the roots that clutch. ")
file.write("what branches grow\n")
file.write("Out of stony rubbish?\n")
file.close()

# reading text (rt) mode
g = open("wasteland.txt", mode="rt", encoding="utf-8")
g.read(32)
g.read()

# move the file pointer to 0
g.seek(0) # value of offset should be accepted by file#seek(offset) is either 0 or return value of file#tell() else unexpected behaviour will occur.
g.readlines()




# appending file
a = open("wasteland.txt", mode="at", encoding="utf-8")
a.writelines([
    "Son of man\n",
    "You cannot say or guess, ",
    "for you know only,\n",
    "A heap of broken images, ",
    "where the sun beats.\n"
])
a.close()

# use files.py for iterating over files