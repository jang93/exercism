def handle_error_by_throwing_exception():
    raise Exception("Error")


def handle_error_by_returning_none(input_data):
    return 1 if input_data == '1' else None


def handle_error_by_returning_tuple(input_data):
    return (True, 1) if input_data == '1' else (False, None)


def filelike_objects_are_closed_on_exception(filelike_object):
    with filelike_object as f:
        f.do_something()
