from typing import List
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from prompts import PROMPT_WITH_HEADINGS, PROMPT_WITHOUT_HEADINGS

load_dotenv()

# =====================================================
# Schema
# =====================================================

class SubSection(BaseModel):
    subsection_name: str
    subsection_passage: str

class KBMetadata(BaseModel):
    solution: str
    region: str
    section: str
    subsections: List[SubSection]

# =====================================================
# LLM Setup
# =====================================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

structured_llm = llm.with_structured_output(KBMetadata)

# =====================================================
# Prompt Selector
# =====================================================

def get_prompt(option: int):
    if option == 1:
        return ChatPromptTemplate.from_template(PROMPT_WITH_HEADINGS)
    else:
        return ChatPromptTemplate.from_template(PROMPT_WITHOUT_HEADINGS)

# =====================================================
# Passage Selector
# =====================================================

def get_passages():
    passage_1 = """
The client operates across the US market.

The engagement falls under Data Advisory.

Executive Overview

Business Context

The client operates in the financial services
industry and requires improved executive reporting.

Current Challenges

Reporting relies heavily on manual spreadsheet
consolidation and disconnected data sources.

Business Objectives

Create a centralized reporting platform,
improve KPI visibility, and automate reporting.

Strategic Vision

Develop a scalable analytics capability that
supports future growth initiatives.
"""

    passage_2 = """
The client operates across the US market.

The engagement falls under Data Advisory.

Executive Overview


The client operates in the financial services
industry and requires improved executive reporting.


Reporting relies heavily on manual spreadsheet
consolidation and disconnected data sources.


Create a centralized reporting platform,
improve KPI visibility, and automate reporting.


Develop a scalable analytics capability that
supports future growth initiatives.
"""
    return passage_1, passage_2