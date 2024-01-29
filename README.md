EcoInvent FastAPI Application

This document provides instructions on how to set up and run the EcoInventDB FastAPI application. The application is designed to model industrial processes and requires a PostgreSQL database.


Before you begin, ensure you have the following installed on your machine:

    Docker Desktop
    Python 3.x
    pip (Python package installer)

Database Setup

The application uses a PostgreSQL database. You can easily set this up using Docker.

1. Start Docker Desktop: Ensure Docker Desktop is running on your machine.

2. Pull PostgreSQL Image (bash):

docker pull postgres
3. Run PostgreSQL Container (bash):

docker run --name EcoInventDB -e POSTGRES_PASSWORD=TheBestPassword -e POSTGRES_USER=admin -e POSTGRES_DB=database -p 5432:5432 -d postgres

This command starts a PostgreSQL server with:

Database name: database
User: admin
Password: TheBestPassword
Port: 5432


Before running the application, you need to set up the database schema by executing the SQL scripts provided in the table_creation.sql file. This file contains the necessary SQL commands to create the tables and relationships needed by the application.

You can run this script using any database management tool that supports PostgreSQL, such as pgAdmin or even via command line using psql. 

Here's how you can do it in pgAdmin:

1. Open pgAdmin and connect to your PostgreSQL server.
2. Navigate to your database (database as per the setup instructions).
3. Open the Query Tool.
4. Load or paste the contents of table_creation.sql into the Query Tool.
5. Execute the script to create the tables.
6. Ensure that the script runs without errors and that all tables are created successfully in your database.

Note:
It is essential that you run this script in the correct database (database), as it sets up the schema that the FastAPI application expects.

Application Setup
Clone the Repository https://github.com/DonchenkoNadia/ecoinv.git to your local machine

Install Dependencies
Navigate to the application directory and run (bash):

pip install -r requirements.txt

This command will install all the necessary Python packages.

Execute the following command to start the FastAPI application (bash):

python main.py
The application will start and be accessible at http://localhost:8080.

After starting the application, you can access the API endpoints through your web browser or API client tools like Postman. 

The application includes an auto-generated interactive API documentation (Swagger UI) accessible at http://localhost:8080/docs


Example of Usage
Once the application is up and running, you can interact with the API endpoints. One of the primary functionalities is to add a new process. Here is an example of how to use the /add_process endpoint.

Adding a New Process
You can add a new industrial process to the system by sending a POST request to http://localhost:8080/add_process with a JSON body. Here is an example of such a request:

Sample Request Body (json):

{
    "name": "Paper Manufacturing",
    "description": "The process of converting wood into paper",
    "type": "Manufacturing",
    "inputs": [
        {
            "properties": [
                {
                    "property_name": "Material Name",
                    "property_value": "Wood"
                },
                {
                    "property_name": "Quantity",
                    "property_value": "1000 kg"
                },
                {
                    "property_name": "Type",
                    "property_value": "Pine"
                }
            ]
        }
    ]
}
This request adds a new process named "Paper Manufacturing" with various inputs and their properties. You can use tools like Postman or Talend to send this request.