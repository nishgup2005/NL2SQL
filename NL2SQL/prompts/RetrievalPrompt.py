from langchain.prompts import PromptTemplate
instruction = """
The user has asked a question that requires simple data retrieval

read the question carefully and generate an appropriate query for this question following the mentioned instructions
Question:{question}

the database has the following schema 
Schema Info: {schema}

**INSTRUCTIONS**
1. use the where clause as required 
2. use the join table clause as necessary to get the necessary tables and their columns 
3. Do not use GROUP BY clause
4. Do not use Order BY clause
5. use the distinct keyword as required
5. Unless mentioned specifically for a PARTICULAR NUMBER of values or ALL values limit your answers to 5
6. use double quotes around all columns names 
7. DO NOT USE DOUBLE QUOTES AROUND LITERALS OR VALUES
8. **RETURN ONLY THE QUERY AS A STATEMENT**

"""

prompt = PromptTemplate.from_template(instruction)