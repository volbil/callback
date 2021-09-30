You can run this example using this command:

```
gunicorn app:app --worker-class eventlet -w 1 --bind 0.0.0.0:9000 --reload
```

Systemd example:

```
[Unit]
Description=Gunicorn instance to serve callback example
After=network.target

[Service]
User=mman
Group=www-data
WorkingDirectory=/home/mman/callback
Environment="PATH=/home/mman/callback/venv/bin"
ExecStart=/home/mman/callback/venv/bin/gunicorn app:app --worker-class eventlet -w 1 --bind 0.0.0.0:9000 --reload

[Install]
WantedBy=multi-user.target
```

Nginx example:

```
server {
    server_name callback.codepillow.io;
    listen 80;

    location / {
        proxy_pass http://localhost:9000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    location /socket.io {
        include proxy_params;
        proxy_http_version 1.1;
        proxy_buffering off;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_pass http://localhost:9000/socket.io;
    }
}

```