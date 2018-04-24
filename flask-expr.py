from flask import Flask, request
from flask.ext.restful import Resource, Api
from flask.ext.restful import reqparse
from flask import render_template

from expr.movement import cal_movement
import leancloud

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello():
    return render_template('index.html')


class Movement(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('r0', type=float, required=True)
        parser.add_argument('r1', type=float, required=True)
        parser.add_argument('a', type=float, required=True)
        parser.add_argument('b', type=float, required=True)
        args = parser.parse_args()
        a = args.get("a")
        b = args.get("b")
        r0 = args.get("r0")
        r1 = args.get("r1")
        if (a == 0 or b == 0 or r0 == 0 or r1 == 0):
            return {}, 400
        result = cal_movement(a, b, r0, r1)
        return result, 200


api.add_resource(Movement, '/cal-movement')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
