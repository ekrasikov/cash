import logging
import sys
import expenses

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

json_expenses = expenses.get_expenses()

print("Got expenses: {}".format(json_expenses))

test_expense = {
    "date": "2018-10-28",
    "user_id": 1,
    "category_id": 9,
    "amount": 45,
    "comment": "Hose"
}

#expenses.add_expense(test_expense)