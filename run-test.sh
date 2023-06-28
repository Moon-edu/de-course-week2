#!/bin/bash
EXIT_CODE=0
echo "Running test"
poetry run pytest --json-report || EXIT_CODE=$?

echo "Printing out report"
OUTCOME=$(cat .report.json | jq -r '.tests[]|"\(.outcome),\(.nodeid)"')

declare -A SCORE
SCORE["test_create_employee_table"]=10
SCORE["test_create_employees"]=5
SCORE["test_create_visit_log_table"]=10
SCORE["test_create_visit_logs"]=5
SCORE["test_female_employee"]=10
SCORE["test_male_employee"]=10
SCORE["test_cnt_visit_log"]=10
SCORE["test_group_by_visit_log_purpose"]=10
SCORE["test_find_visit_employee"]=10
SCORE["test_update_peach_position"]=10
SCORE["test_delete_null_visit"]=10

while IFS= read -r line; do
  echo "Processing line: $line"

  IFS=',' read -r outcome nodeid <<< "$line"

  TEST_ID=$(echo "$nodeid" | awk -F"::" '{print $2}')
  if [ "$outcome" = "passed" ]; then
    echo "Test $TEST_ID passed, Adding ${SCORE[$TEST_ID]}"
    TOTAL=$((TOTAL+${SCORE[$TEST_ID]}))
  else
    echo "Test $TEST_ID $outcome"
  fi
done <<< "$OUTCOME"
echo "Total score: $TOTAL"
exit $EXIT_CODE
