f = open("poem.txt")
content = f.read()
if("twinkle " in content):
    print("The Word twinkle is present in the Content")

else:
    print("The Word twinkle is not present in the Content")

f.close() 