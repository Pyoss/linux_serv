
#!/bin/sh

export ERROR_MSG=$(git pull)
python -m bot_watcher
./monitor.sh
