
if [ ! -f requirements.txt ]; then
    echo "Файл requirements.txt не найден!"
    exit 1
fi

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

echo "Виртуальное окружение создано и зависимости установлены!"
