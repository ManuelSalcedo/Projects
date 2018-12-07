import _mysql

db = _mysql.connect(host="joesmoe",port=3307,passwd="admin123",db="test")

db.query("""SELECT spam, eggs, sausage FROM breakfast
         WHERE price < 5""")

r=db.use_results()