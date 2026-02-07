# Parent class
class Payment:
    def pay(self):
        print("Payment method selected")


# Child class GooglePay
class GooglePay(Payment):
    def pay(self):
        print("Payment made using Google Pay")


# Child class PhonePe
class PhonePe(Payment):
    def pay(self):
        print("Payment made using PhonePe")


# Child class CreditCard
class CreditCard(Payment):
    def pay(self):
        print("Payment made using Credit Card")


# Creating objects
payment = Payment()
gpay = GooglePay()
phonepe = PhonePe()
credit_card = CreditCard()

# Calling pay() method
payment.pay()
gpay.pay()
phonepe.pay()
credit_card.pay()
