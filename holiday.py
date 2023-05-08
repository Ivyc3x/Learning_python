
#creating several functions to calculate different categories towards holiday costs (flight, hotel and car rental)
#in each category function the subcosts are saved to file

#working out flight costs- adjusting options for arrival airport depending on departure airport selection
def plane_costs():
    #open file and overwrite existing content from earlier calculations
    with open ('holcalc_file.txt', 'w') as holcost_file:
        #print(depart_options[0])
        depart_options =['Manchester','Newcastle','Cardiff','Inverness']  
        destin_options = ['Manchester','Newcastle','Cardiff','Inverness']  
        for count, airport in enumerate(depart_options,start=1):
            print(count, airport)
        user_choice_depart= input("Type the number of the airport you are departing from:\t")
        flight_cost_single =" "
        #departure user_choice 1 Manchester
        if user_choice_depart=="1":
            print("\nYou have selected to depart from",depart_options[0],"\nHere are your destination airport options: ")
            destin_options1= destin_options.copy()
            destin_options1.remove("Manchester")
            for count, airport1 in enumerate(destin_options1,start=1):
                print(count, airport1)
            user_choice_destin = input("Type the number of the airport you will fly to:\t")
            if user_choice_destin=="1":
                flight_cost_single =200
                print("\nYou have selected to fly to",destin_options1[0])
                print("Your one way flight will cost:\t£",flight_cost_single)
            elif user_choice_destin=="2":
                flight_cost_single =200
                print("\nYou have selected to fly to",destin_options1[1])
                print("Your one way flight will cost:\t£",flight_cost_single)
            elif user_choice_destin=="3":
                flight_cost_single=300
                print("\nYou have selected to fly to",destin_options1[2])
                print("Your one way flight will cost:\t£",flight_cost_single)
        #departure user_choice 2 Newcastle
        elif user_choice_depart=="2":
            print("\nYou have selected to depart from",depart_options[1],"\nHere are your destination airport options: ")
            destin_options2= destin_options.copy()
            destin_options2.remove("Newcastle")
            for count, airport2 in enumerate(destin_options2,start=1):
                print(count, airport2)
            user_choice_destin = input("Type the number of the airport you will fly to:\t")
            if user_choice_destin=="1":
                flight_cost_single = 200
                print("\nYou have selected to fly to",destin_options2[0])
                print("Your one way flight will cost:\t£",flight_cost_single)
            elif user_choice_destin=="2":
                flight_cost_single = 185
                print("\nYou have selected to fly to",destin_options2[1])
                print("Your one way flight will cost:\t£",flight_cost_single)
            elif user_choice_destin=="3":
                flight_cost_single = 120
                print("\nYou have selected to fly to",destin_options2[2])
                print("Your one way flight will cost:\t£",flight_cost_single)
        #departure user_choice 3 Cardiff
        elif user_choice_depart=="3":
            print("\nYou have selected to depart from",depart_options[2],"\nHere are your destination airport options: ")
            destin_options3= destin_options.copy()
            destin_options3.remove("Cardiff")
            for count, airport3 in enumerate(destin_options3,start=1):
                print(count, airport3)
            user_choice_destin = input("Type the number of the airport you will fly to:\t")
            if user_choice_destin=="1":
                flight_cost_single = 175
                print("\nYou have selected to fly to",destin_options3[0])
                print("Your one way flight will cost:\t£",flight_cost_single)
            elif user_choice_destin=="2":
                flight_cost_single = 185
                print("\nYou have selected to fly to",destin_options3[1])
                print("Your one way flight will cost:\t£",flight_cost_single)
            elif user_choice_destin=="3":
                flight_cost_single = 320
                print("\nYou have selected to fly to",destin_options3[2])
                print("Your one way flight will cost:\t£",flight_cost_single)
        #departure user_choice 4 Inverness
        elif user_choice_depart=="3":
            print("\nYou have selected to depart from",depart_options[3],"\nHere are your destination airport options: ")
            destin_options4= destin_options.copy()
            destin_options4.remove("Inverness")
            for count, airport4 in enumerate(destin_options4,start=1):
                print(count, airport4)
            user_choice_destin = input("Type the number of the airport you will fly to:\t")
            if user_choice_destin=="1":
                flight_cost_single = 300
                print("\nYou have selected to fly to",destin_options4[0])
                print("Your one way flight will cost:\t£",flight_cost_single)
            elif user_choice_destin=="2":
                flight_cost_single = 120
                print("\nYou have selected to fly to",destin_options4[1])
                print("Your one way flight will cost:\t£",flight_cost_single)
            elif user_choice_destin=="3":
                flight_cost_single = 320
                print("\nYou have selected to fly to",destin_options4[2])
                print("Your one way flight will cost:\t£",flight_cost_single)
        else:
            print("There has been an error.  Goodbye!")
            exit()
        #user to decide whether a single or return ticket is needed
        user_choice_return= input("Would you like a return ticket?\nType: Y or N\t").upper()
        if user_choice_return == "Y":
            flight_cost = flight_cost_single * 2
            print("Your return ticket will cost:\t£",flight_cost)
            holcost_file.write("Flight cost:")
            holcost_file.write(f'{flight_cost}')
            holcost_file.write("\n")
        elif user_choice_return =="N":
            flight_cost =flight_cost_single
            print("Okay, your ticket will remain as:\t£",flight_cost)
            holcost_file.write("Flight cost:")
            holcost_file.write(f'{flight_cost}')
            holcost_file.write("\n")
        else:
            print("There has been an error.  Goodbye!")
            exit()
    return (flight_cost)

