import pandas as pd


def load_github():

    return pd.read_csv(
        "output/github_repositories.csv"
    )


def load_jobs():

    return pd.read_csv(
        "output/jsearch_jobs.csv"
    )


def load_global_jobs():

    return pd.read_csv(
        "output/global_ai_jobs.csv"
    )


def load_models():

    return pd.read_csv(
        "output/huggingface_models.csv"
    )


def load_skills():

    return pd.read_csv(
        "output/ai_skills_report.csv"
    )
