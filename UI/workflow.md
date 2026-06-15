1. Opportunity Discovery
            ↓
2. Transcript Intelligence(optional)
            ↓
3. Proposal Copilot - Input Consolidation
            ↓
4. Similar Proposal Discovery
            ↓
5. Proposal Structure Builder
            ↓
6. Proposal Preview
            ↓
7. Generation Setup
            ↓
8. Proposal Generation Progress
            ↓
9. Section Generation Tracking
            ↓
10. Generated Section Review
            ↓
11. Executive Summary Review
            ↓
12. Proposal Assembly Review
            ↓
13. Proposal Successfully Generated
            ↓
14. Proposal Completed Successfully























# AI Proposal Copilot – Complete End-to-End User Workflow

## Overview

The AI Proposal Copilot supports two proposal generation paths:

### Path 1 – Similar Proposal Reuse

If a highly relevant historical proposal is found and the user is satisfied with it, the system can generate a proposal directly using that proposal as the baseline structure and content pattern.

The AI replaces and personalizes content using:

* Metadata
* Questionnaire Responses
* Uploaded Documents
* Meeting Notes
* Transcript Information
* User Prompt

This provides a much faster proposal creation experience.

---

### Path 2 – AI Section-by-Section Generation

If the user feels that none of the retrieved proposals are sufficiently relevant, the system proceeds with a full AI generation workflow.

Each section is generated independently using:

* Knowledge Base Retrieval
* Metadata
* Questionnaire Responses
* Grounded Context
* Web Research (Optional)

This provides maximum flexibility and customization.

---

# PHASE 1 – Opportunity Discovery

## Screen 1 – Opportunity Discovery

The proposal creation journey begins here.

The user creates a new opportunity and provides project information.

### Required Inputs

* Client Name
* Industry
* Solution Type
* Project Category

### Optional Inputs

* Sales Questionnaire
* Meeting Transcript
* MOM Document
* RFP
* Discovery Notes
* Additional Attachments

### Prompt Input

The user may also provide additional context.

Example:

"Client requires a multilingual customer support chatbot deployed on Azure. Expected go-live in four months."

---

## AI Actions

The system automatically extracts:

* Business Problem
* Objectives
* Stakeholders
* Timeline
* Technical Requirements
* Cloud Preference
* Success Criteria

The right panel continuously updates:

### Opportunity Summary

* Client Name
* Industry
* Solution Type
* Timeline
* Stakeholders
* Objectives

### Proposal Readiness Score

Example:

85%

Missing:

* Budget
* Support Model
* Success Metrics

---

## User Action

Continue

↓

---

# PHASE 2 – Optional Transcript Intelligence

## Screen 2 – Transcript Intelligence

This screen appears only if:

* Transcript uploaded
* MOM uploaded
* Meeting Notes uploaded

---

## AI Actions

The system analyzes uploaded content.

Extracts:

* Business Goals
* Challenges
* Timeline
* Stakeholders
* Technical Constraints
* Budget References
* Risks

The extracted information is mapped automatically into proposal requirements.

---

## User Action

Review and approve extracted information.

Continue

↓

If no transcript exists:

Skip this screen.

↓

---

# PHASE 3 – Input Consolidation

## Screen 3 – Input Consolidation

The platform combines all collected information.

Sources:

* Metadata
* Questionnaire
* Prompt
* Transcript (if available)
* MOM (if available)
* RFP (if available)

---

## Display

### Consolidated Project Understanding

* Client Information
* Objectives
* Requirements
* Timeline
* Stakeholders
* Budget
* Constraints

---

### Missing Information

Only unanswered fields are displayed.

Example:

* Success Metrics
* Support Model
* Deployment Constraints

---

## User Action

Fill missing information.

Continue

↓

---

# PHASE 4 – Similar Proposal Discovery

## Screen 4 – Similar Proposal Discovery

The system searches the proposal knowledge base.

Retrieval includes:

* Metadata Filtering
* Keyword Search
* Vector Search
* Hybrid Search
* Semantic Reranking

---

## Display

Top matching proposals.

Example:

Proposal A

Similarity Score: 96%

Proposal B

Similarity Score: 92%

Proposal C

Similarity Score: 89%

---

## User Action

The user selects a proposal and opens preview.

↓

---

# PHASE 5 – Proposal Preview

## Screen 5 – Proposal Preview

The selected proposal is displayed.

The user reviews:

* Structure
* Sections
* Flow
* Technical Content
* Level of Detail

The AI also shows:

### Similarity Breakdown

Industry Match

Solution Match

Architecture Match

Timeline Match

Overall Match

---

# USER DECISION POINT

At this stage the workflow branches into two possible paths.

---

# PATH A – Reuse Similar Proposal

## User Decision

The user selects:

### Use This Proposal

The user feels the retrieved proposal is highly relevant.

---

## AI Action

The platform uses the selected proposal as the baseline proposal.

