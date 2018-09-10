import random
from django.template.loader import render_to_string
from .samples import 아이즈원_찾기, 상한가_크롤링, 테마별_시세_크롤링


def izone(keyword):
    if keyword.find("아이즈원") or keyword.lower().find("izone"):
        if keyword != '':
            keyword = "아이즈원"
        else:
            keyword = "아이즈원 " + keyword
        post_list = 아이즈원_찾기(keyword)
        speech = render_to_string('dialogflow/result_izone.txt', {
            'post_list': post_list,
        })
    else:
        speech = '{}는 지원하지 않습니다.'.format(keyword)
    return {'speech': speech}


def stock_search(stock_search_term):
    if stock_search_term == '상한가 종목':
        speech = 상한가_크롤링()

    elif stock_search_term == '테마별 시세':
        speech = 테마별_시세_크롤링()

    else:
        speech = '{}는 지원하지 않습니다.'.format(stock_search_term)

    return {'speech': speech}
