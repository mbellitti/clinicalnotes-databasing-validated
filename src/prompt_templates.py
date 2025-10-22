TABULAR_TEMPLATE = """
Your task is to convert a neurobehavioral assessment report into JSON format. 

Dates will be provided in month-first format: mm/dd/yy or mm.dd.yy, convert them to ISO format yyyy-mm-dd.

You must output valid JSON.  Do not include extra fields. The fields you are allowed to use are:
vac: numeric patient identifier
completed: date of completion in ISO format, closest date if cannot be determined
age: patient age 
sex: 'male' or 'female'
education: number of years of education
cerad
trailsa
trailsb
fluencytest
bostonnamingtest
verbalnamingtest
gds
gai
lubben
uclaloneliness
behavioral_observations
history
medications
summary

Use 'null' if you cannot safely determine the value of a key. 

Report:

{report}

"""

TABULAR_TEMPLATE_SCHEMA = """Your task is to convert a Neurobehavioral Report into JSON format. 
Use 'null' if you cannot safely determine the value of a key. You must output valid JSON.
Comply with the provided JSON schema. Do not use extra keys, do not include extra information. Pay attention to the field descriptions.

Dates will be provided in USA month-first format: mm/dd/yy or mm.dd.yy, convert them to ISO format yyyy-mm-dd

The encounter type is specified at the beginning of the report. If it is missing, use notes and summaries to help you determine the encounter type.
If you still cannot determine the encounter type, output null.

When reporting medications, only keep medication name and strength, remove origin (e.g. non-va), purpose, and directions about usage.

JSON Schema:

```
{schema}
```

Neurobehavioral Report:

{report}

"""

# - If Boston Naming Test (BNT) is present, the encounter type is either in-person or VVC.
# - If Verbal Naming Test (VNT) is present, the encounter type is telephone.
# Copy notes and comments from the report exactly as written to the appropriate keys.