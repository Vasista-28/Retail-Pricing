from cmath import cos
from tokenize import ContStr
import flask
# from flask import Flask, render_template


app = flask.Flask(__name__,template_folder='template')

@app.route("/")
def index():
    # return "Hello"
    from main import pricewithprofit, Sprice
    from strat import a1

    cost1 = str(pricewithprofit)
    Sprice1 = int(Sprice)
    a2 = int(a1)

    return flask.render_template("index.html", a1=a2,Sprice=Sprice, pricewithprofit=pricewithprofit)
    # # print("Price : ", Cost, "Discount : ", a )
    # return str(cost)
    # return str(a)
    # return "Hi"
# , Sprice=Sprice, a=a, cost=cost
if __name__=="__main__":
    # app.debug = True
    app.run()
