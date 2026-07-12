from typing import Any, Union, Dict
from core.loader import QuestionModel

def score(question: QuestionModel, response: Any) -> bool:
    """
    Evaluates whether the user response is correct for the given question.
    Checks the question type automatically.
    """
    if response is None:
        return False

    q_type = question.type
    correct_ans = question.answer

    if q_type == "mcq" or q_type == "scenario":
        if isinstance(response, int):
            return response == correct_ans
        elif isinstance(correct_ans, int) and question.choices:
            try:
                return response == question.choices[correct_ans]
            except IndexError:
                return False
        return str(response).strip().lower() == str(correct_ans).strip().lower()

    elif q_type == "tf":
        if isinstance(response, bool):
            return response == correct_ans
        # String comparison as fallback
        resp_str = str(response).strip().lower()
        correct_str = str(correct_ans).strip().lower()
        return resp_str == correct_str

    elif q_type == "fill":
        if isinstance(response, str) and isinstance(correct_ans, str):
            return response.strip().lower() == correct_ans.strip().lower()
        return str(response).strip().lower() == str(correct_ans).strip().lower()

    elif q_type == "match":
        if isinstance(response, dict) and isinstance(correct_ans, dict):
            # All pairings must match exactly
            for left_item, right_item in correct_ans.items():
                if response.get(left_item) != right_item:
                    return False
            return True
        return False

    return False
