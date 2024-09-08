
def change(amount):
    #Calculate the resultant change and store the result (res)
    res = []
    coins = [1,5,10,25] # value of pennies, nickels, dimes, quarters
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}

    #divide the amounts*100 ( the amounts in cents) by a coin value
    #record the number of coins that evently divide and the remainder 
    coin = coins.pop()
    num, rem = divmod(int(amount*100), coin)
    #append the coin type and number of coins that had no remainder 
    res.append({num:coin_lookup[coin]})

    # while there is still some remainder, continue adding coins to the res
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num:coin_lookup[coin]})
    return res