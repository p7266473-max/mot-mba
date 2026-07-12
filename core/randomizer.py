import random
from typing import List
from core.loader import QuestionModel

def randomize_questions(questions: List[QuestionModel]) -> List[QuestionModel]:
    shuffled = list(questions)
    random.shuffle(shuffled)
    return shuffled
