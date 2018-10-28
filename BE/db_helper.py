import psycopg2
import psycopg2.extras
import logging
import json
import datetime
import traceback

class DBHelper():
    """Helper Class to save expenses in persistent DB"""

    def __init__(self, host, user, dbname, logger, password="", port=5432):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port

        self.__logger = logger

        self.__conn_str = "host='{0}' dbname='{1}' user='{2}' password='{3}' port={4}".format(
            host, dbname, user, password, port)

    def __date_converter(self, o):
        if isinstance(o, datetime.date):
            print("I'm date converter, {}".format(o.__str__()))
            return o.__str__()

    def __make_connection(self):

        self.__logger.info("Connecting to DB, connstr is {}".format(self.__conn_str))
        try:
            conn = psycopg2.connect(self.__conn_str)
        except:
            print("Cannot create a DB connection")
            return self.__logger.error("Cannot create a DB connection.\n{}".format(
                traceback.format_exc()))

        conn.autocommit = True
        return conn

    def __query(self, query):
        print("I'm query")
        try:
            self.cnx = self.__make_connection()
            cursor = self.cnx.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            #cursor = self.cnx.cursor()

            self.__logger.info("Executing query {}".format(query))
            try:
                cursor.execute(query)
            except:
                return self.__logger.error("Cannot execute cursor.\n{}".format(
                    traceback.format_exc()))

            try:
                #result_dict = [dict((cursor.description[i][0], value) \
                #                    for i, value in enumerate(row)) for row in cursor.fetchall()]

                result_dict = cursor.fetchall()

                print(result_dict)

                self.__logger.info("Query results list: {}".format(result_dict))
                cursor.close()

            except:
                return self.__logger.error("ERROR: Cannot retrieve query data.\n{}".format(
                    traceback.format_exc()))

            return(result_dict)


        except:
            return self.__logger.error("Cannot connect to database.\n{}".format(
                traceback.format_exc()))


        finally:
            try:
                self.cnx.close()
            except:
                pass

    # def add_expense(self, expense):
    #     query = 'INSERT INTO expenses(id, date, user_id, category_id, )'
    #     try:
    #
    #         return response
    #     except:
    #         return None

    def get_expenses(self, limit=50):
        query = 'SELECT * FROM expenses LIMIT {};'.format(limit)
        try:
            expenses = self.__query(query)
            print("And here is a result: \n{}".format(expenses))
            return json.dumps(expenses, default=self.__date_converter)
        except:
            self.__logger.error("Cannot retrieve expenses from DB: {}".format(
                    traceback.format_exc()))
            return json.dumps('')

