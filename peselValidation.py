pesel = "02070803628"
pesel_list =[int(i) for i in pesel]

if len(pesel_list) != 11:
    print("PESEL number must have 11 digits")
    exit()

def sex(pesel_list):
    if pesel_list[-2] % 2 == 0:
        return("women")
    else:
        return("man")
    
year = pesel[:2]
month = int(pesel[2:4])

if month >=20:
    month -=20
else:
    month = int(pesel[3])
day = pesel[4:6]

control_number = 0
weight = [1,3,7,9,1,3,7,9,1,3]

for i in range(len(weight)):
    if(weight[i] * pesel_list[i]) >9:
        control_number += (weight[i] * pesel_list[i]) % 10 
    else:
        control_number += (weight[i] * pesel_list[i])

control_number  = 10 - (control_number % 10) if control_number > 9 else 10 - control_number

pesel_correct = control_number == pesel_list[-1]

print(f"Date of birth: {day}-{month}-{year} Sex: {sex(pesel_list)} Pesel correct: {pesel_correct}")


