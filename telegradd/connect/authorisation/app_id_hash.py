import random
from dataclasses import dataclass
from typing import Optional

class APP_INFO:
    def __init__(self, app: list):
        self.app = app
        self.data = random.choice (app)

    @property
    def app_hash(self):
        app_hash = self.data[1]
        return app_hash

    @property
    def app_id(self):
        app_id = int (self.data[0])
        return app_id


class Apps:
    app_data = 

    def __init__(self) -> None:
        pass
    @property
    def app_info(self):
        app = APP_INFO(Apps().app_data)
        return app.app_id, app.app_hash



