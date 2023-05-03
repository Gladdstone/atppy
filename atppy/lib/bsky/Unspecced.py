from atppy.utils import xrpc
from atppy.utils.SessionManager import SessionManager

class Unspecced:

  def __init__(self, session: SessionManager):
    self._session = session
    self._client = xrpc(session=session)

  def get_popular(self, includeNsfw=False, limit=50, cursor=None):
    res = self._client.get(
      endpoint="app.bsky.feed.getPopular",
      params={
        "includeNsfw": includeNsfw,
        "limit": limit,
        "cursor": cursor
      }
    )
    return res
