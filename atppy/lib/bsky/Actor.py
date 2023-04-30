from atppy.utils import xrpc
from atppy.utils.SessionManager import SessionManager


class Actor:

  def __init__(self, session: SessionManager):
    self._session = session
    self._client = xrpc(session=session)

  def get_profile(self, actor: str):
    res = self._client.get(
      endpoint="app.bsky.actor.getProfile",
      params={
        "actor": actor
      }
    )
    return res

  def get_profiles(self, actors: str):
    actors_list = ','.join(actors)
    res = self._client.get(
      endpoint="app.bsky.actor.getProfiles",
      params={
        "actor": actors_list
      }
    )
    return res

  def get_suggestions(self, limit: int, cursor: int):
    res = self._client.get(
      endpoint="app.bsky.actor.getSuggestions",
      params={
        "limit": limit,
        "cursor": cursor
      }
    )
    return res

  def search_actors(self, term: str, limit: int, cursor: int):
    res = self._client.get(
      endpoint="app.bsky.actor.searchActors",
      params={
        "term": term,
        "limit": limit,
        "cursor": cursor
      }
    )
    return res

  def search_actors_typeahead(self, term: str, limit: int):
    res = self._client.get(
      endpoint="app.bsky.actor.searchActorsTypeahead",
      params={
        "term": term,
        "limit": limit
      }
    )
    return res
