from main import Sprice, intSprice

print("Sprice : ", Sprice)
print("int Sprice: ", intSprice)


#STRATERGIES IMPLEMENTATION

num_str = repr(intSprice)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)

x = 9 - int(last_digit_str)
a = Sprice + x

print("Final Price : ", a)

# if last_digit_str == "8":
#     print( a )
# elif last_digit_str == "7":
#     print(a)
# elif last_digit_str == "6":
#     print(Sprice+3)
# elif last_digit_str == "5":
#     print(Sprice+4)
# elif last_digit_str == "4":
#     print(Sprice+5)
# elif last_digit_str == "3":
#     print(Sprice+6)
# elif last_digit_str == "2":
#     print(Sprice+7)
# elif last_digit_str == "1":
#     print(Sprice+8)

def strat1(Sprice):
    num_str = repr(intSprice)
    last_digit_str = num_str[-1]
    last_digit = int(last_digit_str)
    x = 9 - int(last_digit_str)
    a = Sprice + x
    print("Final Price : ", a)

def strat2(Sprice):
    return Sprice