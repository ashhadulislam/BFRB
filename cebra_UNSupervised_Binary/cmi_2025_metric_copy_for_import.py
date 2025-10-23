import pandas as pd
from sklearn.metrics import f1_score


class ParticipantVisibleError(Exception):
    pass


class CompetitionMetric:
    """Binary F1 for the CMI 2025 binary task."""
    def __init__(self):
        pass

    def calculate_binary_f1(self, sol: pd.DataFrame, sub: pd.DataFrame) -> float:
        y_true = sol["gesture_binary"]
        y_pred = sub["gesture_binary"]
        return f1_score(y_true, y_pred, average='binary', zero_division=0)


def score(solution: pd.DataFrame, submission: pd.DataFrame, row_id_column_name: str) -> float:
    # Validate columns
    for col in (row_id_column_name, 'gesture_binary'):
        if col not in solution.columns:
            raise ParticipantVisibleError(f"Solution file missing required column: '{col}'")
        if col not in submission.columns:
            raise ParticipantVisibleError(f"Submission file missing required column: '{col}'")

    # Align rows
    solution = solution.set_index(row_id_column_name).sort_index()
    submission = submission.set_index(row_id_column_name).sort_index()

    if not solution.index.equals(submission.index):
        raise ParticipantVisibleError("Row IDs in submission do not match those in the solution.")

    # Compute binary F1
    metric = CompetitionMetric()
    return metric.calculate_binary_f1(solution, submission)