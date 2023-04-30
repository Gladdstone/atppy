from datetime import datetime

from atppy.utils import xrpc
from atppy.utils.SessionManager import SessionManager


class Notification:

  def __init__(self, session: SessionManager):
    self._session = session
    self._client = xrpc(session=session)

  def get_unread_count(self, seenAt: str):
    res = self._client.get(
      endpoint="app.bsky.graph.getFollowers",
      params={
        "seenAt": seenAt
      }
    )
    return res

  def list_notifications(self, seenAt=None, limit=50, cursor=None):
    res = self._client.get(
      endpoint="app.bsky.graph.listNotifications",
      params={
        "seenAt": seenAt,
        "limit": limit,
        "cursor": cursor
      }
    )
    return res

  def update_seen(self, seenAt=None):
    if seenAt is None:
      seenAt = datetime.now()
    res = self._client.post(
      endpoint="app.bsky.notification.updateSeen",
      data={
        "seenAt": seenAt
      }
    )
    return res
