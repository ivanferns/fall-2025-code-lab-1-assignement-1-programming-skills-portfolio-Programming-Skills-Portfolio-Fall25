def main():
    a=int(input("Enter the number you want"))
    result=oddeven(a)
    print(f"the number is {result}")

def oddeven(number):
    if number%2==0:
        return("even")
    else:
        return("odd")

if __name__ == "__main__":
    main()

   