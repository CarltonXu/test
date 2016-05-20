#!/usr/bin/python
import sys
def out():
	print 'You are a poor man, get out!!!'
	sys.exit()
products = []
prices = []
shop_cart = []
sale = float(raw_input('Please input your salary:'))
#print type(sale)
if sale == 0:
	out()
else:
	list = open('/root/shopping.txt','r')
	see = list.read()
	print "################"
	print "Items     cost"
	print see
	print "################"
	#while True:
	list = open('/root/shopping.txt','r')
	for line in list.readlines():
		jisuan = line.split()
		products.append(jisuan[0])
		prices.append(int(jisuan[1]))
	#print products
	#print prices
	#print can
	while True:
		buy_items = raw_input('Please input what you want to buy:')
		if buy_items == '':
			print "Sorry,The products not is null!!!"
			continue
		else:
			chioce = buy_items.strip()
			if chioce in products:
				print '\033[34mOK,Your buy items in ours items\033[0m'
				f_index = products.index(chioce)
#				print f_index
				f_price = prices[f_index]
#				print f_price,type(f_price)
				print '\033[34mThe %s prices is %s\033[0m'% (chioce,f_price)
				if sale >= f_price:
					print "\033[34mYou can buy this product!!!\033[0m"
					while True:
						shifou = raw_input('Please tell me whether you buy(Y/N):')
						if shifou == 'Y':
							sale = sale-f_price
							f_products = products[f_index]
							shop_cart.append(f_products)
#							print f_products
							print "Your %s goods have to buy success in your warehouse!!!"% buy_items
							print "You the rest of the money is %d" %sale
							break
#							while True:
#								see = input('If you want your warehouse,please input(Y/N):')
#								see1 = see.strip()
#								if see1 == 'Y':
#									print shop_cart
#									break
#							break
#								elif see1 == 'N':
#									break
#								else:
#									print "Please input aggin!!!"
#									continue
						elif shifou == 'N':
							break
						else:
							print "Please input again"
							continue
				else:
					if sale < min(prices):
						print "\033[31mYou can's buy anything,please Please come again next time bring more money!!!\033[0m"
					#	print "\033[22mYour warehouse is :",shop_cart
						shop_cart.reverse()
						print "Bye!!!"
						sys.exit()
					else:
							print "Your money can't afford to buy the %s, please have a look at other commodities!!!" % buy_items
			else:
					print '\033[36mSorry,The %s not in ours items,Plesase input anothers items\033[0m' % buy_items
