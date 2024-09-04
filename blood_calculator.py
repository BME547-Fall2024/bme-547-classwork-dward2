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
    elif choice == "2":
        ldl_driver()


def hdl_driver():
    # Get the user input
    hdl_value = hdl_input()   
    # Compare user input against normal values
    hdl_result = hdl_analysis(hdl_value)
    # Output the results
    hdl_output(hdl_value, hdl_result)
    
    
def hdl_input():
    user_input = input("Enter the HDL value: ")
    user_number = int(user_input)
    return user_number
    

def hdl_analysis(hdl_value):
    if hdl_value >= 60:
        return "Normal"
    elif 40 <= hdl_value < 60:
        return "Borderline Low"
    else:
        return "Low"
        
        
def hdl_output(hdl_value, hdl_analysis):
    print("The HDL value of {} is {}.".format(hdl_value, 
                                              hdl_analysis))
    return                
  
def ldl_driver():
    ldl_value = ldl_input()   
    ldl_result = ldl_analysis(ldl_value)
    ldl_output(ldl_value, ldl_result)
    
    
def ldl_input():
    user_input = input("Enter the LDL value: ")
    user_number = int(user_input)
    return user_number
    

def ldl_analysis(ldl_value):
    if ldl_value < 130:
        return "Normal"
    elif 130 <= ldl_value <= 159:
        return "Borderline High"
    elif 160 <= ldl_value <= 189:
        return "High"
    else:
        return "Very High"
        
        
def ldl_output(ldl_value, ldl_analysis):
    print("The LDL value of {} is {}.".format(ldl_value, 
                                              ldl_analysis))
    return                

   
    
    
    
interface()

    