from requests import post
from json import dumps


# Імплементація сінгелтона з бібліотеки handy-decorators, котра
# є наразі застарілою
def singleton(cls):
    from functools import wraps
    previous_instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls in previous_instances and\
            previous_instances.get(cls, None).get('args')\
                == (args, kwargs):
            return previous_instances[cls].get('instance')
        else:
            previous_instances[cls] = {
                'args': (args, kwargs),
                'instance': cls(*args, **kwargs)
            }
            return previous_instances[cls].get('instance')
    return wrapper


@singleton
class DropBoxRequest:
    def __init__(self, access_token: str):
        self.access_token = access_token

    def file_upload(self, where_file, file_bytes):
        url = 'https://content.dropboxapi.com/2/files/upload'
        headers = {'Authorization': f'Bearer {self.access_token}',
                   'Dropbox-API-Arg': dumps({'mode': 'add',
                                             'autorename': True,
                                             'mute': False,
                                             'strict_conflict': False,
                                             'path': f'/{where_file}'}),
                   'Content-Type': 'application/octet-stream'}
        return post(url=url, headers=headers, data=file_bytes)

    def file_get_metadata(self, where_file):
        url = 'https://api.dropboxapi.com/2/files/alpha/get_metadata'
        headers = {'Authorization': f'Bearer {self.access_token}',
                   'Content-Type': 'application/json'}
        data = dumps({'path': f'/{where_file}'})
        return post(url=url, headers=headers, data=data)

    def file_delete(self, where_file):
        url = 'https://api.dropboxapi.com/2/files/delete'
        headers = {'Authorization': f'Bearer {self.access_token}',
                   'Content-Type': 'application/json'}
        data = dumps({'path': f'/{where_file}'})
        return post(url, headers=headers, data=data)
