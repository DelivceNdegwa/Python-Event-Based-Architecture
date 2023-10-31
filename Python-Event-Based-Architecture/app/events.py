"""
- We will define our events here.
- An event will have a list of functions that can be called when invoked
- We will have a function to register an event
- We will have another one to call the functions related to an event
"""

events = dict()


def register_event(event_name: str, event_func: callable):
    if events.get(event_name) is None:
        events[event_name] = []
    events[event_name].append(event_func)


def dispatch(event_name: str, *args, **kwargs):
    event_functions = events.get(event_name)
    if event_functions is None:
        raise ValueError(f"Event {event_name} was not found")

    for event_function in event_functions:
        event_function(*args, **kwargs)
