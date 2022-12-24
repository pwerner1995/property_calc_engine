import mysql.connector

COLLECTION_NAME = "tilly"

class MysqlRepository(object):
  def __init__(self):
    tilly_db = mysql.connector.connect(
      host="127.0.0.1",
      user="pete",
      password="1226Conrad!",
      database="tilly"
    )

    print(tilly_db)

    def find_all(self, selector):
      return 