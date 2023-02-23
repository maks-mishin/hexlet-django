def validate_course(course):
    errors = {}
    if not course['title']:
        errors['title'] = "Can't be blank"
    if not course['paid']:
        errors['paid'] = "Can't be blank"
    return errors


def validate_user(user):
    errors = {}
    if not user['first_name']:
        errors['first_name'] = "Can't be blank"
    if not user['last_name']:
        errors['last_name'] = "Can't be blank"
    if not user['email']:
        errors['email'] = "Can't be blank"
    return errors
