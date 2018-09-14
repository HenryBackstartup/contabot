#!/bin/bash
python manage.py migrate        # Apply database migrations
python manage.py collectstatic --clear --noinput # clearstatic files
python manage.py collectstatic --noinput  # collect static files
# Prepare log files and start outputting logs to stdout
touch /code/logs/gunicorn.log
touch /code/logs/access.log
tail -n 0 -f /code/logs/*.log &

echo Starting nginx 
# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn contabot.wsgi:application \
    --name contabot \
    --bind unix:contabot.sock \
    --workers 3 \
    --log-level=info \
    --log-file=/code/logs/gunicorn.log \
    --access-logfile=/code/logs/access.log & 
