import unittest
from tasks.research_task import perform_research
from tasks.writer_task import generate_summary

class TestTasks(unittest.TestCase):
    def test_perform_research(self):
        topic = "AI in Healthcare"
        research_data = perform_research(topic)
        self.assertTrue(len(research_data) > 0, "Research task did not return any data.")

    def test_generate_summary(self):
        research_data = ["AI helps doctors", "AI improves diagnosis"]
        summary = generate_summary(research_data)
        self.assertIn("AI", summary, "Summary task is incorrect.")

if __name__ == "__main__":
    unittest.main()