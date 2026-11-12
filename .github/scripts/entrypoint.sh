#!/bin/bash

# echo "Starting Frequency Analyzer..."
echo "-----------------------"
echo "Ececuting todo.py"
echo "-----------------------"
python3 /app/.github/scripts/todo.py | tee /app/todo_output.txt

echo "-----------------------"
echo "Ececuting todo-test.py"
echo "-----------------------"
python3 /app/.github/scripts/todo.py | tee /app/test_output.txt

echo "-----------------------"
echo "Ececuting update_index.sh"
echo "-----------------------"
bash /app/.github/scripts/update_index.sh /app/todo_output.txt /app/test_output.txt

echo "-----------------------"
echo "Done!"
echo "-----------------------"
