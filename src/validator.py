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
    if len(user['first_name']) <= 4:
        errors['first_name'] = "First name must be greater than 4 characters"
    if not user['last_name']:
        errors['last_name'] = "Can't be blank"
    if not user['email']:
        errors['email'] = "Can't be blank"
    return errors


def validate_school(school):
    errors = {}
    if not school['name']:
        errors['name'] = "Can't be blank"
    return errors


def validate_post(post):
    errors = {}
    if not post.get('title'):
        errors['title'] = "Can't be blank"
    if not post.get('body'):
        errors['body'] = "Can't be blank"
    return errors