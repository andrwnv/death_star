from pydantic import BaseModel


class SendTeamDto(BaseModel):
    team_name: str
    location: str
