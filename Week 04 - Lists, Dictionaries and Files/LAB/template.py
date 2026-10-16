"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here

def status_of(percent, warning_at=90):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference from the limit and the percentage of the limit."""
    percent = value / limit * 100
    difference = value - limit
    return difference, percent

def print_report(label,value,limit,difference,percent,status):
    """Print the full report for one item."""
    print(f"{label:>10}: {value} / {limit}")
    print(f"{'Diff':>10}: {difference:+}")
    print(f"{'Percent':>10}: {percent:.1f}%")
    print(f"{'Status':>10}: {status}")


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

with open("data.txt", "w") as f:
    f.write("R-001,87,100\n")
    f.write("R-002,120,100\n")
    f.write("R-003,64,100\n")

def load_records(path):
    """Read label,value,limit lines and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records

records = load_records("data.txt")

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
