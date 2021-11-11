import psycopg2


# To fill the ids in the database
def checkIfThereIsAnIdSlotAvailable():
    connection = psycopg2.connect(
        host="localhost", database="restapidb", user="postgres", password="admin", port=5432)
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(id) FROM CLIENT_DATA;")
    nRecords = cursor.fetchone()[0]

    cursor.execute("SELECT id FROM CLIENT_DATA;")
    ids = [id[0] for id in cursor.fetchall()]

    cursor.close()
    connection.close()

    data = list(set(range(1, nRecords)) - set(ids))[0]

    return data if data else False


# querydata = [id, fullname, email, gender, credit_card, credit_type]
def executeQuery(querydata: list = None, action: str = "GET", newid: int = None):
    connection = psycopg2.connect(
        host="localhost",
        database="restapidb",
        user="postgres",
        password="admin",
        port=5432,
    )

    cursor = connection.cursor()

    if action == "GET":
        query = "SELECT * FROM CLIENT_DATA ORDER BY id ASC;"
        cursor.execute(query)
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return data

    if action == "POST":
        if checkIfThereIsAnIdSlotAvailable():
            id = checkIfThereIsAnIdSlotAvailable()
            query = f"INSERT INTO CLIENT_DATA(id, fullname, email, gender, credit_card, credit_type) VALUES({id}, '{querydata[0]}', '{querydata[1]}', '{querydata[2]}', '{querydata[3]}', '{querydata[4]}');"
        else:
            match len(querydata):
                case 5:
                    query = f"INSERT INTO CLIENT_DATA(fullname, email, gender, credit_card, credit_type) VALUES('{querydata[0]}', '{querydata[1]}', '{querydata[2]}', '{querydata[3]}', '{querydata[4]}');"
                case 6:
                    query = f"INSERT INTO CLIENT_DATA(id, fullname, email, gender, credit_card, credit_type) VALUES('{querydata[0]}', '{querydata[1]}', '{querydata[2]}', '{querydata[3]}', '{querydata[4]}', '{querydata[5]}');"

        cursor.execute(query)
        connection.commit()

        cursor.close()
        connection.close()

        return executeQuery(action="GET")

    if action == "PUT":
        if len(querydata) == 6:
            query = f"UPDATE CLIENT_DATA SET fullname='{querydata[1]}', email='{querydata[2]}', gender='{querydata[3]}', credit_card='{querydata[4]}', credit_type='{querydata[5]} WHERE id={querydata[0]}';"
        if newid:
            query = f"UPDATE CLIENT_DATA SET id='{newid}' fullname='{querydata[1]}', email='{querydata[2]}', gender='{querydata[3]}', credit_card='{querydata[4]}', credit_type='{querydata[5]} WHERE id={querydata[0]}';"

        cursor.execute(query)
        connection.commit()

        cursor.close()
        connection.close()

        return executeQuery(action="GET")

    if action == "DELETE":
        if querydata == list:
            query = f"DELETE FROM CLIENT_DATA WHERE id={querydata[0]};"
        elif querydata == int:
            query = f"DELETE FROM CLIENT_DATA WHERE id={querydata};"
        elif querydata == str:
            query = f"DELETE FROM CLIENT_DATA WHERE id={int(querydata)};"

        cursor.execute(query)
        connection.commit()

        cursor.close()
        connection.close()

        return executeQuery(action="GET")


if __name__ == "__main__":
    print(executeQuery(action="GET"))


"""create table CLIENT_DATA (id SERIAL PRIMARY KEY, fullname VARCHAR(50) NOT NULL,email VARCHAR(50) NOT NULL,gender VARCHAR(50) NOT NULL, credit_card VARCHAR(50) NOT NULL,credit_type VARCHAR(50) NOT NULL);"""
