import azure.functions as func
from app import create_app


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """Each request is redirected to the WSGI handler."""
    return func.WsgiMiddleware(create_app().wsgi_app).handle(req, context)
