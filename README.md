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
 
## Participants

Bhavesh 

James 

Roksolana 

Sam 

Samir

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
 
NEXT MEETING TO BE IN PERSON, AT ALS on 06/03

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

## Snap meeting with Samir - Welcome to the team!
 - Brought him up to speed that we're using Github
 - Samir will take the file reading job
  - Will take a look at and give us a plan on:
   - How he thinks he will write to the file
   - How he initially thinks the report will look like
   - What data he thinks he will need to get the report

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

