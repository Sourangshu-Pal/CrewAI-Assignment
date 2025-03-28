from agents.writer import Writer

def generate_summary(research_data):
    writer = Writer()
    return writer.summarize(research_data)