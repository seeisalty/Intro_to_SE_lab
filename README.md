# Intro to SE Lab - E-Commerce Platform

## **Project Description**
The Intro to SE Lab project is an e-commerce platform designed to provide a seamless experience for buyers, sellers, and administrators. The platform will allow users to browse, compare, buy, and sell products while enabling administrators to manage user accounts and product listings.

This project is part of a Software Engineering Lab course and follows agile development principles over multiple sprints. The platform will be developed in two versions, with version 1 focusing on core functionalities, while version 2 will incorporate additional features based on feedback.

## **Objective**
The goal of this project is to develop a functional e-commerce web application that meets the needs of different types of users (buyers, sellers, and admins). The project emphasizes:
- Implementing a user-friendly online marketplace.
- Applying Django’s MVC (Model-View-Controller) architecture for structured development.
- Utilizing agile methodologies through iterative sprints.
- Enhancing team collaboration using GitHub and version control.

## **Key Features**
The platform will include the following functionalities:

### **User Roles**
✅ **Buyer:**
- Search, compare, and purchase products.
- Initiate product returns if necessary.

✅ **Seller:**
- List and manage products.
- Receive payments from buyers.

✅ **Admin:**
- Approve or block user accounts and product listings.
- Oversee user activities and platform security.

### **Core Features**
✅ **User Authentication** – Secure login/logout functionality for different roles.  
✅ **Product Management** – Sellers can add and update products.  
✅ **Search & Compare** – Buyers can filter products based on various criteria.  
✅ **Shopping Cart & Payments** – Buyers can add items to the cart and complete purchases.  
✅ **Order Management** – Track purchases and handle returns.  
✅ **Admin Dashboard** – Monitor platform activities and manage content.  

## **Project Type**
- **Web Application / Website**
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite/PostgreSQL (TBD)
- **Version Control:** GitHub

## **Development Plan**
The project will be developed in **four sprints**, each lasting **2 to 4 weeks**, following **agile development methodologies**. Version 1 will implement the core functionalities, while version 2 will introduce **additional features** based on instructor feedback.

## **Team Members**
| Name            | NetID           | GitHub Username                | Email                          | Role                    |
|-----------------|-----------------|--------------------------------|--------------------------------|-------------------------|
| Andrew Moore    | ajm1084         | seeisalty                      | andymoore0204@gmail.com        | Team Leader             |
| Jacob Frayser   | jf1774          | JacobFrayser                   | jacobfrayser@gmail.com         | Backend & Database      |
| Aidan Scahill   | afs214          | AidanScahill                   | aidancontrolled@gmail.com      | Frontend UI/UX          |
| Jeremias Conerly| jlc1667         | Jeremias-27                    | jeremiasc04@icloud.com         | API & Integration       |
| Cameron Cummings| cdc888          |                                | cameroncummings2100@gmail.com  | Documentation & Testing |

## **Repository**
**GitHub Repository:** [Intro_to_SE_lab](https://github.com/seeisalty/Intro_to_SE_lab)

---

## **How to Set Up & Run the Project**
Follow these steps to **set up and run the project** on your local machine.

### **1. Clone the Repository**
```bash
git clone https://github.com/seeisalty/Intro_to_SE_lab.git
cd Intro_to_SE_lab

## **2. Set Up a Virtual Environment**
Set up a virtual environment ensures that dependencies are isolated.

For Windows

python -m venv venv
venv\Scripts\activate

if activation fails on windows try running : Set-ExecutionPolicy Unrestricted -Scope Process

## **3. Install Project Dependencies**
Once the virtual environment is activated, install the required packages:

pip install -r requirements.txt
If requirements.txt is missing, install Django manually:

pip install django
Then generate the file:

pip freeze > requirements.txt

## **4. Apply Database Migrations**
Run the following command to create the necessary database tables:

python manage.py migrate
If any models are added later, run:

python manage.py makemigrations
python manage.py migrate

## **5. Create a Superuser (Admin Access)**
To create an admin account for the Django admin panel:

python manage.py createsuperuser
Follow the prompts to set a username, email, and password. !!!DO NOT FORGET!!!

You can now log in to the admin panel at:
🔗 http://127.0.0.1:8000/admin/

## **6. Run the Development Server**

python manage.py runserver
Once running, open http://127.0.0.1:8000/ in your browser.