The AI performs intelligent content replacement.

It updates:

* Client Information
* Business Context
* Requirements
* Timelines
* Stakeholders
* Deliverables
* Assumptions

using:

* Metadata
* Questionnaire Answers
* Uploaded Documents
* Meeting Notes
* Prompt Inputs

---

## Example

Original Proposal

Client:
ABC Healthcare

Timeline:
6 Months

Solution:
Patient Support Assistant

↓

Generated Proposal

Client:
XYZ Medical

Timeline:
4 Months

Solution:
Multilingual Customer Support Chatbot

---

## User Action

Generate Proposal

↓

Proposal Generation Progress

↓

Proposal Assembly Review

↓

Executive Summary Prompt

↓

Executive Summary Review

↓

Proposal Completed Successfully

---

# PATH B – Full AI Section Generation

## User Decision

The user selects:

### Customize & Generate

or

### Generate New Proposal

The user wants a more customized proposal.

---

## Screen 6 – Proposal Structure Builder

The AI extracts the proposal structure from the retrieved proposal.

Example:

1. Executive Summary

2. Business Context

3. Current Challenges

4. Proposed Solution

5. Technical Architecture

6. Implementation Plan

7. Team Structure

8. Pricing

9. Assumptions

10. Risks

---

## User Actions

* Rename Sections
* Add Sections
* Delete Sections
* Reorder Sections

---

## User Action

Approve Structure

↓

---

# PHASE 6 – Generation Setup

## Screen 7 – Generation Setup

Before generation begins:

The user reviews:

### Proposal Readiness

* Inputs Collected
* Structure Approved
* Missing Information Status

---

### Optional Research

Enable:

* Client Research
* Industry Research
* Architecture Research
* Timeline Suggestions

---

## User Action

Generate Proposal

↓

---

# PHASE 7 – Proposal Generation

## Screen 8 – Proposal Generation Progress

The proposal generation pipeline starts.

Workflow:

Requirement Analysis

↓

Context Retrieval

↓

Structure Alignment

↓

Section Generation

↓

Groundedness Validation

↓

Proposal Assembly

---

Users see:

* Overall Progress
* Current Activity
* Remaining Tasks

↓

---

# PHASE 8 – Section Tracking

## Screen 9 – Section Generation Tracking

Each section is generated individually.

Example:

Business Context

Completed

Technical Architecture

Generating

Implementation Plan

Retrieving Context

Pricing

Waiting

↓

---

# PHASE 9 – Section Review

## Screen 10 – Generated Section Review

For every generated section:

Display:

### Generated Content

### Supporting Sources

### Groundedness Score

### Coverage Score

### Knowledge Alignment

### Hallucination Risk

---

## User Actions

* Edit
* Regenerate
* Approve

Repeat until all sections are approved.

↓

---

# PHASE 10 – Proposal Assembly Review

## Screen 11 – Proposal Assembly Review

The system assembles the complete proposal.

Display:

* All Sections
* Complete Proposal Preview
* Quality Metrics

---

## User Actions

* Edit Sections
* Regenerate Sections
* Approve Proposal

↓

---

# PHASE 11 – Proposal Generated

## Screen 12 – Proposal Successfully Generated

The proposal is complete.

The system asks:

Would you like to generate an Executive Summary?

Options:

Generate Executive Summary

Skip

↓

---

# PHASE 12 – Executive Summary Review

## Screen 13 – Executive Summary Review

AI generates:

* Executive Overview
* Business Challenge
* Solution Summary
* Benefits
* Timeline
* Investment Summary

---

## User Actions

* Edit
* Regenerate
* Approve

↓

---

# PHASE 13 – Final Delivery

## Screen 14 – Proposal Completed Successfully

The final proposal package is delivered.

Available Deliverables:

### Proposal Document

### Executive Summary

### Validation Report

### Quality Metrics

---

## User Actions

* Download DOCX
* Download PDF
* Export Proposal
* Create New Proposal

---

# Final UI Workflow

Opportunity Discovery
↓
Transcript Intelligence (Optional)
↓
Input Consolidation
↓
Similar Proposal Discovery
↓
Proposal Preview
↓
Decision
↓

┌──────────────────────────┐
│ Use Similar Proposal     │
└──────────────────────────┘
↓
Smart Content Replacement
↓
Proposal Generation
↓
Proposal Assembly Review
↓
Executive Summary
↓
Final Delivery

OR

┌──────────────────────────┐
│ Full AI Generation       │
└──────────────────────────┘
↓
Proposal Structure Builder
↓
Generation Setup
↓
Proposal Generation Progress
↓
Section Generation Tracking
↓
Generated Section Review
↓
Proposal Assembly Review
↓
Executive Summary
↓
Final Delivery

This creates two generation experiences: a fast proposal adaptation path and a fully customized AI-generated proposal path, allowing users to choose between speed and flexibility.
