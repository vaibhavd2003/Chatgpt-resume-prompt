import re
import json

def parse_resume(resume_text):
    resume_json = {
        "Name": "",
        "Contact Information": {
            "Email": "",
            "Phone": "",
            "LinkedIn": "",
            "Address": ""
        },
        "Professional Summary": "",
        "Work Experience": [],
        "Education": [],
        "Skills": [],
        "Certifications": [],
        "Projects": []
    }
    
    # Sample parsing logic (this needs to be extended based on resume format)
    name_match = re.search(r"Name:\s*(.*)", resume_text)
    if name_match:
        resume_json["Name"] = name_match.group(1).strip()
    
    email_match = re.search(r"Email:\s*(.*)", resume_text)
    if email_match:
        resume_json["Contact Information"]["Email"] = email_match.group(1).strip()
    
    phone_match = re.search(r"Phone:\s*(.*)", resume_text)
    if phone_match:
        resume_json["Contact Information"]["Phone"] = phone_match.group(1).strip()
    
    # Add more parsing logic for other fields...
    
    return json.dumps(resume_json, indent=4)

if __name__ == "__main__":
    resume_text = """
    Name: John Doe
    Email: john.doe@example.com
    Phone: (123) 456-7890
    LinkedIn: linkedin.com/in/johndoe
    Address: 123 Main St, Anytown, USA

    Professional Summary:
    Experienced software developer...

    Work Experience:
    Job Title: Software Engineer
    Company: Tech Solutions
    Location: New York, NY
    Start Date: Jan 2020
    End Date: Present
    Responsibilities:
    - Developed applications...
    - Collaborated with team...

    Education:
    Degree: BSc in Computer Science
    Institution: University of Anytown
    Location: Anytown, USA
    Start Date: Sep 2015
    End Date: May 2019

    Skills:
    - Python
    - Java
    - SQL

    Certifications:
    Name: Certified Python Developer
    Issuing Organization: Python Institute
    Date: June 2021

    Projects:
    Title: Chatbot Development
    Description: Developed a chatbot using Python...
    Technologies: Python, NLP, AI
    """

    parsed_resume = parse_resume(resume_text)
    print(parsed_resume)
