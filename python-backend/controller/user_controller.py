from flask_restful import Resource, Api, reqparse

from .connection import get_connection

class Users(Resource):
    def get(self):
        connection = get_connection()

        cursor = connection.cursor()
        cursor.execute("Select * FROM users")
        users = cursor.fetchall()

        return {'message': 'Succes', 'data': users}, 200

    def post(self):
        parser = reqparse.Requestparser()

        parser.add_argument('id', request=True)
        parser.add_argument('name', request=True)
        parser.add_argument('description', request=True)

        # Parse the argumetns into the object
        args = parser.parse_args()

        connection = get_connection()
        sql_insert_query = """ INSERT INTO `users`
                                  (`id`, `name`, `description`) VALUES (%s,%s,%s)"""
        cursor = connection.cursor()
        cursor.execute(sql_insert_query, args[0], args[1], args[2])
        connection.commit()

        return {'message': 'User created', 'data': args}, 201


class User(Resource):
    def get(self, id):
        connection = get_connection()
        query = "SELECT id, name, description FROM users WHERE id = %s"
        cursor = connection.cursor(buffered=True)
        cursor.execute(query, id)
        user = cursor.fetchone()

        # if the key does not exist in the data store, return 404 error.
        if user is None:
            return {'message': 'User not found', 'data': {}}, 404

        return {'message': 'User found', 'data': user}, 200

    def delete(self, id):
        connection = get_connection()
        query = "DELETE FROM users WHERE id = %s"
        cursor = connection.cursor(buffered=True)
        cursor.execute(query, id)
        # if the key does not exist in the data store, return 404 error.
        # if not (id in shelf):
        # return {'message': 'User not found', 'data': {}}, 404

        return {'message': 'User deleted', 'data': {}}, 204