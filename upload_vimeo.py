# Script to upload video to Vimeo using the API
#
# Follows steps from https://developer.vimeo.com/api/guides/start
# and https://developer.vimeo.com/api/guides/videos/upload
#
# Requires one to register an "app" in vimeo account.
# The app will have a client_id, client_secret, and you need to add a personal access token with upload and edit scopes
# These should be stored in a file called `credentials_vimeo.toml` as such:
#
# client_id = "<your client id>"
# client_secret = "<your client secret>"
# access_token = "<your personal access token>"
#
# This script uses the Vimeo python client, which can be installed with
#
#   pip install PyVimeo
#

import tomllib
import vimeo

with open("credentials_vimeo.toml", "rb") as f:
    secrets = tomllib.load(f)

client = vimeo.VimeoClient(
    token=secrets["access_token"],
    key=secrets["client_id"],
    secret=secrets["client_secret"],
)

file_name = "ems_intro.mp4"
uri = client.upload(
    file_name,
    data={
        "name": "Test upload via API",
        "description": "Trying to upload the EMS intro using the vimeo API",
    },
)

print(f"Your video URI is: {uri}")
