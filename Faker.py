# TODO: option to select all cols with suggected col names, with clear all schema data
# TODO: defa to create new and load should clear schema

# Category Number | min & max range :=> Salary, Amount, Age...
# Category DOB |  min & max years range so that age is between a & b

# Imports
import streamlit as st
import pandas as pd
import random
import shortuuid
import re
from datetime import datetime as dt
from datetime import timedelta

# SCTN: variables:

FemaleFirstNamesList = ["Aadhira", "Aadhya", "Aadya", "Aahana", "Aanya", "Aaradhya", "Aaravi", "Aarna", "Aarohi", "Aarushi", "Aarvi", 
                        "Aarya", "Aashi", "Aashna", "Aashvi", "Aavya", "Adah", "Adhira", "Adhya", "Adira", "Aditi", "Advika", "Ahana", 
                        "Aija", "Aisha", "Aishani", "Aishwarya", "Aja", "Akasha", "Akira", "Akshara", "Alia", "Alisha", "Alka", "Amaira", 
                        "Amar", "Amara", "Amaya", "Amayra", "Ambar", "Amina", "Amrita", "Anaisha", "Anala", "Ananda", "Ananya", "Anaya", 
                        "Angee", "Anika", "Anila", "Anisha", "Anjali", "Anuka", "Anura", "Anusha", "Anushka", "Anvi", "Aradhana", "Aradhya", 
                        "Aria", "Arohi", "Arya", "Asha", "Ashna", "Ashvi", "Avani", "Avantika", "Avika", "Avira", "Avisha", "Avni", "Ayra", 
                        "Banita", "Bhumi", "Bodhi", "Carina", "Chaaya", "Charisma", "Charu", "Charvi", "Chavi", "Chaya", "Chella", "Chinmayi", 
                        "Daanya", "Darsha", "Deetya", "Devanshi", "Devi", "Devika", "Dhriti", "Dhruvika", "Didi", "Disha", "Divya", "Diya", 
                        "Eesha", "Eila", "Ela", "Elina", "Esha", "Eshaal", "Farah", "Fatima", "Gargi", "Garima", "Gauri", "Gayatri", "Gracia", 
                        "Hamsa", "Hana", "Haniya", "Hansika", "Harini", "Hasina", "Himani", "Hira", "Hiral", "Inaya", "Indira", "Ira", "Isha", 
                        "Ishaani", "Ishana", "Ishani", "Ishika", "Ishita", "Jaanvi", "Janvi", "Jasleen", "Jaya", "Jenisha", "Jhanvi", "Jia", 
                        "Jiya", "Kaeya", "Kaia", "Kaira", "Kali", "Kamala", "Kamya", "Kanya", "Karma", "Kashmir", "Kashvi", "Kavya", "Kayra", 
                        "Kiara", "Kimaya", "Kiran", "Kirti", "Kiya", "Krisha", "Krishika", "Kyra", "Kyrah", "Lakshmi", "Lara", "Larisa", "Lata", 
                        "Lavya", "Laya", "Layla", "Leela", "Leena", "Leia", "Leya", "Lila", "Lisha", "Maahi", "Maanvi", "Mahira", "Mariam", 
                        "Mayra", "Meena", "Meera", "Megha", "Mehar", "Minal", "Mira", "Mirha", "Misha", "Mishika", "Mishka", "Myra", "Naina", 
                        "Naira", "Naisha", "Nalini", "Nandini", "Nara", "Navya", "Naya", "Nayana", "Neela", "Neena", "Neesha", "Neev", "Neha", 
                        "Neysa", "Niara", "Nidhi", "Niharika", "Nikita", "Nila", "Nirali", "Nisha", "Nivisha", "Nyla", "Nyra", "Opal", "Pari", 
                        "Parina", "Pihu", "Pragya", "Pranavi", "Pravya", "Prisha", "Priya", "Radha", "Radhika", "Radhya", "Raina", "Rama", 
                        "Rani", "Rania", "Rayna", "Reva", "Reya", "Rhea", "Ria", "Riddhi", "Ridhi", "Rina", "Rita", "Ritvi", "Riya", "Saanvi", 
                        "Sahana", "Saira", "Saisha", "Salina", "Samaira", "Samara", "Sana", "Sanaya", "Saniya", "Sanvi", "Sara", "Sarita", 
                        "Seema", "Sena", "Shalee", "Shanaya", "Shante", "Sharvi", "Shivanya", "Shree", "Shreya", "Shreyanvi", "Shruti", "Shyla", 
                        "Sia", "Sitara", "Siya", "Sona", "Sony", "Suhana", "Swara", "Taara", "Tamia", "Tanvi", "Tanya", "Tara", "Taruni", "Tia", 
                        "Tiya", "Trisha", "Tula", "Tulsi", "Turvi", "Uma", "Vaani", "Vaanya", "Vamika", "Vanya", "Vara", "Varsha", "Veda", 
                        "Vedanshi", "Veena", "Vianca", "Vidya", "Viha", "Vrinda", "Yashika", "Yashvi", "Zara", "Ziana", "Ziva", "Zoya"]


MaleFirstNamesList = ["Aadi", "Aadiv", "Aahan", "Aandaleeb", "Aarav", "Aarush", "Aaryan", "Abdul", "Abeer", "Abhay", "Abhinav", "Abhiram", 
                      "Adhiraj", "Aditya", "Advait", "Advay", "Advik", "Agastya", "Agilan", "Ahaan", "Ahmed", "Aija", "Ajay", "Ajit", "Akarsh", 
                      "Akash", "Akhil", "Akshat", "Akshay", "Aleem", "Aman", "Amar", "Amay", "Ameya", "Amit", "Amrit", "Anand", "Anang", "Anant", 
                      "Ananya", "Anay", "Angad", "Anik", "Anirudh", "Anjay", "Ansh", "Anshu", "Anshuman", "Anvik", "Arik", "Arin", "Arjan", 
                      "Arjun", "Arnav", "Arun", "Arush", "Arya", "Aryan", "Asha", "Ashish", "Ashvath", "Ashwath", "Ashwin", "Atharv", "Atharva", 
                      "Avan", "Avi", "Avinash", "Avyaan", "Ayaan", "Ayaansh", "Ayush", "Balakrishna", "Bali", "Balveer", "Bhoja", "Bhuv", 
                      "Bhuvan", "Bodhi", "Chaganti", "Chaitanya", "Charun", "Charvik", "Chetan", "Chintak", "Chirayu", "Daksh", "Dakshesh", 
                      "Darsh", "Darshan", "Deepak", "Dev", "Devaansh", "Devansh", "Deven", "Dharma", "Dheeraj", "Dhruv", "Din", "Dinesh", 
                      "Divit", "Eeshan", "Ehan", "Ekansh", "Eshan", "Farhan", "Farid", "Gambhira", "Gautam", "Hanita", "Harish", "Harshad", 
                      "Hem", "Hemant", "Himesh", "Hiral", "Hridaan", "Hriday", "Hrithik", "Indra", "Indrajit", "Iraja", "Ishaan", "Ishan", 
                      "Ishank", "Ishir", "Ivaan", "Jagachandra", "Jai", "Jash", "Jay", "Jiyansh", "Kabir", "Kahaan", "Kailash", "Kairav", 
                      "Kali", "Kalindi", "Kamal", "Kanan", "Kanav", "Karan", "Karanvir", "Karma", "Karthik", "Kartik", "Kash", "Kashmir", 
                      "Kavi", "Keshav", "Kiaan", "Kian", "Kiran", "Krish", "Krishiv", "Krishna", "Krishnakant", "Kush", "Laksh", "Madhav", 
                      "Madhavan", "Mahavira", "Mahir", "Malhar", "Manan", "Manav", "Manish", "Manu", "Medhansh", "Mihir", "Mithran", "Mohammad", 
                      "Mohan", "Mohit", "Naksh", "Naman", "Nandan", "Naveen", "Navi", "Navin", "Neel", "Nihal", "Nikhil", "Niramay", "Nivaan", 
                      "Ojas", "Omkar", "Parth", "Parv", "Prakash", "Pranav", "Praneel", "Pransh", "Prashant", "Pratham", "Pratyush", "Purnit", 
                      "Qadir", "Qasim", "Raghav", "Rahul", "Raj", "Rajah", "Rajesh", "Ram", "Rama", "Rani", "Ranveer", "Ravi", "Rayyan", 
                      "Reyan", "Reyansh", "Rishaan", "Rishabh", "Rishi", "Rivaan", "Rohan", "Ronit", "Roshan", "Ruan", "Ruchir", "Rudra", 
                      "Ruhan", "Rushil", "Sachin", "Sagar", "Sahaj", "Sahas", "Sahil", "Sai", "Sajan", "Samar", "Samarth", "Sameer", "Samir", 
                      "Sandeep", "Sanjay", "Sanjeev", "Sareeq", "Sarthak", "Shaan", "Shaurya", "Shiv", "Shivansh", "Shivay", "Shlok", "Shourya", 
                      "Shreyansh", "Shubh", "Shyam", "Siddhant", "Siddharth", "Skanda", "Soham", "Sohan", "Soma", "Sony", "Sri", "Suresh", 
                      "Surya", "Suveer", "Syed", "Taj", "Taksh", "Tanay", "Tanmay", "Tapan", "Tarak", "Tej", "Tejas", "Tejasvi", "Tenzin", 
                      "Tipu", "Udarsh", "Uday", "Vansh", "Vanshaj", "Varun", "Ved", "Vedant", "Veer", "Vihaan", "Vihan", "Vijay", "Vikas", 
                      "Vikram", "Viraj", "Vishnu", "Vivaan", "Vivan", "Vyom", "Wasim", "Yahya", "Yash", "Yug", "Yuvaan", "Yuvan", "Yuvraj", 
                      "Zaheer", "Zayn", "Zohan"]

