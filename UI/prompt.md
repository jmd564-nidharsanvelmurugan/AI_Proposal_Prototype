You are a senior Next.js architect and frontend engineer.

Generate a complete production-quality Next.js application that demonstrates the full UI workflow of an AI Proposal Copilot platform.

IMPORTANT REQUIREMENTS

This is a UI prototype only.

Do NOT implement any real backend.

Do NOT implement any database.

Do NOT implement Azure services.

Do NOT implement vector search.

Do NOT implement AI calls.

Do NOT implement retrieval systems.

Do NOT implement LangGraph.

Do NOT implement MCP.

Do NOT implement authentication.

Do NOT implement external APIs.

Do NOT create server actions.

Do NOT create actual API routes.

Everything should be simulated using mock data, local state, sample JSON files, and fake async delays.

The objective is to demonstrate the complete user workflow using frontend-only code.

Use dummy data everywhere.

Use mock API functions only.

Example:

```typescript
const fetchSimilarProposals = async () => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(mockProposalData);
    }, 1500);
  });
};
```

No actual API calls should occur.

---

TECH STACK

Next.js 15 App Router

TypeScript

Tailwind CSS

shadcn/ui

Lucide Icons

Framer Motion

React Hook Form

Zustand for state management

Use modern folder structure.

---

PROJECT STRUCTURE

Generate complete code structure.

Include:

app/

components/

hooks/

lib/

store/

types/

data/

public/

---

GLOBAL APPLICATION STATE

Create a ProposalStore using Zustand.

Store:

metadata

questionnaireAnswers

uploadedFiles

selectedProposal

proposalStructure

generatedSections

executiveSummary

proposalStatus

sectionStatus

readinessScore

---

MOCK DATA

Create mock data files.

metadata.ts

questionnaire.ts

similarProposals.ts

generatedProposal.ts

executiveSummary.ts

validationScores.ts

Use realistic proposal content.

---

WORKFLOW

Implement the following screens.

Use routing between pages.

---

SCREEN 1

Opportunity Discovery

Route:

/opportunity-discovery

Features:

Metadata Form

Client Name

Industry

Solution Type

Project Category

Questionnaire Inputs

Free Text Prompt

Upload Components

Transcript

MOM

RFP

Discovery Notes

Right Side:

AI Extracted Information Card

Proposal Readiness Score

Missing Information Card

Continue Button

Populate all data using mock extraction logic.

---

SCREEN 2

Transcript Intelligence

Route:

/transcript-intelligence

Optional screen.

Display uploaded transcript.

Show extracted information.

Show missing fields.

Continue button.

Skip button.

---

SCREEN 3

Input Consolidation

Route:

/input-consolidation

Display all collected information.

Metadata

Questionnaire

Prompt

Transcript

Requirements

Missing Information

Continue button.

---

SCREEN 4

Similar Proposal Discovery

Route:

/similar-proposals

Display proposal cards.

Proposal Name

Similarity Score

Industry Match

Solution Match

Timeline Match

Actions:

Preview

Select

Display three sample proposals.

---

SCREEN 5

Proposal Preview

Route:

/proposal-preview

Display selected proposal.

Left:

Proposal Content Preview

Right:

Extracted Structure

Decision Section

Buttons:

Use Similar Proposal

Customize & Generate

---

WORKFLOW BRANCHING

IF

User clicks:

Use Similar Proposal

Then navigate to:

/proposal-generation-progress

Simulate proposal regeneration using content replacement.

Skip structure builder.

Skip section generation.

Skip section review.

Proceed directly to assembly review.

---

IF

User clicks:

Customize & Generate

Then navigate to:

/proposal-structure-builder

---

SCREEN 6

Proposal Structure Builder

Route:

/proposal-structure-builder

Features:

Section List

Drag and Drop

Add Section

Delete Section

Rename Section

Approve Structure

---

SCREEN 7

Generation Setup

Route:

/generation-setup

Features:

Readiness Summary

Research Toggles

Enable Client Research

Enable Industry Research

Enable Architecture Research

Enable Timeline Suggestions

Generate Proposal Button

---

SCREEN 8

Proposal Generation Progress

Route:

/proposal-generation-progress

Simulate generation process.

Animated progress.

Workflow:

Requirement Analysis

Context Retrieval

Structure Alignment

Section Generation

Groundedness Validation

Proposal Assembly

Progress bar.

Auto navigate when complete.

---

SCREEN 9

Section Generation Tracking

Route:

/section-generation-tracking

Show section cards.

Business Context

Architecture

Timeline

Pricing

Risk

Statuses:

Completed

Generating

Waiting

View Section Button

---

SCREEN 10

Generated Section Review

Route:

/generated-section-review

Display generated content.

Validation Panel:

Groundedness

Coverage

Alignment

Hallucination Risk

Buttons:

Edit

Regenerate

Approve

---

SCREEN 11

Proposal Assembly Review

Route:

/proposal-assembly-review

Display complete proposal.

Left:

Section Navigation

Center:

Proposal Content

Right:

Proposal Quality Summary

Buttons:

Edit

Approve Proposal

---

SCREEN 12

Proposal Successfully Generated

Route:

/proposal-generated

Display:

Would you like to generate Executive Summary?

Buttons:

Generate

Skip

---

SCREEN 13

Executive Summary Review

Route:

/executive-summary-review

Display executive summary.

Buttons:

Edit

Regenerate

Approve

---

SCREEN 14

Proposal Completed Successfully

Route:

/proposal-completed

Display:

Proposal Delivered

Executive Summary

Validation Report

Buttons:

Download DOCX

Download PDF

Create New Proposal

---

COMPONENTS

Create reusable components.

ProposalCard

ReadinessScore

ProgressTimeline

ProposalPreview

SectionCard

ValidationCard

ExecutiveSummaryCard

WorkflowStepper

FileUploader

QuestionnaireForm

MetadataForm

---

UI REQUIREMENTS

Keep UI simple.

Focus on workflow.

Do not add extra dashboards.

Do not add analytics screens.

Do not add user management.

Do not add billing.

Do not add authentication.

Use spacious layouts.

Use enterprise styling.

Use consistent navigation.

Every page should have:

Back Button

Continue Button

Workflow Progress Indicator

---

DELIVERABLE

Generate the COMPLETE Next.js codebase.

Include:

All pages

All components

All mock data

All Zustand stores

All types

All Tailwind styling

All routing

All imports

All file structure

Provide the code file-by-file in proper project structure.

The application must run immediately after:

npm install

npm run dev

without requiring any backend service.
