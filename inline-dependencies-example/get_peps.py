#!/usr/bin/env uv run -S

# /// script
# requires-python = "~=3.13"
# dependencies = [
#   "requests<3",
#   "rich",
#   "structlog",
# ]
# ///

import requests
from rich.pretty import pprint
import structlog

log = structlog.get_logger()

resp = requests.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])

log.info("Done!", count=len(data))
