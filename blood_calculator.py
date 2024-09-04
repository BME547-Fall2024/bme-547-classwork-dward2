def interface():
    print("Blood Calculator")
    print("Select a test")
    print("1 - HDL")
    print("2 - LDL")
    print("3 - Total")
    print("9 - Quit")
    choice = input("Select a test: ")
    print("You selected {}".format(choice))
    if choice == "1":
        hdl_driver()


def hdl_driver():
    # Get the user input
    hdl_value = hdl_input()   
    # Compare user input against normal values
    # Output the results
    
    
def hdl_input():
    user_input = input("Enter the HDL value: ")
    user_number = int(user_input)
    return user_number
   
    
    
    
interface()

    