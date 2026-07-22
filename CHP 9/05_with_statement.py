f = open("file.txt")
print(f.read())
f.close

# The same can Be Witten using with statement like this 
with open("file.txt") as f:
    print(f.read())

    