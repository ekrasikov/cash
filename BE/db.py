import psycopg2
import psycopg2.extras
import logging
import datetime

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
    conn = psycopg2.connect(conn_str)
    conn.autocommit = True
    return conn

def query(query, params, host, dbname, user, password=""):
    """Makes query to DB."""
    results=""
    conn = connect(host, dbname, user, password)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    logger.info("Executing query {}".format(query))
    cursor.execute(query, params)

    if(query[0]=='S'):
        results = cursor.fetchall()
        cursor.close()

    return(results)
