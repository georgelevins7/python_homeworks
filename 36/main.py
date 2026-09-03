from models import Hotel, Room, Guest, Booking, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, func
from datetime import date

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

hotels = [
    Hotel(name="Hotel Parket", country="Georgia", city="Tbilisi", stars=5),
    Hotel(name="Hotel Vintage", country="Georgia", city="Tbilisi", stars=4),
    Hotel(name="Hotel Vinile", country="Georgia", city="Batumi", stars=3)
]

rooms = [
    Room(room_number=101, floor=1, price_per_night=90, hotel_id=1),
    Room(room_number=102, floor=1, price_per_night=120, hotel_id=1),
    Room(room_number=103, floor=1, price_per_night=130, hotel_id=1),
    Room(room_number=201, floor=2, price_per_night=150, hotel_id=2),
    Room(room_number=202, floor=2, price_per_night=180, hotel_id=2),
    Room(room_number=203, floor=2, price_per_night=190, hotel_id=2),
    Room(room_number=301, floor=3, price_per_night=200, hotel_id=3),
    Room(room_number=302, floor=3, price_per_night=230, hotel_id=3),
    Room(room_number=303, floor=3, price_per_night=220, hotel_id=3)
]

guests = [
    Guest(first_name="John", last_name="Doe", email="john.doe@example.com", phone="1234567890"),
    Guest(first_name="Jane", last_name="Smith", email="jane.smith@example.com", phone="0987654321"),
    Guest(first_name="Alice", last_name="Johnson", email="alice.johnson@example.com", phone="1122334455"),
    Guest(first_name="Bob", last_name="Brown", email="bob.brown@example.com", phone="6677889900"),
    Guest(first_name="Charlie", last_name="Davis", email="charlie.davis@example.com", phone="4455667788"),
    Guest(first_name="David", last_name="Evans", email="david.evans@example.com", phone="2233445566"),
    Guest(first_name="Eve", last_name="Foster", email="eve.foster@example.com", phone="3344556677")
]

bookings = [
    Booking(guest_id=1, room_id=1, check_in=date(2026, 9, 1), check_out=date(2026, 9, 5)),
    Booking(guest_id=2, room_id=2, check_in=date(2026, 9, 2), check_out=date(2026, 9, 6)),
    Booking(guest_id=3, room_id=3, check_in=date(2026, 9, 3), check_out=date(2026, 9, 7)),
    Booking(guest_id=4, room_id=4, check_in=date(2026, 9, 4), check_out=date(2026, 9, 8)),
    Booking(guest_id=5, room_id=5, check_in=date(2026, 9, 5), check_out=date(2026, 9, 9)),
    Booking(guest_id=6, room_id=6, check_in=date(2026, 9, 6), check_out=date(2026, 9, 10)),
    Booking(guest_id=7, room_id=2, check_in=date(2026, 9, 2), check_out=date(2026, 9, 6)),
    Booking(guest_id=1, room_id=3, check_in=date(2026, 9, 1), check_out=date(2026, 9, 5))
]

#------------- მონაცემების დამატება -------------

session.add_all(hotels)
session.commit()

session.add_all(rooms)
session.commit()

session.add_all(guests)
session.commit()

session.add_all(bookings)
session.commit()


#------------- Create -------------

def create_hotel(session, hotel):
    session.add(hotel)
    session.commit()

def create_room(session, room):
    session.add(room)
    session.commit()

def create_guest(session, guest):
    session.add(guest)
    session.commit()

def create_booking(session, booking):
    session.add(booking)
    session.commit()

#------------- Read -------------
def get_all_hotels(session):
    return session.execute(select(Hotel)).scalars().all()

def get_hotel(session, hotel_id):
    return session.get(Hotel, hotel_id)

def get_all_rooms(session):
    return session.execute(select(Room)).scalars().all()

def get_guest_by_email(session, email):
    return session.execute(select(Guest).where(Guest.email == email)).scalars().first()


#------------- Update -------------

def room_price_change(session, room_id, new_price):
    room = session.get(Room, room_id)
    if room:
        room.price_per_night = new_price
        session.commit()
    else:
        print(f"Room with ID {room_id} not found.")

#------------- Delete -------------

def guest_delete(session, guest_id):
    guest = session.get(Guest, guest_id)
    if guest:
        session.delete(guest)
        session.commit()
    else:
        print(f"Guest with ID {guest_id} not found.")

def room_delete(session, room_id):
    room = session.get(Room, room_id)
    if room:
        session.delete(room)
        session.commit()
    else:
        print(f"Room with ID {room_id} not found.")


#------------- Query-ები -------------

# ყველა 5-ვარსკვლავიანი სასტუმრო

five_stars = session.execute(select(Hotel).where(Hotel.stars == 5)).scalars().all()

# ყველა სასტუმრო, რომელიც მდებარეობს თბილისში

tbilisi_hotels = session.execute(select(Hotel).where(Hotel.city == "Tbilisi")).scalars().all()
    

# ყველა ოთახი, რომლის ფასი ერთ ღამეში 100-ზე ნაკლებია

cheap_rooms = session.execute(select(Room).where(Room.price_per_night < 100)).scalars().all()

# ყველა ოთახი კონკრეტულ სასტუმროში

hotel = session.get(Hotel, 1)
rooms_in_hotel = hotel.rooms


# კონკრეტული სტუმრის ყველა Booking

guest_id = 1
bookings_of_guest = session.execute(select(Booking).where(Booking.guest_id == guest_id)).scalars().all()

# ყველა Booking, რომლის `check_out` თარიღიც მომავალშია

upcoming_bookings = session.execute(select(Booking).where(Booking.check_out > date.today())).scalars().all()

# ყველაზე ძვირი ოთახი

most_expensive_room = session.execute(select(Room).order_by(Room.price_per_night.desc())).scalars().first()

# თითოეულ სასტუმროში ოთახების რაოდენობა

rooms_count_per_hotel = session.execute(select(Hotel.name, func.count(Room.id)).join(Room).group_by(Hotel.id)).all()

# ყველა სასტუმრო, რომელსაც აქვს მინიმუმ 3 ოთახი.
hotels_with_min_3_rooms = session.execute(select(Hotel.name, func.count(Room.id)).join(Room).group_by(Hotel.id).having(func.count(Room.id) >= 3)).all()

# სტუმრები, რომლებსაც ერთზე მეტი Booking აქვთ

guests_with_multiple_bookings = session.execute(
    select(Guest.first_name, Guest.last_name, func.count(Booking.id)).
    join(Booking).
    group_by(Guest.id).
    having(func.count(Booking.id) > 1)).all()

session.close()