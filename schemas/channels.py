from pydantic import BaseModel


class ChannelRead(BaseModel):
    id: int
    name: str
    description: str | None = None

    class Config:
        orm_mode = True


class ChannelCreate(BaseModel):
    name: str
    description: str | None = None