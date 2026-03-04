AI Command Center

A multi-tool AI agent with basic memory and a simple Streamlit UI.

🎯 Purpose

This project serves as a foundational learning exercise to understand core AI agent concepts, including tool usage, basic memory management, and interactive UI development.

🧠 Features

• Basic tool integration (calculator, web search, Python executor)

• Simple memory persistence (JSON store)

• Interactive Streamlit user interface

🛠 Tech Stack

Python • LangChain • ChromaDB • Streamlit • Hugging Face Inference API (or local model)

▶️ Demo

Demo section will be added later.

🚀 How to Run
```
# Clone the repository
git clone https://github.com/EnigmaDevelop/ai-command-center.git
cd digital-swiss-army-knife

# Create a virtual environment
python -m venv venv

# Activate the environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the app
streamlit run src/app.py
```

📁 Folder Structure

```
📁 ai-command-center
 ┣ 📂 src
 ┃ ┣ 📁 tools
 ┃ ┣ 🧠 agent.py
 ┃ ┗ 🖥️ app.py
 ┣ 📂 notebooks
 ┃ ┗ 📘 tool-tests.ipynb
 ┣ 📂 data
 ┃ ┗ 🧩 memory.json
 ┣ 📂 tests
 ┃ ┗ 🧪 test_tools.py
 ┣ 📄 requirements.txt
 ┣ 📄 .gitignore
 ┗ 📄 README.md
```

📌 Notes

This project was built to practice core AI engineering skills, including tool-use, memory handling, and UI design. Future improvements may include more advanced planning, richer tools, and better memory systems.
