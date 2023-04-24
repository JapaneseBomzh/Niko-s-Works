import os

# Створюємо папку "Україна"
ukraine_dir = os.mkdir("Україна")

oblasti = ["Вінницька", "Волинська", "Дніпропетровська", "Донецька", "Житомирська", "Закарпатська",
           "Запорізька", "Івано-Франківська", "Київська", "Кіровоградська", "Луганська", "Львівська",
           "Миколаївська", "Одеська", "Полтавська", "Рівненська", "Сумська", "Тернопільська", "Харківська",
           "Херсонська", "Хмельницька", "Черкаська", "Чернівецька", "Чернігівська", "м. Київ",
           "Автономна Республіка Крим", "м. Севастополь"]

for oblast in oblasti:
    oblast_dir = os.path.join("Україна", oblast)
    os.mkdir(oblast_dir)


    if oblast == "Вінницька":
        rayoni = ["Вінницький", "Гайсинський", "Жмеринський","Могилів-Подільський","Тульчинський", "Хмільницький"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Волинська":
        rayoni = ["Володимир-Волинський","Камінь-Каширський",  "Ковельський","Луцький"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Дніпропетровська":
        rayoni = ["Дніпровський",  "Кам'янський", "Криворізький","Нікопольський", "Новомосковський","Павлоградський", "Синельниківський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Донецька":
        rayoni = ["Бахмутський", "Волноваський", "Горлівський", "Донецький", "Кальміуський","Краматорський", "Маріупольський", "Покровський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Житомирська":
        rayoni = ["Бердичівський", "Житомирський", "Коростенський", "Новоград-Волинський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Закарпатська":
        rayoni = ["Берегівський", "Мукачівський", "Рахівський", "Тячівський", "Ужгородський","Хустський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Запорізька":
        rayoni = ["Бердянський", "Василівський", "Запорізький",  "Мелітопольський","Пологівський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Івано-Франківська":
        rayoni = ["Верховинський","Івано-Франківський",  "Калуський", "Коломийський", "Косівський", "Надвірнянський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Київська":
        rayoni = [ "Білоцерківський", "Бориспільський", "Броварський", "Бучанський","Вишгородський", "Обухівський", "Фастівський",]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Кіровоградська":
        rayoni = ["Голованівський", "Кропивницький", "Новоукраїнський", "Олександрійський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Луганська":
        rayoni = ["Алчевський", "Довжанський", "Луганський", "Ровеньківський", "Сватівський","Сєвєродонецький", "Старобільський", "Щастинський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Львівська":
        rayoni = ["Дрогобицький", "Золочівський", "Львівський", "Самбірський", "Стрийський","Червоноградський","Яворівський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Миколаївська":
        rayoni = ["Баштанський", "Вознесенський", "Миколаївський", "Первомайський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Одеська":
        rayoni = ["Березівський", "Білгород-Дністровський", "Болградський", "Ізмаїльський", "Одеський район","Подільський","Роздільнянський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Полтавська":
        rayoni = ["Кременчуцький", "Лубенський", "Миргородський", "Полтавський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Рівненська":
        rayoni = ["Вараський", "Дубенський", "Рівненський", "Сарненський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Сумська":
        rayoni = ["Конотопський", "Охтирський", "Роменський", "Сумський район", "Шосткинський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Тернопільська":
        rayoni = ["Кременецький", "Тернопільський", "Чортківський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Харківська":
        rayoni = ["Богодухівський", "Ізюмський", "Красноградський", "Куп`янський", "Лозівський","Харківський","Чугуївський"]
        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Херсонська":
        rayoni = ["Бериславський", "Генічеський", "Каховський", "Скадовський", "Херсонський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Хмельницька":
        rayoni = ["Кам`янець-Подільський", "Хмельницький", "Шепетівський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Черкаська":
        rayoni = ["Звенигородський", "Золотоніський", "Уманський", "Черкаський"]
        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "Чернівецька":
        rayoni = ["Вижницький", "Дністровський", "Чернівецький"]
        
        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)    

    if oblast == "Чернігівська":
        rayoni = ["Чернігівська", "Корюківський", "Ніжинський", "Новгород-Сіверський", "Прилуцький","Чернігівський"]

        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)

    if oblast == "м. Київ":
        districts = ["Дарницький", "Деснянський", "Дніпровський", "Голосіївський", "Оболонський", "Печерський", "Подільський", "Шевченківський"]
        for district in districts:
            district_dir = os.path.join(oblast_dir, district)
            os.mkdir(district_dir)
    
    if oblast == "Автономна Республіка Крим" :
        rayoni = ["Алуштинський", "Бахчисарайський", "Білогірський", "Джанкойський", "Євпаторійський", "Керченський",
                "Кіровський", "Красногвардійський", "Ленінський", "Нижньогірський", "Первомайський", "Роздольненський",
                "Сакський", "Сімферопольський", "Совєтський", "Чорноморський"]


        for rayon in rayoni:
            rayon_dir = os.path.join(oblast_dir, rayon)
            os.mkdir(rayon_dir)


    