from langchain.prompts import PromptTemplate
instruction = """
The user has asked a question that requires the data from a subquery to retrieve data for the larger query

read the question carefully and generate an appropriate query for this question following the mentioned instructions
Question:{question}

the database has the following schema 
Schema Info: {schema}

**INSTRUCTIONS**
1. use the where clause as required 
2. use the join table clause as necessary to get the necessary tables and their columns 
3. Use a subquery in WHERE or HAVING as needed
4. Retrieve at most 10 rows with LIMIT.
5. Include JOINs if needed.
6. Use double quotes around all column names.
7. RETURN ONLY THE QUERY AS A STATEMENT

"""

prompt = PromptTemplate.from_template(instruction)