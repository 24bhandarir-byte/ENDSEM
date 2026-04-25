from agents.researcher import impact_researcher
from agents.extractor import data_extractor
from agents.writer import brief_writer

def run_pipeline(topic):
    print("🔍 Researching...")
    research = impact_researcher(topic)

    print("📊 Extracting data...")
    extracted = data_extractor(research)

    print("📝 Writing brief...")
    report = brief_writer(extracted, topic)

    return report


if __name__ == "__main__":
    topic = input("Enter topic: ")
    result = run_pipeline(topic)

    print("\n=== FINAL REPORT ===\n")
    print(result)