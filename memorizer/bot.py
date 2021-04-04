#! /usr/bin/env python3
import time
from .plugins.naturalization import get_quetion_answers
from .tools import now
from .notifier import send_message
import random

PERIOD = 60  # second
DELAY_AFTER_SEND_QUESTION = 1  # period 
DELAY_AFTER_SEND_ANSWER = 5  # period


def convert_answer(answer):
    return answer


def main():
    print("Start memorizer")
    send_message(f"[Memorizer][{now()}] Started")
    question_answers = list(get_quetion_answers().items())
    while True:
        i = random.randint(0, len(question_answers))
        try:
            question, answer = question_answers[i]
            answer = convert_answer(answer)
            send_message(f"{i}. {question}")
            time.sleep(DELAY_AFTER_SEND_QUESTION * PERIOD)
            send_message(answer)
            time.sleep(DELAY_AFTER_SEND_ANSWER * PERIOD)
        except Exception:
            import traceback; traceback.print_exc()
            time.sleep(DELAY_AFTER_SEND_QUESTION)


if __name__ == "__main__":
    main()
