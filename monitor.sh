 
#!/bin/sh
until python -m test; do
    export ERROR_MSG="'myscript.py' crashed with exit code $?. Restarting..." &>2
    python -m bot_watcher
    sleep 10
done
