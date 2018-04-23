from flask import Flask, request
from flask.ext.restful import Resource, Api
from flask.ext.restful import reqparse

from expr.movement import cal_movement
import leancloud

app = Flask(__name__)
api = Api(app)


class Movement(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('r0', type=int, required=True)
        parser.add_argument('r1', type=int, required=True)
        parser.add_argument('a', type=int, required=True)
        parser.add_argument('b', type=int, required=True)
        args = parser.parse_args()
        a = args.get("a")
        b = args.get("b")
        r0 = args.get("r0")
        r1 = args.get("r1")
        result = cal_movement(a, b, r0, r1)
        return result, 201


api.add_resource(Movement, '/cal-movement')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
