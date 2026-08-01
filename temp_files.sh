
./psychological_warfare &
sleep 0.5
# Find the temp files
ls /tmp/ | grep -E '^[a-zA-Z0-9]{9}$' | head -2 | while read file; do
    echo "=== /tmp/$file ==="
    cat "/tmp/$file"
    echo
done