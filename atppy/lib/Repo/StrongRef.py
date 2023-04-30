class StrongRef:
  def __init__(self, uri: str, cid: str):
    self._uri = uri
    self._cid =cid

  @property
  def uri(self):
    return self._uri

  @property
  def cid(self):
    return self._cid
