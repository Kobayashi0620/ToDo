greeting = "ToDoを入力してください:"
findWord = "完了したToDoを入力してください:"
choiceWord = "機能を選択してください（1:ToDo追加 2:ToDo削除）:"
inputToDo =""
findToDo = ""
choice = ""
ToDo_list = []
finish_list = []

choice = input(choiceWord)

if choice == "1":
    while inputToDo != "finish":
        inputToDo = input(greeting)
        ToDo_list.append(inputToDo)
    else:
        for i in ToDo_list[: -1]:
            print(i)
        print("入力受付を終了しました")

    with open('ToDo/ToDo.txt', 'a') as f:
        for d in ToDo_list[: -1]:
            f.write("%s\n" % d)

elif choice == "2":
    while findToDo != "finish":
        findToDo = input(findWord)
        finish_list.append(findToDo)
    else:
        with open('ToDo/ToDo.txt', 'r') as f:
            ToDo_list = f.read().split("\n")

        for i in finish_list[: -1]:
            ToDo_list.remove(i)
        print("お疲れさまでした")

        for i in ToDo_list:
            print(i)

    with open('ToDo/ToDo.txt', 'w') as f:
        for d in ToDo_list[: -1]:
            f.write("%s\n" % d)

else:
    print("入力に誤りがあります")