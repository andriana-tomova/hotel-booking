import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_secured = pd.read_csv("card_security.csv", dtype=str)

class Hotel:

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""Thank you for your reservation"
                   Here are you booking data
                   name: {self.customer_name}
                   hotel name: {self.hotel.hotel_name}"""
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number
    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration, "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecuredCreditCard(CreditCard):
    def autenticate(self, given_password):
        password = df_cards_secured.loc[df_cards_secured["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


hotel_ID = input("Input id of the hotel:")
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = SecuredCreditCard(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.autenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name:")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
        else:
            print("Credit Card authentication failed!")
    else:
        print("There is a problem with your credit card!")
else:
    print("Hotel is not free")

