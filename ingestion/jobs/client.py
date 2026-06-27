import json

from service import fetch_jobs_data


def save_raw_data(data):
    """
    Save raw Jobs API response to a JSON file.
    """

    with open("data/raw/jobs/jobs_api.json", "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Raw jobs data saved successfully!")


def extract_job_data(data):
    """
    Extract only the required job fields.
    """

    clean_data = []

    # Skip the first metadata object
    for job in data[1:]:

        job_data = {
            "job_id": job.get("id"),
            "job_title": job.get("position"),
            "company": job.get("company"),
            "location": job.get("location"),
            "skills": job.get("tags"),
            "job_url": job.get("url"),
            "posted_date": job.get("date")
        }

        clean_data.append(job_data)

    return clean_data


def save_processed_data(clean_data):
    """
    Save cleaned job data to a JSON file.
    """

    with open("data/processed/jobs/jobs.json", "w") as file:
        json.dump(clean_data, file, indent=4)

    print("✅ Processed jobs data saved successfully!")


def main():
    """
    Main entry point of the Jobs ingestion pipeline.
    """

    data = fetch_jobs_data()

    if data is None:
        return

    # Save raw API response
    save_raw_data(data)

    # Transform raw data
    clean_data = extract_job_data(data)

    # Save processed data
    save_processed_data(clean_data)

    # Display processed jobs
    print("\n💼 Latest AI Jobs")
    print("=" * 80)

    for job in clean_data[:10]:
        print(f"{job['job_title']} | {job['company']}")


if __name__ == "__main__":
    main()
