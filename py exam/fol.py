#todo please note this data is made up by me
# virat_kohli = "He Won 5 matches. He had a 500 rating by odi for captian. He is loved by 800000 people."
# ms_dhoni = "He Won 8 matches. He had a 600 rating by odi for captian. He is loved by 1000000 people."
# saurav_ganguly = "He Won 6 matches. He had a 450 rating by odi for captian. He is loved by 700000 people."

import fileinput
  
# Using fileinput.input() method
input_list = []
for line in fileinput.input(files ='input.txt'):
    input_list.append(line)


virat_kohli = input_list[0]
ms_dhoni =  input_list[1]
saurav_ganguly =  input_list[2]

logic = "Won Matches should be more than = 6 and Rating should be more than 499 and Should be loved by more than 700000 people to be the best captian"

def getAllImpNumbers(name):
    list_name = name.split(" ")
    imp_numbers = []
    for i in list_name:
        try:
            number  = int(i)
            imp_numbers.append(number)
        except:
            continue
    return imp_numbers

def checkallgreater(logic, name):
    if logic[0]<=name[0] and logic[1]<=name[1] and logic[2]<=name[2]:
        return True
    return False

def checkBestCaptian():
    imp_numbers_for_logic = getAllImpNumbers(logic)
    imp_numbers_for_virat_kohli = getAllImpNumbers(virat_kohli)
    imp_numbers_for_ms_dhoni = getAllImpNumbers(ms_dhoni)
    imp_numbers_for_saurav_ganguly = getAllImpNumbers(saurav_ganguly)

    print("Virat Kohli can be the best captian:", checkallgreater(imp_numbers_for_logic,imp_numbers_for_virat_kohli))
    print("Ms Dhoni can be the best captian:", checkallgreater(imp_numbers_for_logic,imp_numbers_for_ms_dhoni))
    print("Saurav Ganguly can be the best captian:", checkallgreater(imp_numbers_for_logic,imp_numbers_for_saurav_ganguly))

    
checkBestCaptian()