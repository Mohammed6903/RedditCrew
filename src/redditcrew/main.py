#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from redditcrew.crew import Redditcrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {
        "user_profile_url": "https://www.reddit.com/user/Hungry-Move-6603",
        "data_timeframe": "1 year",
        "current_date": str(datetime.now().strftime("%Y-%m-%d")),
        "output_filename": "user_persona_hungry_move.txt",
        "min_posts_required": 10,
        "confidence_threshold": 0.7,
        "citation_format": "APA",
    }

    try:
        Redditcrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "user_profile_url": "https://www.reddit.com/user/Hungry-Move-6603",
        "data_timeframe": "6 monts",
        "current_date": str(datetime.now().strftime("%Y-%m-%d")),
        "output_filename": "user_persona_hungry_move.txt",
        "min_posts_required": 5,
        "confidence_threshold": 0.7,
        "citation_format": "APA",
    }
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
    inputs = {
        "user_profile_url": "https://www.reddit.com/user/Hungry-Move-6603",
        "data_timeframe": "6 monts",
        "current_date": str(datetime.now().strftime("%Y-%m-%d")),
        "output_filename": "user_persona_hungry_move.txt",
        "min_posts_required": 5,
        "confidence_threshold": 0.7,
        "citation_format": "APA",
    }

    try:
        Redditcrew().crew().test(
            n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
