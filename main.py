import json
from scripts.evaluate_noise_robustness import evaluate_noise_robustness
from scripts.download_files import download_file, get_file_list

def load_config(config_file="config.json"):
    """Load configuration from the config file."""
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"Error loading config: {e}")
        return {}

def main():
    # Load configuration
    config = load_config()

    print(f"Model: {config["model_name"]}")
    print(f"Noise Rate: {config["noise_rate"]}")
    print(f"Passage Number: {config["passage_num"]}")
    print(f"Number of Queries: {config["num_queries"]}")

    # Download files from the GitHub repository
    files = get_file_list()
    for file in files:
        download_file(file)

    # Load dataset from the local JSON file
    DATA_FILE = "data/en.json"
    dataset = []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            dataset.append(json.loads(line.strip()))  # Load each JSON object per line

    print(f"Loaded {len(dataset)} entries")  # Check how many records were loaded

    # Call evaluate_noise_robustness for each noise rate and model
    evaluate_noise_robustness(dataset, config)


if __name__ == "__main__":
    main()
