print(r'''
*******************************************************************************
                                        /\ /\
                                          /  \---._
                                         / / `     `\
                                         \ \   `'<@)@)      
                                         /`         ~ ~._ 
                                        /                `() 
                                       /    \   (` ,_.:.  /
                                      / ~    `\   (vVvvvvV
                                     /       |`\_ `^^^/
                                 ___/________|_  `---'
                                (___R_U_B_Y_<3__) _
                                _/~          | `(_)
                              _/~             \  
                            _/~               |
                          _/~                 |
                        _/~                   |
                      _/~         ~.          |
                    _/~             \        /\
                 __/~               /`\     `||
               _/~      ~~-._     /~   \     ||
              /~             ~./~'      \    |)
             /                 ~.        \   )|
            /                    :       |   ||
            |                    :       |   ||
            |                   .'       |   ||
       __.-`                __.'--.      |   |`---. 
    .-~  ___.         __.--~`--.))))     |   `---.)))
   `---~~     `-...--.________)))))      \_____)))))
*******************************************************************************
''')
print("Hey! Can you help Francine find her favorite dog Ruby?")
print("Ruby was last seen on the street outside their house.")

direction = str(input("Would you want to go left or right? Enter 'left' or 'right'. "))
if direction.lower() == "left":
    print("__________________________________________________________\n"
          "Their neighbor had a big dog and Ruby would not go there.\n"
          "You lost track of Ruby and she went farther.\n"
          "Game over.\n"
          "__________________________________________________________")
elif direction.lower() == "right":
    print("Great job! You saw Ruby's foot prints but it was gone near a fork road.")
    location = str(input("Do you think Ruby went to the park or the store? Enter 'park' or 'store'. "))
    if location.lower() == "park":
        print("__________________________________________________________\n"
        "Kids were playing at the park and Ruby does not want to be near other people as she gets scared.\n"
        "She went farther and now you lost her.\n"
        "Game over.\n"
        "__________________________________________________________")
    elif location.lower() == "store":
        print("She's at the store as she smelled dog food. Which room do you think Ruby went into?")
        door = str(input("Orange, Green, or Purple? "))
        if door.lower() == "purple":
            print("__________________________________________________________\n"
            "You entered a dark room with a broken door knob.\n" 
            "Now you can't get out.\n"
            "Game over.\n"
            "__________________________________________________________")
        elif door.lower() == "green":
            print(".:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.\n"
            "Excellent choice! You saw Ruby eating some of the dog food displayed on this room.\n"
            "You carry Ruby and bring her back to Francine.\n"
            "You win! Congratulations!\n"
            ".:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.")
        elif door.lower() == "orange":
            print("__________________________________________________________\n"
            "You entered an empty room.\n"
            "Ruby was nowhere to be seen.\n"
            "Game over.\n"
            "__________________________________________________________")
        else:
            print (">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><\n"
            "You gave an incorrect color and was unable to find Ruby.\n"
            "Game over.\n"
            ">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
    else:
        print(">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><\n"
        "Please choose a location from the choices.\n"
        "Game over.\n"
        ">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
else:
    print(">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><\n"
    "Please choose a direction from the choices.\n"
    "Game over.\n"
    ">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
