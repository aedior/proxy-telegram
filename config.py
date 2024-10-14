PORT = 6484

USERS = {
    "tg":  "abcd1234abcd1234abcd1234abcd1234",
}

MODES = {
    # Classic mode, easy to detect
    "classic": True,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": True,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "www.telewebion.com"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "197a18bc6092fa9cda508fbba1a2211d"
