# GruntyBot

Actually addons for Willie (http://willie.dftba.net/)

#Install Instructions
## Prepare yourself

GruntyBot

We'll be using 32bit versions of everything to make things simple.

Download MiniGW (http://sourceforge.net/projects/mingw/files/Installer/mingw-get-setup.exe/download)
Go ahead and install this as soon as it finishes. The second part takes a long time.
Click on "mingw32-base" and "mingw32-gcc-g++"
Click installation -> apply changes -> apply
Once that is done at C:\MinGW to your PATH variable (goo.gl/GndczJ)

Download Python 3.x (3.4.3 at the time of this writing) https://www.python.org/downloads
Install Python 3. (I recommend turning on the "Add python.exe to Path" option)

Download lxml (http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml) make sure it matches what Python you downloaded (lxml‑3.4.4‑cp34‑none‑win32.whl as of this writing)

Download willie (https://github.com/embolalia/willie/archive/master.zip)
Unzip willie-master

Download GruntyBot Files https://github.com/godofgrunts/GruntyBot/archive/master.zip
Unzip the GruntyBot-Master

Create a new account on Twitch.tv for your bot (example: GruntyBot)
Go to http://www.twitchapps.com/tmi/ connect your new bot account to it, and copy the key you get INCLUDING THE "oauth:" part (you'll need to do this anytime your password is reset)



Open Windows Powershell AS ADMIN
First we need to go to your download directory
Copy and paste the following (just right click in the Powershell window and it will paste):
cd C:\Users\$env:username\Downloads
pip install .\lxml-3.4.4-cp34-none-win32.whl (change if yours is different)
cd .\willie-master\willie-master
C:\Python34\Lib\idlelib\idle.bat .\setup.py

In the new window pops up, delete the second line (it says "# coding=utf8"), save, and close the file.

Back at Powershell
python.exe .\setup.py build --compiler=mingw32
python.exe .\setup.py install
C:\Python34\Lib\idlelib\idle.bat C:\Python34\Lib\site-packages\willie-*\EGG*\scripts

This will pop up a window. Click Run -> Run Module. 
That will pop up another window that will ask you questions. Everything here should be LOWER CASE.

Nickname for your bot: This needs to be the name of the Twitch Account. ALL LOWER CASE.
Server to connect to: irc.twitch.tv
Connect with SSL: n
Port to connect: 6667
Your own IRC name: YOUR TWITCH NAME (REMEMBER ALL LOWER CASE)
Channel: HASTAG YOUR TWITCH NAME (REMEMBER ALL LOWER CASE) ex #god_of_grunts
Modules that need configuring (y/n): Up to you, some of the modules won't work correctly if you don't, but those are not in the scope of this tutorial

Now exit out of this window (it might complain that it's still running, but we don't care)

Back in powershell:
notepad.exe C:\Users\$env:username\.willie\default.cfg

This will open a notepad with the information you just put in.

Under "host" add:
server_password = YOUR OAUTH:PASSWORD YOU GOT FROM TWITCHAPPS

Under "channels" add:
prefix = \!
admins = OTHER TWITCH USERS YOU WANT TO HAVE CONTROL OF THE BOT (REMEMBER ALL LOWER CASE)


Under that press enter twice and add:

[clock]
tz = America/New_York (CHANGE FOR YOUR TIME ZONE)
time_format = %b/%d/%y - %R

Back to powershell:

cp C:\Users\$env:username\Downloads\GruntyBot-Master\GruntyBot-Master * C:\Users\$env:username\.willie\modules
Set-ExecutionPolicy remotesigned
y
cd C:\Python34\Lib\site-packages\willie-*\EGG*\scripts
.\willie
echo "python.exe $pwd\willie" > willie.ps1
C:\Python34\Lib\idlelib\idle.bat .\willie

In the window that opens up, get rid of everything above "from __future__ import unicode_literals" to the first line (blahblah\python.exe)
Save and close.

Back to powershell:

ii .

This opens up the folder with willie.ps1 and willie in it. 
Right-click, and drag willie.PS1 to the desktop.
Let go and choose "Create a shortcut here"
Right click the shortcut and go to properties
Add quotes around everything in target (eg "C:\Python34\Lib\site-packages\willie")
Now in front of all that add:
powershell.exe -command
It should look something like:
powershell.exe -command "C:\Python34\Lib\site-packages\willie"
Now click okay.
The icon should have changed.

Now double click the icon and it should fire up!

I know this was a lot of steps. If you're having trouble with anything, hit me up @god_of_grunts





