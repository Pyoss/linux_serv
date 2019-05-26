
#!/bin/bash
until python -m test; do
    error_msg = "'myscript.py' crashed with exit code $?. Restarting..."
    python -m bot_watcher error_msg
    sleep 1
done
