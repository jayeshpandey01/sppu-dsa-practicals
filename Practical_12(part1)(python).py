'''
Write a python program to store names and mobile numbers of your friends in sorted 
order on names. Search your friend from list using binary search (recursive and nonrecursive). Insert friend if not present in phonebook
'''

class Friend:
    def __init__(self, name, mobile_number):
        self.name = name
        self.mobile_number = mobile_number

def binary_search_recursive(friends, name, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    if friends[mid].name == name:
        return friends[mid]
    elif friends[mid].name > name:
        return binary_search_recursive(friends, name, low, mid - 1)
    else:
        return binary_search_recursive(friends, name, mid + 1, high)

def binary_search_non_recursive(friends, name):
    low = 0
    high = len(friends) - 1

    while low <= high:
        mid = (low + high) // 2
        if friends[mid].name == name:
            return friends[mid]
        elif friends[mid].name > name:
            high = mid - 1
        else:
            low = mid + 1

    return None

def insert_friend(friends, name, mobile_number):
    friend = binary_search_non_recursive(friends, name)

    if friend is None:
        new_friend = Friend(name, mobile_number)
        friends.append(new_friend)
        friends.sort(key=lambda x: x.name)

def main():
    friends = [Friend("Alice", "1234567890"),
               Friend("Bob", "0987654321"),
               Friend("Charlie", "9876543210"),
               Friend("David", "5432167890")]

    # Sorting friends list based on names
    friends.sort(key=lambda x: x.name)

    print("Friends List:")
    for friend in friends:
        print(f"{friend.name}: {friend.mobile_number}")

    # Searching friends using binary search recursive
    search_name = "Bob"
    friend_recursive = binary_search_recursive(friends, search_name, 0, len(friends)-1)
    if friend_recursive is not None:
        print(f"\nFriend found (recursive): {friend_recursive.name}, {friend_recursive.mobile_number}")
    else:
        print(f"\nFriend not found (recursive)")

    # Searching friends using binary search non-recursive
    search_name = "Charlie"
    friend_non_recursive = binary_search_non_recursive(friends, search_name)
    if friend_non_recursive is not None:
        print(f"\nFriend found (non-recursive): {friend_non_recursive.name}, {friend_non_recursive.mobile_number}")
    else:
        print(f"\nFriend not found (non-recursive)")

    # Inserting a friend if not present in phonebook
    insert_friend(friends, "Eve", "9876543210")
    insert_friend(friends, "Bob", "5555555555")

    print("\nUpdated Friends List:")
    for friend in friends:
        print(f"{friend.name}: {friend.mobile_number}")

if __name__ == "__main__":
    main()
