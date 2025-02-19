import threading
from contextlib import contextmanager
from typing import Generator, Optional

from pymongo.asynchronous.client_session import AsyncClientSession

_IS_SYNC = False

_mongo_thread_local_storage = threading.local()

# The async client is not supported, we didn't implemented it yet

@contextmanager
def thread_client_session(session: AsyncClientSession) -> Generator:
    """
    Set the session as the current active session for the thread during the context of this generator.
    """
    _mongo_thread_local_storage.session = session
    try:
        yield session
    finally:
        _mongo_thread_local_storage.session = None


def get_thread_client_session() -> Optional[AsyncClientSession]:
    return getattr(_mongo_thread_local_storage, "session", None)