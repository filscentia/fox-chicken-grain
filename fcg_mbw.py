
# Use 0 and 1 to mean left and right, but assign these to variables
# to the code is eaiser to read
# This is an 'enumeration' - python does have enumeration types but more advanced
LEFT, RIGHT = range(2)

# create globals that hold the state of where things are
fox = RIGHT
farmer = RIGHT
chicken = RIGHT
grain = RIGHT

# Return what the opposite side would be of 'thing'
# doesn't alter the side
def swap_sides(thing):
    return LEFT if thing == RIGHT else RIGHT

# Returns string that represents either left or right
# use some spacing to help with the interface
def side(s):
    return "left     _~~~~_" if s == LEFT else "         _~~~~_    right"

# Ouput the current state
def output():
    # needed to refer to the global variables
    global chicken, farmer, fox, grain

    print("\n----------------------------------------------")
    print(f"The Farmer is on the   {side(farmer)}")
    print(f"The Fox is on the      {side(fox)}")
    print(f"The Chicken is on the  {side(chicken)}")
    print(f"The Grain is on the    {side(grain)}")
    print("------------------------------------------------")

# Parse the choice, and returns True or False if the input is ok
# Also update the global state with the new sides
def parse_choice(choice: str):
    global chicken, farmer, fox, grain

    # to lower case to in case of typing errors and remove spaces
    choice = choice.lower().strip()

    # for each valid choice, swap the sides of the thing
    # always swap the farmer.
    if choice == "fox":
        if fox == farmer:
            fox = swap_sides(fox)
            farmer = swap_sides(farmer)
        else: 
            return False                   
    elif choice == "chicken":
        if chicken == farmer:
            chicken = swap_sides(chicken)
            farmer = swap_sides(farmer)
        else: 
            return False            
    elif choice == "grain":
        if grain == farmer: 
            grain = swap_sides(grain)
            farmer = swap_sides(farmer)
        else: 
            return False            
    elif choice == "farmer":
        farmer = swap_sides(farmer)
    else:
        return False

    return True

# Has anything eaten anything?
def check_eaten():
    global chicken, farmer, fox, grain

    # If the fox and chicken are on the same side, but the farmer isn't
    if fox == chicken and fox == swap_sides(farmer):
        print("The fox eats the chicken")
        return True

    # If the chicken and g rain are on the same side, but the farmet ins't    
    if chicken ==  grain and grain == swap_sides(farmer):
        print("The chicken eats the grain")
        return True


# Python standard for the main code
if __name__ == '__main__':

    print("A fox, chicken and a bag of grain wait by the side of a river.")
    print("Which item(s) will you take in your rowboat to the other side? fox, chicken, grain, or just the farmer themselves?")
    
    output()

    # use state variable to keep looping until game ends
    running = True
    while running:
        choice = input("\nChoose  (fox farmer chicken grain) : ")

        # check and update state
        if parse_choice(choice):
            output()

            # anybody or thing eaten?
            is_eaten = check_eaten()
            if is_eaten:
                print("Sorry about that.....")
                running = False
            elif fox == LEFT and grain == LEFT and chicken == LEFT and farmer == LEFT:
                # end of the game? all on the left?
                print("All safe...")
                print("Well done!")
                running = False
            elif fox == RIGHT and grain == RIGHT and chicken == RIGHT and farmer == RIGHT:
                # end of the game? all on the left?
                print("Back at the start...")                
            else:
                print("All safe... for now...")
        else:     
            print("Can't do that")
