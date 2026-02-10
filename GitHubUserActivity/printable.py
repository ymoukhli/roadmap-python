def main(data, events):
    if data is not None:
        print(f"User: {data.get('login', 'N/A')}")
        print("details: ")
        print(f"1 - followers: {data.get('followers', 'N/A')}")
        print(f"2 - following: {data.get('following', 'N/A')}")
        print(f"3 - events: {len(events) if events else 'N/A'}")
        print("4 - exit")

def followers(data, login):
    if data is not None:
        print(f"Followers of {login}:")
        for follower in data:
            print(f"- {follower.get('login', 'N/A')}")

def following(data, login):
    if data is not None:
        print(f"Following of {login}:")
        for follow in data:
            print(f"- {follow.get('login', 'N/A')}")

def events(data, login=None):
    if data is not None:
        print(f"Events of {login}:")
        for event in data:
            event_type = event.get('type', 'N/A')
            print(f"- {event_type} at {event.get('created_at', 'N/A')}")
            print(f"  - Repo: {event.get('repo', {}).get('name', 'N/A')}")
            if event_type == "PushEvent":
                print(f"  - Commits: {len(event.get('payload', {}).get('commits', []))}")
            elif event_type == "PullRequestEvent":
                print(f"  - Action: {event.get('payload', {}).get('action', 'N/A')}")
            elif event_type == "IssuesEvent":
                print(f"  - Action: {event.get('payload', {}).get('action', 'N/A')}")
            elif event_type == "IssueCommentEvent":
                print(f"  - Action: {event.get('payload', {}).get('action', 'N/A')}")
            elif event_type == "CreateEvent":
                print(f"  - Ref Type: {event.get('payload', {}).get('ref_type', 'N/A')}")
            elif event_type == "DeleteEvent":
                print(f"  - Ref Type: {event.get('payload', {}).get('ref_type', 'N/A')}")
            elif event_type == "ForkEvent":
                print(f"  - Forked to: {event.get('payload', {}).get('forkee', {}).get('full_name', 'N/A')}")
            elif event_type == "GollumEvent":
                print(f"  - Pages: {len(event.get('payload', {}).get('pages', []))}")
            elif event_type == "MemberEvent":
                print(f"  - Action: {event.get('payload', {}).get('action', 'N/A')}")
            elif event_type == "watchEvent":
                print(f"  - Action: {event.get('payload', {}).get('action', 'N/A')}")