import webbrowser
import time
from main import Sprice, intSprice

print("Sprice : ", Sprice)
print("int Sprice: ", intSprice)


#STRATERGIES IMPLEMENTATION

num_str = repr(intSprice)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)
if int(last_digit_str) == 1:
    a1 = round(Sprice-2,2)
    print("Final Price : ", a1, "Rupees")
    # print("Final Price: ", round(Sprice - 2,2), "Rupees")
elif int(last_digit_str) == 2:
    a1 = round(Sprice - 3,2)
    print("Final Price: ", round(Sprice - 3,2), "Rupees")
elif int(last_digit_str) == 3:
    a1 = round(Sprice - 4,2)
    print("Final Price: ", round(Sprice - 4,2), "Rupees")
elif int(last_digit_str) == 4:
    a1 = round(Sprice - 5,2)
    print("Final Price: ", round(Sprice - 5,2), "Rupees")
elif int(last_digit_str) == 5:
    a1 = round(Sprice - 6,2)
    print("Final Price: ", round(Sprice - 6,2), "Rupees")
elif int(last_digit_str) == 6:
    a1 = round(Sprice - 7,2)
    print("Final Price: ", round(Sprice - 7,2), "Rupees")
elif int(last_digit_str) == 7:
    a1 = round(Sprice - 8,2)
    print("Final Price: ", round(Sprice - 8,2), "Rupees")
elif int(last_digit_str) == 8:
    a1 = round(Sprice - 9,2)
    print("Final Price: ", round(Sprice - 9,2), "Rupees")
elif int(last_digit_str) == 0:
    a1 = round(Sprice - 1,2)
    print("Final Price: ", round(Sprice - 1,2))
elif int(last_digit_str) == 9:
    a1 = round(Sprice,2)
    print("Final Price: ", round(Sprice,2))