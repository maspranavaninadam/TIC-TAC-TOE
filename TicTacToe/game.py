import tkinter as tk
from random import randint


def computergame():

    pass
# i will add this later


def multiplayergame():


    def msg(keys, button_states):
        val = "O" if turn is True else "X"
        win = tk.Label(multiplayergame.root, text="Winner is " + val, font="Helvetica 36 bold italic", fg="red")
        win.place(relx=0.3, rely=0.9)
        game_exit = tk.Button(multiplayergame.root, text="exit", font="Helvetica 18 bold italic", fg="black",
                              bg="red", command=multiplayergame.root.destroy)
        game_exit.place(relx=0.8, rely=0.9)
        for i in keys:
            if button_states[i] == "":
                v = i.place_info()
                temp = tk.Button(frame)
                temp.place(relx=v["relx"], rely=v["rely"], relheight=v["relheight"], relwidth=v["relwidth"])

    def check_winner():
        global button_states

        keys = list(button_states.keys())

        if button_states[keys[0]] == button_states[keys[1]] == button_states[keys[2]] != "":
            msg(keys, button_states)
        elif button_states[keys[3]] == button_states[keys[4]] == button_states[keys[5]] != "":
            msg(keys, button_states)
        elif button_states[keys[6]] == button_states[keys[7]] == button_states[keys[8]] != "":
            msg(keys, button_states)
        elif button_states[keys[0]] == button_states[keys[3]] == button_states[keys[6]] != "":
            msg(keys, button_states)
        elif button_states[keys[1]] == button_states[keys[4]] == button_states[keys[7]] != "":
            msg(keys, button_states)
        elif button_states[keys[2]] == button_states[keys[5]] == button_states[keys[8]] != "":
            msg(keys, button_states)
        elif button_states[keys[0]] == button_states[keys[4]] == button_states[keys[8]] != "":
            msg(keys, button_states)
        elif button_states[keys[2]] == button_states[keys[4]] == button_states[keys[6]] != "":
            msg(keys, button_states)
        else:
            for i in keys:
                if button_states[i] != "":
                    continue
                else:
                    break
            else:
                win = tk.Label(multiplayergame.root, text="That's a draw", font="Helvetica 36 bold italic", fg="red")
                win.place(relx=0.28, rely=0.9)
                game_exit = tk.Button(multiplayergame.root, text="exit", font="Helvetica 18 bold italic", fg="black",
                                      bg="red", command=multiplayergame.root.destroy)
                game_exit.place(relx=0.8, rely=0.9)

    def get_symbol(bname):
        global turn, button_states
        v = bname.place_info()
        l = tk.Button(frame, text="X" if turn is True else "O", font="Helvetica 80", bg="#f06f69" if turn is
                                                                                                     True else "#8b9dc3")
        l.place(relx=v["relx"], rely=v["rely"], relheight=v["relheight"], relwidth=v["relwidth"])
        turn = not turn
        button_states[bname] = l.cget("text")
        check_winner()

    height = 500
    width = 600

    multiplayergame.root = tk.Tk()
    multiplayergame.root.title("TIC TAC TOE Multiplayer")

    print(multiplayergame.root.winfo_exists())
    # game.multi_button.pressed = False

    canvas = tk.Canvas(multiplayergame.root, height=height, width=width)
    canvas.pack()

    frame = tk.Frame(multiplayergame.root, bg='black', bd=10, cursor="dot")
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.75, anchor='n')

    global turn
    turn = True

    global button_states
    button_states = {}

    button1 = tk.Button(frame, command=lambda: get_symbol(button1))
    button_states[button1] = ""
    button1.place(relx=0, relheight=0.33, relwidth=0.33)

    button2 = tk.Button(frame, command=lambda: get_symbol(button2))
    button_states[button2] = ""
    button2.place(relx=0.33, relheight=0.33, relwidth=0.33)

    button3 = tk.Button(frame, command=lambda: get_symbol(button3))
    button_states[button3] = ""
    button3.place(relx=0.66, relheight=0.33, relwidth=0.33)

    button4 = tk.Button(frame, command=lambda: get_symbol(button4))
    button_states[button4] = ""
    button4.place(relx=0, rely=0.33, relheight=0.33, relwidth=0.33)

    button5 = tk.Button(frame, command=lambda: get_symbol(button5))
    button_states[button5] = ""
    button5.place(relx=0.33, rely=0.33, relheight=0.33, relwidth=0.33)

    button6 = tk.Button(frame, command=lambda: get_symbol(button6))
    button_states[button6] = ""
    button6.place(relx=0.66, rely=0.33, relheight=0.33, relwidth=0.33)

    button7 = tk.Button(frame, command=lambda: get_symbol(button7))
    button_states[button7] = ""
    button7.place(relx=0, rely=0.66, relheight=0.33, relwidth=0.33)

    button8 = tk.Button(frame, command=lambda: get_symbol(button8))
    button_states[button8] = ""
    button8.place(relx=0.33, rely=0.66, relheight=0.33, relwidth=0.33)

    button9 = tk.Button(frame, command=lambda: get_symbol(button9))
    button_states[button9] = ""
    button9.place(relx=0.66, rely=0.66, relheight=0.33, relwidth=0.33)

    multiplayergame.root.minsize(600, 600)
    multiplayergame.root.maxsize(800, 800)

    multiplayergame.root.mainloop()


def game():
    if button.pressed is True:
        return
    button.pressed = True
    msg = tk.Label(main_frame, text="Select Your Choice", fg="#f3f2f1", bg="#1f2f3f", font="Helvetica 32 italic")
    msg.pack()
    comp_button = tk.Button(main_frame, text="Computer", bg="#f3f2f1", fg="#1f2f3f", font="Helvetica 18 bold "
                                                                                          "italic", width=20,
                            command=computergame)
    comp_button.pack()
    game.multi_button = tk.Button(main_frame, text="Multiplayer", bg="#f3f2f1", fg="#1f2f3f", font="Helvetica 18 bold "
                                                                                                   "italic", width=20,
                                  command=multiplayergame)
    game.multi_button.pack()
    game.multi_button.pressed = False


main_root = tk.Tk()
main_root.title("TIC TAC TOE")
main_root.minsize(500, 500)
main_root.maxsize(600, 600)

main_frame = tk.Frame(main_root, bg="#1f2f3f")
main_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.75, anchor='n')

welcome = tk.Label(main_frame, text="WELCOME !", fg="#f3f2f1", bg="#1f2f3f", font="Helvetica 38 bold italic",
                   width="20")
welcome.pack()

button = tk.Button(main_frame, text="Play", bg="#f3f2f1", fg="#1f2f3f", font="Helvetica 18 bold italic", width=15,
                   command=game)
button.pack()
button.pressed = False

button_exit = tk.Button(main_frame, text="Exit", bg="#f3f2f1", fg="#1f2f3f", font="Helvetica 18 bold italic", width=15,
                        command=main_root.destroy)
button_exit.pack()

main_root.mainloop()
