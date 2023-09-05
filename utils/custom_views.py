from flask import jsonify, make_response
from flask.views import MethodView


_ALLOWED_HEADERS = 'Accept, Authorization, Content-Type, Origin'
_ALLOWED_METHODS = 'GET, POST, PUT, DELETE, OPTIONS'


class JsonMethodView(MethodView):

    def __init__(self):
        super(JsonMethodView, self).__init__()

    @staticmethod
    def create_response(code,
                        body,
                        content_type: str = "text/plain",
                        allow_headers: str = _ALLOWED_HEADERS,
                        allow_methods: str = _ALLOWED_METHODS):

        """
        Create a plain response without modifying the content, respecting the provided body, code, and content-type

        :param code:
        :param body:
        :param content_type:
        :param allow_headers:
        :param allow_methods:
        :return:
        """

        response = make_response(body, code)

        response.headers['Access-Control-Allow-Headers'] = allow_headers
        response.headers['Access-Control-Allow-Methods'] = allow_methods
        response.headers['Content-Type'] = content_type

        return response

    def create_json_response(self,
                             code,
                             content,
                             content_type: str = 'application/json'):
        """
        Create a response with JSON content.  Content is expected to be bytes, str, or dict.
        :param self:
        :param code:
        :param content:
        :param content_type:
        :return:
        """
        if isinstance(content, bytes):
            content = content.decode('utf-8')
        if isinstance(content, str):
            content = {'message': content}

        return self.create_response(code=code, body=jsonify(content), content_type=content_type)

