from langchain_core.prompts import PromptTemplate
intent = """
You are an intelligent {dialect} expert

A user wants to ask you a question for a database
with the tables {table_names}

a question can have the following intents:
INTENT 1:
Retrieval: If the question asks for directly available information which might or might not be based on some condition
    example include but are not limited to:{{
        - what is the name of employee with id 4
        - what is the name of project with project_id 5
        - what is the salary of employee with id 2
        - which projects are assigned to employee with name "John Smith"
    }}

INTENT 2:
Ascending Ranking: If the question asks for the lowest value in any column which might or might not be based on some condition 
    examples include but are not limited to:{{
        - which employee has the least salary
        - who has the lowest salary
        - which employee has the lowest bonus
    }}

INTENT 3:
Descending Ranking: If the question asks for the highest value in any column which might or might not be based on some condition
    examples include but are not limited to:{{
        - which employee has the Highest salary
        - which project has the earliest start date
        - which employee has the lowest bonus
    }}

INTENT 4:
Aggregated: If the question asks for any aggregated value like SUM, AVG, COUNT or any other data that essentially requires grouping data on the basis of certain conditions
    examples include but are not limited to:{{
        - which department has more than 5 employees
        - what is average salary in department with id 4
        - what is the aggregate salary of each department
        - which employee has the least number of leaves
        - which employee has the most active projects
    }}

INTENT 5: 
SUBQUERY RETRIEVAL: If the question is layered and asks for more than one things like comparison with aggregates
    examples include but are not limited to:{{
        - which department has the lowest aggregate salary
        - which employees have above than average salary
        - which employee has more than 2 active projects
        - which employee has performance review in the top 10 percent of all employees
    }}

INTENT 6:
GENERIC: If any of the above intent are not displayed by the question then classify it as a generic query and return the intent 6


INTENT 7:
INVALID: If the question does not classify into any of the above intents or does not make seem relevant to the the database tables then return intent 7 
    examples include but are not limited to:{{
        - what is the highest temperature for today
        - what is your favourite colour
        - what is secret to life
        - which number is the answer to everything 
    }}
The following question is asked by the user 
{question}

Read the question CAREFULLY and classify it into one of these 5 intents. 
Return the intent and and a list of table names that are relevant to the question
in the format below:
{{
    "intent":value_of_intent,
    "relevant_tables":list_of_relevant_table_names
}}

"""

prompt = PromptTemplate.from_template(intent)