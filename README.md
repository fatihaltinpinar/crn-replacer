# CRN - Replacer

This script will replace CRN's in the 'End-of-term Survey Announcement' with the corresponding instructor name since there are probably many people who are not
filling the surveys because they don't know which CRN they took (like me). Also, it is not easy to find out which CRN 
you took since:
- Classes on Ninova does not have the CRN all the time.
- Class schedules get updated on SIS before the term ends thus no luck there as well.
- Ninova mobile app's calendar would have helped if the term has not ended.
- An option is logging into SIS, choosing a term, then looking into registered courses. This takes quite some time and it not so easy to navigate in SIS on mobile.
- Another option is web archive which again probably no one will bother going there.

# Requirements
You need Python 3. 
```bash
pip install -r requirements.txt
```

# Usage
In order to obtain the CRN - Instructor information, you need to run following command with a date that is likely to contain right crn instructor pairs of that term over SIS.

```bash
python parser.py YYYYMMDD
```
Example:
```bash
python parser.py 20191010
```

Then run replacer.py which provides a graphical user interface.
```bash
python replacer.py
```

# Contributing
Pull requests are always welcome.

# License
The MIT License (MIT)

Copyright (c) 2020  Fatih Altınpınar
