# Source - https://stackoverflow.com/a/35688301
# Posted by Quinn, modified by community. See post 'Timeline' for change history
# Retrieved 2026-11-04, License - CC BY-SA 4.0

# The following code will search 'MM/DD/YYYY' (e.g. 11/30/2016 or NOV/30/2016, etc ),
# and replace with 'MM-DD-YYYY' in multi-line mode.
import re
with open ('E:\\test\\abi_farmer\abi_farmer.txt', 'w' ) as f:
    content = f.read()
    content_new = re.sub('[0-9][0-9][:][ ][0-9][:][ ][0-9][:][ ][0-9][0-9]', 'BASS', content)
