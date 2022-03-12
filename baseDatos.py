import pymysql

class DataBase():
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user='root',
            password= '',
            db= 'ventas'
        )
        self.cursor= self.connection.cursor()
    def agregarUsuario(self,nombre,contrasena,tipo,email):
        sql= 'INSERT INTO usuario(contrasena,nombre,tipo,email,flag) Values({},{},{},{},{})'

        try:
            self.cursor.execute(sql.format(nombre,contrasena,tipo,email,"1"))
            self.connection.commit()
            print("add usuario")

        except Exception as e:
            raise
    def agregarProducto(self,idUsuario,precio,costo,nombre):
        sql= 'INSERT INTO producto(nombre,idUsuario,precio,costo,flag) VALUES({},{},{},{},{})'

        try:
            self.cursor.execute(sql.format(nombre,idUsuario,precio,costo,"1"))
            self.connection.commit()
            print("add producto")

        except Exception as e:
            raise
    def agregarVenta(self,idProducto,envio,dia):
        sql= 'INSERT INTO venta(idProducto,envio,dia,flag) VALUES({},{},{},{})'
        try:
            self.cursor.execute(sql.format(idProducto,envio,dia,"1"))
            self.connection.commit()
            print("add venta")

        except Exception as e:
            raise
    



dataBase= DataBase()
dataBase.agregarVenta("'1'","'100'","'2022-12-03'")