correctpassword = "12345"
maxattempts = 5
attemptsused = 0

while attemptsused < maxattempts:  
    userinput = input("\nPlease enter your password: ")
    attemptsused += 1
    if userinput == correctpassword:
        print(" Access Granted")
        break
    else:
        remaining = maxattempts - attemptsused
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempt(s) remaining.")
        else:
            print("Access Denied")