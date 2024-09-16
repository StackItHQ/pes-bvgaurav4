[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AHFn7Vbn)
# Superjoin Hiring Assignment

### Welcome to Superjoin's hiring assignment! 🚀

### Objective
Build a solution that enables real-time synchronization of data between a Google Sheet and a specified database (e.g., MySQL, PostgreSQL). The solution should detect changes in the Google Sheet and update the database accordingly, and vice versa.

### Problem Statement
Many businesses use Google Sheets for collaborative data management and databases for more robust and scalable data storage. However, keeping the data synchronised between Google Sheets and databases is often a manual and error-prone process. Your task is to develop a solution that automates this synchronisation, ensuring that changes in one are reflected in the other in real-time.

### Requirements:
1. Real-time Synchronisation
  - Implement a system that detects changes in Google Sheets and updates the database accordingly.
   - Similarly, detect changes in the database and update the Google Sheet.
  2.	CRUD Operations
   - Ensure the system supports Create, Read, Update, and Delete operations for both Google Sheets and the database.
   - Maintain data consistency across both platforms.
   
### Optional Challenges (This is not mandatory):
1. Conflict Handling
- Develop a strategy to handle conflicts that may arise when changes are made simultaneously in both Google Sheets and the database.
- Provide options for conflict resolution (e.g., last write wins, user-defined rules).
    
2. Scalability: 	
- Ensure the solution can handle large datasets and high-frequency updates without performance degradation.
- Optimize for scalability and efficiency.

## Submission ⏰
The timeline for this submission is: **Next 2 days**

Some things you might want to take care of:
- Make use of git and commit your steps!
- Use good coding practices.
- Write beautiful and readable code. Well-written code is nothing less than a work of art.
- Use semantic variable naming.
- Your code should be organized well in files and folders which is easy to figure out.
- If there is something happening in your code that is not very intuitive, add some comments.
- Add to this README at the bottom explaining your approach (brownie points 😋)
- Use ChatGPT4o/o1/Github Co-pilot, anything that accelerates how you work 💪🏽. 

Make sure you finish the assignment a little earlier than this so you have time to make any final changes.

Once you're done, make sure you **record a video** showing your project working. The video should **NOT** be longer than 120 seconds. While you record the video, tell us about your biggest blocker, and how you overcame it! Don't be shy, talk us through, we'd love that.

We have a checklist at the bottom of this README file, which you should update as your progress with your assignment. It will help us evaluate your project.

- [ ] My code's working just fine! 🥳
- [ ] I have recorded a video showing it working and embedded it in the README ▶️
- [ ] I have tested all the normal working cases 😎
- [ ] I have even solved some edge cases (brownie points) 💪
- [ ] I added my very planned-out approach to the problem at the end of this README 📜

## Got Questions❓
Feel free to check the discussions tab, you might get some help there. Check out that tab before reaching out to us. Also, did you know, the internet is a great place to explore? 😛

We're available at techhiring@superjoin.ai for all queries. 

All the best ✨.

## Developer's Section
*Add your video here, and your approach to the problem (optional). Leave some comments for us here if you want, we will be reading this :)*

## My Approach

here is my approach 
first i made a server which can handle the CRUD and the spreadsheets

1. Database
      - the database I used was MYSQL cause its easy and has a better performance compared to postgres
      - i made 2 tables the schema is given in the my_sql.sql file
2. Google Cloud api
      - i have used google spread sheets and google apps scripts apis and drive api 
      - this is for creating and CRUD for the spreadsheets
3. NGROK
    - this is for tunneling


I made a server using python flask and made endpoints for he CRUD operations ins server.py file.

## requirments

    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

    pip install gspread

    pip install flask

    pip install pyngrok 


the functions file has the all the spreadsheets CRUD operations

## Usage
    

    first start the server by running server  by
    python server.py

    then on a different terminal run the tunnel

    python tunneling.py

    this will setup a tunnel for the server 
    this is set to post 5000

- then open postman or send a post request  to the server at the  create_spreadsheet endpoint to create the spreadsheet

- then u will get the spreadsheet_id open this spread sheets and add the extentions apps scripts and paste the trigger.gs file in the code editor to create a trigger this is for the 1. Real-time Synchronisation of the sheet and the database 

appscrits.json
this is the settings to make it visible.
and paste it in that
![alt text](image.png)

i coudnt auto mate this cause i kept getting 403 error even with the SCOPES set.

- create a trigger and change the event type to "on edit"

- this will notify the server the changes to the server and the server will change the data on the spread sheet if u change the data on the database.


i have done the authorization so u dont have to.

## Demo

videos

https://drive.google.com/file/d/116hI-me14GOLwjnG9RXVzwYZHWCA6lq6/view?usp=sharing, 
https://drive.google.com/file/d/1rJTKIlFOQIm2YH-v9r1HohS06SgSvcx_/view?usp=sharing
