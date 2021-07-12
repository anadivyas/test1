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
        "timestamp": get_timestamp(),
    },
    "event2": {
        "eventtype": "type-2",
        "uuid": "event2",
        "timestamp": get_timestamp(),
    },
    "event3": {
        "eventtype": "type-3",
        "uuid": "event3",
        "timestamp": get_timestamp(),
    },
}


def read_all():
    """
    This function responds to a request for /api/event
    with the complete lists of event
    :return:        json string of list of event
    """
    # Create the list of event from our data
    return [EVENT[key] for key in sorted(EVENT.keys())]


def read_one(uuid):
    
    #This function responds to a request for /api/event/{uuid}
    if uuid in EVENT:
        event = EVENT.get(uuid)

    else:
        abort(
            404, "Event with uuid {uuid} not found".format(uuid=uuid)
        )

    return event


def create(event):
    uuid = event["uuid"]
    eventtype = event["eventtype"]

    if uuid not in EVENT and uuid is not None:
        EVENT[uuid] = {
            "uuid": uuid,
            "eventtype": eventtype,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{uuid} successfully created".format(uuid=uuid), 201
        )

    else:
        abort(
            406,
            "Event with uuid {uuid} already exists".format(uuid=uuid),
        )


