_labels = {
    'first_name': 'First Name',
    'last_name': 'Last Name',
    'dob': 'Date of Birth (YYYY-MM-DD)',
    'gender': 'Gender (M/F/Other)',
    'phone': 'Phone Number',
    'insurance': 'Insurance (yes/no)',
    'email': 'Email (optional)',
}

_optionals = ['email']


def new_to_old(new_key: str) -> str:
    return _labels[new_key]


def old_to_new(old_key: str) -> str:
    for new_key, value in _labels.items():
        if old_key == value:
            return new_key
    raise ValueError(f'Wrong mapping: {old_key}')


def is_optional(key: str) -> bool:
    return key in _optionals


def ask(value_name: str) -> str:
    label = new_to_old(value_name)
    return input(label + ': ')
