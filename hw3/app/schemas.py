from pydantic import BaseModel


class ClientFeatures(BaseModel):
    age: int
    income: float
    months_on_book: int
    credit_limit: float
