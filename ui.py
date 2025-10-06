import tkinter as tk

from constants import Color, Font
from utils import center_window

class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # 제목 라벨
        title_lbl = tk.Label(self, text="RoaD", font=Font.TITLE)
        title_lbl.pack(pady=(80, 0))

        # 버전 라벨
        version_lbl = tk.Label(self, text="version 2.0", font=Font.BODY)
        version_lbl.pack(pady=(0, 10))

        # 로그인 프레임
        login_frm = tk.Frame(self, bg=Color.DARK)
        login_frm.pack(expand=True)

        # ID 입력창
        username_ent = tk.Entry(
            login_frm,
            bg=Color.GREY,
            font=Font.ENTRY,
            fg=Color.FONT_ENTRY,
            justify='center',
            insertbackground=Color.FONT_ENTRY
            )
        username_ent.insert(0, 'Username')
        username_ent.bind('<FocusIn>', self.clear_placeholder)
        username_ent.bind("<FocusOut>", self.restore_placeholder)
        username_ent.bind('<Return>', self.login_enter)
        username_ent.pack(padx=80, pady=(60, 50))

        # 로그인 버튼
        login_btn = tk.Button(
            login_frm,
            text='Log in',
            font=Font.BUTTON,
            bg=Color.GREEN,
            width=17
            )
        login_btn.pack(pady=(0, 4))

        # 메시지 라벨
        self.message_lbl = tk.Label(
            login_frm,
            bg=Color.DARK,
            text='later',
            font=Font.CAPTION,
            fg=Color.FONT_WARNING
            )
        self.message_lbl.pack(pady=(0, 20))

        # or 라벨
        or_lbl = tk.Label(login_frm, bg=Color.DARK, text='OR', font=Font.BODY)
        or_lbl.pack(pady=(0, 10))

        # 계정관리 프레임
        account_frm = tk.Frame(login_frm, bg=Color.DARK)
        account_frm.grid_columnconfigure(0, weight=1, uniform='col')
        account_frm.grid_columnconfigure(1, weight=1, uniform='col')
        account_frm.pack(pady = (0, 40))

        # 회원가입 라벨
        signup_lbl = tk.Label(
            account_frm,
            bg=Color.DARK,
            text='Sign up',
            font=Font.CAPTION
            )
        signup_lbl.bind("<Button-1>", lambda e: self.open_signup_window())
        signup_lbl.grid(row=0, column=0, padx=(0, 30))

        # 계정삭제 라벨
        delaccount_lbl = tk.Label(
            account_frm,
            bg=Color.DARK,
            text='Delete account',
            font=Font.CAPTION
            )
        delaccount_lbl.bind("<Button-1>", lambda e: self.open_delaccount_window())
        delaccount_lbl.grid(row=0, column=1, padx=(30, 0))

    def clear_placeholder(self, event):
        if event.widget.get() == 'Username':
            event.widget.delete(0, len(event.widget.get()))

    def restore_placeholder(self, event):
        if event.widget.get() == "":
            event.widget.insert(0, 'Username')

    def login_enter(self, event):
        pass

    def open_signup_window(self):
        signup_window = tk.Toplevel(self, bg=Color.DARK)
        signup_window.title("Sign Up")
        signup_window.resizable(False, False)
        center_window(signup_window, 500, 420)

        # 타이틀
        title_lbl = tk.Label(signup_window, text='RoaD', font=Font.TITLE_SMALL, bg=Color.DARK)
        title_lbl.pack(pady=40)

        # 설명라벨
        explain_lbl = tk.Label(
            signup_window,
            text='Enter your ID',
            bg=Color.DARK,
            font=Font.EXPLAIN)
        explain_lbl.pack(pady=(0, 40))

        # ID 입력창
        username_ent = tk.Entry(signup_window,
            bg=Color.GREY,
            font=Font.ENTRY,
            fg=Color.FONT_ENTRY,
            justify='center',
            insertbackground=Color.FONT_ENTRY
            )
        username_ent.insert(0, 'Username')
        username_ent.bind('<FocusIn>', self.clear_placeholder)
        username_ent.pack(pady=(0, 4))

        # 오류메시지
        errormessage = tk.Label(
            signup_window,
            bg=Color.DARK,
            text='later',
            font=Font.CAPTION,
            fg=Color.FONT_WARNING
            )
        errormessage.pack(pady=(0, 16))

        # 계정 만들기 버튼
        signup_button = tk.Button(
            signup_window,
            text='Sign up',
            font=Font.BUTTON,
            bg=Color.GREEN,
            width=17
            )
        # signup_button.config(command = partial(signup, signup_root, id_entry, word_combobox, rootmessage, errormessage))
        signup_button.pack()

    def open_delaccount_window(self):
        delaccount_window = tk.Toplevel(self)
        delaccount_window.title("Delete Account")
        delaccount_window.resizable(False, False)
        center_window(delaccount_window, 450, 400)









class MenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#E0F7FA")
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        lbl_title = tk.Label(self, text="메뉴 화면", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=2, pady=(30, 10))

        btn_test = tk.Button(self, text="테스트 시작",
                             command=lambda: self.controller.show_frame(TestFrame))
        btn_test.grid(row=1, column=0, padx=20, pady=10)

        btn_settings = tk.Button(self, text="설정",
                                 command=lambda: self.controller.show_frame(SettingsFrame))
        btn_settings.grid(row=1, column=1, padx=20, pady=10)

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


class TestFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#FFF3E0")
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # 길이가 긴 텍스트 예시
        text = ("이것은 테스트 화면 예시입니다. 텍스트가 길면 자동으로 줄바꿈이 되도록 "
                "wraplength를 설정했습니다.")
        lbl_text = tk.Label(self, text=text, wraplength=400, justify="center")
        lbl_text.grid(row=0, column=0, columnspan=2, pady=30)

        btn_result = tk.Button(self, text="결과 보기",
                               command=lambda: self.controller.show_frame(ResultFrame))
        btn_result.grid(row=1, column=0, padx=20, pady=10)

        btn_menu = tk.Button(self, text="메뉴로 돌아가기",
                             command=lambda: self.controller.show_frame(MenuFrame))
        btn_menu.grid(row=1, column=1, padx=20, pady=10)

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


class ResultFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#E8F5E9")
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        lbl_title = tk.Label(self, text="결과 화면", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, pady=30)

        btn_menu = tk.Button(self, text="메뉴로 돌아가기",
                             command=lambda: self.controller.show_frame(MenuFrame))
        btn_menu.grid(row=1, column=0, pady=10)

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)


class SettingsFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#FBE9E7")
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        lbl_title = tk.Label(self, text="설정 화면", font=("Arial", 16, "bold"))
        lbl_title.grid(row=0, column=0, pady=30)

        btn_menu = tk.Button(self, text="메뉴로 돌아가기",
                             command=lambda: self.controller.show_frame(MenuFrame))
        btn_menu.grid(row=1, column=0, pady=10)

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
