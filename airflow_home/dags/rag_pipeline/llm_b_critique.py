def llm_b_critique(ti, **context):
    from dotenv import load_dotenv
    load_dotenv()
    import requests
    import os

    # Pull LLM A's answer from XCom
    response_a = ti.xcom_pull(task_ids="llm_a_generate")

    # Call your second LLM API (could be GROQ, OpenAI, Anthropic, etc.)
    critique_prompt = f"Review and improve the following answer for errors and clarity:\n\n{response_a}"
    # placeholder for your second LLM call
    improved_answer = "..."  # Real call here

    print("LLM B Critique Output:", improved_answer)
    return improved_answer
