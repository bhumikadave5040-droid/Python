from payment_gateway import payment_gateway
from upi import upi
from card import card
pg=payment_gateway()

ip=int(input("payment:1.upi2.card3.exit\nenter your choice:"))

if ip==1:
    pg.payment_process(upi())
   
elif ip==2:
     pg.payment_process(card())
   
else:
    print("exit")