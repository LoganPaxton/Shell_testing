#!/bin/bash

# File to store the to-do list
TODO_FILE="todo.txt"

# Check if the to-do file exists, and create it if not
if [ ! -f "$TODO_FILE" ]; then
    touch "$TODO_FILE"
fi

# Add a task to the to-do list
add_task() {
    echo "$1" >> "$TODO_FILE"
    echo "Task added: $1"
}

# View the to-do list
view_tasks() {
    if [ -s "$TODO_FILE" ]; then
        cat -n "$TODO_FILE"
    else
        echo "No tasks found."
    fi
}

# Delete a task from the to-do list
delete_task() {
    if [ -s "$TODO_FILE" ]; then
        if [ "$1" -gt 0 ] 2>/dev/null; then
            sed -i "${1}d" "$TODO_FILE"
            echo "Task deleted: $1"
        else
            echo "Invalid task number."
        fi
    else
        echo "No tasks found."
    fi
}

# Process user commands
case "$1" in
    add)
        shift
        add_task "$@"
        ;;
    view)
        view_tasks
        ;;
    delete)
        shift
        delete_task "$@"
        ;;
    *)
        echo "Usage: ./todo.sh [add|view|delete]"
        ;;
esac
