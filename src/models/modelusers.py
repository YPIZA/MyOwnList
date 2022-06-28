from .entities.user import User
from werkzeug.security import generate_password_hash
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
import psycopg2

con = None
cursor = None

class ModelUser():
    @classmethod
    def login(self, user):
        try:
            con = psycopg2.connect(
                host = 'ec2-18-204-142-254.compute-1.amazonaws.com',
                database = 'd7gehdosecboli',
                user = 'puwucglwuisghg',
                password = '4bed1f246b5d68178df83dc110d26b972d8c67842286130541e9084dde4a537f',
                port = 5432
            )
            cursor = con.cursor()
            cursor.execute('SELECT * FROM users WHERE username = %s', (user.username,))
            row = cursor.fetchone()
            if row != None:
                if int(row[3]) <= 20:
                    plan = 'Aldeano'
                elif int(row[3]) > 20 and int(row[3]) <= 60:
                    plan = 'General'
                elif int(row[3]) > 60 and int(row[3]) <= 120:
                    plan = 'Duque'
                elif int(row[3]) > 120 and int(row[3]) <= 240:
                    plan = 'Principe'
                elif int(row[3]) > 240 and int(row[3]) <= 360:
                    plan = 'Maestro'
                elif int(row[3]) > 360 and int(row[3]) <= 420:
                    plan = 'Sabio'
                elif int(row[3]) > 420 and int(row[3]) <= 560:
                    plan = 'Rey'
                elif int(row[3]) > 560 and int(row[3]) <= 600:
                    plan = 'Conquistador'
                elif int(row[3]) > 600 and int(row[3]) <= 1000:
                    plan = 'Emperador'
                elif int(row[3]) >1000:
                    plan = '✨Monarca✨'
                return  User(row[0], row[1], User.check_password(row[2], user.password), row[4], plan, row[3])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        finally:
            if cursor is not None:
                cursor.close()
            if con is not None:
                con.close()

    @classmethod
    def get_by_id(self, id):
        try:
            con = psycopg2.connect(
                host = 'ec2-18-204-142-254.compute-1.amazonaws.com',
                database = 'd7gehdosecboli',
                user = 'puwucglwuisghg',
                password = '4bed1f246b5d68178df83dc110d26b972d8c67842286130541e9084dde4a537f',
                port = 5432
            )
            cursor = con.cursor()
            cursor.execute('SELECT * FROM users WHERE id = %s', (id,))
            row = cursor.fetchone()
            if row != None:
                if int(row[3]) <= 20:
                    plan = 'Aldeano'
                elif int(row[3]) > 20 and int(row[3]) <= 60:
                    plan = 'General'
                elif int(row[3]) > 60 and int(row[3]) <= 120:
                    plan = 'Duque'
                elif int(row[3]) > 120 and int(row[3]) <= 240:
                    plan = 'Principe'
                elif int(row[3]) > 240 and int(row[3]) <= 360:
                    plan = 'Maestro'
                elif int(row[3]) > 360 and int(row[3]) <= 420:
                    plan = 'Sabio'
                elif int(row[3]) > 420 and int(row[3]) <= 560:
                    plan = 'Rey'
                elif int(row[3]) > 560 and int(row[3]) <= 600:
                    plan = 'Conquistador'
                elif int(row[3]) > 600 and int(row[3]) <= 1000:
                    plan = 'Emperador'
                elif int(row[3]) >1000:
                    plan = '✨Monarca✨'
                return User(row[0], row[1], None, row[4], plan, row[3])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        finally:
            if cursor is not None:
                cursor.close()
            if con is not None:
                con.close()

    @classmethod
    def register(self, user):
        try:
            con = psycopg2.connect(
                host = 'ec2-18-204-142-254.compute-1.amazonaws.com',
                database = 'd7gehdosecboli',
                user = 'puwucglwuisghg',
                password = '4bed1f246b5d68178df83dc110d26b972d8c67842286130541e9084dde4a537f',
                port = 5432
            )
            cur = con.cursor()
            cur.execute(
                '''
                INSERT INTO users(username, password , puntos, foto)
                values(%s, %s, %s, %s)
                ''',
                (user.username, generate_password_hash(user.password), int(1), user.foto)
            )
            con.commit()
            return 'alguna monda'
        except Exception as ex:
            raise Exception(ex)
        finally:
            if cursor is not None:
                cursor.close()
            if con is not None:
                con.close()
    @classmethod
    def crear_tabla(self, user):
        con = psycopg2.connect(
            host = 'ec2-18-204-142-254.compute-1.amazonaws.com',
            database = 'd7gehdosecboli',
            user = 'puwucglwuisghg',
            password = '4bed1f246b5d68178df83dc110d26b972d8c67842286130541e9084dde4a537f',
            port = 5432
        )
        cur = con.cursor()
        
        try:
            sql = f'CREATE TABLE {user}(id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, type VARCHAR(255) NOT NULL, cap VARCHAR(255) NOT NULL, status VARCHAR(255) NOT NULL, link VARCHAR(255) NOT NULL)'
            print(sql)
            cur.execute(sql)
            con.commit()
        except Exception as ex:
            raise Exception(ex)
        finally:
            if cursor is not None:
                cursor.close()
            if con is not None:
                con.close()

    @classmethod
    def get_list(self, user):
        usuario = user.username
        con = psycopg2.connect(
            host = 'ec2-18-204-142-254.compute-1.amazonaws.com',
            database = 'd7gehdosecboli',
            user = 'puwucglwuisghg',
            password = '4bed1f246b5d68178df83dc110d26b972d8c67842286130541e9084dde4a537f',
            port = 5432
        )
        cur = con.cursor()
        try:
            con = psycopg2.connect(
                host = 'ec2-18-204-142-254.compute-1.amazonaws.com',
                database = 'd7gehdosecboli',
                user = 'puwucglwuisghg',
                password = '4bed1f246b5d68178df83dc110d26b972d8c67842286130541e9084dde4a537f',
                port = 5432
            )
            cur = con.cursor()
            cur.execute(f'SELECT * FROM {usuario.lower()}')
            mm = cur.fetchall()
            ahora = []
            retur = []
            for retu in mm:
                data = {
                    'id': retu[0],
                    'name': retu[1],
                    'type': retu[2],
                    'cap': retu[3],
                    'status': retu[4],
                    'link': retu[5]
                }
                ahora.append(data)
            for busqueda in reversed(ahora):
                retur.append(busqueda)
            return retur
        except Exception as ex:
            raise Exception(ex)
        finally:
            if cursor is not None:
                cursor.close()
            if con is not None:
                con.close()

    @classmethod
    def get_list_7(self, list):
        print(list)
        if len(list) != 0:
            g = []
            z = []
            i = 0
            for busqueda in list:
                g.append(busqueda)
            if len(g) > 6:
                for t in range(7):
                    z.append(g[i])
                    i += 1
                return z
            else:
                return g
        else:
            return 0

    @classmethod
    def add_one(self, item, user):
        con = psycopg2.connect(
            host = 'ec2-18-204-142-254.compute-1.amazonaws.com',
            database = 'd7gehdosecboli',
            user = 'puwucglwuisghg',
            password = '4bed1f246b5d68178df83dc110d26b972d8c67842286130541e9084dde4a537f',
            port = 5432
        )
        cur = con.cursor()
        cur.execute(f'INSERT INTO {user.username}(name, type, cap, status, link) values (%s, %s, %s, %s, %s)', (str(item.name), str(item.type), str(item.cap), str(item.status), str(item.link)))
        con.commit()
        return "ok"

    @classmethod
    def by_type(self, type, user):
        con = psycopg2.connect(
            host = 'ec2-18-204-142-254.compute-1.amazonaws.com',
            database = 'd7gehdosecboli',
            user = 'puwucglwuisghg',
            password = '4bed1f246b5d68178df83dc110d26b972d8c67842286130541e9084dde4a537f',
            port = 5432
        )
        cur = con.cursor()
        cur.execute(f'SELECT * FROM {user.username} WHERE type=%s', (type,))
        con.commit()
        mm = cur.fetchall()
        ahora = []
        retur = []
        for retu in mm:
            data = {
                'id': retu[0],
                'name': retu[1],
                'type': retu[2],
                'cap': retu[3],
                'status': retu[4],
                'link': retu[5]
            }
            ahora.append(data)
        for busqueda in reversed(ahora):
            retur.append(busqueda)
        return retur