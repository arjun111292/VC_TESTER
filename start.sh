if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/arjun111292/VC_TESTER.git /VC_TESTER
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /VC_TESTER
fi
cd /VC_TESTER
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
