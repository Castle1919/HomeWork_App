PROJECT_NAME="my_project"

mkdir $PROJECT_NAME && cd $PROJECT_NAME


pip install --upgrade pip
pip install django

pip freeze > requirements.txt

echo "Проект $PROJECT_NAME создан успешно!"
