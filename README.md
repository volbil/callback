You can run this example using this command:

```
gunicorn app:app --worker-class eventlet -w 1 --bind 0.0.0.0:4321 --reload
```