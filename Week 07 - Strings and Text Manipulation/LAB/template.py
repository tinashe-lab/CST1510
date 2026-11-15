"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here


def parse_line(raw_line):
    """Clean one messy 'host, key=value, ...' line into a dict."""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    result = {"hostname": hostname_part.strip().lower()}
    for piece in rest.split(","):
        key, value = piece.split("=")
        result[key.strip().lower()] = float(value.strip())
    return result


def status_of(record):
    """Return OVER LIMIT, WARNING or OK based on used/total percentage."""
    col = record["used"] / record["total"] * 100
    if col >= 100:
        return "OVER LIMIT"
    if col >= 90:
        return "WARNING"
    return "OK"


for raw in ["  Srv-01 , used=87 , total=100  ", "SRV-02,USED=120,total=100", "srv-04 ,used = 90, total=100"]:
    record = parse_line(raw)
    print(record["hostname"], status_of(record))


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = [line for line in open("example.txt") if line.strip()]

for raw_record in raw_records:
    record = parse_line(raw_record)
    print(record["hostname"], status_of(record))


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

with open("example.txt") as f:
    raw_records = [line for line in f if line.strip()]

flagged = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)
    print(record, status)
    if status != "OK":
        flagged += 1

print(f"{len(raw_records)} records, {flagged} flagged")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring



