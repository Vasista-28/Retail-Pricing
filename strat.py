from main import Sprice

print(Sprice)


#STRATERGIES IMPLEMENTATION
num_str = repr(Sprice)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)
if last_digit_str == "8":
    print( Sprice+1)
elif last_digit_str == "7":
    print(Sprice+2)
elif last_digit_str == "6":
    print(Sprice+3)
elif last_digit_str == "5":
    print(Sprice+4)
elif last_digit_str == "4":
    print(Sprice+5)
elif last_digit_str == "3":
    print(Sprice+6)
elif last_digit_str == "2":
    print(Sprice+7)
elif last_digit_str == "1":
    print(Sprice+8)

        