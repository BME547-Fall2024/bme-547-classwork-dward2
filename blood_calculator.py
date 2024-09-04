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
  

   
    
    
    
interface()

    