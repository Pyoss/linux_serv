
#!/bin/sh

export ERROR_MSG=$(git pull)
./monitor.sh
