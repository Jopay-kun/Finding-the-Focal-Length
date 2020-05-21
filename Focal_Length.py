# Python Program for focal length of a spherical mirror and lens
# Determines focal length of a spherical concave mirror
# R = Radius
def focal_length_concave(R): 
    return R / 2
# Determines focal length of a spherical convex mirror
# R = Radius
def focal_length_convex(R): 
    return - ( R / 2 )
# Determines focal length of a spherical concave lens
# U = Object Distance V = Image Distance F = Focal Length
def concave():
    F = 1/V - 1/U
    return 1/F
# Determines focal length of a spherical convex lens
# U = Object Distance V = Image Distance F = Focal Length
def convex():
    F = 1/U + 1/V
    return 1/F
# Main
while True:
    print("Finding the Focal Length of a Spherical Mirror and Lens")
    print("Welcome 🙂 New here? I can explain how this system works or you can just skip ahead if you want to..")
    T = input("Ned help? Y/N? Press E to Exit:")
    if T == "Y" or T == "y":
        print("\nFinally someone who listens..")
        print("Focal length of a spherical MIRROR is distance between the focus and the pole\nWhen parallel light rays when reflected on the mirror meet at a point that Is called the\nfocal point (focus)and the length between the focal point and Pole is known as focal length\nor you can say that the centre of curvature divided by 2 is also called as focal length")
        print("Focal length of a spherical LENS is defined as the distance between optical center and focus of the lens.")
        print("\nThere are inputs in this system which involves typing just a single letter or typing numbers")
        test = input("You can try it right here: ")
        print("Got everything? Good! Lets go try it out shall we?..")
    elif T == "N" or T == "n":
        print("Well then you may carry on..")
    elif T == "E" or T == "e":
        I = input("Do you want to exit? Y/N?:")
        if I == "Y" or I == "y":
            print("Bye bye..")
            break
        elif I == "N" or I == "n":
            continue
        else:
            print("It's a Yes or No qeustion c'mon...")
            continue
    else:
        print ("A, B, and C..That's your choices..")
        continue
    while True:
        print("Focal length of what?")
        print("A.Spherical Mirror \nB.Spherical Lens \nC.Back")
        C = input("Kindly select your prefered option: ")
        if C == "A" or C == "a":
            while True:
                print("Spherical Mirror option selected..")
                print("A.Concave \nB.Convex \nC.Diffent Objects \nD.Back")
                choice = input("What do you want todo next?: ")
                if choice == 'A' or choice == 'a':
                    print ("Concave option selected.")
                    try:
                        R = float(input("Kindly enter a Radius: "))
                        print("The focal length of a spherical concave mirror is: ",focal_length_concave(R))
                    except ValueError:
                        print ("Err.. numbers only")
                        continue
                elif choice == 'B' or choice == 'b':
                    print ("Convex option selected.")
                    try:
                        R = float(input("Kindly enter a Radius: "))
                        print("The focal length of a spherical convex mirror is: ",focal_length_convex(R))
                    except ValueError:
                        print ("Err.. numbers only")
                        continue
                elif choice == "C" or choice == "c":
                    while True:
                        print("Diffent Objects selected..")
                        print("A.Basketball \nB.Small round rock \nC.The Earth \nD.Back")
                        O = input("Kindly select your prefered object: ")
                        if O == "A" or O == "a":
                            R = 4.7
                            print("The Radius of a Basketball is 4.7 Inches..")
                            print("The focal length of a Basketball in a spherical concave mirror is: ",focal_length_concave(R),"Inches")
                            print("The focal length of a Basketball in a spherical convex mirror is: ",focal_length_convex(R),"Inches")
                        elif O == "B" or O == "b":
                            R = 1.9
                            print("The Radius of a Small round rock is 1.9 Inches..")
                            print("The focal length of a Small round rock in a spherical concave mirror is: ",focal_length_concave(R),"Inches")
                            print("The focal length of a Small round rock in a spherical convex mirror is: ",focal_length_convex(R),"Inches")
                        elif O == "C" or O == "c":
                            R = 6371
                            print("The Radius of The Earth is 6,371 km..")
                            print("The focal length of The Earth in a spherical concave mirror is: ",focal_length_concave(R),"km")
                            print("The focal length of The Earth in a spherical convex mirror is: ",focal_length_convex(R),"km")
                        elif O == "D" or O == "d":
                            break
                        else:
                            print("That's not even an option..")
                            break
                elif choice == "D" or choice == "d":
                    E = input("Are you sure you want to go back? Y/N?: ")
                    if E == "Y" or E == "y":
                        print("See you next time 🙂")
                        break
                    elif E == "N" or E == "n":
                        print("Wellcome Back 🙂")
                        continue
                    else:
                        print("It's a Yes or No qeustion c'mon...")
                        continue
                else:
                    print("That's not even an option..")
                    continue
                #Looping
                Q = input("You want to try again? Y/N?: ")
                if Q == "Y" or Q == "y":
                    print("Okay here we go again...")
                    continue
                elif Q == "N" or Q == "n":
                    E = input("Do you want to go back? Y/N?: ")
                    if E == "Y" or E == "y":
                        print("Loading system...")
                        break
                    elif E == "N" or E == "n":
                        print("Loading main menu..")
                        continue
                    else:
                        print("It's a Yes or No qeustion c'mon...")
                        continue
                else:
                    print("It's a Yes or No qeustion c'mon...")
        elif C == "B" or C == "b":
            while True:
                print("Spherical Lens option selected..")
                print("A.Concave \nB.Convex \nC.Diffent Objects \nD.Back")
                choice = input("What do you want todo next?: ")
                if choice == 'A' or choice == 'a':
                    print ("Concave option selected.")
                    try:
                        U = float(input("Kindly enter Object Distance: "))
                        V = float(input("Kindly enter Image Distance: "))
                        print ("The focal length of spherical concave lens is: ",concave())
                    except ValueError:
                        print ("Err.. numbers only")
                        continue
                elif choice == 'B' or choice == 'b':
                    print ("Convex option selected.")
                    try:
                        U = float(input("Kindly enter Object Distance: "))
                        V = float(input("Kindly enter Image Distance: "))
                        print ("The focal length of spherical concave lens is: ",convex())
                    except ValueError:
                        print ("Err.. numbers only")
                        continue
                elif choice == "C" or choice == "c":
                    while True:
                        print("Diffent Objects selected..")
                        print("A.Basketball \nB.Small round rock \nC.The Earth \nD.Back")
                        O = input("Kindly select your prefered object: ")
                        if O == "A" or O == "a":
                            U = 7
                            V = U*2
                            print("The focal length of a Basketball through a concave lens is: ",concave(),"cm")
                            print("The focal length of a Basketball through a convex lens is: ",convex(),"cm")
                        elif O == "B" or O == "b":
                            U = 5
                            V = U*2
                            print("The Radius of a Small round rock is 1.9 Inches..")
                            print("The focal length of a Small round rock through a concave lens is: ",concave(),"cm")
                            print("The focal length of a Small round rock through a convex lens is: ",convex(),"cm")
                        elif O == "C" or O == "c":
                            U = 384400
                            V = U*2
                            print("The focal length of The Earth through a concave lens is: ",concave(),"km")
                            print("The focal length of The Earth through a convex lens is: ",convex(),"km")
                        elif O == "D" or O == "d":
                            break
                        else:
                            print("That's not even an option..")
                            break
                elif choice == "D" or choice == "d":
                    E = input("Are you sure you want to go back? Y/N?: ")
                    if E == "Y" or E == "y":
                        print("See you next time 🙂")
                        break
                    elif E == "N" or E == "n":
                        print("Wellcome Back 🙂")
                        continue
                    else:
                        print("It's a Yes or No qeustion c'mon...")
                        continue
                else:
                    print("That's not even an option..")
                    continue
        elif C == "C" or C == "c":
            print("Going back around now..")
            break
        else:
            print("There are only 3 choices dude..")
            continue