#hotel costs by type of room and length of stay
def hotel_cost():
    #print(room_options[0])
    with open ('holcalc_file.txt', 'a') as holcost_file:
        room_options=['single', 'double']
        user_choice_room = ""
        #total_cost_hotel = 0
        cost_per_night = 0
        print("\nThe Grand hotel is the perfect place for your city break")
        user_choice_nights = int(input("How many nights do you wish to stay at the hotel?\t"))
        print("Here are the different rooms available:\n")
        for count, nights in enumerate(room_options,start=1):
            print(count, nights)
        user_choice_room = input("Enter the number of the type of room you'd like to book:\t")
        if user_choice_room =="1":
                cost_per_night = 120
                total_cost_hotel = user_choice_nights * cost_per_night
                print("\nYou have selected to book a",room_options[0],"for",user_choice_nights,"nights at £",cost_per_night,"per night")
                print("The total cost for your hotel stay will be £\t", total_cost_hotel)
                holcost_file.write("Hotel cost:")
                holcost_file.write(f'{total_cost_hotel}')
                holcost_file.write("\n")
        elif user_choice_room =="2":
                cost_per_night = 160
                total_cost_hotel = user_choice_nights * cost_per_night
                print("\nYou have selected to book a",room_options[1],"for",user_choice_nights,"nights at £",cost_per_night,"per night")
                print("The total cost for your hotel stay will be £\t", total_cost_hotel)
                holcost_file.write("Hotel cost:")
                holcost_file.write(f'{total_cost_hotel}')
                holcost_file.write("\n")
        else:
            print("There has been an error.  Goodbye!")
            exit()
    return (total_cost_hotel)

#car rental by number of days renting and type of car
def car_rental():
    #print(car_options[0])
    with open ('holcalc_file.txt', 'a') as holcost_file:
        car_options=['Two-door city car', 'Four-door saloon car']
        user_choice_car = ""
        cost_per_day = 0
        user_choice_days = int(input("How many days do you want to hire a car?\t"))
        print("Choose the best car for your city break\n")
        print("Here are the different cars available:\n")
        for count, days in enumerate(car_options,start=1):
            print(count, days)
        user_choice_car = input("Enter the number of the type of car you'd like to book:\t")
        if user_choice_car =="1":
                cost_per_day = 40
                total_cost_car = user_choice_days * cost_per_day
                print("\nYou have selected to book a",car_options[0],"for",user_choice_days,"days at £",cost_per_day,"per day")
                print("The total cost for your car rental will be £\t", total_cost_car)
                holcost_file.write("Car cost:")
                holcost_file.write(f'{total_cost_car}')
                holcost_file.write("\n")
        elif user_choice_car =="2":
                cost_per_day = 55
                total_cost_car = user_choice_days * cost_per_day
                print("\nYou have selected to book a",car_options[1],"for",user_choice_days,"days at £",cost_per_day,"per day")
                print("The total cost for your car rental will be £\t", total_cost_car)
                holcost_file.write("Car cost:")
                holcost_file.write(f'{total_cost_car}')
                holcost_file.write("\n")
        else:
            print("There has been an error.  Goodbye!")
            exit()
    return (total_cost_car)

#function to open the file to read a breakdown of costs per category
def hol_file_open():
   with open('holcalc_file.txt', 'r')as holcost_file:
      print(holcost_file.read())

#function to open the file to split text and convert breakdown costs into integers and to sum total holiday costs
def hol_file_open2():
   with open('holcalc_file.txt', 'r')as holcost_file:
    info = holcost_file.readlines()
    type_cost =[]
    cost_item =[]
    for i in info:
            as_list= i.split(':')
            type_cost.append(as_list[0])
            cost_item.append(as_list[1].strip("\n"))
            total_int =[int(x)for x in cost_item]
    print("Your total holiday cost is:\t£",sum(total_int))
  
def holiday_costs():
    #walking the user through the holiday calculator and calling definitions at appropriate times
    print("Welcome to the city break calculator\nUse this calculator to cost your flight, hotel and car rental\n")
    print("Select one of the following options:\n")
    menu_options=['Begin your holiday calculation','Exit the calculator']
    print(menu_options[0])
    for count, menu in enumerate(menu_options,start=1):
        print(count, menu)
    user_choice_menu=input("\nType the number of the option you want:\t") 
    if user_choice_menu =="1":
        plane_costs()
        print("\nNow work out your hotel details")
        hotel_cost()
        print("\nLastly, decide on your car rental")
        car_rental()
        print("\nThank you for using the city break calculator\nHere are the final details for your holiday")  
        hol_file_open()
        hol_file_open2()
    elif user_choice_menu =="2":
        print("You've selected to leave the holiday calculator.  Goodbye!")
        exit()
    else:
        raise TypeError("There has been an error in your menu choice")
    exit()

holiday_costs()
 
