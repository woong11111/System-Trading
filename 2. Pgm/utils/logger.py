import os
import logging

def set_logger(name) :

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)  # INFO 레벨 이상 출력하도록 설정 DEBUG < INFO < ERROR < CRITICAL

    formatter = logging.Formatter("%(asctime)s [%(name)s] %(message)s", "%Y-%m-%d %H:%M:%S")

    stream_handler = logging.StreamHandler()  # 핸들러란 내가 로깅한 정보가 출력되는 위치 설정을 말함
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler('trading_history.log')  # jupyter 디렉토리 내에 my.txt (내용 : hello world) 파일이 형성됨
    file_handler.setFormatter(formatter)  # file handler 에 formatter 해줘야지 메모장에 같이 업데이트 됨
    logger.addHandler(file_handler)  # 실행을 여러번하면 동일 파일 내 로깅 내용이 내리차순으로 쌓임

    #logger.info(name)

    return logger
