#!/bin/bash

WEEK=$(sed '3!d' issue_raw | awk -F '_' '{print $1}' | awk '{print $2}')
PROB=$(sed '3!d' issue_raw | awk -F '_' '{print $2}' | awk '{print $2}')

echo -n $WEEK $PROB | tr -d "\r" > issue_metadata

START=$(grep -m2 -n "\`\`\`" issue_raw | cut -d: -f1 | head -1)
END=$(expr $(grep -m2 -n "\`\`\`" issue_raw | cut -d: -f1 | tail -1) - 1)

LEN=$(expr $END - $START)

head -$END issue_raw | tail -$LEN > issue_trimmed.py