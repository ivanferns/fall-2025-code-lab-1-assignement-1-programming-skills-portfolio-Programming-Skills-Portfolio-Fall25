dictionary={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
userinput=int(input("Enter the month number"))
if userinput in dictionary:
    print(dictionary[userinput])
else:
    print("Enter a proper number : ")