import psycopg2
import psycopg2.extras
import logging
import datetime
import traceback

logger = logging.getLogger(__name__)

def date_converter(o):
    """Converts date to string for JSON serialization."""
    if isinstance(o, datetime.date):
        return o.__str__()

def connect(host, dbname, user, password="", port=5432):
    """Returns DB connection."""
    conn_str = "host='{0}' dbname='{1}' user='{2}' password='{3}' port={4}".format(
        host, dbname, user, password, port)
    logger.info("Connecting to DB, connstr is {}".format(conn_str))
    try:
        conn = psycopg2.connect(conn_str)
    except:
        return logger.error("Cannot create a DB connection.\n{}".format(
            traceback.format_exc()))
    conn.autocommit = True
    return conn

def query(query, params, host, dbname, user, password=""):
    """Makes query to DB."""
    results=""
    try:
        conn = connect(host, dbname, user, password)
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        logger.info("Executing query {}".format(query))
        try:
            cursor.execute(query, params)
        except:
            return logger.error("Cannot execute cursor.\n{}".format(
                traceback.format_exc()))

        if(query[0]=='S'):
            try:
                results = cursor.fetchall()
                cursor.close()
            except:
                return logger.error("ERROR: Cannot retrieve query data.\n{}".format(
                    traceback.format_exc()))

        return(results)


    except:
        return logger.error("Cannot connect to database.\n{}".format(
            traceback.format_exc()))

    finally:
        try:
            conn.close()
        except:
            pass