import db
import json
import traceback
import logging

logger = logging.getLogger(__name__)

def get_expenses(db_params, limit=15):
    """Returns expenses in JSON format."""
    tablename = 'expenses'
    query = 'SELECT * FROM {} ORDER BY date DESC, id DESC LIMIT {};'.format(tablename, limit)

    try:
        expenses = db.query(query, '', db_params["host"], db_params["dbname"], db_params["user"], db_params["password"])
        return json.dumps(expenses, default=db.date_converter)
    except:
        logger.error("Cannot retrieve expenses from DB: {}".format(
            traceback.format_exc()))
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
