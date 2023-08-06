from importlib import import_module
from re import A
from starlette.templating import Jinja2Templates

from starlitecms.typings import Application


def load_config():
    _temp = import_module("app.settings")
    return _temp


def load_templates(config, installed_apps: list[Application]):
    result = [
        app.templates_dir for app in installed_apps if app.templates_dir is not None
    ]
    result.append(config.TEMPLATES_DIR)
    return result


def load_apps(config):
    installed_apps = getattr(config, "APPS")
    # - templates
    # - context processors
    # - other

    result = []
    for app_name in installed_apps:
        templates_dir = config.BASE_DIR / app_name / "templates"
        _application = Application(
            name=app_name, templates_dir=templates_dir if templates_dir.is_dir() else None
        )

        result.append(_application)
    return result


def load_middlewares():
    middlewares_list = []
    return middlewares_list


config = load_config()
installed_apps = load_apps(config)

templates = Jinja2Templates(
    directory=load_templates(config, installed_apps),
    auto_reload=True,
)


middlewares = load_middlewares()
