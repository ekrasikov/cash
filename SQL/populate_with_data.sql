INSERT INTO users (id, name) VALUES (1, 'Masha');
INSERT INTO users (id, name) VALUES (2, 'Eugene');

INSERT INTO categories (id, name) VALUES (1, 'Supermarket');
INSERT INTO categories (id, name) VALUES (2, 'Transport');
INSERT INTO categories (id, name) VALUES (3, 'Lunch');
INSERT INTO categories (id, name) VALUES (4, 'Beauty');
INSERT INTO categories (id, name) VALUES (5, 'Bike');
INSERT INTO categories (id, name) VALUES (6, 'Restaraunts');
INSERT INTO categories (id, name) VALUES (7, 'Household');
INSERT INTO categories (id, name) VALUES (8, 'Apartment rental');
INSERT INTO categories (id, name) VALUES (9, 'Clothes');
INSERT INTO categories (id, name) VALUES (10, 'Telco');
INSERT INTO categories (id, name) VALUES (50, 'Other');

INSERT INTO expenses (id, date, user_id, category_id, amount, comment) VALUES (
	0, '2018-10-24', 1, 1, 2.5, 'Milch und Breze'
);
INSERT INTO expenses (id, date, user_id, category_id, amount, comment) VALUES (
	1, '2018-10-25', 1, 1, 42.5, 'Obst und Gemüse'
);
INSERT INTO expenses (id, date, user_id, category_id, amount) VALUES (
	2, '2018-10-25', 2, 3, 12
);
INSERT INTO expenses (id, date, user_id, category_id, amount, comment) VALUES (
	3, '2018-10-25', 1, 5, 3.5, 'Coffee'
);
INSERT INTO expenses (id, date, user_id, category_id, amount, comment) VALUES (
	4, '2018-10-26', 2, 2, 12.5, 'Streifenkarte'
);
INSERT INTO expenses (id, date, user_id, category_id, amount) VALUES (
	5, '2018-10-26', 1, 6, 4
);
INSERT INTO expenses (id, date, user_id, category_id, amount, comment) VALUES (
	6, '2018-10-26', 2, 50, 6, 'Stuff in airport'
);