from atppy.utils import xrpc
from atppy.utils.SessionManager import SessionManager


class Feed:

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
      endpoint="app.bsky.feed.getLikes",
      params={
        "uri": uri
      }
    )
    return res

  def get_post_thread(self, uri: str):
    res = self._client.get(
      endpoint="app.bsky.feed.getPostThread",
      params={
        "uri": uri
      }
    )
    return res

  def get_posts(self, uris: list):
    uris_list = ','.join(uris)
    res = self._client.get(
      endpoint="app.bsky.feed.getPosts",
      params={
        "uris": uris_list
      }
    )
    return res

  def get_reposted_by(self, uri: str):
    res = self._client.get(
      endpoint="app.bsky.feed.getRepostedBy",
      params={
        "uris": uri
      }
    )
    return res

  def get_timeline(self, limit: int, cursor: str):
    res = self._client.get(
      endpoint="app.bsky.feed.getRepostedBy",
      params={
        "limit": limit,
        "cursor": cursor
      }
    )
    return res

  def like(self, subject: str, createdAt: str):
    res = self._client.post(
      endpoint="app.bsky.feed.like",
      params={
        "subject": subject,
        "createdAt": createdAt
      }
    )
    return res

  def post(self, text: str, createdAt: str):
    res = self._client.post(
      endpoint="app.bsky.feed.post",
      params={
        "text": text,
        "createdAt": createdAt
      }
    )
    return res

  def repost(self, subject: str, createdAt: str):
    res = self._client.post(
      endpoint="app.bsky.feed.repost",
      params={
        "subject": subject,
        "createdAt": createdAt
      }
    )
    return res
