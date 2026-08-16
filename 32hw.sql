DROP TABLE IF EXISTS cars;

CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    brand VARCHAR(30) NOT NULL,
    model VARCHAR(30) NOT NULL,
    year INT NOT NULL,
    vin VARCHAR(17) UNIQUE,
    created_at DATE DEFAULT current_date,
    engine_capacity DECIMAL(3, 1) CHECK (engine_capacity > 0.5),
    mileage INT DEFAULT 0,
    customs BOOLEAN DEFAULT false,
    price DECIMAL(10, 2),
    description TEXT,
    sold BOOLEAN DEFAULT false
);

INSERT INTO cars (brand, model, year, vin, engine_capacity, mileage, customs, price, description, sold)
VALUES
    ('Toyota', 'Camry', 2020, 'JTNB11HK0L1234567', 2.5, 15000, false, 25000.00, 'A reliable sedan with great fuel efficiency.', false),
    ('Honda', 'Civic', 2019, '2HGFC2F59KH123456', 2.0, 20000, false, 22000.00, 'Compact car with sporty handling and good resale value.', true),
    ('Ford', 'F-150', 2021, '1FTFW1E50MFA12345', 3.5, 10000, true, 35000.00, 'A powerful pickup truck with excellent towing capacity.', false),
    ('BMW', 'M3', 2022, 'WBS8M9C05N1234567', 3.0, 5000, false, 70000.00, 'A high-performance sports car with exceptional handling.', true),
    ('BMW', 'X5', 2022, '5UXCR6C0XL1234567', 3.0, 5000, true, 60000.00, 'Luxury SUV with advanced technology and performance.', false),
    ('Audi', 'A4', 2020, 'WAUENAF48LN123456', 2.0, 12000, false, 40000.00, 'A stylish sedan with a premium interior and smooth ride.', true),
    ('Mercedes-Benz', 'C-Class', 2021, 'W1KZF8EB3MA123456', 2.0, 8000, true, 45000.00, 'A luxury sedan with cutting-edge technology and comfort.', false),
    ('BMW', '3 Series', 2019, 'WBA5R1C05KA123456', 2.0, 15000, false, 35000.00, 'A sporty sedan with excellent handling and performance.', true),
    ('Nissan', 'Altima', 2019, '1N4AL3AP6KC123456', 2.5, 25000, false, 21000.00, 'A midsize sedan with a comfortable interior and good fuel economy.', false),
    ('Volkswagen', 'Passat', 2020, '1VWAA7A36LC123456', 2.0, 18000, true, 23000.00, 'A spacious sedan with a refined ride and advanced safety features.', true);

SELECT * FROM cars;
SELECT brand, model, year, price FROM cars;
SELECT * FROM cars WHERE brand = 'BMW';