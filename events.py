"""
This is the event module and supports all the REST actions for the
Event collection
"""

from datetime import datetime
from flask import make_response, abort

# Helper function 
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
EVENT = {
    "event1": {
        "eventtype": "type-1",
        "uuid": "event1",
        # "timestamp": get_timestamp(),
    },
    "event2": {
        "eventtype": "type-2",
        "uuid": "event2",
        # "timestamp": get_timestamp(),
    },
    "event3": {
        "eventtype": "type-3",
        "uuid": "event3",
        # "timestamp": get_timestamp(),
    },
}

def create(event):
    uuid = event["uuid"]
    eventtype = event["eventtype"]

    if uuid not in EVENT and uuid is not None:
        EVENT[uuid] = {
            "uuid": uuid,
            "eventtype": eventtype,
            # "timestamp": get_timestamp(),
        }
        return make_response(
            "{uuid} successfully created".format(uuid=uuid), 201
        )

    else:
        abort(
            406,
            "Event with uuid {uuid} already exists".format(uuid=uuid),
        )


