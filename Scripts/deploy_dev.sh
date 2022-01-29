cd ..

pip freeze > requirements.txt
git add .
git commit -m "Deployed development"
git push origin main

#ssh -i C:/Users/Nikita/.ssh/id_rsa nikikone@159.89.232.171 'sh ~/server_development/SIT_dev_prod/Scripts/build.sh'