def change(amount):
    # Calculates the resultant change and store the result (res)
    res = []
    coins = [1, 5, 10, 25]  # Value of pennies, nickels, dimes, quarters
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}

    # Divide the amount*100 (converts amount to cents) by a coin value
    # Record the number of coins that evenly divide and the remainder
    coin = coins.pop()
    num, rem = divmod(int(amount * 100), coin)
    # Append the coin type and number of coins that had no remainder
    res.append({num: coin_lookup[coin]})

    # While there is still some remainder, continue adding coins to the result
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num: coin_lookup[coin]})
    return res
