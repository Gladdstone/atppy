# attpy - AT Protocol Python Client

## Installation

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

bsky = atppy.Bsky(session)
res = bsky.get_author_feed(handle)
```