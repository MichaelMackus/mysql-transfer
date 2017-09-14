from setuptools import setup

setup(name='mysql-transfer',
      version='0.2',
      description='Transfer MySQL databases. Also has support for '
                  'loading parameters from YAML files and checking '
                  'for a migration version match (before transfer).',
      url='http://github.com/MichaelMackus/mysql-transfer',
      author='Michael Mackus',
      author_email='michaelmackus@gmail.com',
      license='MIT',
      packages=['mysql_transfer'],
      zip_safe=False)
