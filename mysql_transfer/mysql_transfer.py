import subprocess

class MySQLTransferException(Exception):
    pass

def transfer_db(from_params, to_params, tables=[]):
    """
    Transfer database along with a list of tables.

    ARGUMENTS:

    from_params - Database to transfer *from*. This should be an
        instance of MySQLParams (or similar).
    to_params - Database to transfer *to*. This should be an
        instance of MySQLParams (or similar).
    tables - List of tables. Leave empty to transfer all tables.
    """

    try:
        p = subprocess.Popen(
            'mysqldump {from_args} | mysql {to_args}'.format(
                from_args=from_params.get_dump_args(tables),
                to_args=to_params.get_mysql_args()),
            shell=True)
    except AttributeError:
        raise MySQLTransferException('Invalid MySQLParams object passed '
                                     'to transfer_db.')

    r = p.communicate()
    if r[1]:
        raise MySQLTransferException(
            "MySQL transfer error: {}".format(r[1]))

    print(r[0])
