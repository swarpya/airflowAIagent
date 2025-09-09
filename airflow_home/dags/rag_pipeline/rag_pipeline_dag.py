from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum

from datetime import timedelta
import sys
import os

# Optionally, add your custom modules' location
sys.path.append(os.path.join(os.path.dirname(__file__)))

from retrieval import retrieve_documents
from llm_a_generate import llm_a_generate
from llm_b_critique import llm_b_critique
from utils import notify_failure
         # Placeholder function

# Basic default_args for a production pipeline
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['swaroopingavale73@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    "rag_llm_chain_pipeline",
    default_args=default_args,
    description="RAG pipeline chaining LLMs (GROQ + Critique)",
    schedule="0 * * * *",
    start_date=pendulum.now("UTC").subtract(days=1),
    catchup=False,
    max_active_runs=1,
) as dag:

    retrieval_task = PythonOperator(
        task_id="retrieve_documents",
        python_callable=retrieve_documents,
    )

    llm_a_task = PythonOperator(
        task_id="llm_a_generate",
        python_callable=llm_a_generate,
    )

    llm_b_task = PythonOperator(
        task_id="llm_b_critique",
        python_callable=llm_b_critique,
    )

    notify_task = PythonOperator(
        task_id="notify_failure",
        python_callable=notify_failure,
        trigger_rule="one_failed",
    )

    retrieval_task >> llm_a_task >> llm_b_task
    [llm_a_task, llm_b_task, retrieval_task] >> notify_task