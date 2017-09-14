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
            'mysqldump -h {from_host} -P {from_port} -u {from_user} {from_args} | '
            'mysql -h {to_host} -P {to_port} -u {to_user} {to_args}'.format(
                from_host=from_params.host,
                from_port=from_params.port,
                from_user=from_params.user,
                from_args=from_params.get_dump_args(tables),
                to_host=to_params.host,
                to_port=to_params.port,
                to_user=to_params.user,
                to_args=to_params.get_mysql_args()),
            shell=True)
        r = p.communicate()
    except AttributeError:
        raise MySQLTransferException('Invalid MySQLParams object passed '
                                     'to transfer_db.')

    if r[1]:
        raise MySQLTransferException(
            "MySQL transfer error: {}".format(r[1]))

    print(r[0])
