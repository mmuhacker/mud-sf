<div align="center">

# 🌐 Subdomain Finder — أداة اكتشاف النطاقات الفرعية

**تعمل على نظام Kali Linux و تطبيق Termux**

꧁ঔৣ☬ Muhannad Daher ☬ঔৣ꧂

---

![Version](https://img.shields.io/badge/1.0-%EF%BA%8D%EF%BB%B9%EF%BA%BB%EF%BA%AA%EF%BA%8D%EF%BA%AE-blue?style=for-the-badge)<br>
![Platform](https://img.shields.io/badge/%EF%BB%9B%EF%BA%8E%EF%BB%9F%EF%BB%B2%20%EF%BB%9F%EF%BB%B4%EF%BB%A8%EF%BB%9C%EF%BA%B2-%EF%BA%8D%EF%BB%9F%EF%BA%92%EF%BB%B4%EF%BA%8C%EF%BA%94-green?style=for-the-badge&logo=kalilinux)<br>
![Platform](https://img.shields.io/badge/%EF%BA%84%EF%BB%A7%EF%BA%AA%EF%BA%AE%EF%BB%AE%EF%BB%B3%EF%BA%AA-%EF%BA%8D%EF%BB%9F%EF%BA%92%EF%BB%B4%EF%BA%8C%EF%BA%94-green?style=for-the-badge&logo=android)<br>
![Python](https://img.shields.io/badge/3.x-%EF%BA%91%EF%BA%8E%EF%BB%B3%EF%BA%9C%EF%BB%AE%EF%BB%A6-blue?style=for-the-badge&logo=python)<br>
![License](https://img.shields.io/badge/MIT-%EF%BA%8D%EF%BB%9F%EF%BA%98%EF%BA%AE%EF%BA%A7%EF%BB%B4%EF%BA%BA-red?style=for-the-badge)<br>
![Status](https://img.shields.io/badge/%EF%BB%A7%EF%BA%B8%EF%BB%82-%EF%BA%8D%EF%BB%9F%EF%BA%A4%EF%BA%8E%EF%BB%9F%EF%BA%94-blue?style=for-the-badge)

---

**المحتويات:**

</div>

- [الوصف](#الوصف)
- [المميزات](#المميزات)
- [التثبيت](https://github.com/mmuhacker/mud-sf/blob/main/README.md#%EF%B8%8F-%D8%A7%D9%84%D8%AA%D8%AB%D8%A8%D9%8A%D8%AA)
  - [التثبيت على Termux](#التثبيت-على-termux)
  - [التثبيت على Kali Linux](#التثبيت-على-kali-linux)
- [التشغيل](#التشغيل)
- [طريقة الاستخدام](#طريقة-الاستخدام)
- [مثال](#مثال)
- [المتطلبات](#المتطلبات)
- [إخلاء المسؤولية](#إخلاء-المسؤولية)
- [المطوّر](#المطوّر)

---

<div align="center" id="الوصف">

## 📌 الوصف

</div>

أداة لاكتشاف النطاقات الفرعية النشطة لأي نطاق عبر حل أسماء DNS، مكتوبة بلغة Python وتعمل على Termux و Kali Linux. تدعم قائمة مدمجة من أشهر النطاقات الفرعية أو ملف قاموس مخصص.

---

<div align="center" id="المميزات">

## ✨ المميزات

</div>

- 🌐 قائمة مدمجة من 60+ نطاق فرعي شائع
- 📂 دعم ملفات القاموس المخصصة
- 🔎 عرض عنوان IP لكل نطاق مكتشف
- ⚡ تعدد الخيوط للسرعة القصوى
- 🧹 تنظيف النطاق تلقائياً (يزيل http:// و www.)
- 🌍 واجهة عربية بالكامل

---

<div align="center" id="التثبيت-على-termux">

## ⚙️ التثبيت

### Termux

</div>

**الخطوة 1 — تحديث النظام**
```bash
pkg update && pkg upgrade -y
```

**الخطوة 2 — تثبيت المتطلبات** *(لمرة واحدة فقط)*
```bash
pkg install python tor curl fontconfig rust -y
```
```bash
pip install requests pysocks arabic-reshaper
pip install python-bidi==0.4.2
```

**الخطوة 3 — تثبيت الخط العربي** *(لمرة واحدة فقط)*
```bash
curl -L "https://fonts.gstatic.com/s/notonaskharabic/v33/RrQ5bpV-9Dd1b1OAGA6M9PkyDuVBePeKNaxcsss0Y7bwvc-VaA.ttf" -o ~/.termux/font.ttf
termux-reload-settings
```

**الخطوة 4 — تنزيل الأداة**
```bash
curl -o $PREFIX/bin/mud_sf.py https://raw.githubusercontent.com/mmuhacker/mud-sf/main/mud_sf.py
```

**الخطوة 5 — إعطاء صلاحية التشغيل**
```bash
chmod +x $PREFIX/bin/mud_sf.py
```

**الخطوة 6 — إنشاء رابط الاختصار**
```bash
ln -sf $PREFIX/bin/mud_sf.py $PREFIX/bin/sf
```

**⚡ أو قم بكل شيء بأمر واحد مجمّع**
```bash
pkg update && pkg upgrade -y && pkg install python tor curl fontconfig rust -y && pip install requests pysocks arabic-reshaper && pip install python-bidi==0.4.2 && curl -L "https://fonts.gstatic.com/s/notonaskharabic/v33/RrQ5bpV-9Dd1b1OAGA6M9PkyDuVBePeKNaxcsss0Y7bwvc-VaA.ttf" -o ~/.termux/font.ttf && termux-reload-settings && curl -o $PREFIX/bin/mud_sf.py https://raw.githubusercontent.com/mmuhacker/mud-sf/main/mud_sf.py && chmod +x $PREFIX/bin/mud_sf.py && ln -sf $PREFIX/bin/mud_sf.py $PREFIX/bin/sf && sf
```

---

<div align="center" id="التثبيت-على-kali-linux">

### Kali Linux

</div>

**الخطوة 1 — تحديث النظام**
```bash
sudo apt update && sudo apt upgrade -y
```

**الخطوة 2 — تثبيت المتطلبات** *(لمرة واحدة فقط)*
```bash
pip install requests arabic-reshaper python-bidi==0.4.2 --break-system-packages
```

**الخطوة 3 — تنزيل الأداة**
```bash
sudo curl -o /usr/local/bin/mud_sf.py https://raw.githubusercontent.com/mmuhacker/mud-sf/main/mud_sf.py
```

**الخطوة 4 — إعطاء صلاحية التشغيل**
```bash
sudo chmod +x /usr/local/bin/mud_sf.py
```

**الخطوة 5 — إنشاء رابط الاختصار**
```bash
sudo ln -sf /usr/local/bin/mud_sf.py /usr/local/bin/sf
```

**⚡ أو قم بكل شيء بأمر واحد مجمّع**
```bash
sudo apt update && sudo apt upgrade -y && pip install requests arabic-reshaper python-bidi==0.4.2 --break-system-packages && sudo curl -o /usr/local/bin/mud_sf.py https://raw.githubusercontent.com/mmuhacker/mud-sf/main/mud_sf.py && sudo chmod +x /usr/local/bin/mud_sf.py && sudo ln -sf /usr/local/bin/mud_sf.py /usr/local/bin/sf && sf
```

---

<div align="center" id="التشغيل">

## 🚀 التشغيل

</div>

```bash
sf
```

**أو بالأمر الكامل**

```bash
mud_sf.py
```

---

<div align="center" id="طريقة-الاستخدام">

## 📖 طريقة الاستخدام

</div>

1. أدخل النطاق: مثلاً `example.com`
   *(الأداة تقبل أيضاً: `https://example.com` أو `www.example.com`)*
2. اختر وضع البحث:

<div align="center">
   
| الوضع | الوصف |
|-------|-------|
| `1` قائمة مدمجة | بحث في 60+ نطاق فرعي شائع ⚡ |
| `2` ملف قاموس | أدخل مسار ملف .txt مخصص 📂 |
</div>
---

<div align="center" id="مثال">

## 💡 مثال

</div>

أدخل النطاق: example.com
اختيارك: 1

  [مكتشف]  www.example.com    →  93.184.216.34
  [مكتشف]  mail.example.com   →  93.184.216.50
  [مكتشف]  api.example.com    →  93.184.216.55

[✓] النطاقات الفرعية المكتشفة (3)
[✓] انتهى البحث: 14:25:10

---

<div align="center" id="المتطلبات">

## 🔧 المتطلبات


| المتطلب | الوصف |
|---------|-------|
| Python 3.6+ | لغة البرمجة |
| arabic-reshaper | دعم النص العربي |
| python-bidi | اتجاه النص العربي |
| curl | تنزيل الأداة |

</div>

> ⚠️ **ملاحظة:** بدون تثبيت `arabic-reshaper` و `python-bidi` سيظهر النص العربي معكوساً ومتقطعاً.

---

<div align="center" id="إخلاء-المسؤولية">

## ⚖️ إخلاء المسؤولية

</div>

هذه الأداة مخصصة **لأغراض تعليمية واختبار الأنظمة التي تملك صلاحية اختبارها فقط**.
استخدامها على أنظمة بدون إذن يُعدّ مخالفاً للقانون.

---

<div align="center" id="المطوّر">

## 👨‍💻 المطوّر

**Muhannad Daher**

[![GitHub](https://img.shields.io/badge/GitHub-mmuhacker-black?style=for-the-badge&logo=github)](https://github.com/mmuhacker)

---

***Madarik Tools — صُنع بالعربية***

⭐ **إذا أعجبتك الأداة، لا تنسَ النجمة!** ⭐

</div>
