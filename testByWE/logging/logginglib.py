# logging 라이브러리 연습
# 포매터(출력될 로그의 포맷)
# 핸들러(logger를 컨트롤 여기서는 stream handler와 file handler 사용)이용
# 파일 저장 까지 함

# docs : https://docs.python.org/ko/3/howto/logging.html
# blog : 블로그 주로 참고함 https://hamait.tistory.com/880

# level
# DEBUG : 상세한 정보, 문제 진단시 사용
# INFO : 예상대로 작동하는지 확인
# WARNING : 예상치 못한 일이 발생했거나 가까운 미래에 발생할 문제
# ERROR : 더욱 심각한 문제, 소프트웨어가 일부 기능을 수행하지 못함
# CRITICAL : 심각한 에러, 프로그램 자체가 실행되지 않을 수 있음

# logging work flow
# logger : 어플리케이션 코드가 직접 사용할 수 있는 인터페이스 제공
# handler : logger에 의해 만들어진 log 기록들을 적합한 위치로 보냄
# filter : 어떤 log 기록들이 출력되어야 하는지 결정
# formatter : log 기록들의 최종 출력본 레이아웃 결정

import logging
import os

# 실행중인 파이썬 경로
path = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    mylogger = logging.getLogger("my")
    mylogger.setLevel(logging.INFO) # log의 레벨을 설정, 기본은 warning 이상만 출력됨

    formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s] : %(message)s')

    stream_hander = logging.StreamHandler()
    stream_hander.setFormatter(formatter)
    mylogger.addHandler(stream_hander)

    logpath = str(path) + "/my.log"

    file_handler = logging.FileHandler(logpath)
    mylogger.addHandler(file_handler)

    mylogger.info("server start!!!")
    mylogger.info("server end!!!")
