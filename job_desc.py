#!/usr/bin/env python
# coding: utf-8

# In[11]:


#!pip install streamlit


# In[12]:


#!pip install --upgrade text-generation==0.5.0


# In[10]:


import streamlit as st
import text_generation

def generate_job_responsibilities(job_title, work_experience_required, skillset_required):
    client = text_generation.InferenceAPIClient("OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")

    complete_answer = ""
    for response in client.generate_stream(
        f"<|prompter|>Write Job Responsibilities for {job_title} with {work_experience_required} years of experience and {skillset_required} .<|endoftext|><|assistant|>",
        max_new_tokens=1000,
    ):
        if response.token.special:
            continue
        complete_answer += response.token.text + " "

    return complete_answer


def main():
    st.title("ABC COMPANY :red[JD GENERATOR]:")
    
    about_the_company = st.text_area("ENTER BRIEFLY ABOUT THE COMPANY: ")
    
    job_title = st.text_input("ENTER THE JOB TITLE: ")
    companys_no_of_employees = st.text_input("ENTER THE COMPANY'S NUMBER OF EMPLOYEES: ")
    work_experience_required = st.text_input("ENTER THE WORK EXPERIENCE REQUIRED: ")
    skillset_required = st.text_input("ENTER THE SKILL SET REQUIRED: ")
    company_name = st.text_input("ENTER THE COMPANY NAME: ")
    job_type = st.selectbox("ENTER THE JOB TYPE: ", ('Full time', "Part time", "Contract", "Temporary", "Internship", "Others"))
    job_location = st.text_input("ENTER THE JOB LOCATION: ")
    work_mode = st.selectbox("ENTER THE WORK MODE: ", ("On-Site", "Hybrid", "Remote"))
    shift = st.selectbox("SELECT THE SHIFT: ", ("Day shift", "Evening shift", "Morning shift", "Night shift", "Rotational shift", "UK shift", "US shift"))
    job_benefits = st.text_input("ENTER THE JOB BENEFITS: ")
    field = st.text_input("ENTER THE FIELD: ")
    currency = st.text_input("ENTER THE CURRENCY: ")
    package = st.text_input("ENTER THE PACKAGE WITH CURRENCY FORMAT: ")
    notice_period = st.text_input("ENTER THE NOTICE PERIOD: ")
    qualification = st.text_input("ENTER THE QUALIFICATION REQUIRED: ")
    no_of_openings = st.text_input("ENTER THE NUMBER OF OPENINGS: ")
    date_posted = st.date_input("ENTER THE DATE POSTED: ")
    posting_end_date = st.date_input("ENTER THE POSTING END DATE: ")

    job_details = f"""
    
**JOB TITLE :** {job_title}

**COMPANY :** {company_name}

**JOB TYPE :** {job_type}

**LOCATION :** {job_location}

**WORK MODE :** {work_mode}

**SHIFT :** {shift}

**BENEFITS :** {job_benefits}

**FIELDS :** {field}

**SALARY :** {currency} {package}

**QUALIFICATION :** {qualification}

**NOTICE PERIOD :** {notice_period}
"""
    generate_button = st.button("Generate you job description",key=f"generate") 

    def job_reponsibilities_app():

         job_responsibilities = generate_job_responsibilities(
        job_title, work_experience_required, skillset_required
         )
         st.write(f"**Job Responsibilities for {job_title}:**\n{job_responsibilities}")
        
 
    #st.write(f"**Job Responsibilities for {job_title}**\n{job_responsibilities}")
    if generate_button:
        st.write(f"**Job Details:**\n{job_details}")
        job_reponsibilities_app()
        #st.write(f"**Job Responsibilities for {job_title}:**\n{job_responsibilities}"
        
if __name__ == "__main__":
    main()


# In[ ]:




