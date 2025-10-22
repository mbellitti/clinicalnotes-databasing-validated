from pydantic import BaseModel, Field
from datetime import date
from typing import Dict, List


class MocaTest(BaseModel):
    """Montreal Cognitive Assessment (MoCA). The answers are numeric scores for each question or section."""

    visuospatial_executive: int = Field( None, ge=0, le=5, description="Score for Visuospatial/Executive section (0-5).")
    naming: int = Field(None, ge=0, le=3, description="Score for Naming section (0-3).")
    attention: int = Field( None, ge=0, le=6, description="Score for Attention section (0-6).")
    language: int = Field( None, ge=0, le=3, description="Score for Language section (0-3).")
    abstraction: int = Field( None, ge=0, le=2, description="Score for Abstraction section (0-2).")
    delayed_recall: int = Field( None, ge=0, le=5, description="Score for Delayed Recall/Memory section (0-5).")
    orientation: int = Field( None, ge=0, le=6, description="Score for Orientation section (0-6).")
    total_score: int = Field( None, ge=0, le=30, description="Total score for the MoCA test (0-30).")
    notes: str = Field(None, description="Notes about MoCA.")


class MmseTest(BaseModel):
    """Mini-Mental State Examination (MMSE). The answers are numeric scores for each question or section."""

    orientation: int = Field( None, ge=0, le=10, description="Score for Orientation to Time and Space.")
    registration: int = Field(None, ge=0, le=3, description="Score for Registration.")
    attention_and_calculation: int = Field( None, ge=0, le=5, description="Score for Attention and Calculation.")
    recall: int = Field(None, ge=0, le=3, description="Score for Recall.") 
    language: int = Field(None, ge=0, le=8, description="Score for Language.")
    visual_construction: int = Field( None, ge=0, le=1, description="Score for Visual Construction/Copying.")
    total_score: int = Field( None, ge=0, le=30, description="Total score for the MMSE test.")
    notes: str = Field(None, description="Notes about MMSE.")


class CeradTest(BaseModel):
    """CERAD word test."""

    encoding_trials: List[int] = Field( None, description="Scores for the three encoding trials (0-10).")
    encoding_total: int = Field(None, description="Total score for Encoding.")
    delayed_recall: int = Field( None, ge=0, le=10, description="Score for Delayed Recall (0-10, cutoff: 5).")
    recognition_hits: int = Field( None, ge=0, le=10, description="Number of Recognition Hits (RH) (0-10).")
    false_positives: int = Field( None, ge=0, le=10, description="Number of False Positives (FP) (0-10).")
    corrected_recognition_total: int = Field( None, description="Corrected Recognition Total (RH-FP, cutoff: 8).")
    rapid_forgetting: int = Field(None, description="Score for Rapid Forgetting.")
    rapid_forgetting_words: Dict[str, int] = Field( None, description="Encoded words subject to rapid forgetting.")


class TrailsATest(BaseModel):
    """Trail Making Test part A (including oral version)."""

    time_in_seconds: float = Field( None, ge=0, description="Time to complete the test in seconds.")
    errors: int = Field( None, ge=0, description="Number of errors made during the test.")
    notes: str = Field(None, description="Notes about Trails A.")


class TrailsBTest(BaseModel):
    """Trail Making Test part B (including oral version)."""

    time_in_seconds: float = Field( None, ge=0, description="Time to complete the test in seconds.")
    errors: int = Field( None, ge=0, description="Number of errors made during the test.")
    notes: str = Field(None, description="Notes about Trails B.")



class LetterFluencyTest(BaseModel):
    """Letter Fluency test: letters F, A, S."""

    total: int = Field(None, ge=0, description="The total score for letter fluency.")

    F_score: int = Field(None, ge=0, description="Score for letter F.")
    F_rule_breaks: int = Field(None, ge=0, description="Number of rule breaks for letter F.")
    F_repetitions: int = Field(None, ge=0, description="Number of repetitions for letter F.")

    A_score: int = Field(None, ge=0, description="Score for letter A.")
    A_rule_breaks: int = Field(None, ge=0, description="Number of rule breaks for letter A.")
    A_repetitions: int = Field(None, ge=0, description="Number of repetitions for letter A.")

    S_score: int = Field(None, ge=0, description="Score for letter S.")
    S_rule_breaks: int = Field(None, ge=0, description="Number of rule breaks for letter S.")
    S_repetitions: int = Field(None, ge=0, description="Number of repetitions for letter S.")



