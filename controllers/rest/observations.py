from utils.custom_views import JsonMethodView
from utils.db_conn import SqliteClient
from http import HTTPStatus
from marshmallow import Schema, fields
from flask import request


class Observations(JsonMethodView):

    class Observations(Schema):
        observation_list = fields.List(fields.Int())

    def get(self):
        # Get the data from the request
        db = SqliteClient()
        observations = db.query(f"""
            SELECT 
                sepal_length,
                petal_length,
                petal_width,
                species_id
            FROM Observation
            """)
        db.close_conn()

        observation_dict_response = [{"observations": observation} for observation in observations]

        return self.create_json_response(HTTPStatus.OK, observation_dict_response)

    def post(self):
        # Get the data from the request
        request_data = self.Observations().loads(request.data)
        specie_id_list = request_data.get('observation_list')

        if len(specie_id_list) == 1:
            species_id_values = f"({specie_id_list[0]})"
        else:
            species_id_values = tuple(specie_id_list)

        db = SqliteClient()
        observations = db.query(f"""
                    SELECT 
                        sepal_length,
                        petal_length,
                        petal_width,
                        species_id
                    FROM Observation
                    WHERE species_id IN {species_id_values}
                    """)
        db.close_conn()

        observation_dict_response = {idx: [observation] for idx, observation in enumerate(observations)}

        return self.create_json_response(HTTPStatus.OK, observation_dict_response)
