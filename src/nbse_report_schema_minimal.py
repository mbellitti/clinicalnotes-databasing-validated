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
    # is_telephone_encounter: Union[bool, None] = Field(description="True if this a telephone encounter.")
    # is_vvc_encounter: Union[bool, None] = Field(description="True if this a VVC encounter (Video).")
    # is_f2f_encounter: Union[bool, None] = Field(description="True if this an in-person encounter.")
    encounter_type: Union[str, None] = Field(description="Encounter type, one of: 'in-person', 'telephone', 'VVC'.")

    # MoCA Test (Montreal Cognitive Assessment)
    moca_total_score: Union[int, None] = Field(ge=0, le=30, description="Total score for the MoCA test (0-30).")
    # moca_notes: Union[str, None] = Field(description="Notes about MoCA.")


    # MMSE Test (Mini-Mental State Examination)
    mmse_total_score: Union[int, None] = Field(ge=0, le=30, description="Total score for the MMSE test.")
    # mmse_notes: Union[str, None] = Field(description="Notes about MMSE.")

    # Telephone ACES 
    aces_total_score: Union[int, None] = Field(ge=0, le=30, description="Total score for the ACES test.")
    # aces_notes: Union[str, None] = Field(description="Notes about ACES.")

    # Clock drawing
    # clock_drawing_notes: Union[str, None] = Field(description="Notes about clock drawing test.")

    # CERAD Test
    # cerad_encoding_trials: Union[List[int], None] = Field(description="Scores for the three encoding trials (0-10).")
    cerad_encoding_total: Union[int, None] = Field(description="Total score for Encoding, sum of three trials (0-30).")
    cerad_delayed_recall: Union[int, None] = Field(ge=0, le=10, description="Score for Delayed Recall (0-10).")
    # cerad_recognition_hits: Union[int, None] = Field(ge=0, le=10, description="Number of Recognition Hits (RH) (0-10).")
    # cerad_false_positives: Union[int, None] = Field(ge=0, le=10, description="Number of False Positives (FP) (0-10).")
    cerad_corrected_recognition_total: Union[int, None] = Field(description="Corrected Recognition Total (RH-FP).")
    # cerad_rapid_forgetting: Union[bool, None] = Field(description="True if Rapid Forgetting present. True if rapid forgetting larger than 0.")
    # cerad_rapid_forgetting_words: Union[Dict[str, int], None] = Field(description="Encoded words subject to rapid forgetting, with number of how many times they were encoded.")
    # cerad_notes: Union[str, None] = Field(description="Notes about CERAD word list memory test.")

    # Trail Making Test A
    trailsa_time_in_seconds: Union[float, None] = Field(ge=0, description="Time to complete the Trails A test in seconds (including oral trails).")
    trailsa_errors: Union[int, None] = Field(ge=0, description="Number of errors made during the Trails A test.")
    # trailsa_notes: Union[str, None] = Field(description="Notes about Trails A.")

    # Trail Making Test B
    trailsb_time_in_seconds: Union[float, None] = Field(ge=0, description="Time to complete the Trails B test in seconds (including oral trails).")
    trailsb_errors: Union[int, None] = Field(ge=0, description="Number of errors made during the Trails B test.")
    # trailsb_notes: Union[str, None] = Field(description="Notes about Trails B.")

    # Letter Fluency Test
    letter_fluency_total: Union[int, None] = Field(ge=0, description="The total score for letter fluency.")

    # Category Fluency Test
    category_fluency_total: Union[int, None] = Field(ge=0, description="The total score for category fluency.")

    # Fluency Test Notes
    # fluency_notes: Union[str, None] = Field(description="Notes about fluency tests.")

    # Boston Naming Test
    boston_naming_total_score: Union[int, None] = Field(ge=0, le=15, description="Boston Naming Test (BNT): Total score out of 15.")
    # boston_naming_missed: Union[int, None] = Field(ge=0, description="Boston Naming Test (BNT): Number of missed items.")
    # boston_naming_semantic_cues: Union[int, None] = Field(ge=0, description="Boston Naming Test (BNT): Number of semantic cues used (SC).")
    # boston_naming_phonemic_cues: Union[int, None] = Field(ge=0, description="Boston Naming Test (BNT): Number of phonemic cues used (PC).")
    # boston_naming_notes: Union[str, None] = Field(description="Boston Naming Test (BNT): A summary of the test performance.")

    # Verbal Naming Test
    verbal_naming_total_score: Union[int, None] = Field(ge=0, le=55, description="Verbal Naming Test (VNT): Total score out of 55.")
    # verbal_naming_missed: Union[int, None] = Field(ge=0, description="Verbal Naming Test (VNT): Number of missed items.")
    # verbal_naming_phonemic_cues: Union[int, None] = Field(ge=0, description="Verbal Naming Test (VNT): Number of phonemic cues used (PC).")
    # verbal_naming_notes: Union[str, None] = Field(description="Verbal Naming Test (VNT): A summary of the test performance.")

    # Geriatric Depression Scale
    # gds_total_score: Union[int, None] = Field(ge=0, le=15, description="Total score out of 15.")
    # gds_notes: Union[str, None] = Field(description="A summary of the results.")

    # Geriatric Anxiety Index
    # gai_total_score: Union[int, None] = Field(ge=0, le=20, description="Total score out of 20.")
    # gai_notes: Union[str, None] = Field(description="A summary of the results.")

    # Lubben Social Network Scale
    # lubben_total_score: Union[int, None] = Field(ge=0, le=30, description="Total score out of 30.")
    # lubben_notes: Union[str, None] = Field(description="A summary of the results.")

    # UCLA Loneliness Scale
    # ucla_loneliness_total_score: Union[int, None] = Field(ge=0, le=9, description="Total score out of 9.")
    # ucla_loneliness_notes: Union[str, None] = Field(description="A summary of the results.")

    # General Report Fields
    # behavioral_observations: Union[str, None] = Field(description="Behavioral observations.")
    # history: Union[str, None] = Field(description="History.")
    medications: Union[List[str], None] = Field(description="List of current Medications. Only medication name and strenght, remove directions.")
    # medications_notes: Union[str, None] = Field(description="Notes about current Medications.")
    # summary: Union[str, None] = Field(description="Overall report summary.")
    
    # Conclusions
    adl_impaired: Union[bool, None] = Field(description="True if activities of daily living (ADL) are impaired, False if intact (indepedent).")
    iadl_impaired: Union[bool, None] = Field(description="True if iADL are impaired, False if intact (independent).")
    diagnosis: Union[str, None] = Field(description="Most appropriate diagnosis at this time. One of: Normal Cognition, Subjective Cognitive Decline (SCD), Mild Cognitive Impairment (MCI), Very Mild Dementia, Mild Dementia, Moderate Dementia, Severe Dementia. No other values allowed.)")

    clinical_syndrome: Union[str, None] = Field(description="Clinical Syndrome (Examples: amnestic mci, progressive amnestic dysfunction, primary progressive aphasia, executive dysfunction, global cognitive impairment, alheimer's disease, traumatic encephalopathy). null if it cannot be determined.")
    # underlying_etiology: Union[List[str], None] = Field(description="List of underlying etiologies to consider.")

    neuropsychological_testing_recommended: Union[bool, None] = Field(description="True if the report summary recommends neuropsychological testing after this visit. False otherwise (Example: neuropsychological testing was in the past -> False).")
    pet_recommended: Union[bool, None] = Field(description="True if the report summary requests or recommends amyloid PET. False otherwise.")
    


if __name__ == "__main__":
    json_schema = Report.model_json_schema()

    import json

    with open("report_schema.json", "w") as f:
        json.dump(json_schema, f, indent=2)