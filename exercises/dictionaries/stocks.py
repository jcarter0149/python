stockDict = {'GM': 'General Motors', 'CAT': 'Caterpillar', 'EK': 'Eastman Kodak'}

purchases = [ ('GM', 100, '10-sep-2001', 48),
    ('CAT', 100, '1-apr-1999', 24),
    ('EK', 200, '1-jul-1998', 56)]

for company, v in stockDict.items():
    if company == purchases[0][0]:
        print(v, purchases[0][1] * purchases[0][3], purchases[0][2])
    elif company == purchases[1][0]:
        print(v, purchases[1][1] * purchases[1][3], purchases[1][2])
    elif company == purchases[2][0]:
<<<<<<< HEAD
        print(v, purchases[2][1] * purchases[2][3], purchases[2][2])



stockDict = { 'GE': 'General Electric',
 'MSFT': 'Microsoft',
 'APPL': 'Apple',
 'CAT':'Caterpillar', 'EK':'Eastman Kodak' }

purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
 ( 'CAT', 100, '1-apr-1999', 24 ),
 ( 'MSFT', 1000, '1-apr-1999', 198 ),
 ( 'MSFT', 250, '1-apr-1999', 75 ),
 ( 'MSFT', 333, '1-apr-1999', 100 ),
 ( 'APPL', 50, '1-apr-1999', 144 ),
 ( 'EK', 300, '5-apr-2017', 9 ),
 ( 'GE', 200, '1-jul-1998', 56 ) ]



























portfolio = dict()
for purchase in purchases:
    ticker = purchase[0]

    full_company_name = stockDict[ticker]
    number_of_shares = purchase[1]
    purchase_price = purchase[3]
    full_purchase_price = number_of_shares * purchase_price

    minimal_purchase = (purchase[1], purchase[2], purchase[3])

    try:
        portfolio[ticker].append(purchase) # Append the purchase to the ticker list
    except KeyError:
        portfolio[ticker] = list() # If the key doesn't exist yet, create it
        portfolio[ticker].append(purchase)


    print("I purchased {} stock for ${}".format(full_company_name, full_purchase_price))

print(portfolio)







for ticker,purchases in portfolio.items():
    print("------ {} ------".format(ticker))
    total_portfolio_stock_value = 0
    for purchase in purchases:
        total_portfolio_stock_value += purchase[1] * purchase[3]
        print("    {}".format(purchase))
    print("Total value of stock in portfolio: ${}\n\n".format(total_portfolio_stock_value))
=======

        print(v, purchases[2][1] * purchases[2][3], purchases[2][2])

        print(v, purchases[2][1] * purchases[2][3], purchases[2][2])

>>>>>>> 12eef606c680ee7f01bbcbf5178c2abc673b3306
