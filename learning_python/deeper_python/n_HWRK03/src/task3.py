from re import findall
from collections import Counter


def init_task3():
    with open('../text.txt', 'r', encoding='utf-8') as issue_file:
        issue_text = ''.join(line.strip() for line in issue_file)
    issue_words = Counter(findall(r'\w+', issue_text.lower()))
    print('10 самых частых слов в статье: ', issue_words.most_common(10))
    return
