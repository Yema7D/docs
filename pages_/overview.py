

def load_overview(st):
    st.title("Developing a Chatbot Fine-tuned on a Custom Context Based on French Language Models (LLMs) to Generate Video Game Stories")
    st.subheader("Objective")
    st.write("""
    The proposed objective is the establishment of a smart chatbot based on Retrieval Augmented Generation (RAG), LangChain, and Vector Databases, fine-tuned in a small French corpus. This demonstrates a comprehensive and ambitious project. To further improve it in an academic way, consider the following refinements:
    """)
    
    st.subheader("Introduction and Motivation")
    st.write("""
    - Clearly articulate the motivation behind choosing RAG, LangChain, and Vector Databases for the chatbot.
    - Provide a brief literature review on the existing chatbot technologies, especially in French language processing.
    - Clearly define the scope and limitations of your chatbot in the field of game story generation.
    """)

    st.subheader("Methodology")
    st.write("""
    - Elaborate on the step-by-step methodology for implementing Retrieval Augmented Generation (RAG), LangChain, and Vector Databases.
    - Provide references to the original papers and research studies supporting the choice of these technologies.
    - Discuss the fine-tuning process, detailing how the selected corpus (see the document “1-scenario de jeu video.pdf”) contributes to the chatbot's effectiveness.
    """)

    st.subheader("Backend Development")
    st.write("""
    - Explain in detail the choice of FastAPI or Flask for the backend, justifying the decision based on factors like performance, scalability, and ease of development.
    - Discuss how DevOps tools will be integrated into the development lifecycle for continuous integration and deployment.
    """)

    st.subheader("Single Page Application (SPA)")
    st.write("""
    - Clarify the reasons for choosing a Single Page Application architecture for the backend.
    - Discuss the benefits and challenges associated with SPA in the context of your chatbot.
    """)

    st.subheader("Language Model Training")
    st.write("""
    - Provide insights into the process of fine-tuning the language models for French, considering linguistic nuances and cultural contexts.
    - Discuss any challenges encountered during the fine-tuning process and proposed solutions.
    """)

    st.subheader("User Interface (UI) Design")
    st.write("""
    - If applicable, detail the UI/UX design for the chatbot's frontend.
    - Discuss accessibility considerations and how the UI design aligns with the cultural preferences of the target audience.
    """)
    st.image("images/overview.png", caption="Overview Image", use_column_width=True)

    st.subheader("Tools")
    st.write("""
    - LLMs (GPT, Falcon, Eagle…)
    - LangChain
    - Vector database (Cassandra, Elasticsearch, Chroma, Drant)
    - MLOps
    - Angular
    - FastAPI
    - Docker
    - French NLP
    """)