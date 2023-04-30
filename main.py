import atppy

username="disastrousgamemaster@gmail.com"
password="svzw-3bbt-bunt-psbz"
pds = "https://bsky.social"
handle = "joefarrell.bsky.social"
nsid = "com.bsky.social"

credentials = atppy.Credentials(username, password)

session = atppy.SessionManager(pds, credentials)

# bsky = atppy.bsky.Actor(session)
# res = bsky.get_profile(handle)

# ref = atppy.Repo.StrongRef("https://bsky.app/profile/joefarrell.bsky.social", "3jukjlnbx6r2m")

bsky = atppy.bsky.Graph(session)
res = bsky.get_followers(handle, limit=5)

print(res.text)