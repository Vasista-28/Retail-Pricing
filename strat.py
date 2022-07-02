import webbrowser
import time
from main import Sprice, intSprice

print("Sprice : ", Sprice)
print("int Sprice: ", intSprice)


#STRATERGIES IMPLEMENTATION

num_str = repr(intSprice)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)
if Sprice > 500:
    x = 9 - int(last_digit_str)
    global a
    a = Sprice + x
    print("Final Price : ", int(a))
    
else:
    print("Final Price : ", int(Sprice))
