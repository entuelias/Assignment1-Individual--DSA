class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description
    def isCompleted(self):
        return self.completed

    def markCompleted(self):
        self.completed = True

class Node:
    def __init__(self,task):
        self.task = task
        self.next = None

class TodoList:
    def __init__(self):
        self.head = None

    def addToDo(self,task):
        new_node = Node(task)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def markToDoAsCompleted(self,title):
        current = self.head
        while current:
           if current.task.getTitle() == title:
               current.task.markCompleted()
               return
           current = current.next
        print("Task not found")

    def viewToDoList(self):
        current = self.head
        while current:
            task = current.task
            status = "Completed" if task.isCompleted() else "Not Completed"
            print(f"Title: {task.getTitle()}, Description: {task.getDescription()} ,Status: {status}")
            current = current.next

def main():
    todo_list = TodoList()


    task1 = Task("Buy sweets", "Buy chocolate, candy, and cake")
    task2 = Task("Read Quran", "Read 'Chapter 7: The Elevated Places '")
    task3 = Task("Go for a run", "Run 2 kilometers in the morning")


    todo_list.addToDo(task1)
    todo_list.addToDo(task2)
    todo_list.addToDo(task3)


    print("To-Do List:")
    todo_list.viewToDoList()


    todo_list.markToDoAsCompleted("Read Quran")


    print("\nTo-Do List after marking 'Read Quran' as completed:")
    todo_list.viewToDoList()

if __name__ == "__main__":
    main()








