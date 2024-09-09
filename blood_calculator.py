def interface():
    print("Blood Calculator")
    while True:
        print("Select a test")
        print("1 - HDL")
        print("2 - LDL")
        print("3 - Total")
        print("9 - Quit")
        choice = input("Select a test: ")
        print("You selected {}".format(choice))
        if choice == "1":
            hdl_driver()
        elif choice == "2":
            ldl_driver()
        elif choice == "9":
            break


def hdl_driver():
    # Get the user input
    test_name = "HDL"
    hdl_value = generic_input(test_name)   
    # Compare user input against normal values
    hdl_result = hdl_analysis(hdl_value)
    # Output the results
    generic_output(test_name, hdl_value, hdl_result)
    
    
def generic_input(test_name):
    user_input = input("Enter the {} value: ".format(test_name))
    user_number = int(user_input)
    return user_number
    

def hdl_analysis(hdl_value):
    if hdl_value >= 60:
        return "Normal"
    elif 40 <= hdl_value < 60:
        return "Borderline Low"
    else:
        return "Low"
        
        
def generic_output(test_name, value, analysis):
    print("The {} value of {} is {}.".format(test_name, value, 
                                              analysis))
    return                
  
def ldl_driver():
    test_name = "LDL"
    ldl_value = generic_input(test_name)   
    ldl_result = ldl_analysis(ldl_value)
    generic_output(test_name, ldl_value, ldl_result)
    
    
def ldl_analysis(ldl_value):
    if ldl_value < 130:
        return "Normal"
    elif 130 <= ldl_value <= 159:
        return "Borderline High"
    elif 160 <= ldl_value <= 189:
        return "High"
    else:
        return "Very High"
        
            
interface()

    