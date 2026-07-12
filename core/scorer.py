from typing import List, Dict, Any, Union
from core.loader import QuestionModel

def calculate_score(questions: List[QuestionModel], user_answers: Dict[str, Any]) -> Dict[str, Any]:
    correct_count = 0
    total = len(questions)
    detailed_feedback = {}
    
    for idx, q in enumerate(questions):
        ans = user_answers.get(q.id)
        is_correct = False
        
        if q.type in ["mcq", "tf", "scenario"]:
            # ans should be choice index (int) or string matching choices
            if ans is not None:
                try:
                    if isinstance(ans, int):
                        is_correct = (ans == q.answer)
                    elif isinstance(q.answer, int) and q.choices:
                        is_correct = (ans == q.choices[q.answer])
                except (ValueError, IndexError):
                    pass
        elif q.type == "fitb":
            if ans and isinstance(ans, str) and isinstance(q.answer, str):
                is_correct = (ans.strip().lower() == q.answer.strip().lower())
        elif q.type == "match":
            # ans should be a Dict[left_item, selected_right_item]
            if ans and isinstance(ans, dict) and isinstance(q.answer, dict):
                # match all
                is_correct = True
                for left, right in q.answer.items():
                    if ans.get(left) != right:
                        is_correct = False
                        break
                        
        if is_correct:
            correct_count += 1
            
        detailed_feedback[q.id] = {
            "is_correct": is_correct,
            "correct_answer": q.answer,
            "user_answer": ans,
            "explanation": q.explanation
        }
        
    score_pct = (correct_count / total) * 100 if total > 0 else 0
    
    return {
        "score": correct_count,
        "total": total,
        "percentage": score_pct,
        "feedback": detailed_feedback
    }
