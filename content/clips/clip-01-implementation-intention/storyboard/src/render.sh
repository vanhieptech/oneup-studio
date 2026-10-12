python3 gen.py && for i in 01 02 03 04 05 06 07 08 09 10; do google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=1080,1920 --virtual-time-budget=3000 --screenshot=../beat-$i.png beat-$i.html >/dev/null 2>&1; done
cd .. && ffmpeg -loglevel error -y -i beat-%02d.png -vf "scale=270:-1,tile=5x2:padding=8:color=white" /tmp/peek.png
