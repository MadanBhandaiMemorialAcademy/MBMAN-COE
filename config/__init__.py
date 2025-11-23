from .celery import app as celery_app

__all__ = ("celery_app",)

# Use PyMySQL as a fallback for MySQL if mysqlclient isn't installed
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
