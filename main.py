from tasks.research_task import perform_research
from tasks.writing_task import generate_summary

def main():
    topic = "Impact of AI in Healthcare"
    research_data = perform_research(topic)
    summary = generate_summary(research_data)
    print("Final Summary:", summary)

if __name__ == "__main__":
    main()