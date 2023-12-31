from faker import Faker

# Основной URL тестируемого сайта
URL = 'https://b2c.passport.rt.ru'

# Путь к драйверу
PATH = "chromedriver_mac/chromedriver"

# Валидные данные для авторизации
valid_email = 'TEST_VALID_EMAIL'
valid_phone = 'TEST_VALID_PHONE (+79264375678)'
valid_password = 'TEST_VALID_PASSWORD'

# Невалидные данные для авторизации
fake = Faker()
fake_password = fake.password()
