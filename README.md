# NL2SQL: Natural Language to SQL Query Generator

NL2SQL is a Python-based tool that leverages advanced language models (LLMs) to convert natural language questions into SQL queries, execute them on a specified database, and return human-readable answers. The system is modular, extensible, and supports prompt engineering for various SQL query types (aggregation, retrieval, ordering, etc.).

---

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Testing](#testing)
- [Prompts & Customization](#prompts--customization)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Features
- Convert natural language questions to SQL queries using LLMs (Google Gemini, via LangChain)
- Support for multiple query types: intent detection, retrieval, aggregation, ordering (ASC/DESC), subqueries, and answer generation
- Modular prompt templates for extensibility
- PostgreSQL database support (can be extended to others via SQLAlchemy)
- Environment-based configuration for API keys and database credentials
- Data generation scripts for populating test databases

---

## Project Structure
```
NL2SQL/
├── main.py               # Main entry: CLI for NL2SQL
├── main2.py              # Alternative entry with advanced tools
├── test.py               # Data generation and test script
├── NL2SQL/
│   ├── Base.py           # TypedDicts and base types
│   ├── utils.py          # Utility functions (query execution, state management)
│   ├── prompts/          # Prompt templates for LLM
│   └── settings/
│       └── config.py     # Configuration (env loading, DB, LLM init)
├── .env.example          # Example environment config
├── README.md             # This file
└── ...
```

---

## Requirements
- Python 3.10+
- PostgreSQL (or compatible SQL database)

### Python Packages
- langchain-core
- langchain-community
- langchain
- pydantic-settings
- google-generativeai
- psycopg2-binary
- faker

You can create a `requirements.txt` like below:
```
langchain-core
langchain-community
langchain
pydantic-settings
psycopg2-binary
faker
google-generativeai
```

---

## Installation
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd NL2SQL
   ```
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix/macOS:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables:**
   - Copy `.env.example` to `.env` and fill in your credentials:
     - `GEMINI_API_KEY`: Your Google Gemini API key
     - `DATABASE_URI`: SQLAlchemy-style URI to your database (e.g., `postgresql+psycopg2://user:password@localhost:5432/company`)

---

## Configuration
All configuration is managed via the `.env` file. Example:
```
GEMINI_API_KEY=your-google-gemini-api-key
DATABASE_URI=postgresql+psycopg2://user:password@localhost:5432/company
```
Other database parameters are also supported for flexibility.

---

## Usage
### 1. Run the NL2SQL CLI
```bash
python main.py
```
- Enter your question in natural language when prompted.
- To exit, type `exit`, `escape`, or `quit`.

### 2. Alternative Entrypoint
```bash
python main2.py
```
- This version exposes additional tools for programmatic use and more advanced prompt engineering.

---

## Testing
- Use `test.py` to populate your database with synthetic data for development/testing:
```bash
python test.py
```
- This script uses Faker to generate realistic data for tables like employees, departments, projects, etc.
- **Warning:** This script will DELETE all existing data in the target tables!

---

## Prompts & Customization
- All LLM prompt templates are stored in `NL2SQL/prompts/`.
- You can modify these prompts to adapt to different database schemas, query types, or LLM providers.
- Extend the prompt set for new SQL operations as needed.

---

## Troubleshooting
- **Missing API Key:** Ensure your `.env` file is present and correct.
- **Database Connection Errors:** Double-check your `DATABASE_URI` and that your DB server is running.
- **Dependency Issues:** Ensure all packages in `requirements.txt` are installed and compatible with your Python version.
- **LLM Errors:** Make sure your Gemini API key is valid and has sufficient quota.

---

## License
This project is for educational and research purposes. Please check the repository for license details.