import requests
import traceback


class AppError(Exception):

    def __init__(self, msg, details):
        self.msg = msg
        self.details = details


def get_json(path, **kwargs):
    err_msg = 'Impossible to communicate with Ryanair backend'

    try:
        r = requests.get(path, **kwargs)

    except Exception:
        raise AppError(err_msg, traceback.format_exc())

    if not r.ok:
        msg = (
            'Requested URL:%s\n'
            'Params: %s\n'
            'Backend responded with status %s\n'
            'and contents: %s\n'
        ) % (path, kwargs, r.status_code, r.text)

        raise AppError(err_msg, msg)

    return r.json()