class CategoryFluencyTest(BaseModel):
    """Category Fluency test: categories Animals, Vegetables, Fruits"""

    total: int = Field(None, ge=0, description="The total score for category fluency.")


    Animals_score: int = Field(None, ge=0, description="Score for letter Animals.")
    Animals_rule_breaks: int = Field(None, ge=0, description="Number of rule breaks for letter Animals.")
    Animals_repetitions: int = Field(None, ge=0, description="Number of repetitions for letter Animals.")

    Vegetables_score: int = Field(None, ge=0, description="Score for letter Vegetables.")
    Vegetables_rule_breaks: int = Field(None, ge=0, description="Number of rule breaks for letter Vegetables.")
    Vegetables_repetitions: int = Field(None, ge=0, description="Number of repetitions for letter Vegetables.")

    Fruits_score: int = Field(None, ge=0, description="Fruitscore for letter Fruits.")
    Fruits_rule_breaks: int = Field(None, ge=0, description="Number of rule breaks for letter Fruits.")
    Fruits_repetitions: int = Field(None, ge=0, description="Number of repetitions for letter Fruits.")


class FluencyTest(BaseModel):
    """
    The main Pydantic model for the complete Letter and Category Fluency test.
    """
    letter_fluency: LetterFluencyTest
    category_fluency: CategoryFluencyTest
    notes: str


class BostonNamingTest(BaseModel):
    """ Boston Naming Test - Short Form (BNT-15). """

    total_score: int = Field(None, ge=0, le=15, description="Total score out of 15.")
    missed: int = Field(None, ge=0, description="Number of missed items.")
    semantic_cues: int = Field( None, ge=0, description="Number of semantic cues used (SC).")
    phonemic_cues: int = Field( None, ge=0, description="Number of phonemic cues used (PC).")
    notes: str = Field(None, description="A summary of the test performance.")


class VerbalNamingTest(BaseModel):
    """ Verbal Naming Test """

    total_score: int = Field(None, ge=0, le=55, description="Total score out of 55.")
    missed: int = Field(None, ge=0, description="Number of missed items.")
    phonemic_cues: int = Field( None, ge=0, description="Number of phonemic cues used (PC).")
    notes: str = Field(None, description="A summary of the test performance.")


class GeriatricDepressionScale(BaseModel):
    """ Geriatric Depression Scale (GDS)"""
    total_score: int = Field(None, ge=0, le=15, description="Total score out of 15.")
    notes: str = Field(None, description="A summary of the results.")


class GeriatricAnxietyIndex(BaseModel):
    """ Geriatric Anxiety Index (GAI).  """
    total_score: int = Field(None, ge=0, le=20, description="Total score out of 20.")
    notes: str = Field(None, description="A summary of the results.")


class LubbenSocialNetworkScale(BaseModel):
    """ Lubben Social Network Scale (LSNS-6).  """
    total_score: int = Field(None, ge=0, le=30, description="Total score out of 30.")
    notes: str = Field(None, description="A summary of the results.")


class UclaLonelinessScale(BaseModel):
    """ UCLA Loneliness Scale """
    total_score: int = Field(None, ge=0, le=9, description="Total score out of 9.")
    notes: str = Field(None, description="A summary of the results.")


class Report(BaseModel):

    vac: int = Field(None, le=3000, description="Unique VAC numeric identifier.")
    completed: date = Field(None, description="Date the test was completed.")
    age: int = Field(None, ge=0, description="Patient age.")
    sex: str = Field(None, description="Sex of the patient, 'male' or 'female'.")
    education: int = Field(None, ge=0, description="Years of education.")

    moca: MocaTest = Field(None, description="MoCA test results (optional).")
    mmse: MmseTest = Field(None, description="MMSE test results (optional).")
    cerad: CeradTest = Field( None, description="CERAD word list memory test results (optional).")
    trailsa: TrailsATest = Field(None, description="Trails A test results (optional).")
    trailsb: TrailsBTest = Field(None, description="Trails B test results (optional).")
    fluencytest: FluencyTest = Field( None, description="Letter and Category fluency test results (optional).")
    bostonnamingtest: BostonNamingTest = Field( None, description="Boston Naming test results (optional).")
    verbalnamingtest: VerbalNamingTest = Field( None, description="Verbal Naming test results (optional).")
    gds: GeriatricDepressionScale = Field( None, description="Geriatric Depression Scale test results (optional).")
    gai: GeriatricAnxietyIndex = Field( None, description="Geriatric Anxiety Index test results (optional).")
    lubben: LubbenSocialNetworkScale = Field( None, description="Lubben Social Network scale results (optional).")
    uclaloneliness: UclaLonelinessScale = Field( None, description="UCLA Loneliness scale results (optional).")

    behavioral_observations: str = Field(None, description="Behavioral observations.")
    history: str = Field(None, description="History.")
    medications: List[str] = Field(None, description="List of current Medications.")
    summary: str = Field(None, description="Overall report summary.")


if __name__ == "__main__":
    json_schema = Report.model_json_schema()

    import json

    with open("report_schema.json", "w") as f:
        json.dump(json_schema, f, indent=2)
