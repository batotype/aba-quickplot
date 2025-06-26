*Note: content in ` ` is code. Content in < > is variable: you are not intended to write `` or <> into your terminal.

Install WSL (preferrably Debian Buster) if you are on Windows; otherwise, just open a terminal.
Be sure Git and Python3 are installed by following their official installation instructions.
You can get our repo by typing `git clone https://github.com/batotype/aba-quickplot.git`

-==OPTIONAL BEGIN==-
If you want to make your own copy of the repo, that is okay--anyone can use or modify this library for free without consequences.

If you create your own repo, you may be asked for a password. 
If so, please go to https://github.com/settings/tokens and generate a classic token and use the personal access token (classic) as your password. Write it down it will only be shown once.
-==OPTIONAL END==-

Now, type `python3 -m venv ./venv`
Then `source ./venv/bin/activate`
Then `pip install matplotlib`
Then `python <filename>.py` (replace <filename> with the desired filename). 

You can open the py files and modify the data, ticmarks, etc. Just play around with the contents: hopefully the comments will be helpful for you.
I have tried my best to follow a good commenting style, but I would be very open to improvements. 

Sometimes it is up to 20+ times faster to work with a text-only interface so I prefer this to Excel.

-==NEWS BEGIN==-
I am going to create some folders for different ways of managing data, also--csv, tsv, json, etc.
I am going to include a github tutorial for branching, this week, also. Git is a very useful communication tool for software developers.
-==NEWS END==-

-==Citation data, optional==-
Botto, J. (2025). ABA-Quickplot (Latest) [Computer software]. GitHub. https://github.com/batotype/aba-quickplot.git

-==Acknowledgement==-
Thank you to (a) my brother and (b) my best friend, for troubleshooting support.
