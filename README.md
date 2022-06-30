# fastapi_python_assignment
Signality take-home assignment

Restfull API Using Flaskapi framework
-------

Prerequisite
1.Docker deaman run in the system. 
2.Python and pip is installed.

#How to run the Programme 
>Go to the project root directory and run below command

Create docker image
>docker build -t fastapi .

Run the Container 
>docker run -p 8000:8000 --name fastapi-v1.0 fastapi

Once it up and run the server you can perform api calls using  below with swagger client
If it is localhost then you can access line below.
>http://localhost:8000/docs

else 
>http://ip:8000/docs 

