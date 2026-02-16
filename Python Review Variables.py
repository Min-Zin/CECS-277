
print("Enter a 5 positive values: ")    #Sets prompt for the program
sum = 0                                 #Sets global variable sum
count = 1                               #Sets global variable count
while count <= 5:                       #Condition that if variable count is less then or equal to 5, keep asking for a value
    val = int(input(f"Enter the value #{count}: "))
    if val >= 0:                        #Create condition for "val" to be a positive number
        sum += val                      #Increase variables "sum" & "count"
        count += 1
    else:
        print ("Invalid value")         #Incase "val" is not a positive number
print (f"Sum = {str(sum)}")             #Prints the sum of value
print (f"Average = {str(sum / 5)}")     #Prints the average of sum
