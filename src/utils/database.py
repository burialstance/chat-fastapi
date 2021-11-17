import os
from pathlib import Path
from typing import List

from src.conf.settings import settings
import logging


def fetch_apps_models(folder='apps', installed_apps: List[str] = None) -> List:
    """
    :param folder: apps folder
    :param installed_apps: if provided, autodiscover models only in
    :return: list all apps models
    """
    apps_folders = settings.BASE_DIR.joinpath(folder)

    if not apps_folders.exists():
        raise Exception(f'default apps path: {apps_folders.as_uri()} not found')

    models = []

    apps = [i for i in apps_folders.iterdir() if i.is_dir()]
    for app_name in apps:
        if installed_apps and app_name.name not in installed_apps:
            continue
        app_models_folder = app_name.joinpath('models')

        if app_models_folder.exists():
            app_models = ([
                i.name.removesuffix(i.suffix) for i in app_models_folder.iterdir()
                if all([i.is_file(), not i.name.startswith('__')])
            ])
            for model in app_models:
                models.append(
                    '.'.join([
                        settings.BASE_DIR.name,
                        apps_folders.name,
                        app_name.name,
                        'models',
                        model
                    ])
                )
    logging.debug(f'autodiscover models: {models}')
    return models
