# mysql-transfer python module

This python module is for transferring MySQL databases.

## Quick Start

Install mysql_transfer with `pip install git+ssh://git@github.com/MichaelMackus/mysql-transfer.git`.

Transferring a symfony site:

```python
from contextlib import closing
import mysql_transfer

from = mysql_transfer.load_params('path/to/parameters.yml',
                           db_params={'host': 'database_host',
                                      'name': 'database_name',
                                      'user': 'database_user',
                                      'password': 'database_password',
                                      'port': 'database_port'},
                           param_key='parameters')

to = mysql_transfer.load_params('path/to/parameters.yml',
                           db_params={'host': 'database_host',
                                      'name': 'database_name',
                                      'user': 'database_user',
                                      'password': 'database_password',
                                      'port': 'database_port'},
                           param_key='parameters')


tables = [] # set list of tables to transfer - empty means *ALL*
mysql_transfer.transfer_db(from, to, tables)
```

To transfer a bolt site, use:

```python
from contextlib import closing
import mysql_transfer

from = mysql_transfer.load_params('path/to/parameters.yml',
                           db_params={'host': 'host',
                                      'name': 'databasename',
                                      'user': 'username',
                                      'password': 'password',
                                      'port': 'port'},
                           param_key='database')

to = mysql_transfer.load_params('path/to/parameters.yml',
                           db_params={'host': 'host',
                                      'name': 'databasename',
                                      'user': 'username',
                                      'password': 'password',
                                      'port': 'port'},
                           param_key='database')


tables = [] # set list of tables to transfer - empty means *ALL*
mysql_transfer.transfer_db(from, to, tables)
```

For more details, see `help(mysql_transfer.load_params)`, `help(mysql_transfer.MySQLParams)`, and
`help(mysql_transfer.transfer_db)` in a python REPL (you'll have to `import mysql_transfer` first).
