import os
import orjson
from typing import List, Dict, Any, Optional, Union
from pydantic import BaseModel

class QuestionModel(BaseModel):
    id: str
    type: str  # mcq, tf, fill, match, scenario
    question: str
    choices: Optional[List[str]] = None
    answer: Union[int, bool, str, Dict[str, str]]
    scenario: Optional[str] = None
    left: Optional[List[str]] = None
    right: Optional[List[str]] = None
    explanation: Optional[str] = None

def load_category_file(file_path: str) -> List[QuestionModel]:
    if not os.path.exists(file_path):
        return []
    with open(file_path, "rb") as f:
        content = f.read()
        if not content.strip():
            return []
        data = orjson.loads(content)
        if isinstance(data, list):
            return [QuestionModel(**item) for item in data]
        return []

def load_week_questions(base_dir: str, week_num: int) -> List[QuestionModel]:
    week_str = f"week{week_num:02d}"
    week_dir = os.path.join(base_dir, "data", week_str)
    
    questions = []
    categories = ["mcq.json", "tf.json", "fill.json", "match.json", "scenario.json"]
    
    for cat in categories:
        cat_path = os.path.join(week_dir, cat)
        if os.path.exists(cat_path):
            questions.extend(load_category_file(cat_path))
            
    return questions
