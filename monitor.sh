
#!/bin/bash
until python -m test; do
    $ERROR_MSG="'myscript.py' crashed with exit code $?. Restarting..."
    python -m bot_watcher $ERROR_MSG
    sleep 1
done
