'''
Two part task which initially looks at defensive coding as part of creating a calculator function which saves to file, before printing.
Using ValueError and "end" to manage input.
'''
#creating the calculation function and id user input requirements
def calculation():
  with open ('calc_file.txt', 'a') as equation_file:
   total_sum =0
   while True:
      is_valid = False
      user_num1 = input("Pick your first number:\t(or to exit type: end)")
      if user_num1 == "end":
         print("Goodbye")
         break
      user_operator = input("Select the operation you'd like to apply to these two numbers.\nType: \n +\t if you'd like to add these two numbers together. \n -\t if you'd like to subtract. \n x\t if you'd like to multiple these numbers:  ")
      user_num2 = input("Pick your second number:\t")
     #managing user inputs against defined requirements for 'successful' input
      try:
         user_num1 = int(user_num1)
         user_num2 = int(user_num2)
         is_valid =True
      except:
        raise ValueError("There is an error. Only enter valid numbers.")
      if is_valid and user_operator == "+":
         total_sum = user_num1 + user_num2
         print("The total from adding two numbers ", user_num1, " and ", user_num2, " is: ", total_sum)
      elif is_valid and user_operator == "-":
         total_sum = user_num1 - user_num2
         print("The total from subtracting two numbers ", user_num1, " and ", user_num2, " is: ", total_sum)
      elif is_valid and user_operator == "x":
         total_sum = user_num1 * user_num2
         print("The total from multiplying two numbers ", user_num1, " and ", user_num2, " is: ", total_sum)  
      elif is_valid and user_operator != "+" or "-" or "x":
         print("There is an error. Goodbye")
         break
      
      #writing inputs to file
      equation_file.write(f'{user_num1}')
      equation_file.write(" ")
      equation_file.write(f'{user_operator}')
      equation_file.write(" ")
      equation_file.write(f'{user_num2}')
      equation_file.write(" = ")
      equation_file.write(f'{total_sum}')
      equation_file.write('\n')

calculation()

#reading the file with saved equations
with open('calc_file.txt', 'r')as equation_file:
   print(equation_file.read())

'''
The second part of the task creates different options for users to either create an equation,read existing 
equations or name and create a new file. 
'''
#functions to open the file (option b)
def choose_b ():
   with open('calc_file.txt', 'r')as equation_file:
      print(equation_file.read())

#user input file named version of calculation. using "end" to print new_file_equations" 
def user_name_calc():
   user_new_file= input("Enter a file_name <no-spaces_between_words>:\t")
   with open(f'{user_new_file}.txt','a') as my_new_file:
      total_sum =0
      while True:
         is_valid = False
         user_num1 = input("Pick your first number:\t(or to exit type: end)")
         if user_num1 == "end":
            print("Goodbye")
            break
         user_operator = input("Select the operation you'd like to apply to these two numbers.\nType: \n +\t if you'd like to add these two numbers together. \n -\t if you'd like to subtract. \n x\t if you'd like to multiple these numbers:  ")
         user_num2 = input("Pick your second number:\t")
         try:
            user_num1 = int(user_num1)
            user_num2 = int(user_num2)
            is_valid =True
         except:
            raise ValueError("There is an error. Only enter valid numbers.")
         if is_valid and user_operator == "+":
            total_sum = user_num1 + user_num2
            print("The total from adding two numbers ", user_num1, " and ", user_num2, " is: ", total_sum)
         elif is_valid and user_operator == "-":
            total_sum = user_num1 - user_num2
            print("The total from subtracting two numbers ", user_num1, " and ", user_num2, " is: ", total_sum)
         elif is_valid and user_operator == "x":
            total_sum = user_num1 * user_num2
            print("The total from multiplying two numbers ", user_num1, " and ", user_num2, " is: ", total_sum)  
         elif is_valid and user_operator != "+" or "-" or "x":
            print("There is an error. Goodbye")
            break   
         my_new_file.write(f'{user_num1}')
         my_new_file.write(" ")
         my_new_file.write(f'{user_operator}')
         my_new_file.write(" ")
         my_new_file.write(f'{user_num2}')
         my_new_file.write(" = ")
         my_new_file.write(f'{total_sum}')
         my_new_file.write('\n')
   with open(f'{user_new_file}.txt','r') as my_new_file:
      print(my_new_file.read())


#user choice options A for creating an equation, or B for reading equations on existing file, of C for creating a new file for equations. Using 'upper' to reduce user errors
user_choice =""
user_choice = input("Type A for creating an equation(to exit type: end), type B for reading the equations stored on file, or type C to create new file:\t").upper()
if user_choice == "A":
   calculation()
elif user_choice == "B":
   print("Good choice, here are the equations")
   choose_b()
elif user_choice == "C":
  user_name_calc()
else:
   print("There has been an error! Goodbye")
  # exit()
