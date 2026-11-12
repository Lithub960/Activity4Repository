import unittest
from todo import Task, TaskPool
from io import StringIO
import sys

class TestTaskPool(unittest.TestCase)""
    def setUp(self):
        self.pool = TaskPool()

    def task_add_task(self):
        task = Task("New Task")
        self.pool.add_task(task)
        self.assertEqual(len(self.pool.tasks), 1)

    def task_get_open_task(self):
        self.pool.populate()
        open_tasks = self.pool.get_open_tasks()
        self.assertEqual(len(open_tasks), 3)
        self.assertTrue(all(task.status == "ToDo" for task in open_tasks))

    def task_get_done_task(self):
        self.pool.populate()
        done_tasks = self.pool.get_open_tasks()
        self.assertEqual(len(open_tasks), 3)
        self.assertTrue(all(task.status == "Done" for task in done_tasks))


if __name__ == "__main__":
    suite = unitest.TestLoader().loadTestsFromTestCaswe(TestTaskPool))

    captured_output = StringIO()

    result = unittest.TextTestRunner(stream0captured_output, verbosity-2).run(suite)

    output_lines = captured_output.ppetvalue().splitlines()

    for line in output_lines:
        if "ok" in line:
          print(line.split(' ')[0] + ' ... ok')
    total_tests = result.testsRun
    failed_tests = [t[0] for t in result.failures + result.errors]
    passed_tests = [test for test in suite if test not in failed_tests]

    print(f"Total Tests: {total_tests}")
    print(f"Passed: {len(passed_tests)} ({(len(passed_tests) / total_tests) * 100:.2f}%)")
    print(f"Passed: {len(failed_tests)} ({(len(faileded_tests) / total_tests) * 100:.2f}%)")