SurnamesList = ["Acharya", "Afreen", "Aftab", "Agarwal", "Ahluwalia", "Ahmed", "Ahuja", "Aishwary", "Akhtar", "Alam", 
                "Aleem", "Ali", "Alwadhi", "Amble", "Anam", "Anand", "Andra", "Anjum", "Anne", "Ansari", "Anupama", "Anwar", 
                "Apte", "Arora", "Arya", "Ashraf", "Atwal", "Awasthi", "Azam", "Azhar", "Azmi", "Babu", "Badal", "Badami", 
                "Baddur", "Bahl", "Bahri", "Bai", "Bail", "Bains", "Bajaj", "Bajpai", "Bajwa", "Bakshi", "Bal", "Bala", 
                "Balakrishnan", "Balan", "Balasubramanian", "Banerjee", "Bano", "Bansal", "Bapat", "Bapna", "Barad", "Barai", 
                "Baranwal", "Barman", "Basak", "Bassi", "Basu", "Batra", "Bawa", "Bedi", "Begam", "Behl", "Ben", "Bhadauria", 
                "Bhagat", "Bhalla", "Bhandari", "Bhardwaj", "Bhargava", "Bhaskar", "Bhatia", "Bhatnagar", "Bhatt", "Bhattacharjee", 
                "Bhattacharya", "Bhatti", "Bhavsar", "Bhushan", "Bibi", "Bindal", "Bisht", "Biswas", "Borah", "Borde", "Bose", 
                "Brar", "Butala", "Chacko", "Chadha", "Chakraborty", "Chand", "Chanda", "Chandel", "Chander", "Chandra", 
                "Chatterjee", "Chaturvedi", "Chaubey", "Chaudhari", "Chaudhary", "Chauhan", "Chaurasia", "Chavan", "Chawla", 
                "Cherian", "Chetan", "Chhabra", "Chokshi", "Chopra", "Choubey", "Choudhary", "Contractor", "Dada", "Dahiya", 
                "Dalal", "Dani", "Dara", "Darshan", "Das", "Dasgupta", "Dash", "Date", "Datta", "Dave", "Dayal", "De", "Deep", 
                "Deol", "Desai", "Deshmukh", "Deshpande", "Dev", "Devi", "Dey", "Dhaliwal", "Dhawan", "Dhillon", "Dhingra", 
                "Dhoni", "Dikshit", "Dixit", "Dora", "Doshi", "Dua", "Dubey", "Dugal", "Dugar", "Dutt", "Dutta", "Dwevedi", 
                "Dwivedi", "Edwin", "Fatima", "Fernandes", "Francis", "Gaba", "Gade", "Gadge", "Gaikwad", "Gala", "Ganapathy", 
                "Gandhi", "Ganesan", "Ganesh", "Ganguly", "Gangwal", "Garde", "Garg", "Garud", "Gaur", "Gautam", "Gayathri", 
                "Gehlot", "Ghose", "Ghosh", "Gill", "Goel", "Gokhale", "Gomashe", "Gopal", "Goswami", "Goyal", "Grewal", "Grover", 
                "Guha", "Gujrati", "Gulati", "Gupta", "Gurjar", "Gutti", "Halder", "Handa", "Hanif", "Hans", "Hansdah", "Hanul", 
                "Hari", "Hasni", "Hayer", "Hegde", "Hussain", "Indora", "Iqbal", "Islam", "Israni", "Issac", "Iyengar", "Iyer", 
                "Jadhav", "Jafri", "Jagaragallu", "Jaggi", "Jagtap", "Jain", "Jaiswal", "Jaitley", "Jajoo", "Jani", "Jassal", 
                "Jawed", "Jay", "Jayaraman", "Jena", "Jeykumaran", "Jha", "Jhaveri", "Jindal", "Jodha", "Johari", "Jose", "Joseph", 
                "Joshi", "Junankar", "Juned", "Juneja", "Jushantan", "Kadakia", "Kade", "Kairati", "Kakar", "Kale", "Kalita", "Kalra", 
                "Kalsi", "Kamble", "Kamdar", "Kanchan", "Kanda", "Kannan", "Kanojia", "Kansal", "Kapadia", "Kapoor", "Kapur", "Karan", 
                "Karnik", "Karpe", "Kasaudhan", "Kasera", "Kashyap", "Kasniya", "Katiyar", "Katta", "Kaul", "Kaur", "Kaushik", "Kavi", 
                "Kesarwani", "Keshari", "Keshri", "Keshwani", "Kewlani", "Khaliq", "Khalsa", "Khan", "Khandekar", "Khandelwal", "Khanna", 
                "Khare", "Khatoon", "Khatri", "Khokhar", "Khosla", "Khurana", "Kidwai", "Kishor", "Kochar", "Kohli", "Konda", "Kori", "Koshy", 
                "Kota", "Kothari", "Krish", "Krishna", "Krishnamurthy", "Krishnan", "Kukreja", "Kulkarni", "Kumar", "Kumari", "Kunda", 
                "Kurian", "Kuruvilla", "Kushwaha", "Kwatra", "Lad", "Lakhmani", "Lal", "Lala", "Lalchandani", "Lall", "Lamba", "Lanka", 
                "Lata", "Lockwani", "Loke", "Luthra", "Machhan", "Machra", "Madaan", "Madan", "Madina", "Magar", "Mahajan", "Mahal", 
                "Mahapatra", "Maharaj", "Mahawar", "Maheshwari", "Mahmood", "Mahto", "Majeed", "Majhi", "Majumdar", "Malekar", "Malhotra", 
                "Malik", "Malviya", "Malwan", "Manda", "Mandal", "Mander", "Mane", "Mangal", "Mangat", "Mangla", "Mani", "Manjhi", "Manju", 
                "Manna", "Mannan", "Manne", "Masood", "Mathai", "Mathur", "Maurya", "Meda", "Meena", "Meghwal", "Mehan", "Mehra", "Mehrotra", 
                "Mehta", "Menon", "Merchant", "Mhaske", "Minhas", "Mishra", "Misra", "Mistry", "Mitra", "Mittal", "Modi", "Mohan", "Mohandas", 
                "Mohanty", "Mondal", "Morar", "More", "Motwani", "Mourya", "Mukherjee", "Mukhopadhyay", "Munda", "Munir", "Munshi", "Murmu", 
                "Murthy", "Mustafa", "Naaz", "Nadaf", "Nadhe", "Nadig", "Nadkarni", "Nag", "Nagar", "Nagarajan", "Nagi", "Nagoria", 
                "Nagraj", "Nagy", "Naidu", "Naik", "Nair", "Nanda", "Nandakumar", "Nanwani", "Naqvi", "Narain", "Narang", "Narasimhan", 
                "Narayan", "Narayanan", "Narula", "Nasreen", "Natarajan", "Nath", "Nayak", "Nayar", "Nazareth", "Negi", "Nigam", "Nisha", 
                "Nori", "Oak", "Obed", "Ojha", "Omkar", "Oommen", "Oswal", "Oza", "Pai", "Paighan", "Pal", "Palan", "Palata", "Palisetti", 
                "Pall", "Pallav", "Panchal", "Pandey", "Pandit", "Pandya", "Panesar", "Pant", "Paramar", "Parashar", "Parekh", "Parmar", 
                "Parul", "Paswan", "Patel", "Pathak", "Pathan", "Patil", "Patra", "Pattnaik", "Pau", "Paul", "Pawar", "Pereira", "Peri", 
                "Pillai", "Pillay", "Pingle", "Poddar", "Porwal", "Prabhakar", "Prabhu", "Pradhan", "Prajapati", "Prakash", "Prasad", 
                "Prasath", "Prashad", "Praveenchand", "Pravesh", "Preetham", "Priya", "Priyadarshi", "Priyadarshini", "Pundir", "Puri", 
                "Purohit", "Purwar", "Putta", "Quadiri", "Quraishi", "Radhakrishnan", "Raghavan", "Rai", "Raj", "Raja", "Rajagopal", 
                "Rajagopalan", "Rajak", "Rajan", "Rajendra", "Rajesh", "Rajput", "Raju", "Ram", "Rama", "Ramachandran", "Ramakrishnan", 
                "Raman", "Ramanathan", "Ramaswamy", "Ramesh", "Rana", "Ranganathan", "Rani", "Ranjan", "Rao", "Rasheed", "Rastogi", "Rathod", 
                "Rathore", "Rattan", "Ratti", "Rau", "Rauniyar", "Rausa", "Raut", "Ravi", "Rawat", "Rawlani", "Ray", "Raykar", "Raza", 
                "Reddy", "Rege", "Rehman", "Rishiraj", "Ritikesh", "Rizvi", "Rizwan", "Roshan", "Rout", "Roy", "Rungta", "Ruqaiya", 
                "Sabharwal", "Sachan", "Sachar", "Sachdev", "Sagar", "Sahai", "Sahni", "Sahota", "Sahu", "Saini", "Saluja", "Salvi", 
                "Samaddar", "Samdharshni", "Sami", "Sampath", "Samra", "Sandal", "Sandhu", "Sandilya", "Sane", "Sangha", "Sanghvi", 
                "Sani", "Sankar", "Sankaran", "Sankary", "Sant", "Sanwal", "Saraf", "Saran", "Saraswat", "Sarath", "Sarawagi", "Sardar", 
                "Sareen", "Sarkar", "Sarnobat", "Sarraf", "Sasanka", "Sathe", "Savant", "Sawhney", "Sawlani", "Saxena", "Sehgal", "Sekh", 
                "Sekhar", "Sekhon", "Selvaraj", "Sen", "Sengar", "Sengupta", "Seshadri", "Seth", "Sethi", "Setty", "Shah", "Shahid", 
                "Shaikh", "Shaji", "Shan", "Shandilya", "Shankar", "Shankdhar", "Shanker", "Sharaf", "Sharma", "Shekhar", "Shenoy", "Shere", 
                "Sheth", "Shetty", "Shinde", "Shingh", "Shivastava", "Shoaib", "Shrivas", "Shrivastav", "Shrivastava", "Shroff", "Shukla", 
                "Sibal", "Siddiqui", "Sidhu", "Sikarwar", "Singam", "Singh", "Singhal", "Singhania", "Sinha", "Siraj", "Sirohi", "Sitaram", 
                "Sivan", "Sodhi", "Solanki", "Soman", "Sonawane", "Soni", "Sonkar", "Sonwani", "Sood", "Souza", "Sridhar", "Srinivas", 
                "Srinivasan", "Srivastav", "Srivastava", "Subbapati", "Subramaniam", "Suchi", "Sule", "Suman", "Sundar", "Sundaram", "Sunder", 
                "Sur", "Surabhi", "Suresh", "Suri", "Swain", "Swaminathan", "Swamy", "Tailor", "Talwar", "Tandon", "Taneja", "Tangirala", 
                "Tank", "Tanu", "Tara", "Tata", "Teja", "Tejaswini", "Tekchandani", "Tewari", "Thakkar", "Thakur", "Thawani", "Tibrewal", 
                "Tidke", "Tiwari", "Tomar", "Tripathi", "Trivedi", "Tulshidas", "Tyagi", "Umar", "Unnikrishnan", "Upadhyay", "Uppal", "Vaidya", 
                "Vaish", "Vaishnavi", "Varghese", "Varma", "Varshney", "Varty", "Varughese", "Vasav", "Vashisth", "Vasistha", "Veerepalli", 
                "Venkataraman", "Venkatesh", "Venkateshwaran", "Verma", "Vikram", "Vilas", "Virani", "Vishal", "Vishwakarma", "Viswanathan", 
                "Vohra", "Vora", "Vyas", "Wadhawan", "Wadhwa", "Wagh", "Wagle", "Walia", "Walla", "Wanve", "Warrior", "Warsi", "Waseem", 
                "Wasif", "Wason", "Wathore", "Waybhase", "Waykos", "Yadav", "Yaddanapudi", "Yamala", "Yogi", "Yohannan", "Zacharia", 
                "Zachariah", "Zaidi", "Zehra", "Zope"]

GenderList = ["Male", "Female"]

BankNamesList = ["State Bank of India", "Punjab National Bank", "Canara Bank", "Bank of Baroda", "Bank of India", 
                 "Union Bank of India", "Indian Bank", "Central Bank of India", "Indian Overseas Bank", 
                 "Bank of Maharashtra", "Punjab & Sind Bank", "UCO Bank","HDFC Bank", "ICICI Bank", "Axis Bank", 
                 "Kotak Mahindra Bank", "IndusInd Bank", "Federal Bank", "Bandhan Bank", "IDBI Bank", "Yes Bank", 
                 "CSB Bank", "City Union Bank", "DBS Bank India", "Karur Vysya Bank", "Tamilnad Mercantile Bank", 
                 "RBL Bank", "Dhanlaxmi Bank", "Jammu & Kashmir Bank", "Nainital Bank", "IDFC FIRST Bank","HSBC", 
                 "Citibank", "Standard Chartered Bank", "Deutsche Bank"]

