from atppy.utils import xrpc
from atppy.utils.SessionManager import SessionManager


class RecordsManager:

  def __init__(self, session: SessionManager):
    self._session = session
    self._client = xrpc(session=session)

  def list_records(self, repo: str, collection: str):
    res = self._client.get(
      endpoint="com.atproto.repo.listRecords",
      params={
        "repo": repo,
        "collection": collection
      }
    )
    return res

  def get_record(self, repo: str, collection: str, rkey: str):
    res = self._client.get(
      endpoint="com.atproto.repo.getRecord",
      params={
        "repo": repo,
        "collection": collection,
        "rkey": rkey
      }
    )
    return res

  def create_record(self, repo: str, collection: str, record: any):
    res = self._client.post(
      endpoint="com.atproto.repo.createRecord",
      data={
        "repo": repo,
        "collection": collection,
        "record": record
      }
    )
    return res

  def put_record(self, repo: str, collection: str, rkey: str, record: str):
    res = self._client.post(
      endpoint="com.atproto.repo.putRecord",
      data={
        "repo": repo,
        "collection": collection,
        "rkey": rkey,
        "record": record
      }
    )
    return res

  def delete_record(self, repo: str, collection: str, rkey: str):
    res = self._client.post(
      endpoint="com.atproto.repo.deleteRecord",
      data={
        "repo": repo,
        "collection": collection,
        "rkey": rkey
      }
    )
    return res

  def describe_repo(self, repo: str):
    res = self._client.get(
      endpoint="com.atproto.repo.describeRepo",
      params={
        "repo": repo
      }
    )
    return res
