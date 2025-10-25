import re
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

        while True:
            response = input("Choose an option (1-6): ")
            try:
                if int(response) < 1 or int(response) > 6:
                    print("Invalid Response. Choose 1-6.")
                    continue

            except ValueError:
                print("Invalid response. Choose 1-6.")
                continue

            else:
                break

        return int(response)

    def print_activity(self, name, activity):
        activity_dict = activity

        print(f"""
        {name} Activity Suggestion:
        ---------------------------------
        Activity: {activity_dict["activity"]}
        Type: {activity_dict["type"]}
        Participants: {activity_dict["participants"]}
        Price: {activity_dict["price"]}
        Web Link: {activity_dict["link"]}
        Accessibility: {activity_dict["accessibility"]}
        """)

    def get_random_activity(self):
        """
        Get a random activity

        API Endpoint: https://bored-api.appbrewery.com/random
        """
        # Get response
        response = self.get_response()
        return response

    def get_activity_by_type(self):
        pass

    def get_activity_by_participants(self):
        pass

    def save_activity(self, activity):
        pass

    def print_saved_activities(self):
        pass


def main():
    bored = ImBored("Boredom Buster")

    while True:
        get_activity = bored.im_bored_cli()
        activity = None

        if get_activity == 6:
            print("Have a good day!! Hope you enjoyed!")
            exit()

        if get_activity == 1:
            activity = bored.get_random_activity()
            bored.print_activity("Random", activity)


if __name__ == "__main__":
    main()

##### TESTING AREA #####
# bored = ImBored("Boredom Buster")
# bored.im_bored_cli()
# # print(bored.get_random_activity())
