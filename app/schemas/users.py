from typing import List, Optional
from pydantic import BaseModel

from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int] = None
    username: str
    role: str

    class Config:
        orm_mode = True