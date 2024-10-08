from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4
from typing_extensions import Annotated


class User(BaseModel):
    username: str
    password: str
