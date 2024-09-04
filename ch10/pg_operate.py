import psycopg2

# 数据库连接参数  

conn_params = {  
    "dbname": "jee",  
    "user": "postgres",  
    "password": "",  
    "host": "127.0.0.1",  
    "port": "5432",  
} 

with psycopg2.connect(**conn_params)  as conn:


    # 创建一个cursor对象，用于执行SQL语句  

    with conn.cursor() as cur:
        #print(dir(conn))
        # 执行SQL查询  
        cur.execute("update production set name='fffff' where id=1")  
        # 获取查询结果  
        print(dir(cur))
        #record = cur.fetchone()
        #print("You are connected to - ", record)  
        conn.commit()
    



