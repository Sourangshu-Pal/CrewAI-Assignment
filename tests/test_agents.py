import unittest
from agents.researcher import Researcher
from agents.writer import Writer

class TestAgents(unittest.TestCase):
    def test_researcher_fetches_data(self):
        researcher = Researcher()
        topic = "AI in Healthcare"
        result = researcher.fetch_data(topic)
        self.assertTrue(len(result) > 0, "Researcher did not return data.")

    def test_writer_summarizes(self):
        writer = Writer()
        research_data = ["AI helps doctors", "AI improves diagnosis"]
        summary = writer.summarize(research_data)
        self.assertIn("AI", summary, "Writer summary is incorrect.")

if __name__ == "__main__":
    unittest.main()

    