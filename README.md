# store-hours-checker-skill

> **GenPark AI Agent Skill** -- Shop open/closed schedule validator.

## Quick Start

```python
from client import StoreHoursCheckerClient
client = StoreHoursCheckerClient()
res = client.verify_status(12)
print(res["is_open"])
```
