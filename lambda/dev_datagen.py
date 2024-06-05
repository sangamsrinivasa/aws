#############################
Authror: Srinivas Sangam   ##
CreationDate: 05 June 2024 ##
- Creating DB Connection   ##
#############################


import logging
import os
import sys
import cx_Oracle
from collections import namedtuple


db_connect = cx_Oracle.connect(user="devschema", password=userpwd, dsn="oradb.dev.com/orclpdb")

db_cursor = db_connect.cursor()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

data_extract = '''
SELECT data1, data2, data3, data4, data5 from load_table1 lta
inner join base_table bta on lta.data1 = bta.data1
'''


def lambda_handler(event, context):

    db_connect = cx_Oracle.connect(user="devschema", password=userpwd, dsn="oradb.dev.com/orclpdb")
    db_cursor = db_connect.cursor()

    QUERY = '''
    SELECT data1, data2, data3, data4, data5 from load_table1 lta
    inner join base_table bta on lta.data1 = bta.data1
    '''

    try:
        db_cursor = db_connect.cursor()
        db_cusrot.execute(data_extract)
        resource_records = db_cursor.fetchall()
        db_cursor.close()

        # do something with the data
        for record in resource_records:
            print(record)

    except Exception as e:  # Catch all for easier error tracing in logs
        logger.error(e, exc_info=True)
        raise Exception('Error occurred during execution')  # notify aws of failure

    return {
        "statusCode": HTTPStatus.OK.value
    }
