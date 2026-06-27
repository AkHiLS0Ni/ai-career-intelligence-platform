import json
from service import fetch_huggingface_data


def save_raw_data(data):
    """
    Save raw Hugging Face API response to a JSON file.
    """

    with open("data/raw/huggingface/huggingface_api.json", "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Raw data saved successfully!")


def extract_model_data(data):
    """
    Extract only the required model fields.
    """

    clean_data = []

    for model in data:

        model_data = {
            "model_name": model.get("id"),
            "author": model.get("author"),
            "downloads": model.get("downloads"),
            "likes": model.get("likes"),
            "task": model.get("pipeline_tag"),
            "last_modified": model.get("lastModified")
        }

        clean_data.append(model_data)

    return clean_data


def save_processed_data(clean_data):
    """
    Save cleaned model data to a JSON file.
    """

    with open("data/processed/huggingface/models.json", "w") as file:
        json.dump(clean_data, file, indent=4)

    print("✅ Processed data saved successfully!")


def main():
    """
    Main entry point of the Hugging Face ingestion pipeline.
    """

    data = fetch_huggingface_data()

    if data is None:
        return

    # Save raw API response
    save_raw_data(data)

    # Transform raw data
    clean_data = extract_model_data(data)

    # Save processed data
    save_processed_data(clean_data)

    # Display processed models
    print("\n🤗 Top Hugging Face Models")
    print("=" * 80)

    for model in clean_data:
        print(f"{model['model_name']} ({model['downloads']} downloads)")


if __name__ == "__main__":
    main()
