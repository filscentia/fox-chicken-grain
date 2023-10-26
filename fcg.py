# Fox, chicken, grain program
fox = 0
chicken = 0
grain = 0
farmer = 0
check_2 = 0
check = 0
print ("A fox, chicken and a bag of grain wait by the side of a river. Which item will you take in your rowboat to the other side? Fox, chicken, grain or farmer?")

choice = input("Choose:")
def choice(one):
   
    
   if choice == "farmer" and farmer == 0:
     farmer == 1
   elif choice == "fox" and fox == 0 and farmer == 0:
    fox == 1
    farmer == 1
   elif choice == "chicken" and chicken == 0 and farmer == 0:
    chicken == 1
    farmer == 1
   elif choice == "grain" and grain == 0 and farmer == 0:
    grain == 1
    farmer == 1
   elif choice == "grain" and grain == 0:
    grain == 1
    farmer == 1
   else:
     print ("That's not an answer.")
    
   def output(): 
      print("\n -----------------------------------")
      if farmer == 1:
          print("\nThe Farmer is on the left of the river.")
      if fox == 1:
          print("\nThe Fox is on the left of the river.")
      if chicken == 1:
          print("\nThe Chicken is on the left of the river.")
      if grain == 1:
          print("\nThe Grain is on the left of the river.")
      if farmer == 0:
          print("\nThe Farmer is on the right of the river.")
      if fox == 0:
          print("\nThe Fox is on the right of the river.")
      if chicken == 0:
          print("\nThe Chicken is on the right of the river.")
      if grain == 0:
          print("\nThe Grain is on the right of the river.")
      print("\n -----------------------------------")
    

    

#Wrong move program

if fox == 0 and chicken == 0 and farmer == 1: 
    print ("The fox eats the chicken")
    check_2 == 1
elif fox == 1 and chicken == 1 and farmer == 0:
    print ("The fox eats the chicken")
    check_2 == 1
else:
    check == 0
if chicken == 0 and grain == 0 and farmer == 1:
    print("The chicken eats the grain")
    check_2 == 1
elif chicken ==1 and grain == 1 and farmer == 0:
    print("The chicken eats the grain")
    check_2 == 1
else:
   check == 0
  
