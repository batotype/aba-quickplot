Install WSL (preferrably Debian Buster) if you are on Windows; otherwise, just open a terminal.
Be sure Git and Python3 are installed by following their official installation instructions.
You can get our repo by typing `git clone https://github.com/batotype/aba-quickplot.git`
If you are asked for a password, please go to https://github.com/settings/tokens and generate a classic token and use the personal access token (classic) as your password. Write it down it will only be shown once.
Now, type `python3 -m venv ./venv`
Then `source ./venv/bin/activate`
Then `pip install matplotlib`
Then `python <filename>.py` (replace <filename> with the desired filename). 

You can open the py files and modify the data, ticmarks, etc. Sometimes it is up to 20+ times faster to work with a text-only interface so I prefer this to Excel.