# CPS305 Fall 2020
# Lab 4 Q2
# Yong Kang He
# 500570639

# This function will take a list of strings and return the total capital gain or loss
# The strings in orders will only be of the form "buy x share(s) at $y each" or "sell x share(s) at $y each"
# You may assume that input is valid (ie. there will be enough shares owned to fulfill a sell order)
def calculateCapitalGain(orders):
    # Your code here
    gain = 0
    purchase = []
    for i in orders:
        i=i.replace('$','')
        line = i.split()
        shares = int(line[1])
        cost = int(line[4])
        if 'buy' in line:
            purchase.append([shares,cost])
        else:
            while shares > 0:
                if purchase[0][0] > shares:
                    purchase[0][0] -= shares
                    gain+= shares * (cost-purchase[0][1])
                    shares = 0
                else:
                    gain+=purchase[0][0]* (cost-purchase[0][1])
                    shares-= purchase[0][0]
                    purchase.pop(0)
    return gain
            
        


# DO NOT EDIT THE FOLLOWING CODE
orders = [
    "buy 100 share(s) at $20 each",
    "sell 50 share(s) at $22 each",
    "buy 250 share(s) at $23 each",
    "sell 200 share(s) at $18 each",
    "buy 400 share(s) at $21 each",
    "sell 300 share(s) at $27 each"
]

capitalGain = calculateCapitalGain(orders)
print(capitalGain)