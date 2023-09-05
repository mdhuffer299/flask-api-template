from flask import Flask, Blueprint
from controllers.rest.species import Species
from controllers.rest.observations import Observations
from flask_cors import CORS


def create_rest_app(config):
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})
    app.config.from_object(config)

    rest_blueprint = Blueprint('rest', __name__,
                               url_prefix='/rest',
                               template_folder='../../templates')

    species = Species.as_view('specie')
    rest_blueprint.add_url_rule('/species',
                                view_func=species,
                                methods=['GET', 'POST'])

    observations = Observations.as_view('observation')
    rest_blueprint.add_url_rule('/observations',
                                view_func=observations,
                                methods=['GET', 'POST'])

    app.register_blueprint(rest_blueprint, url_prefix="/rest")

    return app
