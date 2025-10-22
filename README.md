# **Lesson 6: API Fundamentals \- Homework Assignment**

## **Objective: Build a Bored Activity CLI App**

Create a command-line menu application that helps users find activities when they're bored\!

This homework combines:

- **GET requests** with different parameters
- **CLI menu system** with user input
- **Error handling**
- **Working with query parameters**

---

## **Instructions**

1. **Create a Python file called homework.py**
2. **Build a CLI menu** that lets users choose different options
3. **Use the Bored API** to get activity suggestions
4. **Handle user input** and make appropriate API requests
5. **Test your menu system** thoroughly

---

## **API You'll Use**

- **Bored API**: <https://bored-api.appbrewery.com>

---

## **Your CLI Menu**

Create a menu system that looks like this:

```py
Bored Activity Finder
=====================
1. Get a random activity
2. Get activity by type
3. Get activity by participants
4. Save my favorite activities
5. View my saved activities
6. Exit

Choose an option (1-6):
```

---

## **Required Functions**

### **Function 1: Get Random Activity**

```py
def get_random_activity():
    """
    Get a completely random activity suggestion

    API: https://bored-api.appbrewery.com/random
    """
    # YOUR CODE HERE
    # 1. Make a GET request to the API
    # 2. Parse the JSON response
    # 3. Print the activity and type nicely
    # 4. Handle any errors
    pass
```

### **Function 2: Get Activity by Type**

```py
def get_activity_by_type():
    """
    Let user choose an activity type and get a suggestion

    API: https://bored-api.appbrewery.com/filter?type={type}

    Types: education, recreational, social, diy, charity, cooking, relaxation, music, busywork
    """
    # YOUR CODE HERE
    # 1. Show the user available types
    # 2. Get their choice
    # 3. Make API request with type parameter
    # 4. Display the result
    pass
```

### **Hint:** This one requires query parameters

### **Function 3: Get Activity by Participants**

```py
def get_activity_by_participants():
    """
    Get activity suggestions based on number of participants

    API: https://bored-api.appbrewery.com/filter?participants={number}
    """
    # YOUR CODE HERE
    # 1. Ask user how many participants
    # 2. Make API request with participants parameter
    # 3. Display the activity suggestion
    pass
```

### **Hint:** This one requires query parameters

###

```

```

## **Bonus**

### **Function 5: Save Favorite Activity**

```py
def save_favorite_activity():
    """
    Get an activity and save it to a text file
    """
    # YOUR CODE HERE
    # 1. after getting an activity from one of the other functions
    # 2. Ask user if they want to save it
    # 3. If yes, append to 'favorite_activities' list
         # 4. Print "Activity Saved"
    pass
```

### **Function 6: View Saved Activities**

```py
def view_saved_activities():
    """
    Read and display saved activities from file
    """
    # YOUR CODE HERE
    # Loop through the list of saved activities and display each one
    pass
```

---

## **Main Function & Menu System**

Create your main function with a loop that keeps showing the menu:

```py
import requests

def show_menu():
    """Display the main menu"""
    print("\nBored Activity Finder")
    print("=" * 21)
    print("1. Get a random activity")
    print("2. Get activity by type")
    print("3. Get activity by participants")
    print("4. Save my favorite activities")
    print("5. View my saved activities")
    print("6. Exit")

def main():
    """Main function with menu loop"""
    print("Welcome to the Bored Activity Finder!")

    while True:
        show_menu()

        try:
            choice = input("\nChoose an option (1-7): ")

            if choice == '1':
                get_random_activity()
            elif choice == '2':
                get_activity_by_type()
            elif choice == '3':
                get_activity_by_participants()
            elif choice == '4':
                get_quick_activity()
            elif choice == '5':
                save_favorite_activity()
            elif choice == '6':
                view_saved_activities()
            elif choice == '7':
                print("Thanks for using Bored Activity Finder!")
                break
            else:
                print("Invalid choice! Please choose 1-7.")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

if __name__ == "__main__":
    main()
```

---

## **Example Output**

Here's what your program should look like when running:

```py
Welcome to the Bored Activity Finder!

Bored Activity Finder
=====================
1. Get a random activity
2. Get activity by type
3. Get activity by participants
4. Save my favorite activities
5. View my saved activities
6. Exit

Choose an option (1-6): 1

Random Activity Suggestion:
Activity: Learn to play a musical instrument
Type: Music
Participants: 1
Ready to try it?
```

---

## **Hints for Success**

### **API Response Format**

The Bored API returns JSON like this:

```py
{
  "activity": "Learn to play a musical instrument",
  "type": "music",
  "participants": 1,
  "price": 0.1,
  "link": "",
  "key": "4526284",
  "accessibility": "Few to no challenges"
}
```

---

### **Test Your Program**

Make sure to test:

- All menu options work
- Invalid menu choices are handled
- API errors are handled gracefully
- File saving and reading works
- User can exit cleanly
