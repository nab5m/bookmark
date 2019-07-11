# Django Bookmark example

Practiced Django features. You can do whatever you want.  
Feel free to add features or to customize it.  
This is not stable project.  
Many works will be needed to deploy a stable version of this project.  

장고의 기능을 연습합니다.  
이 프로젝트는 마음껏 새로운 기능을 추가하거나 기존 코드를 수정할 수 있습니다.  
해당 프로젝트는 안정적인 버전이 아닙니다. 배포 버전을 만들기 위해서는 작업이 더 필요합니다.  

  - Live Demo(데모 사이트): http://nab5m.pythonanywhere.com

## New Features will be added someday...(새롭게 추가될 기능)

  - Comments System(댓글)
  - Bookmark Search and Ordering(북마크 정렬/검색)
  - auto complete(자동완성)
  - top search(일간 조회/실시간 검색)
  - and so on...

## How can I install to my local computer?(내 컴퓨터에 설치하는 방법)
Using Windows CMD(윈도우의 명령프롬프트 사용 시)
Used Python 3.6.8
```sh
1. > git clone -b dev https://github.com/nab5m/bookmark
: master branch's content is poor(master 브랜치의 내용은 빈약합니다.)

2. > cd bookmark/venv/Scripts/
3. > activate.bat   :venv를 활성화합니다.
4. > cd ../..

5. > pip install -r requirements.txt    :실행에 필요한 패키지를 설치합니다.
6. > python manage.py migrate
7.(optional) > python manage.py createsuperuser

8. > python manage.py shell
9.(In python intepreter mode) > exec(open('./config/db_test_data.py'.read())
: 테스트 데이터를 DB에 삽입합니다
10. (wait 3 minutes)

11. > python manage.py runserver
```

## When Finished Using this project...(사용 종료하는 법)
```sh
1. > deactivate
// venv의 사용을 중지합니다.
```

<b>Thank you for seeing this! :)</b>
