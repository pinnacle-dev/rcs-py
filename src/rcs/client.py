import httpx
import mimetypes

import os
from .base_client import PinnacleBase, AsyncPinnacleBase
from .utils import parse_inbound


class Pinnacle(PinnacleBase):
    pass


class AsyncPinnacle(AsyncPinnacleBase):
    pass
