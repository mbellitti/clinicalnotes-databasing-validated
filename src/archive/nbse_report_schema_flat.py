from pydantic import BaseModel, Field
from datetime import date
from typing import Any, Dict, List, Union

class Report(BaseModel):
    # Patient Information
    vac: Union[int, None] = Field(ge=0, le=3000, description="Unique VAC numeric identifier.")
    completed: Union[str, None] = Field(description="Date the test was completed, in ISO format.")
    age: Union[int, None] = Field(ge=0, description="Patient age.")
    sex: Union[str, None] = Field(description="Sex of the patient, 'male' or 'female'.")
    education: Union[int, None] = Field(ge=0, description="Years of education.")
    encounter_type: Union[str, None] = Field(description="Encounter type, one of: 'in-person', 'telephone', 'VVC'.")

    # MoCA Test (Montreal Cognitive Assessment)
    moca_visuospatial_executive: Union[int, None] = Field(ge=0, le=5, description="Score for Visuospatial/Executive section (0-5).")
    moca_naming: Union[int, None] = Field(ge=0, le=3, description="Score for Naming section (0-3).")
    moca_attention: Union[int, None] = Field(ge=0, le=6, description="Score for Attention section (0-6).")
    moca_language: Union[int, None] = Field(ge=0, le=3, description="Score for Language section (0-3).")
    moca_abstraction: Union[int, None] = Field(ge=0, le=2, description="Score for Abstraction section (0-2).")
    moca_delayed_recall: Union[int, None] = Field(ge=0, le=5, description="Score for Delayed Recall/Memory section (0-5).")
    moca_orientation: Union[int, None] = Field(ge=0, le=6, description="Score for Orientation section (0-6).")
    moca_total_score: Union[int, None] = Field(ge=0, le=30, description="Total score for the MoCA test (0-30).")
    moca_notes: Union[str, None] = Field(description="Notes about MoCA.")

    # MMSE Test (Mini-Mental State Examination)
    mmse_orientation: Union[int, None] = Field(ge=0, le=10, description="Score for Orientation to Time and Space.")
    mmse_registration: Union[int, None] = Field(ge=0, le=3, description="Score for Registration.")
    mmse_attention_and_calculation: Union[int, None] = Field(ge=0, le=5, description="Score for Attention and Calculation.")
    mmse_recall: Union[int, None] = Field(ge=0, le=3, description="Score for Recall.") 
    mmse_language: Union[int, None] = Field(ge=0, le=8, description="Score for Language.")
    mmse_visual_construction: Union[int, None] = Field(ge=0, le=1, description="Score for Visual Construction/Copying.")
    mmse_total_score: Union[int, None] = Field(ge=0, le=30, description="Total score for the MMSE test.")
    mmse_notes: Union[str, None] = Field(description="Notes about MMSE.")

    # CERAD Test
    cerad_encoding_trials: Union[List[int], None] = Field(description="Scores for the three encoding trials (0-10).")
    cerad_encoding_total: Union[int, None] = Field(description="Total score for Encoding.")
    cerad_delayed_recall: Union[int, None] = Field(ge=0, le=10, description="Score for Delayed Recall (0-10).")
    cerad_recognition_hits: Union[int, None] = Field(ge=0, le=10, description="Number of Recognition Hits (RH) (0-10).")
    cerad_false_positives: Union[int, None] = Field(ge=0, le=10, description="Number of False Positives (FP) (0-10).")
    cerad_corrected_recognition_total: Union[int, None] = Field(description="Corrected Recognition Total (RH-FP).")
    cerad_rapid_forgetting: Union[int, None] = Field(description="Score for Rapid Forgetting.")
    cerad_rapid_forgetting_words: Union[Dict[str, int], None] = Field(description="Encoded words subject to rapid forgetting, with number of how many times they were encoded.")
    cerad_notes: Union[str, None] = Field(description="Notes about CERAD word list memory test.")

    # Trail Making Test A
    trailsa_time_in_seconds: Union[float, None] = Field(ge=0, description="Time to complete the Trails A test in seconds.")
    trailsa_errors: Union[int, None] = Field(ge=0, description="Number of errors made during the Trails A test.")
    trailsa_notes: Union[str, None] = Field(description="Notes about Trails A.")

    # Trail Making Test B
    trailsb_time_in_seconds: Union[float, None] = Field(ge=0, description="Time to complete the Trails B test in seconds.")
    trailsb_errors: Union[int, None] = Field(ge=0, description="Number of errors made during the Trails B test.")
    trailsb_notes: Union[str, None] = Field(description="Notes about Trails B.")

    # Letter Fluency Test
    letter_fluency_total: Union[int, None] = Field(ge=0, description="The total score for letter fluency.")
    letter_fluency_f_score: Union[int, None] = Field(ge=0, description="Score for letter F.")
    letter_fluency_f_rule_breaks: Union[int, None] = Field(ge=0, description="Number of rule breaks for letter F.")
    letter_fluency_f_repetitions: Union[int, None] = Field(ge=0, description="Number of repetitions for letter F.")
    letter_fluency_a_score: Union[int, None] = Field(ge=0, description="Score for letter A.")
    letter_fluency_a_rule_breaks: Union[int, None] = Field(ge=0, description="Number of rule breaks for letter A.")
    letter_fluency_a_repetitions: Union[int, None] = Field(ge=0, description="Number of repetitions for letter A.")
    letter_fluency_s_score: Union[int, None] = Field(ge=0, description="Score for letter S.")
    letter_fluency_s_rule_breaks: Union[int, None] = Field(ge=0, description="Number of rule breaks for letter S.")
    letter_fluency_s_repetitions: Union[int, None] = Field(ge=0, description="Number of repetitions for letter S.")

    # Category Fluency Test
    category_fluency_total: Union[int, None] = Field(ge=0, description="The total score for category fluency.")
    category_fluency_animals_score: Union[int, None] = Field(ge=0, description="Score for Animals.")
    category_fluency_animals_rule_breaks: Union[int, None] = Field(ge=0, description="Number of rule breaks for Animals.")
    category_fluency_animals_repetitions: Union[int, None] = Field(ge=0, description="Number of repetitions for Animals.")
    category_fluency_vegetables_score: Union[int, None] = Field(ge=0, description="Score for Vegetables.")
    category_fluency_vegetables_rule_breaks: Union[int, None] = Field(ge=0, description="Number of rule breaks for Vegetables.")
    category_fluency_vegetables_repetitions: Union[int, None] = Field(ge=0, description="Number of repetitions for Vegetables.")
    category_fluency_fruits_score: Union[int, None] = Field(ge=0, description="Score for Fruits.")
    category_fluency_fruits_rule_breaks: Union[int, None] = Field(ge=0, description="Number of rule breaks for Fruits.")
    category_fluency_fruits_repetitions: Union[int, None] = Field(ge=0, description="Number of repetitions for Fruits.")

    # Fluency Test Notes
    fluency_notes: Union[str, None] = Field(description="Notes about fluency tests.")

    # Boston Naming Test
    boston_naming_total_score: Union[int, None] = Field(ge=0, le=15, description="Boston Naming Test (BNT): Total score out of 15.")
    boston_naming_missed: Union[int, None] = Field(ge=0, description="Boston Naming Test (BNT): Number of missed items.")
    boston_naming_semantic_cues: Union[int, None] = Field(ge=0, description="Boston Naming Test (BNT): Number of semantic cues used (SC).")
    boston_naming_phonemic_cues: Union[int, None] = Field(ge=0, description="Boston Naming Test (BNT): Number of phonemic cues used (PC).")
    boston_naming_notes: Union[str, None] = Field(description="Boston Naming Test (BNT): A summary of the test performance.")

    # Verbal Naming Test
    verbal_naming_total_score: Union[int, None] = Field(ge=0, le=55, description="Verbal Naming Test (VNT): Total score out of 55.")
    verbal_naming_missed: Union[int, None] = Field(ge=0, description="Verbal Naming Test (VNT): Number of missed items.")
    verbal_naming_phonemic_cues: Union[int, None] = Field(ge=0, description="Verbal Naming Test (VNT): Number of phonemic cues used (PC).")
    verbal_naming_notes: Union[str, None] = Field(description="Verbal Naming Test (VNT): A summary of the test performance.")

    # Geriatric Depression Scale
    gds_total_score: Union[int, None] = Field(ge=0, le=15, description="Total score out of 15.")
    gds_notes: Union[str, None] = Field(description="A summary of the results.")

    # Geriatric Anxiety Index
    gai_total_score: Union[int, None] = Field(ge=0, le=20, description="Total score out of 20.")
    gai_notes: Union[str, None] = Field(description="A summary of the results.")

    # Lubben Social Network Scale
    lubben_total_score: Union[int, None] = Field(ge=0, le=30, description="Total score out of 30.")
    lubben_notes: Union[str, None] = Field(description="A summary of the results.")

    # UCLA Loneliness Scale
    ucla_loneliness_total_score: Union[int, None] = Field(ge=0, le=9, description="Total score out of 9.")
    ucla_loneliness_notes: Union[str, None] = Field(description="A summary of the results.")

    # General Report Fields
    behavioral_observations: Union[str, None] = Field(description="Behavioral observations.")
    history: Union[str, None] = Field(description="History.")
    medications: Union[List[str], None] = Field(description="List of current Medications.")
    medications_notes: Union[str, None] = Field(description="Notes about current Medications.")
    summary: Union[str, None] = Field(description="Overall report summary.")


if __name__ == "__main__":
    json_schema = Report.model_json_schema()

    import json

    with open("report_schema.json", "w") as f:
        json.dump(json_schema, f, indent=2)