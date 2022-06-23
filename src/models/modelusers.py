from .entities.user import User
from werkzeug.security import generate_password_hash
import pymongo, random
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
client = pymongo.MongoClient('mongodb+srv://YPIZA:MRsK04L4trelarascas%40outllook.es@myownlist.j55j2.mongodb.net/?retryWrites=true&w=majority')
usuaros = client['UsersWeb']
usuarios = usuaros['users']
usuaios = client['MyList']


class ModelUser():
    @classmethod
    def login(self, user):
        try:
            busqueda = usuarios.find_one({
                "user": user.username
            })
            print(busqueda)
            if busqueda != None:
                usuario = User(busqueda['id'],busqueda['user'], User.check_password(busqueda['pwd'], user.password), busqueda['email'], busqueda['foto'], busqueda['plan'], busqueda['creditos'])
                return usuario
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, id):
        try:
            busqueda = usuarios.find_one({
                "id": int(id)
            })
            if busqueda != None:
                return User(busqueda['id'],busqueda['user'], None, busqueda['email'], busqueda['foto'], busqueda['plan'], busqueda['creditos'])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def register(self, user):
        busqueda = usuarios.insert_one({
                "id": int(random.randint(11111,99999)),
                "user": user.username,
                "creditos": int(1),
                "plan": "Free",
                "pwd": generate_password_hash(user.password),
                "email": user.email,
                "foto": user.foto
            })
        return busqueda.inserted_id

    @classmethod
    def get_list(self, user):
        col = usuaios[user.username]
        i = []
        retur = []
        for busqueda in col.find():
            i.append(busqueda)
        for busqueda in reversed(i):
            retur.append(busqueda)
        return retur

    @classmethod
    def get_list_7(self, list):
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
        col = usuaios[user.username]
        itea = col.insert_one({
            'name': item.name,
            'type': item.type,
            'cap': item.cap,
            'status': item.status,
            'link': item.link
        })
        return itea.inserted_id

    @classmethod
    def by_type(self, type, user):
        col = usuaios[user.username]
        i = []
        retur = []
        for busqueda in col.find({
            'type': type
        }):
            i.append(busqueda)
        for busqueda in reversed(i):
            retur.append(busqueda)
        return retur