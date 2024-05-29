class Task:
    """
    Represents a single task with a title, description, and completion status.
    """

    def __init__(self, title, description):
        """
        Initializes a new Task with the given title and description.
        Sets the task as not completed by default.

        :param title: The title of the task
        :param description: The description of the task
        """
        self.title = title
        self.description = description
        self.completed = False

    def getTitle(self):
        """
        Returns the title of the task.

        :return: The title of the task
        """
        return self.title

    def getDescription(self):
        """
        Returns the description of the task.

        :return: The description of the task
        """
        return self.description

    def isCompleted(self):
        """
        Checks if the task is completed.

        :return: True if the task is completed, False otherwise
        """
        return self.completed

    def markCompleted(self):
        """
        Marks the task as completed.
        """
        self.completed = True


class Node:
    """
    Represents a node in a singly linked list, holding a task and a reference to the next node.
    """

    def __init__(self, task):
        """
        Initializes a new Node with the given task and sets the next node to None.

        :param task: The task to be stored in the node
        """
        self.task = task
        self.next = None


class TodoList:
    """
    Represents a to-do list implemented as a singly linked list.
    """

    def __init__(self):
        """
        Initializes an empty to-do list.
        """
        self.head = None

    def addToDo(self, task):
        """
        Adds a new task to the end of the to-do list.

        :param task: The task to be added
        """
        new_node = Node(task)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def markToDoAsCompleted(self, title):
        """
        Marks the task with the given title as completed.

        :param title: The title of the task to mark as completed
        """
        current = self.head
        while current:
            if current.task.getTitle() == title:
                current.task.markCompleted()
                return
            current = current.next
        print("Task not found")

    def viewToDoList(self):
        """
        Prints the to-do list, showing the title, description, and status of each task.
        """
        current = self.head
        while current:
            task = current.task
            status = "Completed" if task.isCompleted() else "Not Completed"
            print(f"Title: {task.getTitle()}, Description: {task.getDescription()}, Status: {status}")
            current = current.next


def main():
    """
    Main function to demonstrate the functionality of the to-do list.
    """
    # Create a to-do list
    todo_list = TodoList()

    # Create some tasks
    task1 = Task("Buy sweets", "Buy chocolate, candy, and cake")
    task2 = Task("Read Quran", "Read 'Chapter 7: The Elevated Places'")
    task3 = Task("Go for a run", "Run 2 kilometers in the morning")

    # Add tasks to the to-do list
    todo_list.addToDo(task1)
    todo_list.addToDo(task2)
    todo_list.addToDo(task3)

    # View the initial to-do list
    print("To-Do List:")
    todo_list.viewToDoList()

    # Mark a task as completed
    todo_list.markToDoAsCompleted("Read Quran")

    # View the to-do list after marking a task as completed
    print("\nTo-Do List after marking 'Read Quran' as completed:")
    todo_list.viewToDoList()


if __name__ == "__main__":
    main()






