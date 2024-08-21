# **Evalution Test**

**Problem Set 1 - Regex**

1. Write a regex to extract all the numbers with orange color background from the below text in italics (Output should be a list).

   **{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}**

Solution:

```
import re

errorMessage = """{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}"""

numbers = [ int(re.findall(r'\d+',num)[0]) for num in re.findall(r'{"id":\d+}', errorMessage)]
print(numbers)
```

Output:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 648, 649, 650, 651, 652, 653]

**Problem Set 3**

**A.** Write and share a small note about your choice of system to schedule periodic tasks (such as downloading a list of ISINs every 24 hours). Why did you choose it? Is it reliable enough; Or will it scale? If not, what are the problems with it? And, what else would you recommend to fix this problem at scale in production?

**Answer :**

For scheduling periodic tasks like downloading a list of ISINs every 24 hours, I chose **Celery with Celery Beat** because it's easy to integrate with Django, scales well, and is reliable. However, it can become complex to manage at scale and may be resource-intensive.

If more scalability or complex task orchestration is needed, I recommend considering **Apache Airflow** for advanced workflows or
**Kubernetes Cron Jobs** for containerized environments. For serverless setups, **AWS Lambda with EventBridge** is a cost-effective alternative.

**B.** In what circumstances would you use Flask instead of Django and vice versa?

**Answer :**

The choice ultimately depends on our project’s specific needs, development timeline, and the level of control or structure we prefer.
Use Flask for smaller, more flexible applications where you want to hand-pick our components and have full control over the stack.
Use Django for larger, feature-rich applications where built-in tools and rapid development are priorities.

### Prerequisites

Ensure you have the following installed on your system:

- Python
- Django
- Tailwind CSS
- NPM
- Node JS

### To Run The Tailwind CSS

    npm run tailwind

### To Run The Django

    python manage.py runserver
