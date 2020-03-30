# PostcodeCrimeChecker
**Project**: Coursework 2 for SysDev ECM1421 Group Programming Exercise

The goal of this project is to create a program to the following spec:
"Each team is required to build a program with multiple Python modules of your own design. 

These modules, and functions within the modules, should be tested independently.

Your program must use a command-line interface to prompt the user for input parameters, display results, and provide user instructions, i.e. help. 

For commands that produce many lines of output your program should prompt the user for a file name, and save the output to that file.

When your program prompts for user input it must always accept the options of Quit and Restart."

## Table Of Contents

 - [Participants](#participants)
 - [Initial Planning Meeting](#initial-planning-meeting)
 - [MEETING 2 06/03](#meeting-2-0603)
 - [Snap meeting with Samir - Welcome to the team!](#snap-meeting-with-samir---welcome-to-the-team)
 - [MEETING 3 12/03](#meeting-3-1203)
 - [MEETING 4 19/03](#meeting-4-1903)
 - [MEETING 5 26/03 - FINAL MEETING BEFORE DEADLINE](#meeting-5-2603---final-meeting-before-original-deadline)
 - [MEETING 6 02/04 - FINAL MEETING BEFORE NEW DEADLINE](#meeting-6-0204---final-meeting-before-new-deadline)
 ***********************************************
## Participants

Bhavesh 

James 

Roksolana 

Sam 

Samir
***********************************************
## Initial Planning meeting
Date: 17/02/2020
### Agenda
 - Communications
   - Primary Method (Slack)
   - Weekly Meetings (Standups, Webex)
 - Coding Standards
   - Documenting (Docstrings, Banners, etc)
   - Naming conventions
   - Testing
   - TDD
 - Version Control and Infrastructure
   - Setup (Github)
   - Code Sharing (Github)
 - Milestones and Planning
   - Modules and general plan
   - Who will take what, when
 - Responsibilities
   - Team Roles (Not sure if designated roles needed or wanted)
 - Questions and Concerns
   - Anything to put into an email to module lead?
   - Any issues that people are aware of or are concerned about?
   
### MEETING OUTCOME
#### Communications
 - All agreed Slack as primary means of comms.
 - Weekly meetings @1100 on Thursdays for standup, express concerns, et al.
#### Coding Standards
 - ELE Docstrings link: https://vle.exeter.ac.uk/mod/page/view.php?id=748152
   - The video we want is "Documenting modules", 4th from the top
 - Docstrings to follow format:
   - What function does (brief, plain English explanation)
   - What it takes in (var names and data type)
   - What it returns (data type)
 - Naming convention:
   - functions and variables to be all lower case, "\_" to split up words
   -  Classes and Objects to have capitalised first letter (Turtle not turtle) - ask Sam if any queries on this
#### Version Control and Infrastructure
 - Github will become central repo for us to share code
   - This repo should be set to public, if any dramas contributing let Sam know.
#### Milestones and Planning
 - We will tackle the modules like so:
 Bhav:   Summary of Requirements and Work Breakdown - est 1st Draft completion of 09/03 (though a first draft look next week would be nice, though not to worry if not ready)
 Sam:    File Reading - First thoughts on how to tackle to be shared meeting 06/03
 Roxy:   Data Sorting and Filtering - First thoughts on how to tackle to be shared meeting 06/03
 James:  User Interface - First thoughts on how to tackle to be shared meeting 06/03

After these are done, the next most modules are:
File Writing - To be looked at by the person first to finish their section
Test Report - Testing to be handled by all in their respective modules and then to be collated at the end
#### Responsibilities
 - Not discussed, not needed as this is superceded by outcome of Milestones and Planning
#### Questions and Concerns
 - Will try emailing Frank Hermann to get answer to Sam's questions to Saunby (Sam to do)
 
NEXT MEETING TO BE IN PERSON, AT ALS on 06/03 - ALS made virtual, so our meeting was virtual
***********************************************
## MEETING 2 06/03
### Agenda
#### 1st week efforts
 - Outcome of emailing Frank (Sam)
 - Bhav's first notes (if possible, Bhav)
 - Roxy's first thoughts (Roxy)
 - James' first thoughts (James)
 - Sam's first thoughts (Sam)
Each person is to give an assessment and report detailing these at least:
 - Implementation thoughts
 - What they need from other's modules
 - Predicted and Encountered Difficulties

### MEETING OUTCOME
#### Outcome of emailing Frank (Sam)
 - Not done yet, will do again soon
#### Group first Thoughts
 - Bhav, First draft around Wednesday
 - James' UI rough plan to follow something like this:
  1) Welcome screen
  2) Ask for a centre-point postcode
  3) Ask for a radius (1,2,5Km)
  4) Ask for a sort type (Distance, Date, Crime Category)
  5) Ask for a user-defined report name
  6) Confirmation
  At all times, restart and quit are available options. Restart will begin the loop again; quit will close the program. 
 - Sam will get the file reading completed by Thurs next week.
 - Bhav's report can be added to as we go as more requirements are sorted. 
#### Implementation thoughts
 - It was decided that all data from files will be taken in as a list as this is what the group is most comfortable dealing with. 
 - If any are unsure how to use Guthub they can send their files to Sam in order to upload them. 
#### What they need from other's modules
 - The mentioned lists
#### Predicted and Encountered Difficulties
 - James not available Mon 09/03 evening
 - Sam not available 13/03-15/03
***********************************************
## Snap meeting with Samir - Welcome to the team!
 - Brought him up to speed that we're using Github
 - Samir will take the file reading job
  - Will take a look at and give us a plan on:
   - How he thinks he will write to the file
   - How he initially thinks the report will look like
   - What data he thinks he will need to get the report
***********************************************
## MEETING 3 12/03
### Agenda
#### 2nd week efforts
 - If Sam gets time to: A rough diagram of the structure of the program (up for debate, something for us to look at as a reference tool but not as a bible).
 - Discussion about which columns from the postcodes and crime data .csv files we will actually need - THIS IS USEFUL FOR THE DATA FILTERING PART OF GENERATING THE REPORT.
 - Outcome of emailing Frank (Sam)
 - Bhav's Report/Notes (if possible, Bhav)
 - Roxy's first thoughts (Roxy)
 - James' first thoughts (James)
 - Sam's first thoughts (Sam)
 - Implementation thoughts
 - What they need from other's modules
 - Predicted and Encountered Difficulties

### MEETING OUTCOME
#### If Sam gets time to: A rough diagram of the structure of the program (up for debate, something for us to look at as a reference tool but not as a bible).
 - No diagram, though notes and an explanation on how it should all come together was discussed - no objections.
#### Discussion about which columns from the postcodes and crime data .csv files we will actually need - THIS IS USEFUL FOR THE DATA FILTERING PART OF GENERATING THE REPORT.
 - Agreed that the columns from the crime files to include in the final report are:
  - Crime ID
    Month Reported
    Distance from centre
    Longitude
    Latitude
    Location
    Crime type
    Last outcome category
 - It was discussed that the lat and long may be omitted later.
#### Outcome of emailing Frank (Sam)
#### Bhav's Report/Notes (if possible, Bhav)
 - Have been submitted, not yet reviewed but Sam will take a look and send thoughts over right after meeting
#### Roxy's first thoughts (Roxy)
 - Having discussed implementation with Roxy, we now have a plan on how her module's logic will work
#### James' first thoughts (James)
 - James has submitted his first draft and will implement this more fully in the next week
#### Sam's first thoughts (Sam)
 - Has submitted his section for others to view, will continue to offer support to others' sections
#### Samir's section
 - We have now discussed some likely areas to research for how to implement the code. 
 - First draft expected by next week
#### Implementation thoughts
 - Overall "main" module discussed, no objections.
#### What they need from other's modules
 - Defined that James' UI will send a dictionary to others for their use. 
 - Defined what columns are going to be needed in the report.
#### Predicted and Encountered Difficulties
 - Sam will be largely out of contact for this weekend. Feel free to message on Whatsapp but expect delays on responses.
 
 ***********************************************
## MEETING 4 19/03
### Agenda
#### 3rd week efforts
 - If Sam gets time to: A rough diagram of the structure of the program (up for debate, something for us to look at as a reference tool but not as a bible).
 - Outcome of email chain Michael (Sam)
   - We can choose our implementation
   - What this means for printing the report (NEW REQM'T, only if the report is short)
   - Preprocessing of files (see below)
 - Discussion regarding Issue #23
   - How we are going to arrange our new file system
   - What to call the new files
   - Any file formats we want
   - Which rows to lose from postcodes.csv (crimefiles.csv col's have already been discussed and agreed on)
 - Bhav's Report/Notes, anyone else's thoughts so far.
 - Roxy's first full draft of the code (Roxy)
   - Do we want to record the distance from the crime, rather than the coordinates?
 - James' first full draft of the code (James)
   - I have send a series of notes to James and have included in the files
 - Sam's first full draft of the code (Sam)
   - Talk through the main.py logic and how it will all tie together.
 - Samir's first full draft of the code (Samir)
   - If not yet ready, then and ETA and a talk through of his implementation
 - Implementation thoughts, anthing which has come up.
 - Predicted and Encountered Difficulties
 - Github
   - Please, everyone assign issues to themselves (go through the backlog). 
   - Add selves to repo.
   
### MEETING OUTCOME
Absences: Samir; Bhav
#### If Sam gets time to: A rough diagram of the structure of the program (up for debate, something for us to look at as a reference tool but not as a bible).
 - No diagram, though notes and an explanation on how it should all come together was discussed - no objections.
 - If Sam gets time to: A rough diagram of the structure of the program (up for debate, something for us to look at as a reference tool but not as a bible).
#### Outcome of email chain Michael (Sam)
   - Discussed. See next point for more on this. 
   - Also agreed that we will eschew printing the file for now, can add this functionality later. 
#### Discussion regarding Issue #23
   - Agreed that this is something we can get done later, once we have the minimum viable product worked out and ready.
#### Bhav's Report/Notes, anyone else's thoughts so far.
#### Roxy's first full draft of the code (Roxy)
   - Found that the distance from the crime is recorded, so we can add this to the report.
   - Roxy agreed to get next draft in for 
#### James' first full draft of the code (James)
   - I have send a series of notes to James and have included in the files. Went through in some detail in meeting also.
   - James agreed to have next draft in for Monday morning (23/03)
   - Made aware of the use of the messages.py idea, will discuss more later.
#### Sam's first full draft of the code (Sam)
   - Talk through the main.py logic and how it will all tie together.
   - Well received, made participants aware that the code will likely be massaged 
#### Samir's first full draft of the code (Samir)
   - If not yet ready, then and ETA and a talk through of his implementation
#### Implementation thoughts, anthing which has come up.
   - Discussed in the rest of the meeting
#### Predicted and Encountered Difficulties
   - None
#### Github
   - James and Roxy agreed to add to repo and go through backlog for their issues
***********************************************
## MEETING 5 26/03 - FINAL MEETING BEFORE ORIGINAL DEADLINE
### Agenda
#### 4th week efforts
 - Final drafts have to be in by following day at noon, latest.
 - Final checks will be done on the Saturday (28/03) by SR.
 - Late submissions accepted until Sunday evening but will be of a low priority. If the minimum viable product is ready then I am hesitant to add last-minute changes.
 - SR will submit.
 - PEER EVALUATION FORMS! https://vle.exeter.ac.uk/course/view.php?id=6129&section=25
   - Bhav, might be able to do the rounding to 3dp? 
 - Final project thoughts:
   - Do we want to round the results of the distance? Maybe to 3dp?
 - Final Draft Submissions received from:
   - James
   - Roxy
 - Waiting on:
   - Samir
   - Bhav (might already be in, ask for final draft anyway).
### MEETING OUTCOME
Absences: Samir; Bhav
#### Final drafts have to be in by following day at noon, latest.
  - Discussed, OK'd
#### Final checks will be done on the Saturday (28/03) by SR.
  - Made aware.
#### Late submissions accepted until Sunday evening but will be of a low priority. If the minimum viable product is ready then I am hesitant to add last-minute changes.
  - Not really discussed, all present had given final product; more for th absent.
#### SR will submit.
  - OK'd
#### PEER EVALUATION FORMS! https://vle.exeter.ac.uk/course/view.php?id=6129&section=25
 - All aware, happy, know to submit their forms themselves.
#### Final project thoughts:
   - Agreed to round the results of the distance to 3dp - (ROXY to do)
#### Final Draft Submissions received from:
   - James
   - Roxy
#### Waiting on:
   - Were not present so couldn't ask about:
   - Samir
   - Bhav (might already be in, ask for final draft anyway).

***********************************************
## MEETING 6 02/04 - FINAL MEETING BEFORE NEW DEADLINE
### Agenda
#### 4th week efforts
 - Congratulations Team!
 - Very final submissions if anyone forgets anything will be Saturday evening.
   - SR will work on these on Sunday, Whatsapp and Slack SR to inform of this.
   - Late submissions accepted will be of a low priority. If the minimum viable product is ready then I am hesitant to add last-minute changes.
 - SR will submit.
   - Need a volunteer to peer review the submission for errors and omissions.
 - PEER EVALUATION FORMS! https://vle.exeter.ac.uk/course/view.php?id=6129&section=25
 - Final project thoughts:
   - Any?
 - Good work team, you all worked well and I'm pleased with your efforts. While you can't take a break until after the exams, you've certainly earned one.
