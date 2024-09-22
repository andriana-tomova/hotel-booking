import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})

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


hotel_ID = input("Input id of the hotel:")
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name:")
    reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free")



# if __name__ = "__main__":

