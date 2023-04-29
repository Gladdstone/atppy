from atppy.utils import xrpc
from atppy.utils.SessionManager import SessionManager


class FeedManager:

  def __init__(self, session: SessionManager):
    self._session = session
    self._client = xrpc(session=session)

  def get_author_feed(self, actor: str):
    res = self._client.get(
      endpoint="app.bsky.feed.getAuthorFeed",
      params={
        "actor": actor
      }
    )
    return res

  def get_likes(self, uri: str):
    res = self._client.get(
      session=self._session,
      endpoint="app.bsky.feed.getLikes",
      params={
        "uri": uri
      }
    )
    return res

  def get_post_thread(self, uri: str):
    res = self._client.get(
      session=self._session,
      endpoint="app.bsky.feed.getPostThread",
      params={
        "uri": uri
      }
    )
    return res
