# Use PyMySQL as a fallback for MySQL if mysqlclient isn't installed
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
