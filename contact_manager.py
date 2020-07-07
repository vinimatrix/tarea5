import sqlite3
import pandas as pd
from sqlite3 import Error


def create_connection(db_file_name):
     '''CREACION DE UNA CONEXION A UNA DB SQLITE
      :param db_file_name: nombre/ruta de la base de datos
     '''
     conn = None
     try:
        conn = sqlite3.connect(db_file_name)
        print("conectado a la db - version: {0}",sqlite3.version)
     except Error as e:
        print(e)
   
     return conn
     

def create_table(conn,sql_create_command):
    '''CREACION DE UNA TABLA A TRAVEZ DE UN COMANDO SQL
    :param conn: objeto conexion
    :param: sql_create_command: comando sql para la creacion de la tabla
    '''
    try:
        c = conn.cursor()
        c.execute(sql_create_command)
    except Error as e:
        print(e)


def insert_cliente_data(conn, cliente):
      '''INSERTAR DATOS DE CLIENTE A TRAVEZ DE UN COMANDO SQL
      :param conn: objeto conexion
      :param:cliente: datos del cliente a insertar
      '''
      try:
        c = conn.cursor()
        sql_insert_command = """INSERT INTO clientes(first_name,last_name,phone_number,email)
                            VALUES (?,?,?,?);"""
        c.execute(sql_insert_command,cliente)
        conn.commit()
        print(c.lastrowid,cliente[0],cliente[1])

      except Error as e:
        print(e)
        print(e.args)


def insert_vendedor_data(conn, vendedor):
      '''INSERTAR DATOS DE VENDEDOR A TRAVEZ DE UN COMANDO SQL
      :param conn: objeto conexion
      :param:cliente: datos del vendedor a insertar
      '''
      try:
        c = conn.cursor()
        sql_insert_command = """INSERT INTO vendedores( first_name,last_name,departamento,email)
                        VALUES (?,?,?,?);"""
        c.execute(sql_insert_command,vendedor)
        conn.commit()
        print(c.lastrowid,vendedor[0],vendedor[1])
      except Error as e:
        print(e)
        print(e.args)       


def insert_venta_data(conn, venta):
      '''INSERTAR DATOS DE VENTAS A TRAVEZ DE UN COMANDO SQL
      :param conn: objeto conexion
      :param:cliente: datos de la venta a insertar
      '''
      try:
        c = conn.cursor()
        sql_insert_command = """INSERT INTO ventas(venta_date,venta_total,vendedor_id,cliente_id)
                        VALUES (?,?,?,?);"""
        c.execute(sql_insert_command,venta)
        conn.commit()
        print(c.lastrowid,venta[0],venta[1])
      except Error as e:
        print(e)
        print(e.args) 

def main():
    db_file = 'clientes.db'
    conn = create_connection(db_file)
    sql_create_cliente_cmd = """CREATE TABLE IF NOT EXISTS clientes(
            id integer PRIMARY KEY NOT NULL,
            first_name text NOT NULL,
            last_name text NOT NULL,
            phone_number text NOT NULL,
            email text
        );
    """ 
    sql_create_vendedores_cmd = """CREATE TABLE IF NOT EXISTS vendedores(
            id integer PRIMARY KEY NOT NULL,
            first_name text NOT NULL,
            last_name text NOT NULL,
            departamento text NOT NULL,
            email text
        );
    """ 

    sql_create_ventas = """CREATE TABLE IF NOT EXISTS ventas(
            id integer PRIMARY KEY NOT NULL,
            venta_date text NOT NULL,
            venta_total real NOT NULL,
            vendedor_id integer NOT NULL,
            cliente_id integer NOT NULL,
            FOREIGN KEY (vendedor_id) REFERENCES vendedores (id),
            FOREIGN KEY (cliente_id) REFERENCES clientes (id)
        );
        """
    create_table(conn,sql_create_cliente_cmd)
    create_table(conn,sql_create_vendedores_cmd)
    create_table(conn,sql_create_ventas)

    print('******TABLAS CREADAS**********')
    print('******POR FAVOR ESPERE**********')
    print('GENERANDO LA DATA')
    
    cliente1 = ('OSCAR','ACOSTA',8096555555,'')
    cliente2 =('JHON','DOE','8096555556','')
    cliente3 = ('JANE','DOE','8096555557','janed@gmail.com')
    cliente4 =('FULANITO','DE TAL','8096555558','elfula@hotmail.com')
    cliente5 = ('PERENSEJO','PEREZ','8096555559','')  
 
    ''''DATA DE LOS VENDEDORES '''''
    vendedor1 = ('JUAN','DE LOS PALOTES','VENTAS EMPRESARIALES','juandlp@empresa.com')
    vendedor2 = ('MICHAEL','DOEL','VENTAS DE CONTADO','michaeld@empresa.com')
    vendedor3 =  ('JUANA','DOEL','VENTAS DE CONTADO','juanad@empresa.com')
    vendedor4 =  ('JOSE','DE LOS MOROS','VENTAS ELECTRONICOS','josedm@empresa.com')
    vendedor5 =  ('PETER','DE LA NUEZ','VENTAS SOFTWARE','peterdn@empresa.com')                                 
    
    
    ''' DATA DE VENTAS '''
    venta1 = ('2020-07-06',105.00,1,1)
    venta2 = ('2020-07-06',200.00,1,2)
    venta3 = ('2020-07-06',500.00,2,3)   
    venta4 = ('2020-07-06',30.00,3,4)
    venta5 = ('2020-07-06',30.00,4,3)         

    '''''INSERTANDO DATA'''''

    print('\n******GENERANDO DATA DE CLIENTES*******')
    insert_cliente_data(conn,cliente1)
    insert_cliente_data(conn,cliente2)
    insert_cliente_data(conn,cliente3)
    insert_cliente_data(conn,cliente4)
    insert_cliente_data(conn,cliente5)

    
    print('\n******GENERANDO DATA DE VENDEDORES*******')  
    insert_vendedor_data(conn,vendedor1)
    insert_vendedor_data(conn,vendedor2)
    insert_vendedor_data(conn,vendedor3)
    insert_vendedor_data(conn,vendedor4)
    insert_vendedor_data(conn,vendedor5)

    print('\n******GENERANDO DATA DE VENTAS*******')
    insert_venta_data(conn,venta1)
    insert_venta_data(conn,venta2)
    insert_venta_data(conn,venta3)
    insert_venta_data(conn,venta4)
    insert_venta_data(conn,venta5)
    
    print("*****la data de testeo se ha generado*********")



if __name__  == "__main__":
    main()






