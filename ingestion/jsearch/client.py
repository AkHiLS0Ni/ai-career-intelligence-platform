import json

from service import fetch_jobs_data


def save_raw_data(data):
    """
    Save raw JSearch API response.
    """

    with open("data/raw/jsearch/jobs_api.json", "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Raw jobs data saved successfully!")


def extract_job_data(data):
    """
    Extract required fields from the JSearch API response.
    """

    clean_data = []

    # JSearch stores all jobs inside data["data"]["jobs"]
    jobs = data["data"]["jobs"]

    for job in jobs:

        job_data = {
            "job_id": job.get("job_id"),
            "job_title": job.get("job_title"),
            "company": job.get("employer_name"),
            "location": job.get("job_location"),
            "city": job.get("job_city"),
            "state": job.get("job_state"),
            "country": job.get("job_country"),
            "employment_type": job.get("job_employment_type"),
            "salary_min": job.get("job_min_salary"),
            "salary_max": job.get("job_max_salary"),
            "salary_period": job.get("job_salary_period"),
            "remote": job.get("job_is_remote"),
            "posted_at": job.get("job_posted_at_datetime_utc"),
            "apply_link": job.get("job_apply_link"),
            "description": job.get("job_description"),
        }

        clean_data.append(job_data)

    return clean_data


def save_processed_data(clean_data):
    """
    Save cleaned jobs data.
    """

    with open("data/processed/jsearch/jobs.json", "w") as file:
        json.dump(clean_data, file, indent=4)

    print("✅ Processed jobs data saved successfully!")


def main():
    """
    Main entry point of the JSearch pipeline.
    """

    data = fetch_jobs_data()

    if data is None:
        return

    # Save raw response
    save_raw_data(data)

    # Extract useful fields
    clean_data = extract_job_data(data)

    # Save processed data
    save_processed_data(clean_data)

    # Display first 10 jobs
    print("\n💼 AI Jobs")
    print("=" * 80)

    for job in clean_data[:10]:
        print(f"{job['job_title']} | {job['company']}")


if __name__ == "__main__":
    main()
