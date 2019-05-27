
#!/bin/sh
ERROR_MSG=$(git pull)
export ERROR_MSG
./monitor.sh
