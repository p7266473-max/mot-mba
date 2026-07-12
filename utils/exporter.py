import pandas as pd
from io import BytesIO
from typing import Dict, Any

def export_score_to_csv(score_data: Dict[str, Any]) -> bytes:
    """
    Exports detailed score dictionary into CSV bytes format.
    """
    records = []
    for q_id, fb in score_data.get("feedback", {}).items():
        records.append({
            "Question ID": q_id,
            "Is Correct": fb["is_correct"],
            "Correct Answer": str(fb["correct_answer"]),
            "User Answer": str(fb["user_answer"]),
            "Explanation": fb.get("explanation", "")
        })
        
    df = pd.DataFrame(records)
    return df.to_csv(index=False).encode("utf-8")

def export_score_to_excel(score_data: Dict[str, Any]) -> bytes:
    """
    Exports detailed score dictionary into Excel bytes format.
    """
    records = []
    for q_id, fb in score_data.get("feedback", {}).items():
        records.append({
            "Question ID": q_id,
            "Is Correct": fb["is_correct"],
            "Correct Answer": str(fb["correct_answer"]),
            "User Answer": str(fb["user_answer"]),
            "Explanation": fb.get("explanation", "")
        })
        
    df = pd.DataFrame(records)
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Quiz Results", index=False)
    return output.getvalue()
