import json
import tkinter
from tkinter import ttk
import re


def replace(data, text):
    ret_text = ""
    for line in text.split('\n'):
        for r in re.finditer('[0-9]{5}', line):
            crn = r.group()
            try:
                ret_text += f'{crn}\t{data[crn]["course_title"]}\t{data[crn]["instructor"]}\n'
            except KeyError:
                ret_text += f"{crn}\tNo Data\n"
            except:
                ret_text += "Something terrible happened\n"
    return ret_text


def select_all(event):
    print('hi')
    event.widget.tag_add('sel', '1.0', 'end')


def get_replaced(data, text, message):
    # text_str = text.get("1.0", "end-1c")
    text = replace(data, text)
    message.configure(state='normal')
    message.delete('1.0', tkinter.END)
    message.insert('end', text)
    message.configure(state='disabled')


def copy(main, message):
    main.clipboard_clear()
    main.clipboard_append(message.get("1.0", "end-1c"))
    main.update()


if __name__ == '__main__':
    with open('data.json', 'r') as f:
        data = json.load(f)

    main = tkinter.Tk()
    ttk.Style().configure('button.TButton', foreground='black', backgroud='white')
    main.title = 'CRN - Replacer'
    main.geometry('800x400')
    text = tkinter.Text(main)
    text.place(x=0, y=0, width=400, height=350)
    text.bind('<Control-a>', select_all)
    text.bind('<Command-a>', select_all)
    text.bind('<Control-A>', select_all)
    text.bind('<Command-A>', select_all)
    message = tkinter.Text(main)
    message.insert('end', "Output will appear here!")
    message.configure(state='disabled')
    message.place(x=400, y=0, width=400, height=350)
    replace_button = ttk.Button(main, command=lambda: get_replaced(data, text.get("1.0", "end-1c"), message), text='Replace!', style='button.TButton')
    replace_button.place(x=0, y=350, width=400, height=50)
    # replace_button = tkinter.Button(main, highlightbackground='#3E4149', text='Replace!').place(x=0, y=350, width=400, height=50)
    copy_button = ttk.Button(main, command=lambda: copy(main, message), text='Copy to Clipboard', style='button.TButton')
    copy_button.place(x=400, y=350, width=400, height=50)
    main.mainloop()

