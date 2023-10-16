from sentry_sdk import set_tag, capture_exception


def send_to_sentry(tag1, tag2, exception):
    """ method to send report to Sentry when exception captured """

    set_tag(tag1, tag2)
    capture_exception(exception)
