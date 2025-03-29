# 🏥 ShadowFox Project
# Medibot - AI-Powered Medical Assistant


*Intelligent symptom analysis with medical knowledge retrieval*

## 🌟 Key Features

- **📄 PDF Knowledge Base** - Medical document processing and vector storage
- **🧠 Memory-Augmented AI** - Context-aware conversations
- **💊 Medication Advisor** - Drug information retrieval
- **🤒 Symptom Analyzer** - Preliminary condition assessment

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Pipenv (included in Pipfile)

```bash
# 1. Clone repository
git clone https://github.com/Lakshi2006/ShadowFox-Projects.git
cd ShadowFox-Projects/Medical_Chatbot

# 2. Install dependencies
pipenv install

# 3. Set up vector store (requires medical PDFs in /data)
python create_memory_for_llm.py

# 4. Launch the chatbot
pipenv run python medibot.py
🧠 System Architecture

    A[User Input] --> B(medibot.py)
    B --> C{Memory System}
    C --> D[connect_memory_with_llm.py]
    D --> E[(FAISS VectorStore)]
    E --> F[PDF Knowledge]
    C --> G[Response Generation]
📂 Project Structure
Copy
Medical_Chatbot/
├── data/                   # Medical PDF knowledge base
├── vectorstore/db_faiss/   # Processed vector embeddings
├── Pipfile                 # Python environment config
├── Pipfile.lock            # Dependency tree
├── Requirements.txt        # Alternative requirements
├── medibot.py              # Main chatbot interface
├── create_memory_for_llm.py # FAISS vector store creator
└── connect_memory_with_llm.py # Memory retrieval system
🛠️ Customization
To add new medical knowledge:

Place PDFs in /data folder

Rebuild vector store:

bash
Copy
python create_memory_for_llm.py
Configure memory settings:

python
Copy
# In connect_memory_with_llm.py
MEMORY_CONFIG = {
    "search_depth": 3,      # Number of relevant passages
    "similarity_threshold": 0.7  # Minimum match score
}
⚠️ Medical Disclaimer
"This AI system provides preliminary health information for educational purposes only. It is not a substitute for professional medical advice, diagnosis or treatment."


---
*⭐ If this project helped you, consider starring it to help others discover it too.*





