# Android TV APK — Git LFS

Большой APK хранится через Git LFS, поэтому ограничение GitHub Web 25 MB не применяется к этому файлу.

## Первый раз

Установить Git LFS:
```bash
git lfs install
```

Добавить APK:
```bash
mkdir input
git lfs track "input/app.apk"
copy "ПУТЬ_К_ТВОЕМУ_APK" input\app.apk
git add .gitattributes input/app.apk
git commit -m "Add APK via Git LFS"
git push
```

После push APK будет храниться через Git LFS.

## Сборка

Открой:
GitHub → Actions → Build Android TV APK → Run workflow

Workflow декодирует APK, применит Android TV manifest-патч, пересоберёт, выровняет и подпишет APK.
