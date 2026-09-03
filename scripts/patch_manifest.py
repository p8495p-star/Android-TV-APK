from pathlib import Path
import re, sys

p = Path(sys.argv[1])
s = p.read_text(encoding="utf-8")

if "android.intent.category.LEANBACK_LAUNCHER" not in s:
    s = s.replace(
        '<action android:name="android.intent.action.MAIN" />',
        '<action android:name="android.intent.action.MAIN" />\n'
        '                <category android:name="android.intent.category.LEANBACK_LAUNCHER" />',
        1
    )

if "android.hardware.touchscreen" not in s:
    m = re.search(r"(<manifest\b[^>]*>)", s)
    if m:
        s = (s[:m.end()] +
             '\n    <uses-feature android:name="android.hardware.touchscreen" android:required="false" />' +
             s[m.end():])

p.write_text(s, encoding="utf-8")
