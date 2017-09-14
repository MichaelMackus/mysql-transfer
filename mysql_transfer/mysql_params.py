class MySQLParseException(Exception):
    pass

class MySQLParams:
    """
    Container for MySQL parameters. Has some helpful methods to get
    args for the `mysql` and `mysqldump` commands, as well as a method
    to load the MySQLdb database.
    """

    def __init__(self, params):
        """
        Initialize MySQLParams. You probably want to load the params
        using load_params if your params are in a YAML file.

        
        ARGUMENTS:

        params - dictionary with keys: name, user, host, password, and
            port. Only name and user are required.
        """

        if 'name' not in params:
            raise MySQLParseException('"name" is a required parameter')
        if 'user' not in params:
            raise MySQLParseException('"user" is a required parameter')

        self.name = params['name']
        self.user = params['user']
        self.host = params['host'] if 'host' in params else 'localhost'
        self.password = params['password'] if 'password' in params else None
        self.port = params['port'] if 'port' in params else 3306

    def get_dump_args(tables=[]):
        "Get args for mysqldump"
        return '-h {} -P {} -u {} {}'.format(
            this.host, this.port, this.user, ' '.join(this.name, tables))

    def get_mysql_args():
        "Get args for mysql"
        return '-h {} -P {} -u {} {}'.format(
            this.host, this.port, this.user, this.name, tables)

    def load_db(self):
        "Load DB using MySQLdb"
        from MySQLdb import connect
        return connect(host=self.host,
                       user=self.user,
                       passwd=self.password,
                       db=self.name,
                       port=self.port)

def load_params(path,
                db_params={'host': 'database_host',
                           'name': 'database_name',
                           'user': 'database_user',
                           'password': 'database_password',
                           'port': 'database_port'},
                param_key='parameters'):

    """
    Load database parameters from YAML file. Returns an instance of
    MySQLParams on success, or throws a MySQLParseException on failure.


    ARGUMENTS:

    path - Full or relative path to YAML file.

    param_key - Top-level key to lookup in YAML file for database
        params. *NOTE*: If this is set to None, the database params will
        be assumed to be at the top-level of the YAML document.

    db_params - Dictionary with the DB param of "host", "name", "user",
        "password", or "port" as key, and the corresponding value found in
        the YAML document (under the `param_key` item).


    So, by default, it looks up DB params in a document looking like:


    parameters:
        database_host: host
        database_name: name
        database_user: user
        database_password: password
        database_port: port
    """

    import yaml

    with open(path) as f:
        if param_key is None:
            loaded_params = yaml.safe_load(f)
        else:
            try:
                loaded_params = yaml.safe_load(f)[param_key]
            except KeyError:
                raise MySQLParseException(
                    '{} is not a valid params file: param_key {} not found'
                        .format(path, param_key))

        params = {}
        for key, param in db_params.iteritems():
            if param in loaded_params and loaded_params[param] is not None:
                cast = str if key != 'port' else int
                params[key] = cast(loaded_params[param])

        return MySQLParams(params)
