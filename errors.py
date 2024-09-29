def function_name():
    # Have this function generate an error
    # TypeError   x = 2 + "b"
    # ValueError  float("hello")
    # IndexError    x = [1, 2, 3];  print(x[10])
    # ZeroDivisionError  x = 3 / 0
    # NameError   x = {}  
    pas
    
def calc_square_root(n):

    try:
        from my_calculator import sqrt
    except ModuleNotFoundError:
        from math import sqrt

    answer = sqrt(n)
    return answer


    
def main():
    input_value = -4
    try:
        x = calc_square_root(input_value)
        print("Reached here")
    except TypeError:
        x = calc_square_root(int(input_value))
    except ValueError:
        x = calc_square_root(-input_value)
 
    
        
        
    print(x)
    
    
if __name__ == "__main__":
    main()
