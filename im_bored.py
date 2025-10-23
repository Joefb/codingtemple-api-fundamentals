import requests


class ImBored:
    def __init__(self, name):
        self.name = name
        self.base_url = "https://bored-api.appbrewery.com/random"

    def get_response(self):
        """
        Method to handle GET requests
        Parses data and returns
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
        try:
            if int(response) < 1 or int(response) > 6:
                print("Invalid Response. Choose 1-6.")

        except ValueError:
            print("Invalid response. Choose 1-6.")

        if int(response) == 1:
            self.get_random_activity()

    def get_random_activity(self):
        """
        Get a random activity

        API Endpoint: https://bored-api.appbrewery.com/random
        """
        # Get response
        response = self.get_response()
        print(response)
        return response


bored = ImBored("Boredom Buster")
bored.im_bored_cli()
# print(bored.get_random_activity())
