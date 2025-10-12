import os
os.system("pytest -v --maxfail=1 --reruns 2 --reruns-delay 2 -n auto --html=reports/report.html")