# OCD-E
## Repository for OCD-E, SSL'21 Project
### This is Official Documentation for OCD-E

#### [ALL RIGHTS RESERVED BY DYNAMIC DUDES]

Developed by Dhananjay Kejriwal (200050034), Sri Harsha (200050041), Margav Savsani (200050072) and Sartaj Islam (2000500128)

NOTE: Branch "harsha" has final commit
<br>
<br>
Description: OCD-E is a web-app which allows user to practice, code without any downloads i.e. completely on browser itself, in three popular languages namely C++, Python and JAVA.

### Developers' View of OCD-E
<ui>
  <li>Backend is developed using Django Web Framework provided by Python</li>
  <li>Frontend is developed using CSS and Bootstrap in HTML</li>
  <li>Code Execution is done in Docker for Enviroment Isolation</li>
  <li>User Authentication is done by Google Open Authentication</li>
</ui>

<br>

### Salient features of our web-app
<ui>
  <li>User has a facility to sign up and make an account on our website via Google Open Authentication, this makes it easier for user to login anytime using google account (as we all forget passwords at least three times in our life)</li>
  <li>We have used Social Accounts App provided by Django and intergrated with OAuth account made using gsuite account
  <li>User can code in text editor provided by web-app or can paste their code in three languages (C++, Python and JAVA)</li>
  <li>User can save code written by them (upto 10 files) and can access them at any other time after authorisation</li>
  <li>User can update or delete their saved code anytime</li>
  <li>User can also add title for easy identification, however it is must for user to name title as the name of class if code is in JAVA</li>
  <li>User can see all of their saved code files in their dashboard and can access them</li>
  <li>User can list all other users and their codes also, but cannot edit them for obvious reasons</li>
  <li>User can execute ANY code i.e. of other users also, along with input, and can see the output as well as error mesage if any </li>
  <li>Excution is done in disposable docker container so that any notorious user must not corrupt the server side of web-app</li>
  <li>For the promotion of Dynamic Dudes Corporation, User can also see "About Us" from second link in navigation bar (Can also contact us for paid collaboration :p ) 
</ui>

#### Some necessary requirements for a machine to host the Server
Machine must have python installed, along with latest version of Django. It should also have a docker image named "cs251aut2021" with necessary softwares installed, and sudo permission must be given to server terminal (or also works if password is "kurama") which will be used to make docker containers