DepartmentNamesList = ["Human Resources", "Finance & Accounts", "Marketing & Corporate Communications", 
                       "Information Technology", "Sales & Business Development", "Operations & Production", 
                       "Legal & Compliance", "Administration & General Services", "Supply Chain, Logistics & Procurement", 
                       "Research & Development", "Quality Assurance", "Customer Service / Support", "Innovations"]

LanguageNamesList = ["Hindi", "English", "Bengali", "Marathi", "Telugu", "Tamil", "Urdu", "Gujarati", "Kannada", 
                     "Odia", "Punjabi", "Malayalam", "Assamese", "Maithili", "Santali", "Kashmiri", "Nepali", 
                     "Sanskrit", "Sindhi", "Dogri", "Konkani", "Meitei", "Bodo"]

CompanyNamesList = ["Synchrony International", "Aye Finance", "DHL Express", "ITC Hotels", 
                    "PNB MetLife", "HDFC Life Insurance", "Intercontinental ", "Welspun Living", 
                    "ISS Facility Services", "Marriott International", "Reliance Retail", 
                    "Barbeque Nation Hospitality", "R1 RCM Global", "Reliance Nippon Life Insurance", 
                    "Quess Corp", "Angel One", "Harrisons Malayalam", "Lifestyle International", 
                    "Mr Cooper INC", "Piramal Finance", "Ujjivan Small Finance Bank", "Bajaj Finance", 
                    "Axis Max Life Insurance", "Edelweiss Life Insurance", "Accenture Solutions", 
                    "Navitasys India", "S&P Global", "Hardcastle Restaurants", "Ericsson", 
                    "PGP Glass", "PepsiCo", "Gokaldas Exports", "UNO Minda", "HashedIn Technologies", 
                    "Cadence Design Systems", "Ryan Tax Services", "Compass", "Zensar Technologies", 
                    "Allianz Partners", "Gainwell Commosales", "AU Small Finance Bank", 
                    "Century Plyboards", "Encora Innovation Labs", "Impetus Technologies", 
                    "Amara Raja Energy & Mobility", "Satin Creditcare Network", "Dow Chemical International", 
                    "Agilent Technologies", "First American", "Bharat Financial Inclusion", 
                    "Bharti AXA Life Insurance", "HDB Financial Services", "Blue Dart Express", 
                    "Niva Bupa Health Insurance", "Blue Yonder", "MSC Technology", "Aegis Customer Support Services", 
                    "Trane Technologies", "Lodha Developers", "Oberoi Realty", "YASH Technologies", "IIFL Finance", 
                    "TVS Credit Services", "Future Generali Insurance", "Fractal Analytics", "GRT Hotels & Resorts", 
                    "Hero FinCorp", "ElasticRun", "Firstsource Solutions", "Kotak Mahindra Bank", "Shoppers Stop", 
                    "Carelon Global Solutions LLP", "AGS Health", "Broadridge Financial Solutions", 
                    "Schneider Electric", "SMFG Credit Co. Ltd.", "Admiral Solutions", "Virtusa Consulting Services", 
                    "First Life Insurance", "National Engineering Industries", "LUCAS TVS", "Tata Communications"]

ReligionNamesList = ['Hinduism', 'Muslim', 'Christian', 'Sikhi', 'Buddhist', 'Jain', 'Sufi', 'Atheists']
EmailProvidersList = ["zohomail.com", "rediffmail.com", "gmail.com", "outlook.com", "hotmail.com", "yahoo.co.in"]

DesignationNamesList = ["Chief Executive Officer", "Managing Director", "Chief Operating Officer", "Chief Financial Officer", 
                        "Chief Technology Officer", "Chief Human Resources Officer", "Chief Marketing Officer", "President", 
                        "Vice President ", "Director", "General Manager", "Regional Manager", "Branch Manager", 
                        "Assistant Vice President", "Senior Manager", "Manager", "Assistant Manager", "Team Lead", 
                        "Section Head", "Project Manager", "Coordinator", "Senior Consultant", "Specialist", 
                        "Subject Matter Expert", "Consultant", "Analyst", "Associate", "Executive", "Systems Engineer", 
                        "Technical Lead", "Junior Associate", "Assistant", "Trainee", "Intern", "Peon"]

AirlineNamesList = ["IndiGo", "Air India", "Akasa Air", "SpiceJet:", "Alliance Air", "Fly91", "Star Air", "IndiaOne Air", "Al Hind Air", 
                    "FlyExpress", "Shankh Air"]

PetCategoryList = ["Labrador Retriever", "Golden Retriever", "German Shepherd", "Beagle", "Shih Tzu", "Pomeranian", "Cocker Spaniel", 
                   "Pug", "Pit Bull", "Boxer", "Siberian Husky", "Indian Pariah", "Mudhol Hound ", "Gaddi Kutta", "Rajapalayam", 
                   "Kombai", "Rampur Greyhound", "Indian Spitz", "Pandikona", "Persian cats", "Siamese cats", "Budgerigars", 
                   "Indian Ringneck Parrots", "Cockatiels", "Sun Conures", "Lovebirds", "Macaws", "African Grey Parrots", 
                   "Rabbits", "Hamsters", "Guinea Pigs", "Ornamental fish", "Vechur cows"]

