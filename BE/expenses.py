import db
import json
import traceback
import logging

logger = logging.getLogger(__name__)

def get_expenses(limit=50):
    """Returns expenses in JSON format."""
    tablename = 'expenses'
    query = 'SELECT * FROM {} LIMIT {};'.format(tablename, limit)
    host = '127.0.0.1'
    dbname = 'expensedb'
    user = 'expenserole'


    try:
        expenses = db.query(query, '', host, dbname, user)
        return json.dumps(expenses, default=db.date_converter)
    except:
        logger.error("Cannot retrieve expenses from DB: {}".format(
            traceback.format_exc()))
        return json.dumps("")

def add_expense(expense):
    """Adds expense to database."""
    tablename = 'expenses'
    query = "INSERT INTO {} (date, user_id, category_id, amount, comment) \
            VALUES (%(date)s, %(user_id)s, %(category_id)s, %(amount)s, %(comment)s)".format(tablename)
    host = '127.0.0.1'
    dbname = 'expensedb'
    user = 'expenserole'
    try:
        db.query(query, expense, host, dbname, user)
    except:
        logger.error("Cannot save expense to DB: {}".format(
            traceback.format_exc()))
