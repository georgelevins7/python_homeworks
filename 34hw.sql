DROP TABLE IF EXISTS guests;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS hotels;

CREATE TABLE hotels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    location VARCHAR(100) NOT NULL,
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5)
);

CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    room_number VARCHAR(10) NOT NULL,
    floor INT NOT NULL CHECK (floor >= 1 AND floor <= 100),
    price DECIMAL(10, 2) CHECK (price > 0),
    hotel_id INT NOT NULL REFERENCES hotels(id) ON DELETE CASCADE
);

CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) CHECK (price > 0),
    room_id INT NOT NULL REFERENCES rooms(id) ON DELETE CASCADE
);

CREATE TABLE guests (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    phone VARCHAR(15) UNIQUE,
    room_id INT NOT NULL REFERENCES rooms(id) ON DELETE CASCADE
);

INSERT INTO hotels (name, location, rating) VALUES
    ('Grand Plaza', 'New York', 5),
    ('Ocean View', 'Miami', 4),
    ('Mountain Retreat', 'Denver', 3);

INSERT INTO rooms (room_number, floor, price, hotel_id) VALUES
    ('101', 1, 150.00, 1),
    ('102', 1, 200.00, 1),
    ('311', 3, 300.00, 1),
    ('200', 2, 250.00, 2),
    ('212', 2, 300.00, 2),
    ('303', 3, 100.00, 2),
    ('204', 2, 250.00, 3),
    ('209', 2, 300.00, 3),
    ('306', 3, 100.00, 3);

INSERT INTO services (name, price, room_id) VALUES
    ('Room Cleaning', 20.00, 1),
    ('Breakfast', 15.00, 1),
    ('Spa Access', 50.00, 2),
    ('Gym Access', 10.00, 2),
    ('Room Cleaning', 20.00, 3),
    ('Breakfast', 15.00, 3),
    ('Spa Access', 50.00, 4),
    ('Gym Access', 10.00, 4),
    ('Room Cleaning', 20.00, 5),
    ('Breakfast', 15.00, 5),
    ('Spa Access', 50.00, 6),
    ('Gym Access', 10.00, 6),
    ('Room Cleaning', 20.00, 7),
    ('Breakfast', 15.00, 7),
    ('Spa Access', 50.00, 8),
    ('Gym Access', 10.00, 8),
    ('Room Cleaning', 20.00, 9),
    ('Breakfast', 15.00, 9);

INSERT INTO guests (first_name, last_name, phone, room_id) VALUES
    ('John', 'Doe', '123-456-7890', 1),
    ('Jane', 'Smith', '234-567-8901', 1),
    ('Mike', 'Johnson', '345-678-9012', 2),
    ('Emily', 'Davis', '456-789-0123', 2),
    ('David', 'Brown', '567-890-1234', 3),
    ('Sarah', 'Miller', '678-901-2345', 3),
    ('Chris', 'Wilson', '789-012-3456', 4),
    ('Jessica', 'Moore', '890-123-4567', 4),
    ('Daniel', 'Taylor', '901-234-5678', 5),
    ('Laura', 'Clark', '012-345-6789', 5),
    ('James', 'Lewis', '143-456-7890', 6),
    ('Olivia', 'Walker', '034-567-8901', 6),
    ('Matthew', 'Hall', '344-678-9012', 7),
    ('Sophia', 'Allen', '454-789-0123', 7),
    ('Andrew', 'Young', '547-890-1234', 8),
    ('Isabella', 'Hernandez', '648-901-2345', 8),
    ('Joshua', 'King', '789-012-3356', 9),
    ('Mia', 'Wright', '890-123-4547', 9);

-- ყველა ნომერს შესაბამისი სასტუმროს სახელთან ერთად
SELECT rooms.room_number, hotels.name FROM rooms, hotels WHERE rooms.hotel_id = hotels.id;

-- ყველა სტუმარს მისი ნომრის ნომრითა და სასტუმროს სახელით
SELECT guests.first_name, guests.last_name, rooms.room_number, hotels.name
FROM guests, rooms, hotels
WHERE rooms.hotel_id = hotels.id AND guests.room_id = rooms.id;

-- კონკრეტული სასტუმროს ყველა სტუმარს
SELECT guests.first_name, guests.last_name, hotels.name
FROM guests, rooms, hotels
WHERE rooms.hotel_id = hotels.id AND guests.room_id = rooms.id AND hotels.name = 'Grand Plaza';

-- თითო სასტუმროში არსებული ნომრების რაოდენობას
SELECT hotels.name, COUNT(*) FROM rooms, hotels
WHERE rooms.hotel_id = hotels.id
GROUP BY hotels.name;

-- იმ ნომრებს, რომელთათვისაც სერვისი ჯერ არ არის შეკვეთილი
SELECT room_number FROM rooms
LEFT OUTER JOIN services ON services.room_id = rooms.id
WHERE services.room_id IS NULL;

-- წაშალეთ ერთი ნომერი და დააკვირდით, როგორ აისახება ეს მასთან დაკავშირებულ სტუმრებსა და სერვისებზე;
DELETE FROM rooms WHERE id = 1;
SELECT * FROM guests;
SELECT * FROM services;

-- შეცვალეთ კონკრეტული ნომრის ღირებულება
UPDATE rooms SET price = 500 WHERE rooms.id = 5;
SELECT * FROM rooms;

-- ერთი სტუმარი გადააწერეთ სხვა ნომერზე
UPDATE guests SET room_id = 4 WHERE guests.id = 18;
SELECT * FROM guests;