from requests import Session

from atppy.utils.SessionManager import SessionManager


class xrpc:

  pds: str = ""
  default_headers = {"Content-Type": "application/json"}

  def __init__(self, session: SessionManager):
    self.pds = session.pds
    self._session = session.session


  def get(self, endpoint: str, params=None):
    try:
      res = self._session.get(
        url=f"{self.pds}/xrpc/{endpoint}",
        params=params
      )

      return res
    except Exception as err:
      raise err

  def put(self, endpoint: str, body={}):
    try:
      res = self._session.put(
        url=f"{self.pds}/xrpc/{endpoint}",
        data=body
      )

      return res
    except Exception as err:
      raise err

  def post(self, endpoint: str, body={}):
    try:
      res = self._session.post(
        url=f"{self.pds}/xrpc/{endpoint}",
        data=body
      )

      return res
    except Exception as err:
      raise err
