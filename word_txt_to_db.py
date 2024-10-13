import sqlite3
from random import shuffle
import tkinter as tk
from functools import partial

def input_txt_output_database(english, korean, name, result):
    # 영어, 뜻 텍스트파일에서 단어를 한줄씩 읽어들여 튜플형태로 격납 할 변수
    word = []
    
    # words_txt라는 폴더안에있는 텍스트파일을 읽어들임
    english = english.get()
    korean = korean.get()
    name = name.get()
    english, korean = 'words_txt\\' + english, 'words_txt\\' + korean
    
    # 파일을 열 때 발생할 수 있는 예외를 처리
    try:
        with open(english, 'r', encoding='UTF-8') as en, open(korean, 'r', encoding='UTF-8') as ko:
            while True:
                e, k = en.readline().rstrip(), ko.readline().rstrip()

                # 문제없이 영어, 뜻을 전부 word에 격납 했을 경우
                if e == '' and k == '':
                    break

                # 영어, 뜻 텍스트파일의 단어개수가 다르거나, 둘이 1대1 매칭이 안되거나 등등
                elif e == '' or k == '':
                    # print('텍스트 파일에 문제가 있으니 텍스트파일을 수정.')
                    result.config(text = '텍스트 파일에 문제가 있으니 텍스트파일을 수정.')
                    return False

                # 한줄씩 읽어들인 영어, 뜻을 word 리스트 변수에 (영어, 뜻)의 튜플형태로 격납
                else:
                    word.append((e, k))
                    
        # 단어를 데이터베이스 테이블에 삽입하기전에 무작위로 섞음
        shuffle(word)

        # 데이터베이스에 연결 및 테이블 생성
        try:
            db = sqlite3.connect('data.db')
            cur = db.cursor()
            
            # 입력받은 테이블이름으로 단어테이블 생성
            cur.execute(f'CREATE TABLE {name} (number int, words text, means text)')
            
            # 테이블에 단어 번호 매기면서 격납
            for i, (eng, kor) in enumerate(word, 1):
                cur.execute(f'INSERT INTO {name} (number, words, means) VALUES (?, ?, ?)', (i, eng, kor))
            
            db.commit()

            result.config(text = '성공적으로 만들어짐')

        except sqlite3.OperationalError as e:
            # 정한 이름의 테이블이 이미 존재할 경우
            if 'already exists' in str(e):
                result.config(text = '입력한 이름의 테이블이 이미 존재함. 테이블 이름을 다시 설정.')
                # print('입력한 이름의 테이블이 이미 존재함. 테이블 이름을 다시 설정.')
            # 그외 데이터베이스 작업 중 오류
            else:
                result.config(text = f'데이터베이스 작업 중 오류 발생: {e}')
                # print(f'데이터베이스 작업 중 오류 발생: {e}')

            return False

        finally:
            db.close()

        return True

    except FileNotFoundError:
        result.config(text = '텍스트 파일을 찾을 수 없습니다.')
        return False
    
    except IOError as e:
        result.config(text = f'파일을 읽는 중 오류 발생: {e}')
        # print(f'파일을 읽는 중 오류 발생: {e}')
        return False

# True시 문제없이 작동, False시 문제발생
# print(input_txt_output_database('L06_워마COMPLETE_ENG.txt', 'L06_워마COMPLETE_KOR.txt', 'L06_워마COMPLETE'))

root = tk.Tk()
root.title('텍스트파일 데이터베이스에 넣는 프로그램')
root.state('zoomed')
root.geometry('800x700')
root.option_add('*Font', '맑은고딕 20')

ex1 = tk.Label(text = '''
               텍스트 파일을 데이터베이스에 넣는 프로그램
               데이터베이스에 잘 들어가야만 프로그램이 잘 작동함

               영어 텍스트파일과 뜻 텍스트파일 두개를 words_txt라는 파일안에다가 둔 이후에 아래 빈칸에 입력
               ''')
ex1.pack()

tk.Label(text = '아래에 영어 텍스트 파일(.txt까지 입력) : ').pack()
en1 = tk.Entry(width = 30)
en1.pack()

tk.Label(text = '아래에 뜻 텍스트 파일(.txt까지 입력) : ').pack()
en2 = tk.Entry(width = 30)
en2.pack()

tk.Label(text = '''
         단어장 이름 짓기 : 
         (ex. L01_워마중등기초_800_ENG.txt 이게 영어파일이고
         L01_워마중등기초_800_KOR.txt 이게 뜻 파일이면
         아래 빈칸에는 L01_워마중등기초_800 등등)
         ''').pack()
en3 = tk.Entry(width = 30)
en3.pack()

result = tk.Label()
result.config(text = '')
result.config(fg = 'red')

tk.Label(text = '\n\n위의 3개의 빈칸을 다 채웠다면 아래의 실행 버튼 누르기').pack()

btn = tk.Button(root, text = '실행', command = partial(input_txt_output_database, en1, en2, en3, result))
btn.pack()

result.pack()

root.mainloop()