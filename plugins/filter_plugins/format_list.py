#!/user/bin/python3

from ansible import errors, parsing

def format_list(_list, pattern, prefix=False):
    """ A filter plugin that transforms elements in a list.
        _list: list             list of strings to be transformed
        pattern: string         string pattern to add to each element in list
        prefix: bool            adds pattern to beginning of element.
                                Default (False): adds pattern to end of element
        returns: list
    """

    # Type checking
    # Check if _list is list
    if type(_list) not in [list, tuple, set]:
        raise errors.AnsibleFilterError(
            'format_list: invalid argument passed in as _list (arg0).'
            'Expected: list, tuple, set. Received: {}'.format(type(_list)))

    # Check if pattern is a string
    if type(pattern) not in [str, parsing.yaml.objects.AnsibleUnicode]:
        raise errors.AnsibleFilterError(
            'format_list: invalid argument passed in as pattern (arg1).'
            'Expected: str. Received: {}'.format(type(pattern)))

    new_list = []
    for element in _list:
        # Check each element in list is valid
        if type(element) not in [str, parsing.yaml.objects.AnsibleUnicode]:
            raise errors.AnsibleFilterError(
                'format_list: invalid argument passed in as _list (arg0).'
                'Expected: list[str], tuple[str], set[str].'
                'Received: [{}]'.format(type(element)))

        if prefix:
            new_list.append("".join([pattern, element]))
        else:
            new_list.append("".join([element, pattern]))

    return new_list

class FilterModule(object):
    def filters(self):
        return {
          'format_list': format_list
        }
