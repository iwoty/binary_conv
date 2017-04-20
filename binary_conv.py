entry = input().split() #creating a list from input with index[0]=number and index[1]=numeral system

if len(entry) > 2 :
    print("Enter only number to convert and actual system (2 or 10)! Nothing else!")
elif len(entry) < 2 :
    print("Enter number to convert and actual system (2 or 10)!")
elif len(entry) == 2 :

    #BINARY TO DECIMAL
    if int(entry[1]) == 2 :
        entry = entry[0][::-1] #'extended slices' [begin:end:step] - leaving begin and end, -1 reverses a string, helps with for loop
        decimal = 0
        for i in range(len(entry)) :
            x = int(entry[i])*pow(2,i)
            decimal += x #sum of powers of 2 multiplied by 0 or 1 from entry (reversed) list
        print("/----------------------------\ ")
        print("|               ",decimal,"10 |") #OUTPUT OF BINARY TO DECIMAL
        print("\----------------------------/")

    #DECIMAL TO BINARY
    elif int(entry[1]) == 10 :
        entry = int(entry[0]) #change entered number to int
        binary = [entry] #first element of the list is entered number
        while entry > 1 : #next floor divisions to list
            entry //= 2
            binary.append(entry)
        for i in range(len(binary)) : #changing the list from floor divisions to binary numbers
            binary[i] %= 2 # if there is modulus - there would be 1, if not - 0
        binary.reverse() #reverse to get proper binary number
        print("/----------------------------\ ")
        for i in range(len(binary)) :
            print(binary[i], end='') #print binary from list to one line
        print("| 2 |") #with addition of numeral system
        print("\----------------------------/")
    else : #if provided numeral system is not 2 or 10
        print("Enter only numeral system 2 or 10!")
