
#!/bin/bash
until python -m test; do
    echo "'myscript.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done
