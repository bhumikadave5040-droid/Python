import datetime
status = {}

# Upload Status
def status_upload():
    user = input("Enter username: ")
    msg = input("Enter message: ")

    status[user] = {
        "message": msg,
        "time": datetime.datetime.now(),
        "views": 0
    }

    print("Status Uploaded ")

#expire status after 24 hours
def expire_status():
     current_time = datetime.datetime.now()
     delete = []

for user in status:
     current_time= datetime.datetime.now()
     delete=[]
     for user in status:
          diff = current_time - status[user]["time"]
          if diff>= datetime.timedelta(hours=24):
               delete.append(user)
               for user in delete:
                    status.pop(user)
                    print(f"Status of {user} has expired and deleted")
        
#view status
def view_status():
     expire_status()
     if len(status) == 0:
         print("No status available")
         return
     print("Available status:")
     user = input("Enter username to view status: ")
     if user in status:
         print(f"Status of {user}: {status[user]['message']}\nViews: {status[user]['views']}")
         status[user]["views"] += 1
     else:
         print("User not found")
#view analytics
def view_analytics():
        expire_status()
        if len(status) == 0:
            print("No status available")
            return
        print("Available status:")
        for user in status:
            print(f"Status of {user}: {status[user]['message']}\nUploaded at: {status[user]['time']}\nViews: {status[user]['views']}")

while True:
        print("\n1.Status Upload\n2. View Status\n3. View Analytics\n4. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                status_upload()
            case "2":
                view_status()
            case "3":
                view_analytics()
            case "4":
                print("Thank you")
                break
            case _:
                print("invalid choice")



