import db
import json
import traceback
import logging

logger = logging.getLogger(__name__)

def get_data(tablename, db_params, limit=20):
    """Returns expenses/categories/users in JSON format."""
    if tablename == "expenses":
        query = 'SELECT expenses.id, expenses.date, users.name AS user, categories.name AS category, amount, comment \
                FROM expenses, categories, users WHERE category_id = categories.id AND user_id = users.id \
                ORDER BY date DESC, expenses.id DESC LIMIT {};'.format(limit)
    else:
        query = 'SELECT * FROM {} ORDER BY id;'.format(tablename)

    try:
        result = db.query(query, '', db_params["host"], db_params["dbname"], db_params["user"], db_params["password"])
        return json.dumps(result, default=db.date_converter)
    except:
        logger.error("Cannot retrieve {} from DB: {}".format(tablename, traceback.format_exc()))
        return False

def add_expense(expense, db_params):
    """Adds expense to database."""
    tablename = 'expenses'
    query = "INSERT INTO {} (date, user_id, category_id, amount, comment) \
            VALUES (%(date)s, %(user_id)s, %(category_id)s, %(amount)s, %(comment)s)".format(tablename)
    try:
        db.query(query, expense, db_params["host"], db_params["dbname"], db_params["user"], db_params["password"])
    except:
        logger.error("Cannot add expense to DB: {}".format(
            traceback.format_exc()))
        return False
    else:
        return True


def delete_expense(expense_id, db_params):
    """Deletes expense from database."""
    tablename = 'expenses'
    query = "DELETE FROM {} WHERE id={}".format(tablename, expense_id)
    try:
        db.query(query, '', db_params["host"], db_params["dbname"], db_params["user"], db_params["password"])
    except:
        logger.error("Cannot delete expense from DB: {}".format(
            traceback.format_exc()))
        return False
    else:
        return True
