# Duck Typing
# """If it walks like a duck and quacks like a duck, then it must be a duck."""

class Dog:
    def speak(self):
        return "Woof! Woof!"

class Cat:
    def speak(self):
        return "Meow! Meow!"

class Duck:
    def speak(self):
        return "Quack! Quack!"

def animal_speak(animal):
    print(animal.speak())

# Creating instances of the classes
dog = Dog()
cat = Cat()
duck = Duck()

# Passing different objects to the same function
animal_speak(dog)
animal_speak(cat)
animal_speak(duck)

#2
class Item:
    def fly(self,item):
        print(f"{item} flies in the sky")
    
    def lives(self,item,type):
        print(f"{item} lives in {type}")

aeroplane = Item()
aeroplane.fly("Aeroplane")
aeroplane.lives("Aeroplane","Sky")

fish = Item()
fish.fly("Fish")
fish.lives("Fish","Water")

man = Item()
man.fly("Man")
man.lives("Man","Land")

#3
class CreditCard:
    def pay(self,amount):
        print(f"Amount {amount} is paid using Credit Card")

class DebitCard:
    def pay(self,amount):
        print(f"Amount {amount} is paid using Debit Card")

class UPI:
    def pay(self,amount):
        print(f"Amount {amount} is paid using UPI")

def payment(card,amount):
    card.pay(amount)

credit_card = CreditCard()
debit_card = DebitCard()
upi = UPI()

payment(credit_card,100)
payment(debit_card,200)
payment(upi,300)

#4
class Email:
    def sendMessage(self):
        print("Message is sent using Email")

class SMS:
    def sendMessage(self):
        print("Message is sent using SMS")

class WhatsApp:
    def sendMessage(self):
        print("Message is sent using WhatsApp")

def send_message(medium):
    medium.sendMessage()

email = Email()
sms = SMS()
whatsapp = WhatsApp()

send_message(email)
send_message(sms)
send_message(whatsapp)