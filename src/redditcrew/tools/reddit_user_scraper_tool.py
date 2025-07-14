import os
import re
import json
from typing import Type, Optional
from pydantic import BaseModel, Field, ValidationError
import praw
from datetime import datetime, timedelta

from crewai.tools import BaseTool


class RedditUserScrapeInput(BaseModel):
    """Input schema for RedditUserScraperTool."""

    user_identifier: str = Field(
        ...,
        description=(
            "The Reddit username or full user profile URL (e.g., 'https://www.reddit.com/user/kojied/')"
            "to scrape. If a URL is provided, the username will be extracted."
        ),
    )
    timeframe_months: int = Field(
        6,
        description="Number of months back from the current date to scrape data. Default is 6 months.",
    )
    max_items_per_category: Optional[int] = Field(
        200,
        description="Maximum number of posts/comments to fetch for the given timeframe. Set to None for no limit (can be slow).",
    )


class RedditUserScraperTool(BaseTool):
    name: str = "Reddit User Scraper"
    description: str = (
        "A tool to scrape a Reddit user's profile, including their bio, recent posts, and recent comments "
        "within a specified timeframe. It accepts either a Reddit username or a full user profile URL."
        "Returns a JSON string containing the user's karma, creation date, bio (if available), posts, and comments."
    )
    args_schema: Type[BaseModel] = RedditUserScrapeInput

    def _get_reddit_instance(self):
        """Initializes and returns a PRAW Reddit instance."""
        client_id = os.getenv("REDDIT_CLIENT_ID")
        client_secret = os.getenv("REDDIT_CLIENT_SECRET")
        user_agent = os.getenv("REDDIT_USER_AGENT")

        if not all([client_id, client_secret, user_agent]):
            raise ValueError(
                "Reddit API credentials (client ID, client secret, user agent) "
                "not found in environment variables. Please set REDDIT_CLIENT_ID, "
                "REDDIT_CLIENT_SECRET, and REDDIT_USER_AGENT."
            )

        reddit = praw.Reddit(
            client_id=client_id, client_secret=client_secret, user_agent=user_agent
        )
        return reddit

    def _extract_username_from_url(self, user_identifier: str) -> str:
        """Extracts username from a Reddit user profile URL."""
        match = re.search(r"reddit\.com/user/([^/]+)", user_identifier)
        if match:
            return match.group(1)
        return user_identifier  # Return as is if no URL pattern found, assume it's already a username

    def _run(
        self,
        user_identifier: str,
        timeframe_months: int = 6,
        max_items_per_category: Optional[int] = 200,
    ) -> str:
        try:
            username = self._extract_username_from_url(user_identifier)
            reddit = self._get_reddit_instance()
            user = reddit.redditor(username)

            user_data = {
                "username": username,
                "karma": {
                    "comment": user.comment_karma,
                    "link": user.link_karma,
                    "total": user.total_karma,
                },
                "created_utc": datetime.fromtimestamp(user.created_utc).isoformat(),
                "bio": user.subreddit["public_description"]
                if hasattr(user, "subreddit") and user.subreddit
                else "No public bio found.",
                "posts": [],
                "comments": [],
                "scraped_at": datetime.now().isoformat(),
            }

            cutoff_date = datetime.now() - timedelta(days=timeframe_months * 30)

            print(
                f"Scraping posts for user: {username} within last {timeframe_months} months..."
            )
            posts_count = 0
            for submission in user.submissions.new(limit=max_items_per_category):
                post_date = datetime.fromtimestamp(submission.created_utc)
                if post_date < cutoff_date:
                    break
                user_data["posts"].append(
                    {
                        "id": submission.id,
                        "title": submission.title,
                        "url": submission.url,
                        "score": submission.score,
                        "num_comments": submission.num_comments,
                        "subreddit": submission.subreddit.display_name,
                        "created_utc": post_date.isoformat(),
                        "selftext": submission.selftext
                        if submission.is_self
                        else None,  # Text content of self-posts
                        "is_self": submission.is_self,
                        "is_video": submission.is_video,
                        "link_flair_text": submission.link_flair_text,
                        "over_18": submission.over_18,
                    }
                )
                posts_count += 1
                if max_items_per_category and posts_count >= max_items_per_category:
                    break  # Stop if max items reached

            print(f"Scraped {posts_count} posts for {username}.")

            print(
                f"Scraping comments for user: {username} within last {timeframe_months} months..."
            )
            comments_count = 0
            for comment in user.comments.new(limit=max_items_per_category):
                comment_date = datetime.fromtimestamp(comment.created_utc)
                if comment_date < cutoff_date:
                    break
                user_data["comments"].append(
                    {
                        "id": comment.id,
                        "body": comment.body,
                        "score": comment.score,
                        "subreddit": comment.subreddit.display_name,
                        "created_utc": comment_date.isoformat(),
                        "link_to_post": f"https://www.reddit.com{comment.permalink.split('?')[0]}",
                        "link_id": comment.link_id,  # ID of the submission the comment is on
                        "parent_id": comment.parent_id,  # ID of the parent (post or comment)
                    }
                )
                comments_count += 1
                if max_items_per_category and comments_count >= max_items_per_category:
                    break  # Stop if max items reached

            print(f"Scraped {comments_count} comments for {username}.")

            return json.dumps(user_data, indent=2, ensure_ascii=False)

        except ValidationError as e:
            return f"Validation error for input: {e}"
        except Exception as e:
            return f"An error occurred during Reddit scraping: {e}"
