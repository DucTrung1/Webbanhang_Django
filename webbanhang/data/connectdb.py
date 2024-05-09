import mysql.connector
db = mysql.connector.connect(user = 'root', password = '123456789', host = 'localhost', database = 'qlsv1')
code = 'create DATABASE `qls1` ;'

#TAO BANG TRONG DATABASE
CODE1 = "INSERT INTO `qlsv1`.`sinh_vien` (`ID`, `NAME`, `YEAR`) VALUES ('1', 'DUC TRUNG', '2002');"
mycursor = db.cursor()
mycursor.execute(CODE1)
# HAM UPDATE DB
db.commit()