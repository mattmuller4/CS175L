comission_rate_p = float(input("Enter comission rate percentae (ex 0.03) on stock purchase: "))
comission_rate_s = float(input("Enter comission rate percentage (ex 0.03) on stock sale: "))
num_shares_p = float(input("Enter number of shares purchased: "))
num_shares_s = float(input("Enter number of shares sold: "))
purchase_price = float(input("Enter purchase price per share: "))                   
selling_price = float(input("Enter selling price per share: "))

amountPaidForStock = num_shares_p * purchase_price
purchaseComission = comission_rate_p * amountPaidForStock
totalPaid = amountPaidForStock + purchaseComission
stockSoldFor = num_shares_s * selling_price
sellingComission = comission_rate_s * stockSoldFor
totalReceived = stockSoldFor - sellingComission
profitOrLoss = totalReceived - totalPaid

print(f'Amount paid for the stock:${amountPaidForStock: ,.2f}')
print(f'Commission paid on the purchase:${purchaseComission: ,.2f}')
print(f'Amount the stock sold for:${stockSoldFor: ,.2f}')
print(f'Commission paid on the sale:${sellingComission: ,.2f}')
print(f'Profit (or loss if negative):${profitOrLoss: ,.2f}')
 
