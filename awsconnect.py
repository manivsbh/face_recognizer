from boxsdk import Client, OAuth2

oauth = OAuth2(
    client_id='39c4cpu81b79w6ukvqegv1luzrgb9r0y',
    client_secret='GkjxNYvA7T5DpYmAkTxr8IHoT1bZIavM',
    access_token='ACCESS_TOKEN',
    refresh_token='REFRESH_TOKEN',
)

client = Client(oauth)
user = client.user().get()