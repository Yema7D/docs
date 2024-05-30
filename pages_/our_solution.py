


def load_our_solution(st):
    # Section: Our Solution
    st.title('Our Solution')

    # Subsection: Data
    st.subheader('Data')

    st.markdown("""
    In our project, we faced a significant challenge: the lack of available datasets for French video game story data. To address this, we utilized translation techniques to convert an existing English corpus into French, enabling us to create a comprehensive dataset for our needs.
    """)
    st.image("images/archite-data-translation.jpg", caption="Data Translation Image", use_column_width=False)
    st.markdown("""
    - **Source Dataset:** The primary dataset we used is [IconicAI/DDD](https://huggingface.co/datasets/IconicAI/DDD), which contains a rich collection of English video game stories.
    - **Dataset after translation to French:** After translating the source dataset into French, we created [samir5636/samir-games-dataset](https://huggingface.co/datasets/samir5636/samir-games-dataset). This new dataset retains the original narratives but in French, making it suitable for our project’s requirements.
    - **Model used for translation:** The translation process was carried out using advanced machine translation models available on Hugging Face. Specifically, we employed models such as [EasyNMT](https://huggingface.co/easynmt) that are renowned for their accuracy in translating between English and French. These models leverage state-of-the-art neural machine translation techniques to ensure high-quality translations.

    This approach allowed us to overcome the data scarcity issue and enabled the development of a robust dataset tailored to the French language, which is crucial for training and fine-tuning our language models. The translated dataset maintains the integrity and context of the original stories, ensuring that the nuances and intricacies of the video game narratives are preserved.
    """)

    # Subsection: Fine-Tuning
    st.subheader('Fine-Tuning')
    

    st.markdown("""
    For fine-tuning, we selected the Mistral 7B model as our base model. Mistral 7B is a highly capable language model known for its performance and efficiency. We trained this model on the [IconicAI/DDD](https://huggingface.co/datasets/IconicAI/DDD) dataset to adapt it specifically to the domain of video game stories.
    """)
    st.image("images/archite-fine-tunning.png", caption="Fine-Tuning Image", use_column_width=True)
    st.markdown("""
    - **Base Model:** [Mistral 7B](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)
    - **Training Dataset:** [IconicAI/DDD](https://huggingface.co/datasets/IconicAI/DDD)

    The fine-tuning process involved several steps:

    - **Preprocessing:** The dataset was preprocessed to ensure compatibility with the Mistral 7B model, including tokenization and formatting.
    - **Training:** We employed techniques such as gradient accumulation and learning rate scheduling to optimize the training process and achieve the best possible model performance.
    - **Validation:** Regular validation was performed to monitor the model’s performance and prevent overfitting.

    Through this fine-tuning process, the Mistral 7B model was effectively adapted to understand and generate content in the context of video game stories, making it a powerful tool for our project.
    """)

    # Subsection: RAG: Document Question Answering
    st.subheader('RAG: Document Question Answering')

    st.markdown("""
    For document question answering, we implemented Retrieval-Augmented Generation (RAG) to enhance the model's ability to provide accurate and contextually relevant answers. RAG combines the strengths of retrieval-based and generation-based models.
    """)
    st.image("images/archite-rag.png", caption="RAG Image", use_column_width=True)
    st.markdown("""
    - **Vector Database:** We used ChromaDB as our vector database. ChromaDB is designed to efficiently store, index, and retrieve high-dimensional vectors, making it ideal for handling the embeddings required in our RAG system.
    - **Embeddings:** To represent the documents and queries as embeddings, we employed the SentenceTransformer model [paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2). This model provides high-quality multilingual embeddings, suitable for our bilingual dataset.

    The RAG system operates as follows:

    - **Retrieval:** Given a user query, the system retrieves relevant documents from the ChromaDB based on the similarity of their embeddings to the query embedding.
    - **Generation:** The retrieved documents provide context for the language model, which then generates a detailed and contextually accurate answer to the query.

    By integrating ChromaDB and SentenceTransformer, our RAG system effectively bridges the gap between information retrieval and natural language generation, ensuring that the answers provided are both precise and informative.
    """)