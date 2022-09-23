#
# Copyright (c) 2014 NSONE, Inc.
#
# License under The MIT License (MIT). See LICENSE in project root.
#

import logging
from ns1 import NS1, Config

# to enable verbose logging, set 'verbosity' in the config and use
# the standard python logging system

config = Config()
config.createFromAPIKey("<<CLEARTEXT API KEY>>")
config["verbosity"] = 5
logging.basicConfig(level=logging.DEBUG)
print(config)
api = NS1(config=config)

# now all requests will show up in the logging system

# exception handling:
# the follow exceptions may be thrown
# from ns1.rest.errors import ResourceException, \
#     RateLimitException, AuthException

# ResourceException is the base exception (Auth and RateLimit extend it)
# it (and therefore they) have the properties message, response, body

# AuthException is raised when apikey is incorrect or the key doesn't
# have permission to the requested resource

# RateLimitException is raised when rate limit is exceed
# you can access the properties by, limit, and period to calculate backoff

# ResourceException is raised in any other exception situation