# pin = city_prefix + random(000–999)
CityNamesList = { "Adilabad": {"PinPrefix": 504, "State": "Telangana"}, 
                  "Agartala": {"PinPrefix": 799, "State": "Manipur"}, 
                  "Agra": {"PinPrefix": 282, "State": "Uttar Pradesh"}, 
                  "Ahmedabad": {"PinPrefix": 380, "State": "Gujarat"}, 
                  "Ahmednagar": {"PinPrefix": 413, "State": "Maharashtra"}, 
                  "Ajmer": {"PinPrefix": 305, "State": "Rajasthan"}, 
                  "Akola": {"PinPrefix": 444, "State": "Maharashtra"}, 
                  "Aligarh": {"PinPrefix": 202, "State": "Uttar Pradesh"}, 
                  "Alipore": {"PinPrefix": 700, "State": "West Bengal"}, 
                  "Allahabad": {"PinPrefix": 211, "State": "Uttar Pradesh"}, 
                  "Alleppey": {"PinPrefix": 688, "State": "Kerala"}, 
                  "Almora": {"PinPrefix": 263, "State": "Uttarakhand"}, 
                  "Alwar": {"PinPrefix": 301, "State": "Rajasthan"}, 
                  "Alwaye": {"PinPrefix": 682, "State": "Kerala"}, 
                  "Amalapuram": {"PinPrefix": 533, "State": "Andhra Pradesh"}, 
                  "Amaravati": {"PinPrefix": 444, "State": "Maharashtra"}, 
                  "Ambala": {"PinPrefix": 133, "State": "Haryana"}, 
                  "Amreli": {"PinPrefix": 364, "State": "Gujarat"}, 
                  "Amritsar": {"PinPrefix": 143, "State": "Punjab"}, 
                  "Anakapalle": {"PinPrefix": 531, "State": "Andhra Pradesh"}, 
                  "Anand": {"PinPrefix": 387, "State": "Gujarat"}, 
                  "Anantapur": {"PinPrefix": 515, "State": "Andhra Pradesh"}, 
                  "Andaman & Nicobar Islands": {"PinPrefix": 744, "State": "Andaman & Nicobar Islands"}, 
                  "Anna Road": {"PinPrefix": 600, "State": "Tamil Nadu"}, 
                  "Arakkonam": {"PinPrefix": 631, "State": "Tamil Nadu"}, 
                  "Arunachal Pradesh": {"PinPrefix": 790, "State": "Arunachal Pradesh"}, 
                  "Asansol": {"PinPrefix": 713, "State": "West Bengal"}, 
                  "Aska": {"PinPrefix": 761, "State": "Odisha"}, 
                  "Aurangabad": {"PinPrefix": 423, "State": "Maharashtra"}, 
                  "AurangabadBihar": {"PinPrefix": 824, "State": "Bihar"}, 
                  "Azamgarh": {"PinPrefix": 221, "State": "Uttar Pradesh"}, 
                  "Bagalkot": {"PinPrefix": 587, "State": "Karnataka"}, 
                  "Bahraich": {"PinPrefix": 271, "State": "Uttar Pradesh"}, 
                  "Balaghat": {"PinPrefix": 480, "State": "Madhya Pradesh"}, 
                  "Balangir": {"PinPrefix": 767, "State": "Odisha"}, 
                  "Balasore": {"PinPrefix": 751, "State": "Odisha"}, 
                  "Ballari": {"PinPrefix": 583, "State": "Karnataka"}, 
                  "Ballia": {"PinPrefix": 221, "State": "Bihar"}, 
                  "Banaskantha": {"PinPrefix": 385, "State": "Gujarat"}, 
                  "Banda": {"PinPrefix": 210, "State": "Uttar Pradesh"}, 
                  "Bankura": {"PinPrefix": 722, "State": "West Bengal"}, 
                  "Barabanki": {"PinPrefix": 225, "State": "Uttar Pradesh"}, 
                  "Baramulla": {"PinPrefix": 193, "State": "Jammu and Kashmir"}, 
                  "Barasat": {"PinPrefix": 700, "State": "West Bengal"}, 
                  "Bardoli": {"PinPrefix": 394, "State": "Gujarat"}, 
                  "Bareilly": {"PinPrefix": 229, "State": "Uttar Pradesh"}, 
                  "Barmer": {"PinPrefix": 344, "State": "Rajasthan"}, 
                  "Bastar": {"PinPrefix": 491, "State": "Chattisgarh"}, 
                  "Basti": {"PinPrefix": 272, "State": "Andaman & Nicobar Islands"}, 
                  "Beawar": {"PinPrefix": 305, "State": "Rajasthan"}, 
                  "Beed": {"PinPrefix": 413, "State": "Maharashtra"}, 
                  "Begusarai": {"PinPrefix": 848, "State": "Bihar"}, 
                  "Belagavi": {"PinPrefix": 590, "State": "Karnataka"}, 
                  "Bengaluru": {"PinPrefix": 560, "State": "Karnataka"}, 
                  "Berhampur": {"PinPrefix": 760, "State": "Odisha"}, 
                  "Bhadrak": {"PinPrefix": 756, "State": "Odisha"}, 
                  "Bhagalpur": {"PinPrefix": 812, "State": "Bihar"}, 
                  "Bharatpur": {"PinPrefix": 321, "State": "Rajasthan"}, 
                  "Bharuch": {"PinPrefix": 391, "State": "Gujarat"}, 
                  "Bhatinda": {"PinPrefix": 151, "State": "Punjab"}, 
                  "Bhavnagar": {"PinPrefix": 364, "State": "Gujarat"}, 
                  "Bhilwara": {"PinPrefix": 311, "State": "Rajasthan"}, 
                  "Bhimavaram": {"PinPrefix": 534, "State": "Andhra Pradesh"}, 
                  "Bhiwani": {"PinPrefix": 127, "State": "Haryana"}, 
                  "Bhojpur": {"PinPrefix": 802, "State": "Bihar"}, 
                  "Bhopal": {"PinPrefix": 462, "State": "Madhya Pradesh"}, 
                  "Bhubaneswar": {"PinPrefix": 751, "State": "Odisha"}, 
                  "Bhusaval": {"PinPrefix": 424, "State": "Maharashtra"}, 
                  "Bidar": {"PinPrefix": 585, "State": "Karnataka"}, 
                  "Bijnor": {"PinPrefix": 246, "State": "Uttar Pradesh"}, 
                  "Bikaner": {"PinPrefix": 331, "State": "Rajasthan"}, 
                  "Bilaspur": {"PinPrefix": 495, "State": "Chattisgarh"}, 
                  "Birbhum": {"PinPrefix": 731, "State": "West Bengal"}, 
                  "Budaun": {"PinPrefix": 242, "State": "Uttar Pradesh"}, 
                  "Bulandshahar": {"PinPrefix": 203, "State": "Uttar Pradesh"}, 
                  "Buldana": {"PinPrefix": 443, "State": "Maharashtra"}, 
                  "Burdwan": {"PinPrefix": 713, "State": "West Bengal"}, 
                  "Cachar": {"PinPrefix": 788, "State": "Assam"}, 
                  "Calicut": {"PinPrefix": 673, "State": "Kerala"}, 
                  "Cannanore": {"PinPrefix": 670, "State": "Kerala"}, 
                  "Chamba": {"PinPrefix": 176, "State": "Himachal Pradesh"}, 
                  "Chamoli": {"PinPrefix": 246, "State": "Uttarakhand"}, 
                  "Chandigarh": {"PinPrefix": 140, "State": "Chandigarh"}, 
                  "Chandrapur": {"PinPrefix": 441, "State": "Maharashtra"}, 
                  "Changanacherry": {"PinPrefix": 686, "State": "Kerala"}, 
                  "Channapatna": {"PinPrefix": 561, "State": "Karnataka"}, 
                  "Chengalpattu": {"PinPrefix": 603, "State": "Tamil Nadu"}, 
                  "Chennai": {"PinPrefix": 600, "State": "Tamil Nadu"}, 
                  "Chhatarpur": {"PinPrefix": 471, "State": "Madhya Pradesh"}, 
                  "Chhindwara": {"PinPrefix": 460, "State": "Madhya Pradesh"}, 
                  "Chikkamagaluru": {"PinPrefix": 577, "State": "Karnataka"}, 
                  "Chikodi": {"PinPrefix": 591, "State": "Karnataka"}, 
                  "Chitradurga": {"PinPrefix": 577, "State": "Karnataka"}, 
                  "Chittoor": {"PinPrefix": 517, "State": "Andhra Pradesh"}, 
                  "Chittorgarh": {"PinPrefix": 312, "State": "Rajasthan"}, 
                  "Churu": {"PinPrefix": 331, "State": "Rajasthan"}, 
                  "Coimbatore": {"PinPrefix": 641, "State": "Tamil Nadu"}, 
                  "Contai": {"PinPrefix": 721, "State": "West Bengal"}, 
                  "Cooch Behar": {"PinPrefix": 735, "State": "West Bengal"}, 
                  "Cuddalore": {"PinPrefix": 607, "State": "Tamil Nadu"}, 
                  "Cuddapah": {"PinPrefix": 516, "State": "Andhra Pradesh"}, 
                  "Cuttack": {"PinPrefix": 752, "State": "Odisha"}, 
                  "Cuttackuth": {"PinPrefix": 754, "State": "Odisha"}, 
                  "Darbhanga": {"PinPrefix": 846, "State": "Bihar"}, 
                  "Darjeeling": {"PinPrefix": 734, "State": "West Bengal"}, 
                  "Darrang": {"PinPrefix": 784, "State": "Assam"}, 
                  "Dehra Gopipur": {"PinPrefix": 176, "State": "Himachal Pradesh"}, 
                  "Dehradun": {"PinPrefix": 247, "State": "Uttarakhand"}, 
                  "Deoria": {"PinPrefix": 274, "State": "Uttar Pradesh"}, 
                  "Dhanbad": {"PinPrefix": 818, "State": "Jharkhand"}, 
                  "Dharamsala": {"PinPrefix": 176, "State": "Himachal Pradesh"}, 
                  "Dharmanagar": {"PinPrefix": 799, "State": "Tripura"}, 
                  "Dharmapuri": {"PinPrefix": 635, "State": "Tamil Nadu"}, 
                  "Dharwad": {"PinPrefix": 580, "State": "Karnataka"}, 
                  "Dhenkanal": {"PinPrefix": 759, "State": "Odisha"}, 
                  "Dholpur": {"PinPrefix": 321, "State": "Rajasthan"}, 
                  "Dhule": {"PinPrefix": 424, "State": "Maharashtra"}, 
                  "Dibrugarh": {"PinPrefix": 784, "State": "Assam"}, 
                  "Dinajpur": {"PinPrefix": 733, "State": "West Bengal"}, 
                  "Dindigul": {"PinPrefix": 624, "State": "Tamil Nadu"}, 
                  "Dungarpur": {"PinPrefix": 314, "State": "Rajasthan"}, 
                  "Durg": {"PinPrefix": 490, "State": "Chattisgarh"}, 
                  "Eluru": {"PinPrefix": 534, "State": "Andhra Pradesh"}, 
                  "Ernakulam": {"PinPrefix": 682, "State": "Kerala"}, 
                  "Erode": {"PinPrefix": 638, "State": "Tamil Nadu"}, 
                  "Etah": {"PinPrefix": 207, "State": "Uttar Pradesh"}, 
                  "Etawah": {"PinPrefix": 206, "State": "Uttar Pradesh"}, 
                  "Faizabad": {"PinPrefix": 224, "State": "Uttar Pradesh"}, 
                  "Faridabad": {"PinPrefix": 121, "State": "Haryana"}, 
                  "Faridkot": {"PinPrefix": 142, "State": "Punjab"}, 
                  "Fatehgarh": {"PinPrefix": 209, "State": "Uttar Pradesh"}, 
                  "Fatehpur": {"PinPrefix": 212, "State": "Uttar Pradesh"}, 
                  "Ferozpur": {"PinPrefix": 142, "State": "Punjab"}, 
                  "Gadag": {"PinPrefix": 582, "State": "Karnataka"}, 
                  "Gandhinagar": {"PinPrefix": 380, "State": "Gujarat"}, 
                  "Gaya": {"PinPrefix": 804, "State": "Bihar"}, 
                  "Ghaziabad": {"PinPrefix": 201, "State": "Uttar Pradesh"}, 
                  "Ghazipur": {"PinPrefix": 232, "State": "Uttar Pradesh"}, 
                  "Giridih": {"PinPrefix": 815, "State": "Jharkhand"}, 
                  "Goa": {"PinPrefix": 403, "State": "Goa"}, 
                  "Goalpara": {"PinPrefix": 783, "State": "Assam"}, 
                  "Gokak": {"PinPrefix": 591, "State": "Karnataka"}, 
                  "Gonda": {"PinPrefix": 271, "State": "Uttar Pradesh"}, 
                  "Gondal": {"PinPrefix": 360, "State": "Gujarat"}, 
                  "Gorakhpur": {"PinPrefix": 273, "State": "Uttar Pradesh"}, 
                  "Gudivada": {"PinPrefix": 521, "State": "Andhra Pradesh"}, 
                  "Gudur": {"PinPrefix": 524, "State": "Andhra Pradesh"}, 
                  "Guna": {"PinPrefix": 473, "State": "Madhya Pradesh"}, 
                  "Guntur": {"PinPrefix": 522, "State": "Andhra Pradesh"}, 
                  "Gurdaspur": {"PinPrefix": 143, "State": "Punjab"}, 
                  "Gurgaon": {"PinPrefix": 122, "State": "Haryana"}, 
                  "Guwahati": {"PinPrefix": 781, "State": "Assam"}, 
                  "Gwalior": {"PinPrefix": 474, "State": "Madhya Pradesh"}, 
                  "Hamirpur": {"PinPrefix": 174, "State": "Himachal Pradesh"}, 
                  "Hanamkonda": {"PinPrefix": 506, "State": "Telangana"}, 
                  "Hardoi": {"PinPrefix": 241, "State": "Uttar Pradesh"}, 
                  "Hassan": {"PinPrefix": 573, "State": "Karnataka"}, 
                  "Haveri": {"PinPrefix": 581, "State": "Karnataka"}, 
                  "Hazaribagh": {"PinPrefix": 825, "State": "Jharkhand"}, 
                  "Hindupur": {"PinPrefix": 515, "State": "Andhra Pradesh"}, 
                  "Hissar": {"PinPrefix": 125, "State": "Haryana"}, 
                  "Hooghly": {"PinPrefix": 712, "State": "West Bengal"}, 
                  "Hoshangabad": {"PinPrefix": 461, "State": "Madhya Pradesh"}, 
                  "Hoshiarpur": {"PinPrefix": 144, "State": "Punjab"}, 
                  "Howrah": {"PinPrefix": 711, "State": "West Bengal"}, 
                  "Hyderabad": {"PinPrefix": 500, "State": "Andhra Pradesh"}, 
                  "Idukki": {"PinPrefix": 685, "State": "Kerala"}, 
                  "Indore": {"PinPrefix": 452, "State": "Madhya Pradesh"}, 
                  "Irinjalakuda": {"PinPrefix": 680, "State": "Kerala"}, 
                  "Jabalpur": {"PinPrefix": 482, "State": "Madhya Pradesh"}, 
                  "Jaipur": {"PinPrefix": 302, "State": "Rajasthan"}, 
                  "Jalandhar": {"PinPrefix": 144, "State": "Punjab"}, 
                  "Jalgaon": {"PinPrefix": 424, "State": "Maharashtra"}, 
                  "Jalpaiguri": {"PinPrefix": 734, "State": "West Bengal"}, 
                  "Jammu": {"PinPrefix": 180, "State": "Jammu and Kashmir"}, 
                  "Jamnagar": {"PinPrefix": 360, "State": "Gujarat"}, 
                  "Jaunpur": {"PinPrefix": 222, "State": "Uttar Pradesh"}, 
                  "Jhansi": {"PinPrefix": 284, "State": "Uttar Pradesh"}, 
                  "Jhunjhunu": {"PinPrefix": 331, "State": "Rajasthan"}, 
                  "Jodhpur": {"PinPrefix": 342, "State": "Rajasthan"}, 
                  "Junagadh": {"PinPrefix": 362, "State": "Daman and Diu"}, 
                  "Kakinada": {"PinPrefix": 533, "State": "Andhra Pradesh"}, 
                  "Kalaburagi": {"PinPrefix": 585, "State": "Karnataka"}, 
                  "Kalahandi": {"PinPrefix": 766, "State": "Odisha"}, 
                  "Kanchipuram": {"PinPrefix": 601, "State": "Tamil Nadu"}, 
                  "Kanniyakumari": {"PinPrefix": 629, "State": "Tamil Nadu"}, 
                  "Kanpur": {"PinPrefix": 208, "State": "Uttar Pradesh"}, 
                  "Kapurthala": {"PinPrefix": 144, "State": "Punjab"}, 
                  "Karaikudi": {"PinPrefix": 630, "State": "Tamil Nadu"}, 
                  "Karimnagar": {"PinPrefix": 505, "State": "Telangana"}, 
                  "Karnal": {"PinPrefix": 126, "State": "Haryana"}, 
                  "Karur": {"PinPrefix": 621, "State": "Tamil Nadu"}, 
                  "Karwar": {"PinPrefix": 581, "State": "Karnataka"}, 
                  "Kasaragod": {"PinPrefix": 671, "State": "Kerala"}, 
                  "Keonjhar": {"PinPrefix": 758, "State": "Odisha"}, 
                  "Khammam": {"PinPrefix": 507, "State": "Telangana"}, 
                  "Khandwa": {"PinPrefix": 450, "State": "Madhya Pradesh"}, 
                  "Kheda": {"PinPrefix": 387, "State": "Gujarat"}, 
                  "Kheri": {"PinPrefix": 224, "State": "Uttar Pradesh"}, 
                  "Kodagu": {"PinPrefix": 571, "State": "Karnataka"}, 
                  "Kolar": {"PinPrefix": 561, "State": "Karnataka"}, 
                  "Kolhapur": {"PinPrefix": 415, "State": "Maharashtra"}, 
                  "Kolkata": {"PinPrefix": 700, "State": "#N/A"}, 
                  "Koraput": {"PinPrefix": 763, "State": "Odisha"}, 
                  "Kota": {"PinPrefix": 324, "State": "Rajasthan"}, 
                  "Kottayam": {"PinPrefix": 686, "State": "Kerala"}, 
                  "Kovilpatti": {"PinPrefix": 627, "State": "Tamil Nadu"}, 
                  "Krishnagiri": {"PinPrefix": 635, "State": "Tamil Nadu"}, 
                  "Kumbakonam": {"PinPrefix": 609, "State": "Tamil Nadu"}, 
                  "Kurnool": {"PinPrefix": 518, "State": "Andhra Pradesh"}, 
                  "Kurukshetra": {"PinPrefix": 136, "State": "Haryana"}, 
                  "Kutch": {"PinPrefix": 370, "State": "Gujarat"}, 
                  "Lakshadweep": {"PinPrefix": 682, "State": "Lakshadweep"}, 
                  "Leh": {"PinPrefix": 194, "State": "Jammu and Kashmir"}, 
                  "Lucknow": {"PinPrefix": 226, "State": "Uttar Pradesh"}, 
                  "Ludhiana": {"PinPrefix": 141, "State": "Punjab"}, 
                  "Machilipatnam": {"PinPrefix": 521, "State": "Andhra Pradesh"}, 
                  "Madhubani": {"PinPrefix": 847, "State": "Bihar"}, 
                  "Madurai": {"PinPrefix": 625, "State": "Tamil Nadu"}, 
                  "Mahabubnagar": {"PinPrefix": 509, "State": "Andhra Pradesh"}, 
                  "Mahesana": {"PinPrefix": 382, "State": "Gujarat"}, 
                  "Mainpuri": {"PinPrefix": 205, "State": "Uttar Pradesh"}, 
                  "Malda": {"PinPrefix": 732, "State": "West Bengal"}, 
                  "Malegaon": {"PinPrefix": 422, "State": "Maharashtra"}, 
                  "Mandi": {"PinPrefix": 175, "State": "Himachal Pradesh"}, 
                  "Mandla": {"PinPrefix": 481, "State": "Madhya Pradesh"}, 
                  "Mandsaur": {"PinPrefix": 458, "State": "Madhya Pradesh"}, 
                  "Mandya": {"PinPrefix": 571, "State": "Karnataka"}, 
                  "Mangaluru": {"PinPrefix": 574, "State": "Karnataka"}, 
                  "Manipur": {"PinPrefix": 795, "State": "#N/A"}, 
                  "Manjeri": {"PinPrefix": 670, "State": "Kerala"}, 
                  "Mathura": {"PinPrefix": 209, "State": "Uttar Pradesh"}, 
                  "Mavelikara": {"PinPrefix": 689, "State": "Kerala"}, 
                  "Mayiladuthurai": {"PinPrefix": 609, "State": "Tamil Nadu"}, 
                  "Mayurbhanj": {"PinPrefix": 757, "State": "Odisha"}, 
                  "Medak": {"PinPrefix": 502, "State": "Telangana"}, 
                  "Meerut": {"PinPrefix": 245, "State": "Uttar Pradesh"}, 
                  "Meghalaya": {"PinPrefix": 793, "State": "Megalaya"}, 
                  "Midnapore": {"PinPrefix": 721, "State": "West Bengal"}, 
                  "Mirzapur": {"PinPrefix": 231, "State": "Uttar Pradesh"}, 
                  "Mizoram": {"PinPrefix": 796, "State": "Mizoram"}, 
                  "Moradabad": {"PinPrefix": 244, "State": "Uttar Pradesh"}, 
                  "Morena": {"PinPrefix": 476, "State": "Madhya Pradesh"}, 
                  "Mumbai": {"PinPrefix": 400, "State": "Maharashtra"}, 
                  "Munger": {"PinPrefix": 811, "State": "Bihar"}, 
                  "Murshidabad": {"PinPrefix": 742, "State": "West Bengal"}, 
                  "Muzaffarnagar": {"PinPrefix": 247, "State": "Uttar Pradesh"}, 
                  "Muzaffarpur": {"PinPrefix": 842, "State": "Bihar"}, 
                  "Mysuru": {"PinPrefix": 570, "State": "Karnataka"}, 
                  "Nadia": {"PinPrefix": 741, "State": "West Bengal"}, 
                  "Nadiauth": {"PinPrefix": 741, "State": "West Bengal"}, 
                  "Nagaland": {"PinPrefix": 707, "State": "Nagaland"}, 
                  "Nagaon": {"PinPrefix": 782, "State": "Assam"}, 
                  "Nagapattinam": {"PinPrefix": 609, "State": "Tamil Nadu"}, 
                  "Nagaur": {"PinPrefix": 305, "State": "Rajasthan"}, 
                  "Nagpur": {"PinPrefix": 440, "State": "Maharashtra"}, 
                  "Nainital": {"PinPrefix": 244, "State": "Uttarakhand"}, 
                  "Nalanda": {"PinPrefix": 801, "State": "Bihar"}, 
                  "Nalbari": {"PinPrefix": 781, "State": "Assam"}, 
                  "Nalgonda": {"PinPrefix": 508, "State": "Telangana"}, 
                  "Namakkal": {"PinPrefix": 637, "State": "Tamil Nadu"}, 
                  "Nanded": {"PinPrefix": 431, "State": "Maharashtra"}, 
                  "Nandyal": {"PinPrefix": 518, "State": "Andhra Pradesh"}, 
                  "Nanjangud": {"PinPrefix": 571, "State": "Karnataka"}, 
                  "Narasaraopet": {"PinPrefix": 522, "State": "Andhra Pradesh"}, 
                  "Nasik": {"PinPrefix": 422, "State": "Maharashtra"}, 
                  "Navi Mumbai": {"PinPrefix": 400, "State": "Maharashtra"}, 
                  "Navsari": {"PinPrefix": 396, "State": "Gujarat"}, 
                  "Nawadha": {"PinPrefix": 803, "State": "Bihar"}, 
                  "Nellore": {"PinPrefix": 524, "State": "Andhra Pradesh"}, 
                  "New Delhi": {"PinPrefix": 110, "State": "Delhi"}, 
                  "Nilgiris": {"PinPrefix": 643, "State": "Tamil Nadu"}, 
                  "Nizamabad": {"PinPrefix": 503, "State": "Telangana"}, 
                  "Osmanabad": {"PinPrefix": 413, "State": "Maharashtra"}, 
                  "Ottapalam": {"PinPrefix": 673, "State": "Kerala"}, 
                  "Palamau": {"PinPrefix": 822, "State": "Jharkhand"}, 
                  "Palghar": {"PinPrefix": 401, "State": "Maharashtra"}, 
                  "Palghat": {"PinPrefix": 678, "State": "Kerala"}, 
                  "Pali": {"PinPrefix": 306, "State": "Rajasthan"}, 
                  "Panchmahals": {"PinPrefix": 388, "State": "Gujarat"}, 
                  "Pandharpur": {"PinPrefix": 413, "State": "Maharashtra"}, 
                  "Parvathipuram": {"PinPrefix": 503, "State": "Andhra Pradesh"}, 
                  "Patan": {"PinPrefix": 384, "State": "Gujarat"}, 
                  "Pathanamthitta": {"PinPrefix": 689, "State": "Kerala"}, 
                  "Patiala": {"PinPrefix": 140, "State": "Punjab"}, 
                  "Patna": {"PinPrefix": 800, "State": "Bihar"}, 
                  "Pattukottai": {"PinPrefix": 614, "State": "Tamil Nadu"}, 
                  "Pauri": {"PinPrefix": 246, "State": "Uttarakhand"}, 
                  "Peddapalli": {"PinPrefix": 505, "State": "Telangana"}, 
                  "Pharbhani": {"PinPrefix": 431, "State": "Maharashtra"}, 
                  "Phulbani": {"PinPrefix": 762, "State": "Odisha"}, 
                  "Pithoragarh": {"PinPrefix": 262, "State": "Uttarakhand"}, 
                  "Pollachi": {"PinPrefix": 641, "State": "Tamil Nadu"}, 
                  "Pondicherry": {"PinPrefix": 604, "State": "Pondicherry"}, 
                  "Porbandar": {"PinPrefix": 360, "State": "Gujarat"}, 
                  "Prakasam": {"PinPrefix": 504, "State": "Andhra Pradesh"}, 
                  "Pratapgarh": {"PinPrefix": 229, "State": "Uttar Pradesh"}, 
                  "Presidency": {"PinPrefix": 700, "State": "West Bengal"}, 
                  "Proddatur": {"PinPrefix": 516, "State": "Andhra Pradesh"}, 
                  "Pudukkottai": {"PinPrefix": 613, "State": "Tamil Nadu"}, 
                  "Pune": {"PinPrefix": 411, "State": "Maharashtra"}, 
                  "Puri": {"PinPrefix": 752, "State": "Odisha"}, 
                  "Purnea": {"PinPrefix": 854, "State": "Bihar"}, 
                  "Purulia": {"PinPrefix": 723, "State": "West Bengal"}, 
                  "Puttur": {"PinPrefix": 574, "State": "Karnataka"}, 
                  "Quilon": {"PinPrefix": 690, "State": "Kerala"}, 
                  "Raichur": {"PinPrefix": 584, "State": "Karnataka"}, 
                  "Raigad": {"PinPrefix": 402, "State": "Maharashtra"}, 
                  "Raigarh": {"PinPrefix": 496, "State": "Chattisgarh"}, 
                  "Raipur": {"PinPrefix": 492, "State": "Chattisgarh"}, 
                  "Rajahmundry": {"PinPrefix": 533, "State": "Andhra Pradesh"}, 
                  "Rajkot": {"PinPrefix": 360, "State": "Gujarat"}, 
                  "Rajouri": {"PinPrefix": 185, "State": "Jammu and Kashmir"}, 
                  "Ramanathapuram": {"PinPrefix": 623, "State": "Tamil Nadu"}, 
                  "Rampur": {"PinPrefix": 172, "State": "Himachal Pradesh"}, 
                  "Ranchi": {"PinPrefix": 834, "State": "Jharkhand"}, 
                  "Ratlam": {"PinPrefix": 457, "State": "Madhya Pradesh"}, 
                  "Ratnagiri": {"PinPrefix": 415, "State": "Maharashtra"}, 
                  "Rayagada": {"PinPrefix": 761, "State": "Odisha"}, 
                  "Rewa": {"PinPrefix": 485, "State": "Madhya Pradesh"}, 
                  "Rohtak": {"PinPrefix": 124, "State": "Haryana"}, 
                  "Rohtas": {"PinPrefix": 802, "State": "Bihar"}, 
                  "Sabarkantha": {"PinPrefix": 383, "State": "Gujarat"}, 
                  "Sagar": {"PinPrefix": 470, "State": "Madhya Pradesh"}, 
                  "Saharanpur": {"PinPrefix": 247, "State": "Uttar Pradesh"}, 
                  "Saharsa": {"PinPrefix": 813, "State": "Bihar"}, 
                  "Salem": {"PinPrefix": 636, "State": "Tamil Nadu"}, 
                  "Samastipur": {"PinPrefix": 848, "State": "Bihar"}, 
                  "Sambalpur": {"PinPrefix": 768, "State": "Odisha"}, 
                  "Sangareddy": {"PinPrefix": 502, "State": "Telangana"}, 
                  "Sangli": {"PinPrefix": 415, "State": "Maharashtra"}, 
                  "Sangrur": {"PinPrefix": 148, "State": "Punjab"}, 
                  "Santhal Parganas": {"PinPrefix": 813, "State": "Jharkhand"}, 
                  "Saran": {"PinPrefix": 841, "State": "Bihar"}, 
                  "Satara": {"PinPrefix": 412, "State": "Maharashtra"}, 
                  "Sawaimadhopur": {"PinPrefix": 321, "State": "Rajasthan"}, 
                  "Secunderabad": {"PinPrefix": 500, "State": "Telangana"}, 
                  "Sehore": {"PinPrefix": 465, "State": "Madhya Pradesh"}, 
                  "Shahdol": {"PinPrefix": 484, "State": "Madhya Pradesh"}, 
                  "Shahjahanpur": {"PinPrefix": 242, "State": "Uttar Pradesh"}, 
                  "Shimla": {"PinPrefix": 171, "State": "Himachal Pradesh"}, 
                  "Shivamogga": {"PinPrefix": 577, "State": "Karnataka"}, 
                  "Shrirampur": {"PinPrefix": 413, "State": "Maharashtra"}, 
                  "Sibsagar": {"PinPrefix": 785, "State": "Assam"}, 
                  "Sikar": {"PinPrefix": 331, "State": "Rajasthan"}, 
                  "Sikkim": {"PinPrefix": 737, "State": "Sikkim"}, 
                  "Sindhudurg": {"PinPrefix": 416, "State": "Maharashtra"}, 
                  "Singhbhum": {"PinPrefix": 831, "State": "Jharkhand"}, 
                  "Sirohi": {"PinPrefix": 307, "State": "Rajasthan"}, 
                  "Sirsi": {"PinPrefix": 581, "State": "Karnataka"}, 
                  "Sitamarhi": {"PinPrefix": 843, "State": "Bihar"}, 
                  "Sitapur": {"PinPrefix": 261, "State": "Uttar Pradesh"}, 
                  "Sivaganga": {"PinPrefix": 630, "State": "Tamil Nadu"}, 
                  "Siwan": {"PinPrefix": 841, "State": "Bihar"}, 
                  "Solan": {"PinPrefix": 171, "State": "Himachal Pradesh"}, 
                  "Solapur": {"PinPrefix": 413, "State": "Maharashtra"}, 
                  "Sonepat": {"PinPrefix": 131, "State": "Haryana"}, 
                  "Sriganganagar": {"PinPrefix": 335, "State": "Rajasthan"}, 
                  "Srikakulam": {"PinPrefix": 532, "State": "Andhra Pradesh"}, 
                  "Srinagar": {"PinPrefix": 190, "State": "Jammu and Kashmir"}, 
                  "Srirangam": {"PinPrefix": 620, "State": "Tamil Nadu"}, 
                  "Sultanpur": {"PinPrefix": 222, "State": "Uttar Pradesh"}, 
                  "Sundargarh": {"PinPrefix": 769, "State": "Odisha"}, 
                  "Surat": {"PinPrefix": 394, "State": "Gujarat"}, 
                  "Surendranagar": {"PinPrefix": 363, "State": "Gujarat"}, 
                  "Suryapet": {"PinPrefix": 508, "State": "Telangana"}, 
                  "Tadepalligudem": {"PinPrefix": 534, "State": "Andhra Pradesh"}, 
                  "Tambaram": {"PinPrefix": 600, "State": "Tamil Nadu"}, 
                  "Tamluk": {"PinPrefix": 721, "State": "West Bengal"}, 
                  "Tehri": {"PinPrefix": 249, "State": "Uttarakhand"}, 
                  "Tenali": {"PinPrefix": 505, "State": "Andhra Pradesh"}, 
                  "Thalassery": {"PinPrefix": 670, "State": "Kerala"}, 
                  "Thane": {"PinPrefix": 400, "State": "Maharashtra"}, 
                  "Thanjavur": {"PinPrefix": 610, "State": "Tamil Nadu"}, 
                  "Theni": {"PinPrefix": 625, "State": "Tamil Nadu"}, 
                  "Tinsukia": {"PinPrefix": 786, "State": "Assam"}, 
                  "Tiruchirapalli": {"PinPrefix": 608, "State": "Tamil Nadu"}, 
                  "Tirunelveli": {"PinPrefix": 627, "State": "Tamil Nadu"}, 
                  "Tirupati": {"PinPrefix": 517, "State": "Andhra Pradesh"}, 
                  "Tirupattur": {"PinPrefix": 632, "State": "Tamil Nadu"}, 
                  "Tirupur": {"PinPrefix": 638, "State": "Tamil Nadu"}, 
                  "Tirur": {"PinPrefix": 673, "State": "Kerala"}, 
                  "Tiruvalla": {"PinPrefix": 686, "State": "Kerala"}, 
                  "Tiruvannamalai": {"PinPrefix": 604, "State": "Tamil Nadu"}, 
                  "Tonk": {"PinPrefix": 304, "State": "Rajasthan"}, 
                  "Trichur": {"PinPrefix": 679, "State": "Kerala"}, 
                  "Trivandrum": {"PinPrefix": 695, "State": "Kerala"}, 
                  "Trivandrumuth": {"PinPrefix": 695, "State": "Kerala"}, 
                  "Tumakuru": {"PinPrefix": 561, "State": "Karnataka"}, 
                  "Tuticorin": {"PinPrefix": 628, "State": "Tamil Nadu"}, 
                  "Udaipur": {"PinPrefix": 305, "State": "Rajasthan"}, 
                  "Udhampur": {"PinPrefix": 182, "State": "Jammu and Kashmir"}, 
                  "Udupi": {"PinPrefix": 574, "State": "Karnataka"}, 
                  "Ujjain": {"PinPrefix": 456, "State": "Madhya Pradesh"}, 
                  "Una": {"PinPrefix": 174, "State": "Himachal Pradesh"}, 
                  "Vadakara": {"PinPrefix": 673, "State": "Kerala"}, 
                  "Vadodara": {"PinPrefix": 390, "State": "Gujarat"}, 
                  "Vaishali": {"PinPrefix": 843, "State": "Bihar"}, 
                  "Valsad": {"PinPrefix": 396, "State": "Dadra and Nagar Hav."}, 
                  "Varanasi": {"PinPrefix": 221, "State": "Uttar Pradesh"}, 
                  "Vellore": {"PinPrefix": 632, "State": "Tamil Nadu"}, 
                  "Vidisha": {"PinPrefix": 464, "State": "Madhya Pradesh"}, 
                  "Vijayapura": {"PinPrefix": 586, "State": "Karnataka"}, 
                  "Vijayawada": {"PinPrefix": 509, "State": "Andhra Pradesh"}, 
                  "Virudhunagar": {"PinPrefix": 626, "State": "Tamil Nadu"}, 
                  "Visakhapatnam": {"PinPrefix": 530, "State": "Andhra Pradesh"}, 
                  "Vizianagaram": {"PinPrefix": 509, "State": "Andhra Pradesh"}, 
                  "Vriddhachalam": {"PinPrefix": 605, "State": "Tamil Nadu"}, 
                  "Wanaparthy": {"PinPrefix": 509, "State": "Telangana"}, 
                  "Warangal": {"PinPrefix": 506, "State": "Telangana"}, 
                  "Wardha": {"PinPrefix": 442, "State": "Maharashtra"}, 
                  "Yeotmal": {"PinPrefix": 445, "State": "Maharashtra"} }

