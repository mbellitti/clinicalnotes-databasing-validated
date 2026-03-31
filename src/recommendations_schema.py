from pydantic import BaseModel, Field
from datetime import date
from typing import Any, Dict, List, Union


class Recommendations(BaseModel):

    neuropsychological_testing_recommended: Union[bool, None] = Field(
        description="True if the report summary recommends neuropsychological testing after this visit. False otherwise (Example: neuropsychological testing was in the past -> False)."
    )

    amyloid_pet_recommended: Union[bool, None] = Field(
        description="True if the report summary requests or recommends amyloid PET, aPET, or florbetapir PET. False otherwise."
    )

    fdg_pet_recommended: Union[bool, None] = Field(
        description="True if the report summary requests or recommends FDG PET."
    )

    eeg_recommended: Union[bool, None] = Field(
        description="True if the report summary requests or recommends electroencephalography (EEG), false otherwise."
    )

    dat_scan_recommended: Union[bool, None] = Field(
        description="True if the report summary requests or recommends dopamine transporter scan (DaT scan), false otherwise."
    )

    spect_recommended: Union[bool, None] = Field(
        description="True if the report summary requests or recommends SPECT, false otherwise."
    )

    sleep_study_recommended: Union[bool, None] = Field(
        description="True if the report summary requests or recommends sleep study, false otherwise."
    )

    lumbar_puncture_recommended: Union[bool, None] = Field(
        description="True if the report summary requests or recommends lumbar puncture (LP), false otherwise."
    )


if __name__ == "__main__":
    json_schema = Recommendations.model_json_schema()

    import json

    with open("schemas/recommendation_schema.json", "w") as f:
        json.dump(json_schema, f, indent=2)
