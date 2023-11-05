Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\r\n\t\f\ ][^AEIOU][^.,]$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())