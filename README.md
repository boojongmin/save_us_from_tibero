# 신이시여 티베로로부터 우리를 구원해주소서

## 1. isql sql file 실행 스크립트

```bash
*      iusql -v WebDB MyID MyPWD -w < My.sql *
*                                            *
*      Each line in My.sql must contain      *
*      exactly 1 SQL command except for the  *
*      last line which must be blank (unless *
*      -n option specified).
```

위와 같이 isql로 sql을 밀어 넣을때는 하나의 sql은 한줄로 되어야하고 `--` 주석이 있으면 실행중 오류가 발생하여 중단되는 이슈가 있습니다.
이에 자주 반복하는 ddl, dml 작업의 편리성을 위해 스크립트를 작성했습니다.

> 실행방법
```
python sql_runner.py {data_source_name} {sql_file_absolute_path}
ex) python sql_runner.py tibero6 /home/boojongmin/dev/ddl.sql
```

## 2. 리눅스 환경에서 tibero로 odbc 작업시 발생하는 오류를 대응하는 방법 참고 소스입니다.

> `common.py` 참조
