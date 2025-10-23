import requests


class ImBored:
    def __init__(self, name):
        self.name = name
        self.base_url = "https://www.bored-api.appbrewery.com"

    def im_bored_cli(self):
        print("""
        Bored Activity Finder
        ======================
        1. Get a Random Activity
        2. Get Activity by Type
        3. Get Activity by Participans
        4. Save my Favorite Activities
        5. View my Favorite Activities
        6. Exit
        """)

        response = input("Choose an option (1-6): ")
        return response

    def get_random_activity(self):
        """
        Get a random activity

        API Endpoint: https://www.bored-api.appbrewery.com/random
        """

        # Get response
        response = requests.get(self.base_url)

        # Check response, error if not 200
        if response.status_code != 200:
            return f"Invalid response from: {self.base_url} - {response.status_code}"

        # If status 200 parse json to python
        if response.status_code == 200:
            parsed_data = response.json()
            return parsed_data


bored = ImBored("Boredom Buster")
bored.im_bored_cli()
