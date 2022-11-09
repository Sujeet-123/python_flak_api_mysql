import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='#zecData12345',
    database='wscube'
    )


# print(mybd.connection_id)

 
mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE user_info5 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255),phone VARCHAR(15))")



DATA = """INSERT INTO user_info4 (name, address, phone) VALUES('Peter', 'Lowstreet 4','1234567899'),
  ('Amy', 'Apple st 652','1234567899'),
  ('Hannah', 'Mountain 21','1234567899'),
  ('Michael', 'Valley 345','1234567899'),
  ('Sandy', 'Ocean blvd 2','1234567899'),
  ('Betty', 'Green Grass 1','1234567899'),
  ('Richard', 'Sky st 331','1234567899'),
  ('Susan', 'One way 98','1234567899'),
  ('Vicky', 'Yellow Garden 2','1234567899'),
  ('Ben', 'Park Lane 38','1234567899'),
  ('William', 'Central st 954','1234567899'),
  ('Chuck', 'Main Road 989','1234567899'),
  ('Viola', 'Sideway 1633','')"""


mycursor.execute(DATA)

mydb.commit()

print(mycursor.rowcount, "was inserted.")