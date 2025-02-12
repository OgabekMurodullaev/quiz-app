# Quiz App

Quiz App - bu o'qituvchilar uchun test yaratish va talabalar uchun testlarni topshirish imkonini beruvchi veb-ilova.

## 🚀 Loyiha xususiyatlari
- O'qituvchilar test yaratishi va ularni boshqarishi mumkin
- Talabalar testlarni topshirishi va natijalarini ko'rishi mumkin
- Test natijalari bo'yicha **Leaderboard** (reyting jadvali) mavjud
- JWT autentifikatsiya
- PostgreSQL bazasi bilan ishlaydi
- Docker orqali konteynerizatsiya qilingan

---

## 📌 Talablar (Dependencies)
Loyihani ishga tushirishdan oldin quyidagi dasturlar kompyuteringizga o'rnatilgan bo'lishi kerak:

- **Git** → [Yuklab olish](https://git-scm.com/)
- **Docker & Docker Compose** → [Yuklab olish](https://www.docker.com/products/docker-desktop)

---

## 🛠 O'rnatish va ishga tushirish

### **1️⃣ GitHub dan loyihani yuklab olish**
```bash
git clone https://github.com/OgabekMurodullaev/quiz-app.git
cd quiz-app
```

### **2️⃣ .env faylini sozlash**
Loyiha muhit sozlamalarini `.env` faylga kiritish kerak. Agar **.env** fayl mavjud bo'lmasa, `cp .env.example .env` buyrug'i bilan nusxa olib, ichidagi **DATABASE_URL**, **SECRET_KEY**, va boshqa muhim ma'lumotlarni to'ldiring.

### **3️⃣ Docker konteynerlarni ishga tushirish**
```bash
docker-compose up --build
```

Agar `--build` bilan birga ishga tushirsangiz, barcha image'lar qayta build qilinadi.

Agar faqat konteynerlarni ishga tushirmoqchi bo'lsangiz:
```bash
docker-compose up -d
```
**-d** flag konteynerlarni backgroundda ishga tushirish uchun ishlatiladi.

### **4️⃣ Django migrations va superuser yaratish**
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

Superuser yaratgandan so‘ng, administrator paneliga kirib tizimni boshqarish mumkin:
👉 `http://localhost:8000/admin/`

---

## 📡 API Dokumentatsiya
Swagger orqali **API dokumentatsiya** ochish uchun:
```
http://localhost:8000/swagger/
```

ReDoc versiyasi orqali dokumentatsiya:
```
http://localhost:8000/redoc/
```

---

## 🐳 Docker konteynerlarini boshqarish

### **Ishlayotgan konteynerlarni ko'rish**
```bash
docker ps
```

### **Loglarni tekshirish**
```bash
docker-compose logs -f
```

### **Konteynerlarni to'xtatish**
```bash
docker-compose down
```

Agar barcha ma’lumotlarni tozalab konteynerni to‘liq o‘chirmoqchi bo‘lsangiz:
```bash
docker-compose down -v
```

---

## 🔗 Frontend uchun backend URL
Frontend dasturchingiz React yoki boshqa frontend texnologiyasidan foydalansa, `.env` faylda quyidagicha backend API URL'ni qo'shishi kerak:
```
REACT_APP_API_BASE_URL=http://localhost:8000
```

Bu orqali frontend to‘g‘ridan-to‘g‘ri backend bilan integratsiya bo‘lishi mumkin.

---

## 🏗 Loyiha tuzilishi

```
quiz-app/
│-- backend/
│   ├── apps/
│   │   ├── quizzes/       # Test yaratish va boshqarish
│   │   ├── exams/         # Test natijalari va sessiyalar
│   │   ├── users/         # Foydalanuvchilar autentifikatsiyasi
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── manage.py
│
│-- docker-compose.yml    # Docker konfiguratsiya fayli
│-- Dockerfile            # Backend uchun Dockerfile
│-- .env                  # Muhit sozlamalari
│-- requirements.txt      # Python kutubxonalar ro'yxati
│-- README.md             # Loyihani ishga tushirish bo'yicha yo'riqnoma
```

---

## ✨ Muammolar va yechimlar

**1️⃣ Xato:** `django.db.utils.OperationalError: could not connect to server`
**Yechim:** Postgres konteyneri to‘liq ishga tushguncha biroz kutish kerak. Yoki `docker-compose logs db` orqali xatolarni tekshiring.

**2️⃣ Xato:** `ModuleNotFoundError: No module named 'django'`
**Yechim:** Docker konteyner ichida pip install bajarilganligini tekshiring:
```bash
docker-compose exec web pip list
```

**3️⃣ Xato:** `superuser` yaratishda foydalanuvchi e'lon qilinmagan
**Yechim:** Superuser yaratishda username, email va parolni kiritganingizga ishonch hosil qiling.

---

## 🤝 Hissa qo'shish (Contributing)
Agar loyihaga hissa qo‘shmoqchi bo‘lsangiz:
1. Fork qiling
2. O‘zingizning xususiy branch'ni yarating (`git checkout -b new-feature`)
3. O‘zgartirishlarni kiriting (`git commit -m "Yangi imkoniyat qo‘shildi"`)
4. Push qiling (`git push origin new-feature`)
5. Pull Request jo‘nating

---

## 📞 Aloqa
Agar biron muammo yoki taklif bo‘lsa, GitHub Issues orqali bog‘lanishingiz mumkin.

👨‍💻 **Muallif:** [Og'abek Murodullayev](https://github.com/OgabekMurodullaev)

