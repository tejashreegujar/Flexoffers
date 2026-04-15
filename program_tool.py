import requests

class ProgramTool:
    def __init__(self, api_key: str):
        self.base_url = "http://iapi.dev.flexoffers.com/agents/v1"
        self.headers = {    "x-api-key": api_key,
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

    def update_program_categories(self,program_id: int,category_ids: list,mode: str, reason: str,source: str):
        try:
            url = f"{self.base_url}/programs/{program_id}/categories"
            params = {"mode": mode}   # ✅ query param

            print("Calling URL:", url, "Params:", params)

            category = {
                "categoryIds": category_ids,
                "reason": reason,
                "source": source
            }

            response = requests.put(
                url,
                headers=self.headers,
                params=params,   # ✅ pass mode dynamically
                json=category,
                timeout=10
            )
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

    def update_program_status(  self,program_ids: list[int],action: str,reason: str,source: str = "API",dry_run: bool = False,send_notifications: bool = True):
        try:
            url = f"{self.base_url}/programs/status"
            status = {
            "action": action,
            "programIds": program_ids,
            "reason": reason,
            "source": source,
            "dryRun": dry_run,
            "sendNotifications": send_notifications
                       }   
            response = requests.post(url,headers=self.headers,json=status,timeout=10)

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