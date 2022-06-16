import asyncio
import logging

logger = logging.getLogger(__name__)


class EventHandler:
    def __init__(self):
        self.listeners = {}

    def event(self, event: str = None):
        def decorator(func):
            self.add_listener(func, event)
        return decorator

    def add_listener(self, listener, event: str = None):
        try:
            self.listeners
        except AttributeError:
            self.listeners = {}

        if not asyncio.iscoroutinefunction(listener):
            raise TypeError("Listener must be a coroutine")
        if event is None:
            event = listener.__name__
            if not event.startswith("on_"):
                raise ValueError(
                    "Listener function name must start with 'on_' if no event is specified in decorator")
        if not event.startswith("on_"):
            event = "on_" + event
        if self.listeners.get(event) is None:
            self.listeners[event] = []
        self.listeners[event].append(listener)
        logger.debug("Added listener for event '{}'".format(event))

    def dispatch(self, event: str, *args, **kwargs):
        try:
            self.listeners
        except AttributeError:
            self.listeners = {}

        logger.debug("Dispatching event '{}'".format(event))
        if not event.startswith("on_"):
            event = "on_" + event
        if self.listeners.get(event) is None:
            return
        for listener in self.listeners[event]:
            asyncio.ensure_future(listener(*args, **kwargs))
