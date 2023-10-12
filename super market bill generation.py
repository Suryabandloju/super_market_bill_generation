from datetime import datetime
print(25*"-",'welcome to surya mart',25*"-")
Name=str(input('enter your name :'))
print('Available items in our mart')
list='''
salt       Rs 30/kg
cinthol    Rs 40/each
close up   Rs 150/each
coke       Rs 50/each
rice       Rs 50/kg
sugar      RS 45/kg
maggi      Rs 35 '''
print(list)

#items and prices
items={'salt':30,
       'cinthol':40,
       'close up':150,
       'coke':50,
       'rice':50,
       'sugar':45,
       'maggi':35}

#declaration
price=0
finalprice=0
l=[]
pl=[]
q=[]


#calculations
while True:
        item=input('enter item name (or done to exit):')
        if item=='done':
               break        
        quantity=int(input('enter quantity:'))
        price=items[item]*quantity
        l.append(item)
        pl.append(price)
        q.append(quantity)
        gst=(price*2)/100
        finalprice=gst+price 

#bill generation
print(25*"-","surya mart",25*"-") 
print(25*"-","hyderabad",25*"-") 
print("Name:",Name,30*" ","Date:", datetime.now()) 
print(75*"-")
print("sno",8*"",'item',10*"", 'quantity',10*"","price") 
for i in range (len(pl)):
        print(i,20*'',l[i],30*'',q[i],40*'',pl[i])
print(75*"-")
print(50*"*",'price:',4*" ",'Rs',price)
print(50*"*",'gst:',6*" ",'Rs',gst)
print(75*"-")
print(50*"*",'finalprice:','Rs',finalprice)
print(25*"-",'Thank you!',25*"-")


    


















