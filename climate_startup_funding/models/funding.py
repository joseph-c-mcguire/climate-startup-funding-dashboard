from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class Company(BaseModel):
    name: str
    description: Optional[str]
    founded_date: Optional[datetime]
    website: Optional[str]
    sector: Optional[str]

class FundingRound(BaseModel):
    company: Company
    amount: float
    currency: str
    date: datetime
    round_type: str
    investors: List[str]
    source: str
