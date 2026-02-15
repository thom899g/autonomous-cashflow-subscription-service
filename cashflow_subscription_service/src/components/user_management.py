from datetime import datetime
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

class UserManagement:
    def __init__(self):
        self.users = {}  # Simulated storage; replace with DB in production

    def create_user(self, user_id: str, email: str, password_hash: str) -> bool:
        """Creates a new user account."""
        try:
            if user_id in self.users:
                logger.warning(f"User {user_id} already exists.")
                return False
            self.users[user_id] = {
                "email": email,
                "password_hash": password_hash,
                "subscription_status": "active",
                "created_at": datetime.now().isoformat()
            }
            logger.info(f"User {user_id} created successfully.")
            return True
        except Exception as e:
            logger.error(f"Error creating user {user_id}: {str(e)}")
            raise

    def update_subscription(self, user_id: str, new_plan: str) -> bool:
        """Updates the subscription plan for a user."""
        try:
            if user_id not in self.users:
                logger.warning(f"No such user {user_id}.")
                return False
            self.users[user_id]["subscription_status"] = "active"
            self.users[user_id]["plan"] = new_plan
            logger.info(f"Subscription updated to {new_plan} for user {user_id}.")
            return True
        except Exception as e:
            logger.error(f"Error updating subscription for {user_id}: {str(e)}")
            raise

    def authenticate(self, user_id: str, password_hash: str) -> bool:
        """Authenticates a user."""
        try:
            if not self.users.get(user_id):
                return False
            return self.users[user_id]["password_hash"] == password_hash
        except Exception as e:
            logger.error(f"Authentication error for {user_id}: {str(e)}")
            raise