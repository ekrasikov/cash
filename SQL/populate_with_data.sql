INSERT INTO users (id, name) VALUES (1, 'Masha');
INSERT INTO users (id, name) VALUES (2, 'Eugene');

INSERT INTO categories (id, name) VALUES (1, 'Supermarket');
INSERT INTO categories (id, name) VALUES (2, 'Lunch');
INSERT INTO categories (id, name) VALUES (3, 'Transport');
INSERT INTO categories (id, name) VALUES (4, 'Household');
INSERT INTO categories (id, name) VALUES (5, 'Restaraunts');
INSERT INTO categories (id, name) VALUES (6, 'Entertainment');
INSERT INTO categories (id, name) VALUES (7, 'Beauty');
INSERT INTO categories (id, name) VALUES (8, 'Apps and communnications');
INSERT INTO categories (id, name) VALUES (9, 'Clothes');
INSERT INTO categories (id, name) VALUES (10, 'Bike');
INSERT INTO categories (id, name) VALUES (11, 'Travel');
INSERT INTO categories (id, name) VALUES (12, 'Car');
INSERT INTO categories (id, name) VALUES (13, 'Therapist');
INSERT INTO categories (id, name) VALUES (14, 'Parents');
INSERT INTO categories (id, name) VALUES (15, 'Apartment rental');
INSERT INTO categories (id, name) VALUES (16, 'Medicine');
INSERT INTO categories (id, name) VALUES (17, 'Courses');
INSERT INTO categories (id, name) VALUES (50, 'Other');

INSERT INTO expenses (date, user_id, category_id, amount, comment) VALUES (
	'2018-10-24', 1, 1, 2.5, 'Milch und Breze'
);
INSERT INTO expenses (date, user_id, category_id, amount, comment) VALUES (
	'2018-10-25', 1, 1, 42.5, 'Obst und Gemüse'
);
INSERT INTO expenses (date, user_id, category_id, amount) VALUES (
	'2018-10-25', 2, 3, 12
);
INSERT INTO expenses (date, user_id, category_id, amount, comment) VALUES (
	'2018-10-25', 1, 5, 3.5, 'Coffee'
);
INSERT INTO expenses (date, user_id, category_id, amount, comment) VALUES (
	'2018-10-26', 2, 2, 12.5, 'Streifenkarte'
);
INSERT INTO expenses (date, user_id, category_id, amount) VALUES (
	'2018-10-26', 1, 6, 4
);
INSERT INTO expenses (date, user_id, category_id, amount, comment) VALUES (
	'2018-10-26', 2, 50, 6, 'Stuff in airport'
);