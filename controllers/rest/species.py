from utils.custom_views import JsonMethodView
from utils.db_conn import SqliteClient
from http import HTTPStatus
from marshmallow import Schema, fields
from flask import request


class Species(JsonMethodView):

    class Species(Schema):
        specie_list = fields.List(fields.Str())

    def get(self):
        # Get the data from the request
        db = SqliteClient()
        species = db.query(f"SELECT species FROM Species")
        db.close_conn()

        specie_dict_response = [{"specie": specie[0]} for specie in species]

        return self.create_json_response(HTTPStatus.OK, specie_dict_response)

    def post(self):
        # Get the data from the request
        request_data = self.Species().loads(request.data)
        specie_list = request_data.get('specie_list')

        if len(specie_list) == 1:
            species_values = f"('{specie_list[0]}')"
        else:
            species_values = tuple(specie_list)

        db = SqliteClient()
        species = db.query(f"SELECT species FROM Species WHERE species IN {species_values};")
        db.close_conn()

        species_dict_response = {idx: specie[0] for idx, specie in enumerate(species)}

        return self.create_json_response(HTTPStatus.OK, species_dict_response)
