from langchain.prompts import PromptTemplate
instruction = """
The user has asked a question that requires the aggregated data

read the question carefully and generate an appropriate query for this question following the mentioned instructions
Question:{question}

the database has the following schema 
Schema Info: {schema}

**INSTRUCTIONS**
1. Use the where clause as required 
2. Use the join table clause as necessary to get the necessary tables and their columns 
3. Use GROUP BY clause as necessary
4. Use Order by only if necessary
5. use double quotes around all columns names 
6. RETURN ONLY THE QUERY AS A STATEMENT

"""

prompt = PromptTemplate.from_template(instruction)