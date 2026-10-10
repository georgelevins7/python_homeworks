from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class JobPosting(BaseModel):
    title: str
    required_experience_years: int | None = None
    required_skills: list[str]
    nice_to_have_skills: list[str]
    work_type: str | None = None
    salary_min: float | None = None
    salary_max: float | None = None
    salary_currency: str | None = None
    english_level: str | None = None
    skills_match: list[str]
    missing_skills: list[str]

candidate_skills = ["Python", "Docker", "Git", "FastAPI", "PostgreSQL"]
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = "gemini-3.1-flash-lite"
job_1 = """
We are looking for a Junior AI Engineer to join our growing
technology team.

The ideal candidate should have practical experience with Python
and a good understanding of REST APIs. Familiarity with FastAPI
and PostgreSQL is required.

Experience with Docker, Git, and integrating Large Language Models
(LLMs) into applications would be a plus.

You will work on developing AI-powered services, integrating
third-party APIs, and collaborating with backend developers.

We offer a fully remote position, flexible working hours,
and opportunities for professional growth.
"""

job_2 = """
We are looking for a Middle Backend Developer to join our
international development team.

The candidate must have at least 3 years of professional
experience in backend development.

Strong knowledge of Python, Django, and PostgreSQL is required.
Experience with Redis and Docker is also mandatory.

Familiarity with FastAPI, Kubernetes, and AWS would be
considered an advantage.

The position is hybrid, requiring employees to work from
our Tbilisi office two days per week.

We offer a competitive salary ranging from $2500 to $4000
per month, depending on experience and qualifications.

English proficiency at B2 level or higher is required.

Additional benefits include private health insurance,
paid vacation, and an annual professional development budget.
"""

job_3 = """
We are hiring a Frontend Developer with experience in React and TypeScript.

The candidate should be familiar with modern frontend build tools, version control using Git, and have a good understanding of REST APIs.

Experience with UI/UX design, integrating with backend services, and knowledge of Docker is a plus.

The role includes developing responsive web applications, collaborating with backend developers, and participating in code reviews.

This is a remote position with flexible working hours and opportunities for professional growth.
"""

jobs = [job_1, job_2, job_3]
for job in jobs:
    response = client.models.generate_content(
        model=MODEL,
        contents=f"""
        Candidate Skills: {candidate_skills}
        Job Description: {job}""",
    config=types.GenerateContentConfig(
        system_instruction = """
You are an expert IT recruiter and job posting analyzer.

Your task is to extract structured information from job descriptions
and compare required skills with the candidate's skills.

Rules:
1. Extract information only from the provided job description.
2. Do not invent missing information.
3. Use None for missing optional fields and empty lists for missing skills.
4. Separate required skills from nice-to-have skills.
5. Include only matching required skills in skills_match.
6. Include required skills the candidate does not have in missing_skills.
7. Do not assume the candidate has skills that are not explicitly listed.
8. Return data that strictly follows the provided Pydantic schema.
""",
        response_mime_type="application/json",
        response_schema = JobPosting,
        max_output_tokens=1500,
        temperature=0.2,
    )
)

    result = response.parsed
    print(f"\n-- Job {jobs.index(job) + 1} --")
    print(result.model_dump_json(indent=2))