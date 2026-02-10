
import urllib.request
import json
import printable

def fetch_url(url):
    try:
        headers = {
            "User-Agent": "Python-urllib/3.8"
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = response.read()
            json_data = json.loads(data)
            return json_data
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e.msg}")
        return None
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        return None

def get_user_details(username):
    url = f"https://api.github.com/users/{username}"
    return fetch_url(url)

def get_user_followers(username):
    url = f"https://api.github.com/users/{username}/followers"
    return fetch_url(url)

def get_user_following(username):
    url = f"https://api.github.com/users/{username}/following"
    return fetch_url(url)

def get_user_events(username):
    url = f"https://api.github.com/users/{username}/events"
    return fetch_url(url)

generic_input_message = "Press Enter to return to main menu..."

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    data = get_user_details(username)
    events = get_user_events(username)
    if data is None:
        print("Failed to fetch user details.")
        exit(1)
    states = ["main", "followers", "following", "events", "return", "exit"]
    state = "main"
    while state != "exit":
        if state == "main":
            printable.main(data, events)
            choice = input("choose an option: ")
            if choice == "1":
                state = "followers"
            elif choice == "2":
                state = "following"
            elif choice == "3":
                state = "events"
            elif choice == "4":
                state = "exit"
        elif state == "followers":
            followers = get_user_followers(username)
            printable.followers(followers, username)
            input(generic_input_message)
            state = "main"
        elif state == "following":
            following = get_user_following(username)
            printable.following(following, username)
            input(generic_input_message)
            state = "main"
        elif state == "events":
            printable.events(events, login=username)
            input(generic_input_message)
            state = "main"
        # print(json.dumps(data, indent=4))