'''
Ask user to enter a number
ask the user to if they want to stop
convert to float if added a demcial number
if user enters -1 then the programme will stop
update num_loopy and count
calculate and print average
'''
total = 0
count = 0


while True:
    user_input = input("Enter a number or enter -1 to stop: ")
    if user_input == "-1":
         break
    try:
        number = float(user_input)
    
    except ValueError:
        print ("Invalid, please enster a valid number")

total += number
count += 1
  
if count > 0:
        print("Programme stopped")
        average = total / count # calculate average
       
        print(f"The average of entered numbers is: {average}") # print the average
else:
        print("no valid numbers were entered. Cannot calculate an average.")