import tkinter as tk

from ui import LoginFrame, MenuFrame, TestFrame, ResultFrame, SettingsFrame
from db import create_users_table
from constants import Color

class App:
    def __init__(self):
        # 메인 Tk 객체
        self.root = tk.Tk()
        self.root.title("RoaD")
        self.root.minsize(1200, 700)
        self.root.state('zoomed')
        self.root.iconbitmap("resources/BI.ico")
        self.root.option_add("*Background", Color.GREY)
        self.root.option_add("*Foreground", Color.FONT_DEFAULT)

        # 모든 Frame을 담는 container
        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True)

        # Frame 초기화
        self.frames = {}
        for F in (LoginFrame, MenuFrame, TestFrame, ResultFrame, SettingsFrame):
            frame = F(container, self)     # Frame 생성, controller=self
            self.frames[F] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)  # 겹쳐 배치

        # 초기 화면
        self.show_frame(LoginFrame)

    def show_frame(self, frame_class):
        self.frames[frame_class].tkraise()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    create_users_table()
    app = App()
    app.run()