import psycopg2
import psycopg2.extras
import logging
import datetime

# from aws_xray_sdk.core import xray_recorder

logger = logging.getLogger(__name__)

def date_converter(o):
    """Converts date to string for JSON serialization."""
    if isinstance(o, datetime.date):
        return o.__str__()

def connect(host, dbname, user, password="", port=5432):
    """Returns DB connection."""
    conn_str = "host='{0}' dbname='{1}' user='{2}' password='{3}' port={4}".format(
        host, dbname, user, password, port)
    logger.info("Connecting to DB, host='{0}' dbname='{1}' user='{2}'".format(host, dbname, user))
    # subsegment = xray_recorder.begin_subsegment('connect_to_DB')
    # subsegment.put_annotation('host', host)
    conn = psycopg2.connect(conn_str)
    conn.autocommit = True
    # xray_recorder.end_subsegment()
    return conn

def query(query, params, host, dbname, user, password=""):
    """Makes query to DB."""
    results=""
    conn = connect(host, dbname, user, password)

    # Adding trace subsegment to X-Ray
    # subsegment = xray_recorder.begin_subsegment('query_DB')
    # subsegment.put_annotation('query', format(query))
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    logger.info("Executing query {}".format(query))

    cursor.execute(query, params)
    if(query[0]=='S'):
        results = cursor.fetchall()
        cursor.close()

    # xray_recorder.end_subsegment()

    return(results)
