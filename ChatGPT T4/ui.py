import urllib.parse
import os
from langchain.llms.azure_openai import AzureOpenAI  # Change the import to AzureOpenAI

from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import AgentExecutor

from langchain.sql_database import SQLDatabase

from dotenv import load_dotenv # pip install load-dotenv
load_dotenv()

import psycopg2 # pip install psycopg-binary
# os.environ['OPENAI_API_KEY'] = "............."  # No need for OpenAI API key with Azure
# Your details
username = 'postgres'
password = 'Test@1234'
hostname = 'localhost'
dbname = 'TestDB1'

# Encode the password
encoded_password = urllib.parse.quote_plus(password)

# Connection URI
uri = f"postgresql://{username}:{encoded_password}@{hostname}:5432/{dbname}"
db = SQLDatabase.from_uri(uri)

# password = "Test@1234";
# db = SQLDatabase.from_uri('postgresql+psycopg2://postgres:Test@1234@localhost:5432/TestDB1')
print(db)

from langchain.chat_models import ChatOpenAI
# Initialize Azure OpenAI with your Azure API key
azure_api_key = "YOUR_AZURE_API_KEY_HERE"
llm = AzureOpenAI(api_key=azure_api_key, model_name="text-davinci-003")  # Specify the appropriate model name for Azure

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

agent_executor.run("what is the member id of Naveen")
