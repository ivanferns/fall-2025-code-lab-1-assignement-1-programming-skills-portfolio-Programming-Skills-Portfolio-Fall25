L=["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]
userinput=input("Enter the name you want to search")
for i in L:
    if userinput==i:
        print(f"{userinput} is in the list")
