# 🌐 Subdomain Finder — أداة اكتشاف النطاقات الفرعية
**المطور:** ꧁ঔৣ☬ Muhannad Daher ☬ঔৣ꧂ | **الإصدار:** 1.0 | **المستودع:** `mud-sf`

---

## 📌 الوصف
أداة لاكتشاف النطاقات الفرعية النشطة لأي نطاق عبر حل أسماء DNS، مكتوبة بلغة Python وتعمل على Termux و Kali Linux. تدعم قائمة مدمجة من أشهر النطاقات الفرعية أو ملف قاموس مخصص.

---

## ✨ المميزات
- 🌐 قائمة مدمجة من 60+ نطاق فرعي شائع
- 📂 دعم ملفات القاموس المخصصة
- 🔎 عرض عنوان IP لكل نطاق مكتشف
- ⚡ تعدد الخيوط للسرعة القصوى
- 🧹 تنظيف النطاق تلقائياً (يزيل http:// و www.)
- 🌍 واجهة عربية بالكامل

---

## ⚙️ التثبيت

### Termux
```bash
curl -o $PREFIX/bin/mud_sf.py https://raw.githubusercontent.com/mmuhacker/mud-sf/main/mud_sf.py
chmod +x $PREFIX/bin/mud_sf.py
ln -sf $PREFIX/bin/mud_sf.py $PREFIX/bin/sf
```

### Kali Linux
```bash
sudo curl -o /usr/local/bin/mud_sf.py https://raw.githubusercontent.com/mmuhacker/mud-sf/main/mud_sf.py
sudo chmod +x /usr/local/bin/mud_sf.py
sudo ln -sf /usr/local/bin/mud_sf.py /usr/local/bin/sf
```

---

## 🚀 التشغيل
```bash
sf
# أو
mud_sf.py
```

---

## 📖 طريقة الاستخدام

```
1. أدخل النطاق: مثلاً example.com
   (الأداة تقبل أيضاً: https://example.com أو www.example.com)
2. اختر وضع البحث:
   [1] قائمة مدمجة — سريع ومباشر         ⚡
   [2] ملف قاموس  — أدخل مسار ملف .txt   📂
```

---

## 💡 مثال
```
أدخل النطاق: example.com
اختيارك: 1

  [مكتشف]  www.example.com    →  93.184.216.34
  [مكتشف]  mail.example.com   →  93.184.216.50
  [مكتشف]  api.example.com    →  93.184.216.55

[✓] النطاقات الفرعية المكتشفة (3)
[✓] انتهى البحث: 14:25:10
```

---

## 📂 استخدام ملف قاموس مخصص
```bash
# أنشئ ملف قاموس
echo -e "admin\nportal\ntest\ndev\nstaging\nvpn" > subdomains.txt

# شغّل الأداة واختر 2 ثم أدخل المسار
sf
```

---

## 🔧 المتطلبات
- Python 3.6 أو أحدث
- لا توجد مكتبات خارجية

```bash
# التثبيت على Termux إذا لم يكن Python موجوداً
pkg install python
```

---

## ⚖️ إخلاء المسؤولية
هذه الأداة مخصصة **لأغراض تعليمية واختبار الأنظمة التي تملك صلاحية اختبارها فقط**.
استخدامها على أنظمة بدون إذن يُعدّ مخالفاً للقانون.

---

*🇯🇴 Madarik Tools — صُنع بالعربية*