col_list = []
stdf = pd.DataFrame(columns=['Category', 'Column_Name', 'Limits'])
repattern = r'[^a-zA-Z0-9\s]'
date_format = '%d-%m-%Y'

separater_line = f"<hr style='margin-top: 0; margin-bottom: 0; size: 1px; border: 1px solid; color: #000000; '>"
font_name = "Verdana;"

htmlstr = f"""<span style='font-family: {font_name}; font-size: 22pt; font-weight: bold'>Fake Dataset Generator (India)</span><br>"""
htmlstr += "<br>" + separater_line

st.set_page_config(page_title = "Faker", page_icon='🎭', layout = "wide", initial_sidebar_state = "expanded")

# SCTN: functions

def generate_unique_ids_shortuuid(count, length=8):
  unique_ids = set()
  while len(unique_ids) < count:
    new_id = shortuuid.uuid()[:length]  # Generate a short UUID and slice to the desired length
    unique_ids.add(new_id)
  return list(unique_ids)

def CheckIfDateStrIsValid(date_str_to_check):
  try: 
    dt.strptime(date_str_to_check, date_format)   # Attempt to parse the date string into a datetime object
    return True                                   # If successful, the date is valid
  except ValueError:
    return False                                  # If a ValueError is raised, the string is not a valid date in that format

