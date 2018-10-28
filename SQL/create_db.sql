create table users (
	id INT PRIMARY KEY,
	name VARCHAR(80) UNIQUE NOT NULL 
);

create table categories (
	id INT PRIMARY KEY,
	name VARCHAR(80) UNIQUE NOT NULL
);

CREATE TABLE expenses (
	id INT PRIMARY KEY,
	date DATE NOT NULL,
	user_id INT REFERENCES users(id),
	category_id INT REFERENCES categories(id),
	amount REAL CHECK (amount > 0),
	comment VARCHAR(255)
);