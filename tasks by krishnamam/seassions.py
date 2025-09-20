# Write a program to convert a given number (1-4) into its respective season (1 for Spring, 2 for Summer, etc.) using a switch-case equivalent.


num = int(input("Enter a number (1-4) to get the season: "))

match num:
    
    case(num) if num == 3 or num == 4 or num == 5:
        print("Spring")
    case(num) if num == 6 or num == 7 or num == 8:
        print("Summer")
    case(num) if num == 9 or num == 10 or num == 11 :
        print("Fall")
    case(num) if num == 12 or num == 1 or num == 2:
        print("Winter")