def is_integer_value(value):
  if isinstance(value, int):
      return True
  if isinstance(value, float):
      return value.is_integer()
  return False

def GetRandomNumber(start_end_str, recs_count):   # if one/both num limits are not provided, assume random dates between 1 and 100
  narr = []
  if recs_count > 0:
    for _ in range(recs_count):
      random_number = random.randint(1, 100)

      if start_end_str == '': narr.append(random_number)
      else:
        dt_lst = start_end_str.split(',')
        dt_lst = [int(x.strip()) for x in dt_lst if x != '']

        if len(dt_lst) == 1: narr.append(random_number)
        
        elif len(dt_lst) == 2:  # both num limits provided
          if is_integer_value(dt_lst[0]) and is_integer_value(dt_lst[1]): narr.append(random.randint(dt_lst[0], dt_lst[1])) 
          else: narr.append(random_number)

  return narr

def GetRandomDate(start_end_str, recs_count):   # if one/both dates are not provided, assume random dates between today and -80 years
  darr = []
  if recs_count > 0:
    for _ in range(recs_count):
      random_date = (dt.now() + timedelta(days=-random.randint(1, (365*80)))).date()

      if start_end_str == '': darr.append(random_date)
      else:
        dt_lst = start_end_str.split(',')
        dt_lst = [x.strip() for x in dt_lst if x != '']

        if len(dt_lst) == 1: darr.append(random_date)
        
        elif len(dt_lst) == 2:  # both date limits provided
          if CheckIfDateStrIsValid(dt_lst[0]) and CheckIfDateStrIsValid(dt_lst[1]):
            start_date = dt.strptime(dt_lst[0], date_format)        # Convert strings to datetime objects
            end_date = dt.strptime(dt_lst[1], date_format)          # Convert strings to datetime objects

            total_seconds = int((end_date - start_date).total_seconds())
            random_second = random.randrange(total_seconds)

            darr.append(start_date + timedelta(seconds=random_second))

          else: darr.append(random_date)

  return darr

