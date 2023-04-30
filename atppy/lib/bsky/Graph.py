from atppy.utils import xrpc
from atppy.utils.SessionManager import SessionManager


class Graph:

  def __init__(self, session: SessionManager):
    self._session = session
    self._client = xrpc(session=session)

  def get_followers(self, actor: str, limit=50, cursor=None):
    res = self._client.get(
      endpoint="app.bsky.graph.getFollowers",
      params={
        "actor": actor,
        "limit": limit,
        "cursor": cursor
      }
    )
    return res

  def get_follows(self, actor: str, limit=50, cursor=None):
    res = self._client.get(
      endpoint="app.bsky.graph.getFollows",
      params={
        "actor": actor,
        "limit": limit,
        "cursor": cursor
      }
    )
    return res

  def get_mutes(self, limit=50, cursor=None):
    res = self._client.get(
      endpoint="app.bsky.graph.getMutes",
      params={
        "limit": limit,
        "cursor": cursor
      }
    )
    return res

  def mute_actor(self, actor: str):
    res = self._client.get(
      endpoint="app.bsky.graph.muteActor",
      params={
        "actor": actor
      }
    )
    return res

  def unmute_actor(self, actor: str):
    res = self._client.get(
      endpoint="app.bsky.graph.unmuteActor",
      params={
        "actor": actor
      }
    )
    return res
