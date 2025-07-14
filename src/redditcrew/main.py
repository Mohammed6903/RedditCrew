#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from redditcrew.crew import Redditcrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

USER_ID = "kojied"

DEFAULT_CONFIG = {
    "user_profile_url": "https://www.reddit.com/user/" + USER_ID,
    "data_timeframe": "1 year",
    "output_filename": f"user_persona_{USER_ID}.txt",
    "min_posts_required": 10,
    "confidence_threshold": 0.7,
    "citation_format": "APA",
    "current_date": datetime.now().strftime("%Y-%m-%d"),
}


def run():
    """
    Run the crew.
    """
    inputs = DEFAULT_CONFIG

    try:
        Redditcrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = DEFAULT_CONFIG

    try:
        Redditcrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Redditcrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = DEFAULT_CONFIG
    try:
        Redditcrew().crew().test(
            n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
