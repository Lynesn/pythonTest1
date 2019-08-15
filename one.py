#Write a Python program which accepts the radius and height from the user and computes the volume
#of a cylinder. Formula is: 3.14 x radius x radius x height (bonus points for creativity)

pi = 3.14      # declare a constand variable pi

radius = float(input("Enter radius:"))  #prompt user to enter radius
height = float(input("Enter height:"))  # prompt user to enter height.
volume = 3.14*radius*radius*height     # variable volume given by formular

print("The Volume is", volume)     # display final volume.
