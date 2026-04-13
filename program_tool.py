import requests

class ProgramTool:
    def __init__(self, api_key: str):
        self.base_url = "http://iapi.dev.flexoffers.com/agents/v1"
        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json"
        }

    def get_program(self, program_id: int):
        try:
            url = f"{self.base_url}/programs/{program_id}"
            print("Calling URL:", url)
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
        
    def post_program_preFlight(self, program_id: int):
        try:
            url = f"{self.base_url}/programs/{program_id}/preflight"
            print("Calling URL:", url)
            response = requests.post(url, headers=self.headers, timeout=10)

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
        
    def get_categories(self):
        try:
            url = f"{self.base_url}/categories"
            print("Calling URL:", url)
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