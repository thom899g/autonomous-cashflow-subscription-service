import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class PaymentProcessor:
    def __init__(self):
        self.transaction_id_counter = 0
        self.failed_transactions = {}  # Stores failed transaction details for retry

    def charge_card(self, payment_info: Dict[str, str]) -> str:
        """Attempts to charge a credit card."""
        try:
            self.transaction_id_counter += 1
            transaction_id = f"TX-{self.transaction_id_counter}"
            
            # Simulated success; in real system, integrate with payment gateway
            if not self._validate_card(payment_info):
                raise ValueError("Invalid card details.")
            
            logger.info(f"Charge successful for transaction {transaction_id}.")
            return transaction_id
        except Exception as e:
            logger.error(f"Payment failed: {str(e)}")
            self.failed_transactions[transaction_id] = payment_info
            raise

    def retry_failed_transaction(self, transaction_id: str) -> Optional[str]:
        """Retries a previously failed transaction."""
        try:
            if transaction_id not in self.failed_transactions:
                logger.warning("No such failed transaction.")
                return None
            # Simulate retry logic; re-attempt the charge
            payment_info = self.failed_transactions[transaction_id]
            success = self.charge_card(payment_info)
            del self.failed_transactions[transaction_id]
            logger.info(f"Transaction {transaction_id} retried successfully.")
            return transaction_id if success else None
        except Exception as e:
            logger.error(f"Retry failed for {transaction_id}: {str(e)}")
            raise

    def _validate_card(self, payment_info: Dict[str, str]) -> bool:
        """Validates credit card details."""
        # Simplified validation; enhance with