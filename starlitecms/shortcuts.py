from importlib import import_module
from typing import Any, Dict

from starlette.requests import Request

from starlitecms import templates


def render(
    request: Request,
    template_name: str,
    context: Dict[str, Any] | None = None,
    status: int = 200,
):
    if context is None:
        context = {}
    return templates.TemplateResponse(
        request,
        name=template_name,
        context=context,
        status_code=status,
    )


def include(module: str):
    """Include list of routes from application module
    For example: include('home.routes') this import routes
    list from app 'home' from routes.py

    :param module: route module (or module name), eg 'home.routes'
    """
    _temp = import_module(module)
    routes = getattr(_temp, "routes")
    return routes
