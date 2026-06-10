import sys
import os

sys.path.append(os.path.abspath("."))
from dotenv import load_dotenv

from chains.extraction_chain import extraction_chain
from chains.matching_chain import matching_chain
from chains.scoring_chain import scoring_chain
from chains.explanation_chain import explanation_chain

# Load environment variables
load_dotenv()

# Load Job Description
with open("data/job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()

# Resume List
resume_files = [
    "data/resumes/strong_resume.txt",
    "data/resumes/average_resume.txt",
    "data/resumes/weak_resume.txt"
]

# Output file
output_file = open("outputs/results.txt", "w", encoding="utf-8")

# Process each resume
for resume_path in resume_files:

    print("\n" + "="*70)
    print(f"Processing: {resume_path}")
    print("="*70)

    output_file.write("\n" + "="*70 + "\n")
    output_file.write(f"Processing: {resume_path}\n")
    output_file.write("="*70 + "\n")

    # Read Resume
    with open(resume_path, "r", encoding="utf-8") as file:
        resume = file.read()

    # STEP 1 — Extraction
    extracted_data = extraction_chain.invoke({
        "resume": resume
    })

    print("\nEXTRACTED DATA:\n")
    print(extracted_data.content)

    output_file.write("\nEXTRACTED DATA:\n")
    output_file.write(extracted_data.content + "\n")

    # STEP 2 — Matching
    matching_result = matching_chain.invoke({
        "resume_data": extracted_data.content,
        "job_description": job_description
    })

    print("\nMATCHING RESULT:\n")
    print(matching_result.content)

    output_file.write("\nMATCHING RESULT:\n")
    output_file.write(matching_result.content + "\n")

    # STEP 3 — Scoring
    score_result = scoring_chain.invoke({
        "matching_result": matching_result.content
    })

    print("\nSCORE RESULT:\n")
    print(score_result.content)

    output_file.write("\nSCORE RESULT:\n")
    output_file.write(score_result.content + "\n")

    # STEP 4 — Explanation
    explanation_result = explanation_chain.invoke({
        "score_result": score_result.content
    })

    print("\nEXPLANATION:\n")
    print(explanation_result.content)

    output_file.write("\nEXPLANATION:\n")
    output_file.write(explanation_result.content + "\n")

output_file.close()

print("\nProject Execution Completed Successfully")