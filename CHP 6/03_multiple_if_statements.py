a = int(input("Enter your Age :"))
# If Statement no: 1
if(a%2 == 0):

    print("A is Even")

# End Of If Statement no: 1

# If statement no: 2
if(a>18):
    print("You are Above The Age of Consent")
    print("Good for You")

elif(a<0):
    print("You are Entering an invalid Negative Age ")

elif(a==0):
    print("You are Entering 0 Which is Not a Valid Age")    


else:
    print("You are Below The Age of Consent ")    

# End Of If Statement no: 2

print("End of Program") 