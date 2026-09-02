import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.environ["OPEN_AI_KEY"])

business_note = """
Dr. Smith's office called about a patient referral.
They need the referral form and insurance information
sent to the cardiology department.
Please fax it today.
"""
response = client.responses.create(
    model = "gpt-5-mini",
    input = f"""
Extract the business information from this note.
Retrun JSON with exactly these fields:
- department
- action
- priority
- channel

Business note:
{business_note}
"""
)              

print(response.output_text)
