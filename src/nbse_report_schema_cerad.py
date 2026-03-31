from pydantic import BaseModel, Field
from datetime import date
from typing import Any, Dict, List, Union

class Report(BaseModel):
    # Patient Information
    vac: Union[int, None] = Field(ge=0, le=3000, description="Unique VAC numeric identifier.")
    completed: Union[str, None] = Field(description="Date the test was completed, in ISO format.")
    age: Union[int, None] = Field(ge=0, description="Patient age.")
    sex: Union[str, None] = Field(description="Sex of the patient, 'male' or 'female'.")

    # CERAD Test
    cerad_encoding_trial_1: Union[int, None] = Field(description="Scores for the first encoding trial (0-10).")
    cerad_encoding_trial_2: Union[int, None] = Field(description="Scores for the second encoding trial (0-10).")
    cerad_encoding_trial_3: Union[int, None] = Field(description="Scores for the third encoding trial (0-10).")
    cerad_encoding_total: Union[int, None] = Field(description="Total score for Encoding, sum of three trials (0-30).")
    cerad_delayed_recall: Union[int, None] = Field(ge=0, le=10, description="Score for Delayed Recall (0-10).")
    cerad_recognition_hits: Union[int, None] = Field(ge=0, le=10, description="Number of Recognition Hits (RH) (0-10).")
    cerad_false_positives: Union[int, None] = Field(ge=0, le=10, description="Number of False Positives (FP) (0-10).")
    cerad_corrected_recognition_total: Union[int, None] = Field(description="Corrected Recognition Total (RH-FP).")
    cerad_rapid_forgetting_present: Union[bool, None] = Field(description="True if Rapid Forgetting present. True if rapid forgetting larger than 0. False otherwise.")
    cerad_rapid_forgetting_words: Union[Dict[str, int], None] = Field(description="Encoded words subject to rapid forgetting, with number of how many times they were encoded. Example: POLEx3 -> {'pole':3}")
    cerad_notes: Union[str, None] = Field(description="Notes about CERAD word list memory test.")


if __name__ == "__main__":
    json_schema = Report.model_json_schema()

    import json

    with open("report_schema.json", "w") as f:
        json.dump(json_schema, f, indent=2)