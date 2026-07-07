"""
example_usage.py -- Demonstrates StoreHoursCheckerClient
"""
from client import StoreHoursCheckerClient

def main():
    client = StoreHoursCheckerClient()
    result = client.verify_status(current_hour=22, open_hour=9, close_hour=21)
    print("[Store Status Result]")
    print(f"Is Open: {result['is_open']}")
    print(f"Hours until Open: {result['next_change_hours']}")

if __name__ == "__main__":
    main()
