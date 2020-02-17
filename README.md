# SE341
This application is made for the SE 341 Undergrad Research class of Spring 2020 at SCSU. 

Background:
	Healthy Huskies is a health organization at St. Cloud State University, and one of their responsibilities is to handle questions/requests from students via phone (notably Husky PUP sessions or IMPACT class registration). The telephone operator can answer most of these questions/requests, but there are times where the question/request must be handled by a superior (at least once a day). These superiors are often busy so the telephone operator either leaves an email or a sticky note with details for the superior to call the student back at a later date. 
	The problem is that emails/stick notes become lost due to the superiors being overloaded with work, so they never call the user back to fulfill their request. Healthy Huskies has received many angry complaints from students for this very reason, and superiors have voiced their frustration with the current system.

Objective:
Create an application that allows a user (Telephone operator) to write a callback note with student information (Student ID, phone number, reason for call, etc) and store it in a repository. It shall allow another user (Supervisor) to access the repository and see detailed callback notes and sign off on it upon completion.

User Stories:
- A user (Telephone operator) shall be able to write a callback note with student information (Student ID, phone number, reason for call, date, etc)
- The software shall store the note into a repository with the status of “unfinished”
- A user (Superiors) will access the repository and view all callback notes, “unfinished” and “completed”.
- Once a user (Superiors) completes an unfinished callback note, they shall be able to tag that note as “completed” with their name and date.
- The repository shall keep the completed callback notes for reference.