def ordinal(n): return str(n) + {1:'st',2:'nd',3:'rd'}.get(n if n<20 else n%10,'th')

def GenerateStreetAddress(recs_count):
  dwelling_type = ["Flat", "Room", "Suite", "Unit", "Apartment", "House", "Villa", "Block", "Bungalow"]
  building_names = ["Shanti Residency", "Sai Residency", "Green Park Apartments", "Lakeview Towers", "Sunrise Heights", "Silver Oak Apartments", "Golden Enclave", "Krishna Residency", "Laxmi Towers", "Park View Apartments", "Royal Heights", "Garden View Residency", "Shree Apartments", "Shubh Enclave", "Anand Residency", "Harmony Towers", "Om Residency", "Galaxy Apartments", "Skyline Towers", "Metro Heights", "Palm Residency", "Orchid Apartments", "Lotus Enclave", "Sapphire Towers", "Emerald Residency", "Pearl Apartments", "Diamond Heights", "Coral Residency", "Crystal Towers", "Ocean View Apartments", "Green Valley Residency", "Hill View Apartments", "Riverfront Towers", "Central Park Residency", "Blue Sky Apartments", "Sunshine Towers", "Crescent Residency", "Royal Garden Apartments", "Imperial Heights", "Prestige Residency", "Harmony Enclave", "Silver Heights", "Lakefront Towers", "Maple Residency", "Cedar Apartments", "Pine View Residency", "Rosewood Towers", "Tulip Apartments", "Jasmine Residency", "Lotus Heights", "Paradise Towers", "Dreamland Residency", "Urban Heights", "City View Apartments", "Elite Residency", "Prime Towers", "Signature Apartments", "Classic Residency", "Heritage Towers", "Regal Apartments", "Sai Enclave", "Shree Towers", "Ganesh Residency", "Gokul Apartments", "Vaishnavi Towers", "Radha Residency", "Govind Apartments", "Shiv Shakti Towers", "Durga Residency", "Balaji Enclave", "Venkatesh Towers", "Mahadev Residency", "Surya Apartments", "Chandra Residency", "Arya Towers", "Sagar Residency", "Shivalik Apartments", "Nirmal Towers", "Samruddhi Residency", "Sankalp Apartments", "Aashirwad Towers", "Mangalam Residency", "Swastik Apartments", "Shubhkamna Towers", "Utsav Residency", "Anandam Apartments", "Suvidha Towers", "Navrang Residency", "Shantiniketan Apartments", "Prerna Towers", "Samarpan Residency", "Sahyadri Apartments", "Shubham Towers", "Vaibhav Residency", "Siddhi Apartments", "Akash Towers", "Aastha Residency", "Shree Krishna Apartments", "Omkar Towers", "Sukh Sagar Residency"]
  road_type = ["Road", "Street", "Lane", "Marg", "Path", "Chowk", "Circle", "Nagar", "Main Road", "Cross Road", "Avenue", "Bypass", "Extension", "Layout"]

  # street names pattern: 
  # Pattern A — Person Name: 
  person_name = ["Gandhi", "Nehru", "Patel", "Ambedkar", "Subhash", "Tilak", "Tagore", "Vivekananda", "Shivaji", "Rajiv Gandhi", "Indira Gandhi", "Sardar Patel"]
  # Pattern B — Landmark / Feature
  landmark_name = ["Lake", "Temple", "Market", "Station", "College", "Church", "Garden", "Hill", "River", "Park", "Industrial", "Airport", "Metro", "Canal"]
  # Pattern C — Numbered Roads

  # Pattern D — Area + Road
  area_name = ["Brigade", "Residency", "Palace", "Cantonment"]

  if recs_count > 0:
    sarr = []
    for _ in range(recs_count):
      random_street = ''

      # Generate House Number
      random_dwelling = random.choice(dwelling_type)
      hno = random.randint(1,9999)
      hlet = random.randint(64,90)
      hlet = chr(hlet) if hlet >= 65 else ''

      if random_dwelling in ["Villa", "Block", "Bungalow"]: random_street += f"{hno}, "
      else: random_street += f"{random_dwelling} {hlet}{random.choice(['-', '/'])}{hno}, {random.choice(building_names)}, "

      # Generate Street
      patterns = ["person_name", "landmark_name", "ordinal_number", "area_name"]
      chosen_pattern = random.choice(patterns)

      if chosen_pattern == 'person_name': random_street += random.choice(person_name) + ' ' + random.choice(road_type)
      elif chosen_pattern == 'landmark_name': random_street += random.choice(landmark_name) + ' ' + random.choice(road_type)
      elif chosen_pattern == 'ordinal_number': random_street += ordinal(random.randint(1,20)) + ' ' + random.choice(road_type)
      elif chosen_pattern == 'area_name': random_street += random.choice(area_name) + ' ' + random.choice(road_type)

      sarr.append(random_street)

    return sarr

def Instructions():
  hdg_fmt = f"""<span style='background-color: #4b0082; 
                          color: white; 
                          border-radius: 4px; 
                          padding-top: 3px; 
                          padding-bottom: 5px; 
                          padding-left: 0.4em; 
                          padding-right: 0.4em; 
                          font-family: {font_name}; 
                          font-size: 18px; 
                          font-weight: bold;
                          margin-bottom: 3px; '>
            """
  sctn_fmt = f"""<span style='background-color: transparent; 
                              color: #4b0082; 
                              padding-top: 3px;
                              padding-left: 0.4em; 
                              font-family: {font_name}; 
                              font-size: 16px; 
                              font-weight: bold;
                              margin-bottom: 3px; '>
              """
  gen_fmt = f"""<span style='background-color: transparent; 
                              color: gray; 
                              padding-top: 3px;
                              padding-left: 0.8em; 
                              font-family: {font_name}; 
                              font-size: 14px; 
                              margin-bottom: 3px; 
                              '>"""
  six_spcs = "&nbsp;" * 6
  three_spcs = "&nbsp;" * 3
  help_separater_line = f"<hr style='margin-top: 0px; margin-bottom: 10px; size: 1px; border: 1px solid; color: #000000; '>"

  htmlstr = f"""
  {hdg_fmt}Generating a dataset:</span><br>
  {help_separater_line}
  <details>
  <summary>{sctn_fmt}Step 1: Schema Create / Upload:</span><br></summary>
  {gen_fmt}
  &nbsp;1. Click on <b>Manage Schema</b> to open, and either:<br>
  {six_spcs}◾ Create a new schema <b>OR</b><br>
  {six_spcs}◾ Upload a saved schema previously created and saved by this application. <b>OR</b><br>
  {six_spcs}◾ Use a sample schema as a guideline.
  </span>
  </details>

  <details>
  <summary>{sctn_fmt}Step 2a: Schema Detail:</span><br></summary>
  <ol>
  <li>Choose a field category for each field you want in your dataset.</li>
  <li>Give a field name to each new field. The provided field name must not be duplicate, or have spaces or special characters.</li>
  <li>Scema related errors will be displayed on the right pane.</li>
  <li>The schema, if new, can be downloaded as a .CSV file for future repeated use. To do this, move the mouse pointer to the top right of the 
  schema table widget to get the option to download the schema.</li></ol>
  </span>
  </details>

  <details>
  <summary>{sctn_fmt}Step 2b: Fields:</span><br></summary>
  {three_spcs}The field categories are as follows:<br>
  {three_spcs}◾ <i>Sr.</i> - A serial number column.<br>
  {three_spcs}◾ <i>ID</i> - An 8-character random code.<br>
  {three_spcs}◾ <i>Title</i> - A courtesy fe/male salutation.<br>
  {three_spcs}◾ <i>First Name</i> - A fe/male name.<br>
  {three_spcs}◾ <i>Surname</i> - A last name.<br>
  {three_spcs}◾ <i>Full Name</i> - A first + last name (fe/male).<br>
  {three_spcs}◾ <i>Blank Field</i> - An empty values column.<br>
  {three_spcs}◾ <i>Email</i> - Email address.<br>
  {three_spcs}◾ <i>Address</i> - Street address.<br>
  {three_spcs}◾ <i>Gender</i> - Fe/Male values column.<br>
  {three_spcs}◾ <i>Department Names</i> - department names.<br>
  {three_spcs}◾ <i>Company Names</i> - company names.<br>
  {three_spcs}◾ <i>Religion</i> - religion column.<br>
  {three_spcs}◾ <i>Languages</i> - limits, if required, can be start and end dates in DD/MM/YYYY formatcolumn.<br>
  {three_spcs}◾ <i>Numbers</i> - limits, if required, can be start and end integers.<br>
  {three_spcs}◾ <i>List Options</i> - Custom List column. Limits, if required, can contain comma separated values (min:2).<br>
  {three_spcs}◾ <i>Bank Names</i> - bank names column.<br>
  </span><br>
  </details>

  <details>
  <summary>{sctn_fmt}Step 3: Dataset:</span><br></summary>
  <ol>
  <li>Choose the number of records to generate.</li>
  <li>Generated records can be downloaded as a .CSV file - to do this, move the mouse pointer to the top right of the generated 
  dataset table widget to get the option to download the data.</li>
  <li>Data has been localized for India.</li>
  </span>
  </details>
  """

  return htmlstr

def GenerateCityStatePin(recs_count, cat_lst):  # "Adilabad": {"PinPrefix": 504, "State": "Telangana"},
  city_lst, state_lst, pin_lst = [], [], []

  city_lst = random.choices(list(CityNamesList.keys()), k=recs_count)
  state_lst = [CityNamesList[cty]['State'] for cty in city_lst]
  pin_lst = [str(random.randint(CityNamesList[cty]['PinPrefix'] * 1000, (CityNamesList[cty]['PinPrefix'] * 1000)+999)) for cty in city_lst]
  
  if 'City' not in cat_lst: city_lst = []
  if 'State' not in cat_lst: state_lst = []
  if 'Pin' not in cat_lst: pin_lst = []

  return state_lst, city_lst, pin_lst

