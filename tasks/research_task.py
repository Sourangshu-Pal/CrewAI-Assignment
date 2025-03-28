from agents.researcher import Researcher

def perform_research(topic):
    researcher = Researcher()
    return researcher.fetch_data(topic)