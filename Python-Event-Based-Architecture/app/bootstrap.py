from . import event_functions, events


def initialize():
    events.register_event(
        "user_registered", event_functions.send_email
    )
    events.register_event(
        "user_registered", event_functions.notify_slack_users
    )
    events.register_event(
        "user_registered", event_functions.notify_admin
    )
    events.register_event(
        "user_registered", event_functions.create_log
    )
