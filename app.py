from app import app
from flask_restful import Resource, Api

api = Api(app)

class Koctank(Resource):
    def get(self):
        return {"octank": "abp test"}

api.add_resource(Koctank, '/')

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=8443)
