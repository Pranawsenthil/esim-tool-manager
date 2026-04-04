from checker import check_tool, show_tools,check_version
from installer import install_tool
from checker import check_tool

while True:
    print("\n===== eSim Tool Manager =====")
    print("1. Install Tool")
    print("2. Check Tool")
    print("3. Check All Tools")
    print("4. Exit")
    print("5. Show Supported Tools")
    print("6.Check Tool Version")

    choice = input("Enter your choice: ")

    if choice == "1":
        tool = input("Enter tool name: ")
        install_tool(tool)

    elif choice == "2":
        tool = input("Enter tool name: ")
        check_tool(tool)

    elif choice == "3":
        check_tool()

    elif choice == "4":
        print("Exiting...")
        break
    elif choice =="5":
        show_tools()
        break
    elif choice =="6":
        tool =input("Enter Tool name:")
        check_version(tool)
        break
    else:
        print("Invalid choice!")
