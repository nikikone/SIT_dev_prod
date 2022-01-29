cd ..

pip freeze > requirements.txt
git add .
git commit -m "Deployed production"
git push origin main

ssh -i C:/Users/Nikita/.ssh/id_rsa nikikone@159.89.232.171 'cd server_production/SIT_dev_prod/Scripts && sh build.sh'