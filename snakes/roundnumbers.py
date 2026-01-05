import re
import math

#replaced the old godawful rounding script, you're welcome euc -sunlit

with open('readytoconvert.txt', 'r') as file:
    filedata = file.read()

def round_half_away_from_zero(x: float) -> int:
    if x >= 0:
        return int(math.floor(x + 0.5))
    return int(math.ceil(x - 0.5))

def _repl(match: re.Match) -> str:
    s = match.group(0)
    try:
        val = float(s)
    except Exception:
        return s
    rounded = round_half_away_from_zero(val)
    return f"{rounded:.6f}"

# Match signed/unsigned decimal numbers with a fractional part
pattern = re.compile(r"-?\d+\.\d+")
filedata = pattern.sub(_repl, filedata)

with open('readytoconvert.txt', 'w') as file:
    file.write(filedata)
