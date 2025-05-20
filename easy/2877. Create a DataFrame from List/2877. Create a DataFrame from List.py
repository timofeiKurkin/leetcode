from typing import List

import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    pd_data = {"student_id": [], "age": []}

    for data in student_data:
        pd_data["student_id"].append(data[0])
        pd_data["age"].append(data[1])

    return pd.DataFrame(pd_data)
