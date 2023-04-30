import requests

class Credentials:

  def __init__(self, username: str, password: str):
    self._username = username
    self._password = password

  def credentials(self):
    return {
      "identifier": self._username,
      "password": self._password
    }


class SessionManager:

  def __init__(self, pds: str, credentials: Credentials) -> None:
    self._pds = pds
    self._credentials = credentials
    self._default_session_headers = {"Content-Type": "application/json"}
    self._session = self.create_session()

  @property
  def pds(self):
    return self._pds

  @property
  def session(self):
    return self._session

  def create_session(self):
    session = requests.Session()
    session.headers = self._default_session_headers

    try:
      res = session.post(
        url=f"{self._pds}/xrpc/com.atproto.server.createSession",
        json=self._credentials.credentials()
      )
      response = res.json()

      session.headers.update(
        {"Authorization": f"Bearer {response.get('accessJwt')}"}
      )

      return session
    except Exception as err:
      raise err
