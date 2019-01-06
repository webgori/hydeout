---
published: false
title: Jenkins Android SDK 설정하기
---
https://developer.android.com/studio/#downloads

명령줄 도구만 해당 섹션으로 이동

플랫폼에 맞게 파일 다운로드

### Linux
```
mkdir android-sdk
mv ./sdk-tools-linux-4333796.zip android-sdk
cd android-sdk
unzip ./sdk-tools-linux-4333796.zip
./tools/bin/sdkmanager "build-tools;27.0.3"
```

Jenkins -> Manage Jenkins -> Configure System

Check "Environment variables"

add name: ANDROID_HOME, value -> SDK PATH