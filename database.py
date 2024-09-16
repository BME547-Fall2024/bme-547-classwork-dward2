def load_data():
    in_file = open("blood_test_data.txt", "r")
    for line in in_file:
        new_patient = line.strip("\n")
        print(new_patient)
    in_file.close()
    
    # with open("blood_test_data.txt", "r") as in_file:
    #     for line in in_file:
    #         new_patient = line.strip("\n")
    #         print(new_patient)

        
        
def main():
    load_data()
    
    
if __name__ == "__main__":
    main()

    