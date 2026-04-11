import requests

class ProgramTool:
    def __init__(self, api_key: str):
        self.base_url = "http://iapi.dev.flexoffers.com/agents/v1/program"
        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json"
        }

    def get_program(self, program_id: int):
        try:
            url = f"{self.base_url}/{program_id}"

            response = requests.get(url, headers=self.headers, timeout=10)

            if response.status_code == 200:
                return response.json()

            return {
                "success": False,
                "status_code": response.status_code,
                "error": response.text
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }