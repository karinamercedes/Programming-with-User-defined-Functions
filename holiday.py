# Your task will be to calculate a user’s total holiday cost
# which includes the plane cost, hotel cost, and car-rental cost.

# Function to calculate hotel cost
def hotel_cost(num_nights):
    # Assuming hotel cost per night is £80
    return num_nights * 80

# Function to calculate plane cost
# Different cost for different cities
def plane_cost(city_flight):
    if city_flight == "Rome":
        return 100
    elif city_flight == "Paris":
        return 120
    elif city_flight == "London":
        return 150
    elif city_flight == "Barcelona":
        return 200
    else:
        print ("Destination Error")
        cities ()

# Function to calculate car rental cost
def car_rental(rental_days):
    # Assuming the car rental cost per day is £50
    return rental_days * 50


# Function to calculate total holiday cost
def holiday_cost(hotel_cost, plane_cost, car_rental):
    # Calculating individual costs
    hotel = hotel_cost(num_nights)
    flight = plane_cost(city_flight)
    car = car_rental(rental_days)
    # Sum of all the costs
    total_cost = hotel + flight + car
    # Returning total cost
    return total_cost


#Function for menu of different cities/choices
def cities():
    print("\nFor your next holiday, we've selected these possile destionations: ")
    print("\nRome")
    print("Paris")
    print("London")
    print("Barcelona")
    print("None of the above")

# Get inputs from user and calculate chosen destination cost
print("Welcome to your holiday cost calculator!")
city_flight = "x"
cities ()
while city_flight != "None of the above":
    # I add capitalize method to have coherent and grammatically correct inputs and outputs
    city_flight = str.capitalize(input("\nPlease enter your choice: "))

    #I reserched how to express multiple conditions (OR) in one statement
    # if variable in ("x", "y", "z"):  can also be express as  if variable == ("x") or ("y") or ("z"):
    if city_flight in ("Rome", "Paris", "London", "Barcelona"):
        num_nights = int(input(f"Enter the number of nights you want to spend in {city_flight}: "))
        rental_days = int(input("We also offer car rental service for your holiday.\nEnter the number of days for which you will be hiring a car : "))
        print("\nHoliday Details:\n----------------------------------------------")
        print(f"Destination: {city_flight}")
        print(f"Number of Nights in Hotel: {num_nights}")
        print(f"Number of Days for Car Rental: {rental_days}")
        print("----------------------------------------------")
        print(f"Total Holiday Cost: {holiday_cost(hotel_cost, plane_cost, car_rental)}")
        print("\nLooking forward to traveling with you!")
        print("")
        break
    elif city_flight == "None of the above":
        print ("\nSorry, at the moment these are the only destinations available.")
    else:
        # If the user's choice is not on the list of cities, I want to ask again for input
        print ("\nUnrecognized Choice")
        cities ()

