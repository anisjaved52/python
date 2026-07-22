f = open("poem.txt")
content = f.read()
if("wonder " in content):
    print("The Word wonder is present in the Content")

else:
    print("The Word wonder is not present in the Content")

f.close() 