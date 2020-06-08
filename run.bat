@ECHO OFF
echo Checking youtube-dl for updates...
pip3 install --upgrade youtube-dl

set /p url=Input a YouTube video URL: 
python download-tube.py %url%

echo Done downloading. If there were any issues, please contact Nick.
pause