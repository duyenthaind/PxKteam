from connectDB.model import ConnectToDB, Name
from flask_restful import Resource
from flask import request

Session = ConnectToDB()

class NameCollectionAPI(Resource):
    def get(self):
        try:
            session = Session()
            names = session.query(Name).all()
            for i in range(len(names)):
                names[i] = standardizedData(names[i])
            return names
        except Exception as exp:
            raise (exp)
            return []
        finally:
            session.close()


    def post(self):
        try:
            session = Session()
            data = request.get_json()
            name = Name(
                name = data['name']
            )
            session.add(name)
            try:
                session.commit()
            except Exception as exp:
                raise (exp)
                session.rollback()
                return 'error1'
            return 'ok'
        except Exception as exp:
            raise (exp)
            return 'error2'
        finally:
            session.close()





def standardizedData(obj):
    try:
        obj = obj.__dict__
    except:
        return None
    try:
        if '_sa_instance_state' in obj:
            del obj["_sa_instance_state"]
    except:
        pass
    return obj


