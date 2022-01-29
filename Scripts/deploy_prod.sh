cd ..
cd ..

pip freeze > requirements.txt
git add .
git commit -m "Deployed production"
git push origin

#ssh -i C:/Users/Nikita/.ssh/id_rsa nikikone@159.89.232.171 'sh ~/server_production/SIT_laba6/Scripts/build.sh'