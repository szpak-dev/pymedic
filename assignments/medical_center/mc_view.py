from datetime import datetime

_labels = {
    'first_name': 'First Name',
    'last_name': 'Last Name',
    'dob': 'Date of Birth (YYYY-MM-DD)',
    'gender': 'Gender (M/F/Other)',
    'phone': 'Phone Number',
    'insurance': 'Insurance (yes/no)',
    'email': 'Email (optional)',
}


# Validate functions

def _is_valid_name(name: str) -> bool:
    return not any(char.isdigit() for char in name) and len(name) > 1

def _is_valid_dob(dob: str) -> bool:
    format = "%Y-%m-%d"
    try:
        return bool(datetime.strptime(dob, format))
    except ValueError:
        return False
    
def _is_valid_gender(gender: str) -> bool:
    return gender.lower() == 'm' or gender.lower() == 'f' or gender.lower() == 'other'

def _is_valid_email(email: str) -> bool:
    return '@' in email

def _is_valid_phone(phone: str) -> bool:
    return phone.isdigit() and len(phone) == 9

def _is_valid_insurance(insurance: str) -> bool:
    return True if insurance == True or insurance == False else False

# Assertions

def _assert_valid_name(name: str):
    assert _is_valid_name(name), 'Invalid name'

def _assert_valid_dob(dob: str):
    assert _is_valid_dob(dob), 'Invalid date format'

def _assert_valid_gender(gender: str):
    assert _is_valid_gender(gender), 'Invalid gender format'

def _assert_valid_email(email: str):
    assert _is_valid_email(email), 'Invalid email'

def _assert_valid_phone(phone: str):
    assert _is_valid_phone(phone), 'Invalid phone number.'

def _assert_valid_insurance(insurance: bool):
    assert _is_valid_insurance(insurance), 'Invalid insurance status.'

# Dictionary of validators

_validators = {
    'first_name': _assert_valid_name,
    'last_name': _assert_valid_name,
    'dob': _assert_valid_dob,
    'gender': _assert_valid_gender,
    'email': _assert_valid_email,
    'phone': _assert_valid_phone,
    'insurance': _assert_valid_insurance,
}


_optionals = ['email']


def validate(key: str, value: str) -> bool:
    try:
        return _validators[key](value)
    except KeyError:
        return True


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
