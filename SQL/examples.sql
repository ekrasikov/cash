select * from expenses where amount > 10 ORDER BY amount DESC;

SELECT expenses.date, users.name, categories.name, amount, comment FROM expenses, categories, users WHERE category_id = categories.id AND user_id = users.id ORDER BY date;

select * from expenses WHERE amount = (select MAX(amount) from expenses);

SELECT users.name, max(amount) FROM expenses, users WHERE user_id = users.id GROUP BY users.name;

SELECT categories.name, sum(amount) FROM expenses, categories WHERE category_id = categories.id GROUP BY categories.name ORDER BY sum(amount) DESC;
