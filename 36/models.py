from sqlalchemy import create_engine, String, Integer, Date, Float, ForeignKey, CheckConstraint
from datetime import date
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship

engine = create_engine("postgresql+psycopg2://postgres:REVE4TSM@localhost:5432/test", echo=True)



class Base(DeclarativeBase):
    pass

class Hotel(Base):
    __tablename__ = "Hotels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    stars: Mapped[float] = mapped_column(Float, CheckConstraint('stars BETWEEN 1 AND 5'),nullable=False)

    rooms = relationship("Room", back_populates="hotel")

    def __repr__(self):
        return f"Hotel(id={self.id}, name='{self.name}', country='{self.country}', city='{self.city}', stars={self.stars})"

class Room(Base):
    __tablename__ = "Rooms"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    room_number: Mapped[int] = mapped_column(Integer, nullable=False) 
    floor: Mapped[int] = mapped_column(Integer, CheckConstraint('floor BETWEEN 1 AND 100'), nullable = False)
    price_per_night: Mapped[int] = mapped_column(Integer, nullable=False)
    hotel_id: Mapped[int] = mapped_column(Integer, ForeignKey("Hotels.id"), nullable=False)

    hotel = relationship("Hotel", back_populates="rooms")
    bookings = relationship("Booking", back_populates="room")

    def __repr__(self):
        return f"Room(id={self.id}, number='{self.room_number}')"

class Guest(Base):
    __tablename__ = "Guests"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    bookings = relationship("Booking", back_populates="guest")

    def __repr__(self):
        return f"Guest(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}', phone='{self.phone}')"

class Booking(Base):
    __tablename__ = "Bookings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    guest_id: Mapped[int] = mapped_column(Integer, ForeignKey("Guests.id"), nullable=False)
    room_id: Mapped[int] = mapped_column(Integer, ForeignKey("Rooms.id"), nullable=False)
    check_in: Mapped[date] = mapped_column(Date, nullable=False, default=date.today())
    check_out: Mapped[date] = mapped_column(Date, nullable=False, default=date.today())

    room = relationship("Room", back_populates="bookings")
    guest = relationship("Guest", back_populates="bookings")

    def __repr__(self):
        return f"Booking(id={self.id}, guest_id={self.guest_id}, room_id={self.room_id}, check_in='{self.check_in}', check_out='{self.check_out}')"

Base.metadata.create_all(engine)