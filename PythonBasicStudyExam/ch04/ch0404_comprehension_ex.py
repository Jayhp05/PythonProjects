# 다음과 같은 리스트가 있다. 리스트 word의 뜻을 순서에 맞게
# meaning에 저장한 후 딕셔너리 컴프리헨션을 활용해 다음과 같이
# 단어와 그 뜻이 한 쌍으로 이루어진 사전을 만들어 보자.
# word = ["none", "oop", "class", "sequence", "enumerate"]
# meaning = []
#
# 프로그램 실행 결과
# >>> e_dict
# {'none': '아무도(...않다)', 'oop': '객체지향 프로그래밍', 'class': '학급, 수
# 업', 'sequence': '(사건행동 등의) 순서', 'enumerate': '열거하다'}
#
# >>> e_dict.get("none")
# '아무도(...않다)'

word = ["none", "oop", "class", "sequence", "enumerate"]
meaning = ['아무도(...않다)', '객체지향 프로그래밍', '학급, 수업', '(사건행동 등의) 순서', '열거하다']

# 딕셔너리 컴프리헨션을 이용한 사전 만들기
e_dict = {word: meaning for word, meaning in zip(word, meaning)}

print(e_dict)

print(e_dict.get("none"))
