#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================
#  Subdomain Finder — أداة اكتشاف النطاقات الفرعية
#  المطور: Muhannad | مدارك AI Tools
# ============================================

import socket
import sys
import os
import threading
from datetime import datetime

# ── دعم النص العربي ──────────────────────────
def ar(text):
    """دالة لطباعة النص العربي بشكل صحيح في الطرفية"""
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode('utf-8', errors='replace').decode('ascii', errors='replace'))

# ── الألوان ───────────────────────────────────
class لون:
    أخضر   = '\033[92m'
    أحمر   = '\033[91m'
    أصفر   = '\033[93m'
    أزرق   = '\033[94m'
    سماوي  = '\033[96m'
    بنفسجي = '\033[95m'
    عريض   = '\033[1m'
    إعادة  = '\033[0m'

# ── البانر ────────────────────────────────────
def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    ar(f"""
{لون.بنفسجي}{لون.عريض}
╔══════════════════════════════════════╗
║    🌐 أداة اكتشاف النطاقات الفرعية   ║
║       Subdomain Finder v1.0          ║
║      مدارك AI Tools — بالعربية       ║
╚══════════════════════════════════════╝
{لون.إعادة}""")

# ── قائمة النطاقات الفرعية الشائعة ───────────
نطاقات_شائعة = [
    "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1", "ns2",
    "webdisk", "cpanel", "whm", "autodiscover", "autoconfig", "m", "imap",
    "test", "dev", "staging", "api", "blog", "shop", "store", "app",
    "admin", "panel", "dashboard", "portal", "secure", "vpn", "remote",
    "upload", "download", "media", "cdn", "static", "assets", "img",
    "images", "video", "videos", "files", "docs", "wiki", "help",
    "support", "forum", "community", "news", "mobile", "beta", "old",
    "backup", "db", "database", "sql", "mysql", "phpmyadmin", "git",
    "gitlab", "jenkins", "jira", "confluence", "monitor", "status",
    "analytics", "track", "log", "logs", "metrics", "grafana",
    "auth", "login", "sso", "oauth", "id", "account", "accounts",
    "pay", "payment", "checkout", "cart", "order", "orders",
    "search", "map", "maps", "live", "stream", "chat", "bot",
]

# ── نتائج الاكتشاف ────────────────────────────
نطاقات_مكتشفة = []
قفل = threading.Lock()

# ── فحص نطاق فرعي واحد ───────────────────────
def فحص_نطاق(نطاق_فرعي, نطاق_أساسي):
    هدف_كامل = f"{نطاق_فرعي}.{نطاق_أساسي}"
    try:
        ip = socket.gethostbyname(هدف_كامل)
        with قفل:
            نطاقات_مكتشفة.append((هدف_كامل, ip))
            ar(f"  {لون.أخضر}[مكتشف]{لون.إعادة}  {لون.عريض}{هدف_كامل}{لون.إعادة}  →  {لون.أصفر}{ip}{لون.إعادة}")
    except (socket.gaierror, socket.timeout):
        pass

# ── مسح من قائمة مدمجة ───────────────────────
def مسح_قائمة_مدمجة(نطاق, مهلة=2):
    ar(f"\n{لون.أزرق}[*] البحث في {len(نطاقات_شائعة)} نطاق فرعي شائع...{لون.إعادة}\n")
    socket.setdefaulttimeout(مهلة)
    خيوط = []
    for نطاق_فرعي in نطاقات_شائعة:
        خ = threading.Thread(target=فحص_نطاق, args=(نطاق_فرعي, نطاق))
        خيوط.append(خ)
        خ.start()
        if len(خيوط) >= 50:
            for t in خيوط:
                t.join()
            خيوط = []
    for خ in خيوط:
        خ.join()

# ── مسح من ملف قاموس ─────────────────────────
def مسح_من_ملف(نطاق, مسار_ملف, مهلة=2):
    if not os.path.exists(مسار_ملف):
        ar(f"{لون.أحمر}[!] الملف غير موجود: {مسار_ملف}{لون.إعادة}")
        sys.exit(1)
    with open(مسار_ملف, 'r', encoding='utf-8', errors='ignore') as f:
        كلمات = [x.strip() for x in f.readlines() if x.strip()]
    ar(f"\n{لون.أزرق}[*] البحث في {len(كلمات)} نطاق فرعي من الملف...{لون.إعادة}\n")
    socket.setdefaulttimeout(مهلة)
    خيوط = []
    for كلمة in كلمات:
        خ = threading.Thread(target=فحص_نطاق, args=(كلمة, نطاق))
        خيوط.append(خ)
        خ.start()
        if len(خيوط) >= 50:
            for t in خيوط:
                t.join()
            خيوط = []
    for خ in خيوط:
        خ.join()

# ── التحقق من النطاق ──────────────────────────
def تحقق_نطاق(نطاق):
    نطاق = نطاق.strip()
    نطاق = نطاق.replace("http://", "").replace("https://", "").replace("www.", "")
    if '/' in نطاق:
        نطاق = نطاق.split('/')[0]
    return نطاق

# ── القائمة الرئيسية ──────────────────────────
def main():
    banner()

    ar(f"{لون.أصفر}أدخل النطاق الأساسي (مثال: example.com):{لون.إعادة} ", end='')
    نطاق = input().strip()
    if not نطاق:
        ar(f"{لون.أحمر}[!] لم تدخل نطاقاً.{لون.إعادة}")
        sys.exit(1)

    نطاق = تحقق_نطاق(نطاق)

    ar(f"\n{لون.سماوي}[✓] النطاق المستهدف: {نطاق}{لون.إعادة}")
    ar(f"{لون.سماوي}[✓] وقت البدء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{لون.إعادة}\n")

    ar(f"""{لون.عريض}اختر وضع البحث:
  {لون.أخضر}1{لون.إعادة} — بحث بالقائمة المدمجة ({len(نطاقات_شائعة)} نطاق فرعي)
  {لون.أخضر}2{لون.إعادة} — بحث من ملف قاموس خاص
{لون.أصفر}اختيارك:{لون.إعادة} """, end='')
    اختيار = input().strip()

    ar(f"\n{'─'*42}")

    if اختيار == '1':
        مسح_قائمة_مدمجة(نطاق)

    elif اختيار == '2':
        ar(f"{لون.أصفر}أدخل مسار ملف القاموس:{لون.إعادة} ", end='')
        مسار = input().strip()
        مسح_من_ملف(نطاق, مسار)

    else:
        ar(f"{لون.أحمر}[!] اختيار غير صالح.{لون.إعادة}")
        sys.exit(1)

    ar(f"\n{'─'*42}")
    if نطاقات_مكتشفة:
        ar(f"\n{لون.أخضر}{لون.عريض}[✓] النطاقات الفرعية المكتشفة ({len(نطاقات_مكتشفة)}):{لون.إعادة}")
        for نطاق_كامل, ip in sorted(نطاقات_مكتشفة):
            ar(f"    ► {نطاق_كامل}  →  {ip}")
    else:
        ar(f"\n{لون.أحمر}[✗] لم يُعثر على نطاقات فرعية.{لون.إعادة}")

    ar(f"\n{لون.سماوي}[✓] انتهى البحث: {datetime.now().strftime('%H:%M:%S')}{لون.إعادة}\n")

if __name__ == '__main__':
    main()