def GenerateNameRelatedComponents(recs_count, cat_lst): # Title, Gender, First Name, Surname, Full Name, Email
  gender_lst, firstname_lst, surname_lst, fullname_lst, email_lst = [], [], [], [], []

  gender_lst = random.choices(GenderList, k=recs_count)
  firstname_lst = [random.choice(MaleFirstNamesList) if gndr[0] == 'M' else random.choice(FemaleFirstNamesList) for gndr in gender_lst]
  title_lst = [random.choice(['Shri', 'Dr.']) if gndr[0] == 'M' else random.choice(['Smt.', 'Dr.']) for gndr in gender_lst]
  surname_lst = random.choices(SurnamesList, k=recs_count)
  for k, v in enumerate(firstname_lst): fullname_lst.append(title_lst[k] + " " + v + " " + surname_lst[k])
  for k, v in enumerate(firstname_lst): email_lst.append(v + "." + surname_lst[k] + "@" + random.choice(EmailProvidersList))
  # email_lst = [x.replace(' ', '.') + "@" + random.choice(EmailProvidersList) for x in fullname_lst]

  if 'Title' not in cat_lst: title_lst = []
  if 'Gender' not in cat_lst: gender_lst = []
  if 'First Name' not in cat_lst: firstname_lst = []
  if 'Surname' not in cat_lst: surname_lst = []
  if 'Full Name' not in cat_lst: fullname_lst = []
  if 'Email' not in cat_lst: email_lst = []

  return title_lst, gender_lst, firstname_lst, surname_lst, fullname_lst, email_lst

def ValidateListOptions(lst_str_to_chk):
  oplst = []
  if lst_str_to_chk.count(',') >= 1: # at least 2 options are required
    oplst = lst_str_to_chk.split(',')
    oplst = [x.strip() for x in oplst if type(x) == str]

  return oplst

# SCTN: Main code

st.html("""
            <style>
                div.block-container {
                    padding-top: 1.5rem;
                    padding-bottom: 0rem;
                }
                header.stAppHeader {
                    background-color: rgba(255, 255, 255, 0.0);
                }
            </style>
        """)    # remove space at top of page
st.html(htmlstr)

cfg = {}
col_type_dd = ['Sr.', 'ID', 'Title', 'First Name', 'Surname', 'Full Name', 'Email', 'Address', 'Gender', 'State', 'City', 'Pin', 
               'Company Names', 'Department Names', 'Designations', 'Religion', 'Languages', 'Dates', 'Numbers', 'List Options', 
               'Airline Names', 'Pet Types', 'Blank Field', 'Bank Names']

cfg['Category'] = st.column_config.SelectboxColumn(label='Category', 
                                                    default='', 
                                                    required=True, 
                                                    options=col_type_dd, 
                                                    width="small",
                                                    help='Choose Category from the dropdown list')
cfg['Column_Name'] = st.column_config.TextColumn(label='Column Name', 
                                                  default='', 
                                                  required=True, 
                                                  width="medium",
                                                  help='Set output Column Name (one word, no special characters)')
cfg['Limits'] = st.column_config.TextColumn(label='Column Limits', 
                                                   default='', 
                                                   width="medium",
                                                   help=':blue[Lower] and :blue[Upper] column limits are :blue[only] applicable for the Number and the Date column, and, :blue[if specified], must be in the format: :blue[Lower, Upper]. \n\nBoth limits will be ignored if not/partially specified.\n\nDate Limits, if specified, must be in the DD-MM-YYYY format eg. :blue[25-01-2025, 15-12-2026].\n\nNumber Limits, if specified, must be in the integer format eg. :blue[12, 26].')

scm1, scm2 = st.columns(2)
with scm1:  
  scmm1, scmm2 = st.columns((9,1))
  with scmm2.popover(":material/quick_reference:", width='stretch'): st.html(Instructions())

  with scmm1.expander(label=":blue[Manage Schema:]", icon=':material/account_tree:', expanded=False):
    create_load_schema = st.radio('', ('Create Schema', 'Load Schema', 'Sample Schema'), horizontal=True, index=0, label_visibility='collapsed')
  
  
    if create_load_schema == 'Create Schema':
      stdf = pd.DataFrame(columns=['Category', 'Column_Name', 'Limits'])

    elif create_load_schema == 'Load Schema':
      uploaded_file = st.file_uploader('', type=['csv'], accept_multiple_files = False, label_visibility='collapsed')
      if uploaded_file is not None: 
        stdf = pd.read_csv(uploaded_file)
        stdf.fillna('', inplace=True)   # fill nan with ''
      else: stdf = pd.DataFrame(columns=['Category', 'Column_Name', 'Limits'])

    elif create_load_schema == 'Sample Schema':
      sdict = {
                'Category': ['Sr.', 'ID', 'Title', 'First Name', 'Surname', 'Full Name', 'Email', 'Address', 'Gender', 'State', 'City', 'Pin', 
                            'Company Names', 'Department Names', 'Designations', 'Religion', 'Languages', 'Dates', 'Dates', 'Numbers', 
                            'List Options', 'List Options', 'List Options', 'Airline Names', 'Pet Types', 'Blank Field', 'Bank Names'],

                'Column_Name': ['Sr', 'ID', 'Title', 'FirstName', 'Surname', 'FullName', 'Email', 'Address', 'Gender', 'State', 'City', 'Pin', 
                                'CompanyNames', 'DepartmentNames', 'Designations', 'Religion', 'Languages', 'BornOn', 'VisitedOn', 'Numbers',
                                'Boolean', 'TrueFalse', 'YNM', 'AirlineNames', 'PetTypes', 'BlankField', 'BankNames'],

                'Limits': ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','01-04-2023, 31-03-2024', '1276,5421', '0,1', 
                          'True, False', 'Yes, No, Maybe', '', '', '', '']
              }
      stdf = pd.DataFrame(sdict)

  st.write(":blue[Schema Detail:]")
  sdf = st.data_editor(stdf, height=450, column_config=cfg, hide_index=True,  num_rows='dynamic', width='stretch')

with scm2:
  vis_error, verrormsg = False, ''
  try:
    if sdf.shape[0] == 0: vis_error, verrormsg = True, verrormsg + '✋ Schema cannot be empty or blank.<br>'
    if (sdf['Column_Name'] == '').any(): vis_error, verrormsg = True, verrormsg + '✋ Column Names must cannot be empty.<br>'
    if (sdf['Column_Name'].duplicated().any()): vis_error, verrormsg = True, verrormsg + '✋ Column Names must be unique.<br>'
    if (sdf['Column_Name'].str.contains(' ', na=False).any()): vis_error, verrormsg = True, verrormsg + '✋ Column Names cannot have embedded spaces.<br>'
    if (sdf['Column_Name'].str.contains(repattern, regex=True, na=False).any()): vis_error, verrormsg = True, verrormsg + '✋ Column Names cannot have special characters.<br>'
  
    uniq_cols = ['Sr.', 'Title', 'First Name', 'Surname', 'Full Name', 'Email', 'Address', 'Gender', 'State', 'City', 'Pin', 
                 'Company Names', 'Department Names', 'Designations', 'Religion', 'Languages', 'Airline Names', 'Pet Types', 
                 'Bank Names']  # these columns can be twice within the same schema
    
    for col_nme in uniq_cols:
      if int(sdf['Category'].value_counts().get(col_nme, 0)) > 1: vis_error, verrormsg = True, verrormsg + f'✋ There cannot be more than 1 {col_nme} Column.<br>'
  
  except: pass

  if not vis_error:
    rc1, rc2 = st.columns(2)
    rc1.write('')
    recs_count = rc2.number_input(label="Number of records to generate:", value=100, format='%d', icon=None, width="stretch")
    rc1.subheader(":blue[Generated Dataset:]")

    if recs_count > 1:
      msg = st.toast("Preparing data...",  icon=":material/line_start:")

      cat_lst = list(sdf['Category'])
      col_list = list(sdf['Column_Name'])
      limits_list = list(sdf['Limits'])
      
      gtdf = pd.DataFrame(columns=col_list)

      msg.toast("Processing fields...", icon=":material/line_start_diamond:")
      
      state_lst, city_lst, pin_lst = GenerateCityStatePin(recs_count, cat_lst)  # get State, City & Pin on basis of city
      title_lst, gender_lst, firstname_lst, surname_lst, fullname_lst, email_lst = GenerateNameRelatedComponents(recs_count, cat_lst)

      for _, cat in enumerate(cat_lst):
        if cat == 'Sr.': gtdf[col_list[_]] = [x+1 for x in range(recs_count)]
        if cat == 'Company Names': gtdf[col_list[_]] = random.choices(CompanyNamesList, k=recs_count)
        if cat == 'Religion': gtdf[col_list[_]] = random.choices(ReligionNamesList, k=recs_count)
        if cat == 'Designations': gtdf[col_list[_]] = random.choices(DesignationNamesList, k=recs_count)
        if cat == 'Department Names': gtdf[col_list[_]] = random.choices(DepartmentNamesList, k=recs_count)
        if cat == 'Languages': gtdf[col_list[_]] = random.choices(LanguageNamesList, k=recs_count)
        if cat == 'Airline Names': gtdf[col_list[_]] = random.choices(AirlineNamesList, k=recs_count)
        if cat == 'Pet Types': gtdf[col_list[_]] = random.choices(PetCategoryList, k=recs_count)
        if cat == 'Bank Names': gtdf[col_list[_]] = random.choices(BankNamesList, k=recs_count)
        if cat == 'ID': gtdf[col_list[_]] = generate_unique_ids_shortuuid(recs_count)     # 8 char + number
        if cat == 'Address': gtdf[col_list[_]] = GenerateStreetAddress(recs_count)
        if cat == 'Blank Field': gtdf[col_list[_]] = [''] * recs_count
        
        if cat == 'State': gtdf[col_list[_]] = state_lst
        if cat == 'City': gtdf[col_list[_]] = city_lst
        if cat == 'Pin': gtdf[col_list[_]] = pin_lst

        if cat == 'Title': gtdf[col_list[_]] = title_lst
        if cat == 'Gender': gtdf[col_list[_]] = gender_lst
        if cat == 'First Name': gtdf[col_list[_]] = firstname_lst
        if cat == 'Surname': gtdf[col_list[_]] = surname_lst
        if cat == 'Full Name': gtdf[col_list[_]] = fullname_lst
        if cat == 'Email': gtdf[col_list[_]] = email_lst
        
        if cat == 'List Options': 
          lolst = ValidateListOptions(limits_list[_])
          if len(lolst) > 0: gtdf[col_list[_]] = random.choices(lolst, k=recs_count)

        if cat == 'Dates':
          gtdf[col_list[_]] = GetRandomDate(limits_list[_], recs_count)
          gtdf[col_list[_]] = pd.to_datetime(gtdf[col_list[_]], dayfirst=True).dt.strftime(date_format)

        if cat == 'Numbers':
          gtdf[col_list[_]] = GetRandomNumber(limits_list[_], recs_count)
          gtdf[col_list[_]] = gtdf[col_list[_]].astype(int)

        if cat == 'Pin':
          gtdf[col_list[_]] = GetRandomNumber('110001, 855117', recs_count)
          gtdf[col_list[_]] = gtdf[col_list[_]].astype(int)

      msg.toast("Dataset complete...", icon=":material/check_box:")
      if gtdf.shape[0] > 0: st.dataframe(gtdf, hide_index=True, height=463)

  else: st.html("<span style='color: red; font-size:18px;'>Errors:</span><br>" + verrormsg)

st.html("<br>" + separater_line)