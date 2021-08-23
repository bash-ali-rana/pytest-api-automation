import copy
import json


def update_request_body(original_request, key_str, action, value):
    """
    Args:
        original_request: Request body that needs to be updated.  Can be a json string or dict
        key_str: key path to be updated i.e. 'key/subkey/subsubkey'
        action: action to perform - update or delete
        value: new value for key
    Returns: dict of an updated request body
    """
    updated_request = None
    key_path = ''
    if isinstance(original_request, str):
        updated_request = json.loads(original_request)
    elif isinstance(original_request, dict):
        updated_request = copy.deepcopy(original_request)
    else:
        raise ValueError(f"Unsupported data type {type(original_request)}")
    if key_str is not None:
        key_path = 'updated_request' + key_str
        if action.lower() == 'delete':
            exec(f'del {key_path}')
        elif action.lower() == 'update':
            exec(f'{key_path} = value')
    elif key_str is None and action.lower() == 'update':
        updated_request = value
    return updated_request
