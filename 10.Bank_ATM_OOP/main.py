from banking import Banking


islem = Banking('1234','ismail','baser','12345')

print(f'ilk balance: {islem.balance}')

islem.balance=500
print(f'balance: {islem.balance}')

islem.withraw(500)

print(f'son balance: {islem.balance}')