# mysql-transfer python module

This python module is for transferring MySQL databases.

## Quick Start

Install mysql_transfer with `pip install git+https://git@github.com/MichaelMackus/mysql-transfer.git`.

Transferring a symfony site:

```python
from contextlib import closing
import mysql_transfer

from_params = mysql_transfer.load_params('path/to/parameters.yml',
                           db_params={'host': 'database_host',
                                      'name': 'database_name',
                                      'user': 'database_user',
                                      'password': 'database_password',
                                      'port': 'database_port'},
                           param_key='parameters')

to_params = mysql_transfer.load_params('path/to/parameters.yml',
                           db_params={'host': 'database_host',
                                      'name': 'database_name',
                                      'user': 'database_user',
                                      'password': 'database_password',
                                      'port': 'database_port'},
                           param_key='parameters')


tables = [] # set list of tables to transfer - empty means *ALL*
mysql_transfer.transfer_db(from_params, to_params, tables)
```

To transfer a bolt site, use:

```python
from contextlib import closing
import mysql_transfer

from_params = mysql_transfer.load_params('path/to/parameters.yml',
                           db_params={'host': 'host',
                                      'name': 'databasename',
                                      'user': 'username',
                                      'password': 'password',
                                      'port': 'port'},
                           param_key='database')

to_params = mysql_transfer.load_params('path/to/parameters.yml',
                           db_params={'host': 'host',
                                      'name': 'databasename',
                                      'user': 'username',
                                      'password': 'password',
                                      'port': 'port'},
                           param_key='database')


tables = [] # set list of tables to transfer - empty means *ALL*
mysql_transfer.transfer_db(from_params, to_params, tables)
```

To transfer via an SSH tunnel:

```
from contextlib import closing
from mysql_transfer import transfer_db
from mysql_transfer.mysql_params import Params, MySQLParams
from mysql_transfer.mysql_tunnel import open_tunnel, SSHParams

from_params = MySQLParams({'host': '127.0.0.1',
                    'name': 'db_name',
                    'user': 'user_name',
                    'password': 'password',
                    'port': '3307'})

to_params = MySQLParams({'host': '127.0.0.1',
                  'name': 'to_db_name',
                  'user': 'local_user_name',
                  'password': 'local_password'})

tables = [] # set list of tables to transfer - empty means *ALL*

# create our SSH tunnel, listening to remote-db.host.com:3306 on
# 127.0.0.1:3307, via SSH tunnel to ssh_host
with open_tunnel(SSHParams('ssh_host'),
                 Params('remote-db.host.com',
                        3306),
                 from_params):
    # do the transfer
    transfer_db(from_params, to_params, tables)
```

For more details, see `help(mysql_transfer.load_params)`, `help(mysql_transfer.MySQLParams)`, and
`help(mysql_transfer.transfer_db)` in a python REPL (you'll have to `import mysql_transfer` first).
