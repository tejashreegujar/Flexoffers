from prefect import flow, task
import requests

@task
def call_mcp():
    return requests.post(
        "http://localhost:8000/tools/get_program",
        json={"program_id": 127}
    ).json()

@flow
def run_flow():
    result = call_mcp()
    print(result)

if __name__ == "__main__":
    run_flow()