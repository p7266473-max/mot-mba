import random
from typing import List
from core.loader import QuestionModel

def get_random_sample(questions: List[QuestionModel], sample_size: int = 15) -> List[QuestionModel]:
    """
    Shuffles and samples a set number of questions (default 15) from the total pool.
    """
    if len(questions) <= sample_size:
        shuffled = list(questions)
        random.shuffle(shuffled)
        return shuffled
    return random.sample(questions, sample_size)
