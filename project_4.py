
print("welcome to the Data Analyzer and Transformer program")
while True:
    print("\nMain Menu:")
    print("1.Input Data")
    print("2.Display Data Summary(Built in Function)")
    print("3.Calculate Factorial(Recursion)")
    print("4.filter data by threshold (lamda Functuon)")
    print("5. Sort data")
    print("6. Display Dataset statistics (Return Multiple Values)")
    print("7. Exit program")

    choice=int(input("please enter your choice:"))

    if choice==1:
        data=input("enter data for a 1D array (seprated by spaces):")
        array=[int(i) for i in data.split()]
        
        print("\n Data has been stored successfully!")
        
    elif choice==2:
        print("Data Summary:")
        Length=len(array)
        print("- Toatal elements:",Length)
        Min=min(array)
        print("- Minimum value:",Min)
        Max=max(array)
        print("- Maxiimum value:",Max)
        Sum=sum(array)
        print("- Sum of all values:",Sum)
        Avg= Sum/Length
        print("- Average value:",Avg)

    elif choice==3:
        num=int(input("enter a number to calculate its factorial:"))
        result=1
        for i in range(1,num+1):
            result *= i

        print(f"factorial of {num} is {result}")

    elif choice == 4:
        pass
        threshold=int(input("enter a threshold value to filter out data below this value:"))
        #for i in array:
            #if i 

       

    elif choice == 5:
        print("choose sorting option:")
        print("1. Ascending")
        print("2. Decending")
              
        choice1=int(input("please enter your choice:"))

        if choice1 == 1:
              a = sorted(array)
              print("Sorted data in ascending order:",a)
        elif choice1 == 2:
            d= sorted(array,reverse = True)
            print("Sorted data in descending order:",d)
        else:
            print("invalid choice")

    elif choice==6:
        print("Dataset Statistics:")
        def statistics(array):
            
            Length = len(array)
            print("- Total elements:", Length)
    
            Min = min(array)
            print("- Minimum value:", Min)
    
            Max = max(array)
            print("- Maximum value:", Max)
    
            Sum = sum(array)
            print("- Sum of all values:", Sum)
    
            Avg = Sum / Length   
            print("- Average value:", Avg)
    
        statistics(array)


    elif choice == 7:
          print("Thank you for using the data analyzer and transformaer program.goodbye!")
          break

    else:
        print("choice is invalid! please try again")
        

        




