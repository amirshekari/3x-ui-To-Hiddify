
# 🔄 3xuiToHiddify

انتقال کاربران پنل سنایی به هیدیفای

📄 [English Version](README_EN.md)


ابزار مهاجرت کاربران از دیتابیس `x-ui` به پنل Hiddify از طریق API.

---

## 📌 خلاصه

این اسکریپت با زبان پایتون توسعه داده شده و کاربران ثبت‌شده در پایگاه داده‌ی `x-ui.db` را استخراج کرده، اطلاعات مصرف و محدودیت آن‌ها را محاسبه می‌کند و در نهایت، کاربران را به صورت خودکار در پنل Hiddify ایجاد می‌کند.

---

## ⚙️ پیش‌نیازها

### 1. نصب Python (در صورت نیاز)

ابتدا بررسی کن که Python روی سیستم نصب هست یا نه:

```
python --version
```

اگر نصب نبود، به وب‌سایت رسمی برو و نصب کن:

🔗 [دانلود Python](https://www.python.org/downloads/)

> ⚠️ هنگام نصب در ویندوز، تیک گزینه‌ی **"Add Python to PATH"** رو حتماً فعال کن.

---

### 2. نصب کتابخانه‌ی موردنیاز (`requests`)

بعد از نصب Python، پکیج `requests` رو با دستور زیر نصب کن:

```
pip install requests
```

---

## 🚀 طریقه استفاده

### 1. دریافت اسکریپت

فایل `3xuiToHiddify.py` را از این مخزن دریافت یا کلون کن:

```
git clone https://github.com/username/3xuiToHiddify.git
cd 3xuiToHiddify
```

### 2. اجرای برنامه

```
python 3xuiToHiddify.py
```

### 3. وارد کردن اطلاعات

در حین اجرای برنامه، سه مورد از شما پرسیده می‌شود:

| ورودی                        | توضیح                                                                |
|-----------------------------|-----------------------------------------------------------------------|
| مسیر پایگاه داده x-ui       | مسیر کامل فایل `x-ui.db` (مثال: `/root/x-ui.db`)                   |
| آدرس API پنل Hiddify        | مثال: `https://domain.com/proxy/api/v2/admin/user/`                 |
| کلید API                    | کلید اختصاصی شما از پنل Hiddify (داخل تنظیمات مدیریتی)             |

---

## 📤 عملکرد برنامه

برنامه به صورت خودکار موارد زیر را انجام می‌دهد:

1. اتصال به دیتابیس SQLite و خواندن اطلاعات کاربران
2. محاسبه مصرف کل اینترنت (آپلود + دانلود)
3. محاسبه حجم مجاز و تاریخ انقضا به روز
4. ارسال هر کاربر به API پنل Hiddify
5. ثبت نتیجه‌ی هر درخواست در فایل `migration_results.json`

---

## 📂 ساختار خروجی

پس از اجرا، فایلی به نام `migration_results.json` ساخته می‌شود که شامل نتیجه هر ارسال است:

```json
[
  {
    "name": "testuser",
    "status_code": 201,
    "response": "{...}",
    "success": true
  },
  ...
]
```

---

## 🧪 نمونه اجرا

```
Enter path to x-ui.db: /root/x-ui.db
Enter full Hiddify API endpoint: https://panel.hiddify.com/proxy/api/v2/admin/user/
Enter your Hiddify API Key: 3f89e***-***-***-****-*******e87
[✓] testuser1 → 201
[✓] testuser2 → 201
[✗] user3 → Error: Connection timed out

Migration completed. Results saved to migration_results.json
```

---

## 🛡️ نکات امنیتی

- کلید API را در فایل یا مخزن عمومی نگهداری نکنید.
- در صورت نیاز از فایل `.env` و ماژول `dotenv` استفاده کنید (در نسخه‌های بعدی ممکن است اضافه شود).

---

## 📄 مجوز

پروژه تحت مجوز MIT منتشر شده است – استفاده آزاد همراه با حفظ حقوق نویسنده.

---

## ✨ توسعه‌دهنده

[👤 github.com/amirshekari](https://github.com/amirshekari)

در صورت مفید بودن پروژه، لطفاً ستاره فراموش نشه ⭐🙂
