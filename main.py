# # import pandas as pd

# # def retailPricing(imp, *args):
# #     inv=100
# #     sellthrough=20
# #     cost=10
# #     profitpercentage=2
# #     perishability=0
# #     OPEX=25
# #     print(OPEX + cost)
# #     print(inv+sellthrough+cost+profitpercentage+perishability+OPEX)
# # retailPricing(inv,sellthrough,cost,profitpercentage,perishability,OPEX)



# def fn(a):
#     return 10 * a

# lst = [1, 2, 3, 4, 5, 6]

# for i in lst:
#     lst[0] = lst[0]*10
#     print(lst[0])
#     print(lst[1])




# lst[1] = (10*lst[0])+50


# ans = []

# for lst[0] in lst:
#     x = fn(lst[0])
#     ans.append(x)
# print(ans)



import json
 
with open('data.json') as json_file:
    data = json.load(json_file)

    print("Data of ITEM 1 : ", data['item1'][0])
    print("\nPrinting nested dictionary as a key-value pair\n")
    for i in data['item1']:
        inventory = i['inventory']
        cost = i['cost']
        OPEX = i['OPEX']
        sellthrough = i['sellthrough']
        profitpercentage = i['profitpercentage']
        perishability = i['perishability']
        print("inventory = ", inventory)
        print("cost = ", cost)
        print("sellthrough = ", sellthrough)
        print("profitpercentage = ", profitpercentage)
        print("perishability = ", perishability)
        print("OPEX = ", OPEX)
        if perishability == 0:
            perishability = 1

        m = (((cost+OPEX) / inventory ) * perishability )
        pricewithprofit = cost + ( ( profitpercentage * cost ) / 100 )
        wrtperishability = pricewithprofit / (inventory - (inventory - sellthrough))
        
        print(pricewithprofit)

        print(wrtperishability)
        
        Sprice = (pricewithprofit - wrtperishability)
        intSprice = int(pricewithprofit - wrtperishability)
        print(Sprice)
        print(intSprice)

        manufacturingCost = inventory * cost
        print("Manufacturing : ", manufacturingCost )
        retSP = inventory * Sprice
        print("Selling ", retSP)
        totalProfit = retSP - manufacturingCost
        print("Total Profit : ", totalProfit)

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

