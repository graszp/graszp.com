<!-- 
graszp SAN template, from https://graszp.com
Licence: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Credit: graszp.com, Vernacular Cloud LLC.

Template version: 0.1 (2026-10-28) Sources: 
- TOGAF ADM (phases A–H)
- ArchiMate (motivation, core and implementation & migration elements)
- PRINCE2 (processes, RAID)
- Scrum (sprints, Definition of Done)
- ITIL
- Microsoft Solutions Framework (Envision).  

[!info] Conventions 
1. Never delete a heading. If it does not apply, write "N/A — <reason>". A considered N/A is a governance trace.
2. Depth is the dial, not the outline. Small/agile project: one line per heading. Governed project: link each heading to a fuller artifact (model, register, spec). 
3. Questions in *italics* are prompts. Replace them with answers; keep them only while a heading is unanswered. \
4. The AI reads this note first and proposes text; the author edits the note. 
5. Tags in [brackets] show where a heading came from. Keep or delete them as you like. 

-->
# Project-Envision
[TOGAF Phase A Architecture Vision · MSF Envisioning] _What is this project trying to accomplish, in a high level summary? What does "done" look like from the outside?_ _Is this  a pilot or reference case for something larger?_
# Project-Estimate
[PRINCE2 Business Case · Scrum forecasting] _How big is it — hours, weeks, sprints? What drives the uncertainty?_ _What is "good enough", and who decides?_
# Project-Promote
[Stakeholder communication · marketing] _Who outside the project might care about the result? Why would they?_ _What must exist before it is worth showing to anyone?_ _What communication channels might be effective?_
# Project-Direct
[PRINCE2 Directing a Project] _Who sets priorities and authorises each stage? How much of the author's attention does it get?_ _What else competes for that attention?_
# Project-Initiate
[PRINCE2 Starting up / Initiating a Project] _When and how does the project formally start? What has to be set up first (repos, tools, AI project, folders, roles)?_
# Project-Plan
## Project-Plan-Motivation
[ArchiMate Motivation elements · TOGAF Phase A / Requirements Management]
### Project-Plan-Motivation-Stakeholder
_Who has an interest? For each: role, what they want, how and how often to communicate._
### Project-Plan-Motivation-Driver
_Why does this matter beyond its own outcome? Which larger goals (career, study, programme, organization) push it?_
### Project-Plan-Motivation-Assessment
_Given those drivers, what is the honest state of affairs today? Strengths, weaknesses,  opportunities, threats, unknowns?_
### Project-Plan-Motivation-Goal
_What does the project aim to achieve? (Direction, not yet measurable. Stories, Use Cases.)_
### Project-Plan-Motivation-Outcome
_What measurable end result shows the goals were met?_
### Project-Plan-Motivation-Principle
_Which standing rules guide every decision? (e.g. "single source of truth", "permalinks never break")_
### Project-Plan-Motivation-Requirement
#### Project-Plan-Motivation-Requirement-Feature
_What must the solution do? 
#### Project-Plan-Motivation-Requirement-Quality
_How well must it do it — reliability, maintainability, review, standards conformance?_
### Project-Plan-Motivation-Constraint (RAID)
[ArchiMate Constraint · PRINCE2 RAID]
#### Project-Plan-Motivation-Constraint-Risk
_What might go wrong? Likelihood, impact, response._
#### Project-Plan-Motivation-Constraint-Assumption
_What are we taking as true without proof?_
#### Project-Plan-Motivation-Constraint-Issue
_What is already a problem?_
#### Project-Plan-Motivation-Constraint-Dependency
_What must arrive from outside the project?_
### Project-Plan-Motivation-Value
_What does each stakeholder actually get out of it?_
## Project-Plan-Business
[ArchiMate Business layer · TOGAF Phase B]
### Project-Plan-Business-Actor
_Who (people, roles, organisations) does the work or uses the result?_
### Project-Plan-Business-Process
_What sequence of work produces the result? (e.g. author → review → publish)_
### Project-Plan-Business-Function
_What ongoing capabilities does the work fit into?_
### Project-Plan-Business-Object
_What business-level information items does the work handle? (concepts, documents, records)_
### Project-Plan-Business-Representation
_In what perceptible forms do those items appear? (websites, documents, posts)_
## Project-Plan-Application
[ArchiMate Application layer · TOGAF Phase C]
### Project-Plan-Application-Component
_Which programs, scripts or apps make up the solution?_
### Project-Plan-Application-Function
_What does each component do?_
### Project-Plan-Application-Interface
_Where do components hand off to each other or to people?_
### Project-Plan-Application-Service
_What externally visible services does the solution use or offer?_
### Project-Plan-Application-Data
_What data objects (files, formats, schemas) flow through it?_
## Project-Plan-Technology
[ArchiMate Technology layer · TOGAF Phase D]
### Project-Plan-Technology-Node
_On what machines, platforms or cloud services does it run?_
### Project-Plan-Technology-Software
_Which languages, runtimes, libraries and tools?_
### Project-Plan-Technology-Artifact
_Which concrete files, repositories, and folders? Where are they stored?_
## Project-Plan-Migration
[ArchiMate Implementation & Migration · TOGAF Phases E–F]
### Project-Plan-Migration-Plateau
_What stable states will the solution pass through? (e.g. release versions)_
### Project-Plan-Migration-WorkPackage
_What units of work move it from one plateau to the next? (e.g. sprints)_
### Project-Plan-Migration-Deliverable
_What does each work package hand over to the next plateau?_
# Project-Decision
[TOGAF Architecture Decision Log · ADR] _One line per decision: ID, date, decision, why, alternative rejected._
- D-001 YYYY-MM-DD decision (Why: … Alt: …)
# Project-Manage
[PRINCE2 Controlling a Stage · Scrum events] _What rhythm keeps the work moving — planning, review, retrospective? Which tools and methods?_
# Project-Deliver
[SDLC: ISO/IEC 12207 · ITIL · Scrum Definition of Done · TOGAF Phase G seam]
_How are particular sequences, stages, iterations, or sprints between plateaus defined, controlled, and executed? Each stage names the architecture section it draws on._
## Project-Deliver-Scope
_What is in and out? ← Motivation-Goal, Requirement_
## Project-Deliver-Specify
_What exactly must be built and to what standard? ← Requirement-Feature, Requirement-Quality_
## Project-Deliver-Design
_How will it be built? ← Business / Application / Technology layers; record choices in Project-Decision_
## Project-Deliver-Build
_What gets made, with what tools? → Technology-Software, Technology-Artifact_
## Project-Deliver-Test
_How do we know it works? ← Requirement-Quality_
## Project-Deliver-Accept
_Who accepts it, against which outcome? ← Motivation-Outcome, Stakeholder_
## Project-Deliver-Deploy
_How does it reach users? → Migration-Plateau_
## Project-Deliver-Support
_Who runs and fixes it afterwards? ← Application-Service, Technology-Node_
## Project-Deliver-Retire
_How is it switched off, archived or replaced? → Project-Close_
# Project-Report
[PRINCE2 highlight reports · Scrum Sprint Review] _Where does status live? Who has access to it?_ _What level of detail is appropriate?_
## Project-Report-Dashboards
_How is the project summarized and presented to actors and stakeholders??_
## Project-Report-Sprints
_One entry per sprint. Sprints are time-boxes; plateaus are releases._
### S-001 YYYY-MM-DD sprint goal
- Target plateau:
- Goals
- Decisions (D-ids)
- Outcomes
- Carry-overs
## Project-Report-Potential
_Capture ideas for later review in an unorganized list of potential features, qualities, requirements, decisions, constraints. Does this have a name in the the TOGAF or Agile worlds?_ 
# Project-Close
[PRINCE2 Closing a Project · TOGAF Phase H] _How and when does it end? What is handed over, archived, or turned into a new project?_
