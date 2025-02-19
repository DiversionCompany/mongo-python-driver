from __future__ import annotations

import threading
from contextlib import contextmanager
from typing import Generator, Optional

from pymongo.synchronous.client_session import ClientSession

_IS_SYNC = True

_mongo_thread_local_storage = threading.local()

# The async client is not supported, we didn't implemented it yet


@contextmanager
def thread_client_session(session: ClientSession) -> Generator:
    """
    Set the session as the current active session for the thread during the context of this generator.
    """
    _mongo_thread_local_storage.session = session
    try:
        yield session
    finally:
        _mongo_thread_local_storage.session = None


def get_thread_client_session() -> Optional[ClientSession]:
    return getattr(_mongo_thread_local_storage, "session", None)
