product1_name,product1_price='Stickynotes' ,50
product2_name,product2_price='Notebook' ,75 
product3_name,product3_price='Studytable' ,800 
product4_name,product4_price='Eraser' ,10
product5_name,product5_price='Craftpaper',30 
product6_name,product6_price='Pens',10
product7_name,product7_price='Pencils',5
product8_name,product8_price='Diaries',200 
product9_name,product9_price='Compassbox', 500
product10_name,product10_price='Colourbox',300 

Shop_name = 'STATIONARY_MALL'
Shop_address = 'Tilak chowk,Solapur'
Shop_branch = 'Branch:Solapur,Pune'

message = 'THANK YOU!! VISIT AGAIN!! \U0001f607'

print('-' *50)

print('\t\t{}'.format(Shop_name.title()))
print('\t\t{}'.format(Shop_address.title()))
print('\t\t{}'.format(Shop_branch.title()))

print('*' * 41)

print('|\tProduct Name\tProduct Price   |')

print('|\t{}\t\trs{}    |'.format(product1_name.title(), product1_price))
print('|\t{}\t\trs{}    |'.format(product2_name.title(), product2_price))
print('|\t{}\t\trs{}   |'.format(product3_name.title(), product3_price))
print('|\t{}\t\t\trs{}    |'.format(product4_name.title(), product4_price))
print('|\t{}\t\trs{}    |'.format(product5_name.title(), product5_price))
print('|\t{}\t\t\trs{}    |'.format(product6_name.title(), product6_price))
print('|\t{}\t\t\trs{}     |'.format(product7_name.title(), product7_price))
print('|\t{}\t\t\trs{}   |'.format(product8_name.title(), product8_price))
print('|\t{}\t\trs{}   |'.format(product9_name.title(), product9_price))
print('|\t{}\t\trs{}   |'.format(product10_name.title(),product10_price))
print('*' * 41)

print('\t\tTotal  ')

total = product1_price + product2_price + product3_price+product4_price+product5_price+product6_price+product6_price+product7_price+product8_price+product9_price+product10_price
print('\t\trs{}'.format(total))

print('-' * 50)
print('-' * 50)


print('\n\t{}\n'.format(message))

print('-' * 50)
print('-' * 50)