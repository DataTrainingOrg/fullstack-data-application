from pydantic import BaseModel
from typing import List


class IrisPredict(BaseModel):
    data: List[float]

class IrisTrain(BaseModel):
    data: List[List[float]]
    targets: List[float]