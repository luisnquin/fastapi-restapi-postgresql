import psycopg2


# To fill the ids in the database
def checkIfThereIsAnIdSlotAvailable():
    connection = psycopg2.connect(
        host="localhost",
        database="restapidb",
        user="postgres",
        password="admin",
        port=5432
    )

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
def executeQuery(action: str = "GET", userdata: list = None, newid: int = None):
    connection = psycopg2.connect(
        host="localhost",
        database="restapidb",
        user="postgres",
        password="admin",
        port=5432,
    )

    cursor = connection.cursor()

    match action:
        case "GET":
            query = "SELECT * FROM CLIENT_DATA ORDER BY id ASC;"
            cursor.execute(query)
            data = cursor.fetchall()

            cursor.close()
            connection.close()

            return data

        case "POST":
            if checkIfThereIsAnIdSlotAvailable():
                id = checkIfThereIsAnIdSlotAvailable()
                query = f"INSERT INTO CLIENT_DATA(id, fullname, email, gender, credit_card, credit_type) VALUES({id}, '{userdata[0]}', '{userdata[1]}', '{userdata[2]}', '{userdata[3]}', '{userdata[4]}');"
            else:
                match len(userdata):
                    case 5:
                        query = f"INSERT INTO CLIENT_DATA(fullname, email, gender, credit_card, credit_type) VALUES('{userdata[0]}', '{userdata[1]}', '{userdata[2]}', '{userdata[3]}', '{userdata[4]}');"
                    case 6:
                        query = f"INSERT INTO CLIENT_DATA(id, fullname, email, gender, credit_card, credit_type) VALUES('{userdata[0]}', '{userdata[1]}', '{userdata[2]}', '{userdata[3]}', '{userdata[4]}', '{userdata[5]}');"
                    case _:
                        raise Exception(
                            "Does not meet the requirements for action.")

            cursor.execute(query)
            connection.commit()

            cursor.close()
            connection.close()

            return executeQuery(action="GET")

        case "PUT":
            if newid:
                query = f"UPDATE CLIENT_DATA SET id='{newid}' fullname='{userdata[1]}', email='{userdata[2]}', gender='{userdata[3]}', credit_card='{userdata[4]}', credit_type='{userdata[5]} WHERE id={userdata[0]}';"
            elif len(userdata) == 6:
                query = f"UPDATE CLIENT_DATA SET fullname='{userdata[1]}', email='{userdata[2]}', gender='{userdata[3]}', credit_card='{userdata[4]}', credit_type='{userdata[5]} WHERE id={userdata[0]}';"
            else:
                raise Exception("Does not meet the requirements for action.")

            cursor.execute(query)
            connection.commit()

            cursor.close()
            connection.close()

            return executeQuery(action="GET")

        case "DELETE":
            match type(userdata):
                case type([0]), type((0)):
                    query = f"DELETE FROM CLIENT_DATA WHERE id={int(userdata[0])};"
                case type(""), type(0):
                    query = f"DELETE FROM CLIENT_DATA WHERE id={int(userdata)};"
                case _:
                    raise Exception(
                        "Does not meet the requirements for action.")

            cursor.execute(query)
            connection.commit()

            cursor.close()
            connection.close()

            return executeQuery(action="GET")


if __name__ == "__main__":
    print(executeQuery(action="GET", userdata=[]))


"""create table CLIENT_DATA (id SERIAL PRIMARY KEY, fullname VARCHAR(50) NOT NULL,email VARCHAR(50) NOT NULL,gender VARCHAR(50) NOT NULL, credit_card VARCHAR(50) NOT NULL,credit_type VARCHAR(50) NOT NULL);"""
