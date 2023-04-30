# attpy - AT Protocol Python Client

## Installation
```
pip install atppy
```

## Usage

```
import atppy

username = "username"
password = "password"
pds = "https://bsky.social"
handle = "joefarrell.bsky.social"
nsid = "com.bsky.social"

credentials = atppy.Credentials(username, password)

session = atppy.SessionManager(pds, credentials)

bsky = atppy.bsky.Actor(session)
res = bsky.get_profile(handle)
```