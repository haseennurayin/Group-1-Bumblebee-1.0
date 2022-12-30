import mysql.connector

def add_reaction(shortcut_id, reaction):
  # connect to the database
  conn = mysql.connector.connect(user='<username>', password='<password>', host='<host>', database='<database>')
  cursor = conn.cursor()

  # add the reaction to the database
  sql = "INSERT INTO reactions (shortcut_id, reaction) VALUES (%s, %s)"
  values = (shortcut_id, reaction)
  cursor.execute(sql, values)
  conn.commit()

  # close the connection
  cursor.close()
  conn.close()

# example usage
add_reaction(1, 'love')
add_reaction(1, 'surprised')
add_reaction(1, 'boo')
add_reaction(2, 'surprised')
