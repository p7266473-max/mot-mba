import os
import orjson
from typing import List, Dict, Union, Optional
from pydantic import BaseModel, Field

class QuestionModel(BaseModel):
    id: str
    type: str  # mcq, tf, fitb, match, scenario
    question: str
    choices: Optional[List[str]] = None
    answer: Union[int, str, Dict[str, str]]
    scenario: Optional[str] = None
    left_items: Optional[List[str]] = None
    right_items: Optional[List[str]] = None
    explanation: Optional[str] = None

class WeekQuiz(BaseModel):
    week: int
    title: str
    questions: List[QuestionModel]

def load_week_quiz(file_path: str) -> WeekQuiz:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Quiz file not found: {file_path}")
    
    with open(file_path, "rb") as f:
        data = orjson.loads(f.read())
        
    return WeekQuiz(**data)
