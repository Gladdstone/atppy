from atppy.lib.Repo.StrongRef import StrongRef
from atppy.utils import xrpc
from atppy.utils.SessionManager import SessionManager


class Admin:

  def __init__(self, session: SessionManager):
    self._session = session
    self._client = xrpc(session=session)

  def disable_invite_codes(self, codes: list, accounts: list):
    res = self._client.post(
      endpoint="com.atproto.admin.disableInviteCodes",
      params={
        "codes": codes,
        "accounts": accounts
      }
    )
    return res

  def get_invite_codes(self, sort="recent", limit=50, cursor=None):
    res = self._client.get(
      endpoint="com.atproto.admin.getInviteCodes",
      params={
        "sort": sort,
        "limit": limit,
        "cursor": cursor
      }
    )
    return res

  def get_moderation_action(self, id: int):
    res = self._client.get(
      endpoint="com.atproto.admin.getModerationAction",
      params={
        "id": id
      }
    )
    return res

  def get_moderation_actions(self, subject: str, limit=50, cursor=None):
    res = self._client.get(
      endpoint="com.atproto.admin.getModerationActions",
      params={
        "id": id
      }
    )
    return res

  def get_moderation_report(self, id: int):
    res = self._client.get(
      endpoint="com.atproto.admin.getModerationReport",
      params={
        "id": id
      }
    )
    return res

  def get_moderation_reports(self, subject: str, resolved: bool, limit=50, cursor=None):
    res = self._client.get(
      endpoint="com.atproto.admin.getModerationReports",
      params={
        "subject": subject,
        "resolved": resolved,
        "limit": limit,
        "cursor": cursor
      }
    )
    return res

  def get_record(self, uri: str):
    res = self._client.get(
      endpoint="com.atproto.admin.getRecord",
      params={
        "uri": uri
      }
    )
    return res

  def get_repo(self, did: str):
    res = self._client.get(
      endpoint="com.atproto.admin.getRepo",
      params={
        "did": did
      }
    )
    return res

  def resolve_moderation_reports(self, actionId: int, reportIds: list, createdBy: str):
    res = self._client.post(
      endpoint="com.atproto.admin.resolveModerationReports",
      params={
        "actionId": actionId,
        "reportIds": reportIds,
        "createdBy": createdBy
      }
    )
    return res

  def reverse_moderation_action(self, id: int, reason: str, createdBy: str):
    res = self._client.post(
      endpoint="com.atproto.admin.reverseModerationAction",
      params={
        "id": id,
        "reason": reason,
        "createdBy": createdBy
      }
    )
    return res

  def search_repos(self, term: str, invitedBy: str, limit=50, cursor=None):
    res = self._client.get(
      endpoint="com.atproto.admin.searchRepos",
      params={
        "term": term,
        "invitedBy": invitedBy,
        "limit": limit,
        "cursor": cursor
      }
    )
    return res

  def take_moderation_action(self, action: str, did: str, strong_ref: StrongRef, reason: str, createdBy: str):
    res = self._client.post(
      endpoint="com.atproto.admin.takeModerationAction",
      params={
        "action": action,
        "subject": [
          did,
          strong_ref.ref
        ],
        "reason": reason,
        "createdBy": createdBy
      }
    )
    return res

  def update_account_email(self, account: str, email: str):
    res = self._client.post(
      endpoint="com.atproto.admin.updateAccountEmail",
      params={
        "account": account,
        "email": email
      }
    )
    return res

  def update_account_handle(self, did: str, handle: str):
    res = self._client.post(
      endpoint="com.atproto.admin.updateAccountHandle",
      params={
        "did": did,
        "handle": handle
      }
    )
    return res
