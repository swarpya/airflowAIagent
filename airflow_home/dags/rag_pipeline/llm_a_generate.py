import os
import logging
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # Ensure .env variables are loaded

def llm_a_generate(ti, **context):
    """
    First-stage LLM generation: receives retrieved documents, builds input prompt, 
    and calls the GROQ LLM for initial answer generation.
    """
    try:
        # Get retrieved docs from previous task via XCom
        retrieved_docs = ti.xcom_pull(task_ids="retrieve_documents")
        if not retrieved_docs:
            raise ValueError("No documents retrieved for generation.")

        # Build prompt for LLM (customize as needed)
        prompt = (
            "You are an expert assistant. Using the facts below, answer the user's question concisely.\n"
            "Facts:\n"
            + "\n".join(retrieved_docs)
        )

        logging.info(f"Prompt for LLM A: {prompt}")

        # Prepare GROQ client
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            raise EnvironmentError("GROQ_API_KEY not set in environment.")

        client = Groq(api_key=api_key)
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="meta-llama/llama-4-scout-17b-16e-instruct",
        )

        answer = chat_completion.choices[0].message.content
        logging.info(f"GROQ LLM Output: {answer}")

        return answer

    except Exception as e:
        logging.error(f"Error in llm_a_generate: {e}")
        raise  # Ensures Airflow registers this as a task failure
