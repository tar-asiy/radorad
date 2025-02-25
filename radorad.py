#!/usr/bin/env python3
import os
import json
import math
import random
import colorsys
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

##################################
# 1. CHOOSING LANGUAGE, MESSAGES
##################################

def choose_language():
    print("Please select language / Bitte Sprache wählen / Будь ласка, оберіть мову:")
    print("1) English\n2) Deutsch\n3) Українська")
    c = input("Enter 1/2/3: ").strip()
    if c=="1":
        return "en"
    elif c=="2":
        return "de"
    else:
        return "uk"

def get_messages(lang):
    if lang=="en":
        return {
            "intro": "=== Welcome to Radorad: create or load a dictionary for a 3-level wheel ===",
            "ask_mode": "What do you want to do?\n1) Load an existing dictionary\n2) Create a new dictionary",
            "mode_load": "Load existing dictionary selected.",
            "mode_create": "Create new dictionary selected.",
            "saved_dict": "Dictionary saved to",
            "build_wheel": "Now generating the wheel...",
            "no_file": "No file selected. Exiting.",
            "no_data": "No dictionary data, exiting.",
            "no_rings": "No data in rings[0], exiting.",

            "root_full_overview": "=== FULL DICTIONARY OVERVIEW (root) ===",
            "root_commands": "Root commands: go X, a (add new 1st-level), view N (1..3), done",
            "item_commands": "Item commands: r (rename), a (add), d (delete), done (back to root), go X",
            "invalid_cmd": "Unknown command.",
            "choose_name": "Enter name for this item (empty=skip):",
            "choose_color": "Choose a color or 'random': ",
            "invalid_color": "Invalid color index, using random.",
            "random_chosen": "Random color chosen: ",
            "colors_available": "Colors available:",
            "cannot_rename_root": "Cannot rename root, ignored.",
            "cannot_delete_root": "Cannot delete root, ignored.",
            "fourth_level_forbidden": "Cannot add a sub here: that would create a 4th level, which is not supported.",
            "renamed": "Renamed.",
            "deleted": "Item deleted. Returning to root.",
            "done_item": "Returning to root.",
            "finish_editing": "Finished editing. Now saving...",
            "invalid_path": "Invalid path. Try again.",

            "current_item": "Current item: ",
            "view_updated": "Root view depth updated to"
        }
    elif lang=="de":
        return {
            "intro": "=== Willkommen bei Radorad: Erstellen oder Laden eines Wörterbuchs für ein dreistufiges Rad ===",
            "ask_mode": "Was möchten Sie tun?\n1) Vorhandenes Wörterbuch laden\n2) Neues Wörterbuch erstellen",
            "mode_load": "Bestehendes Wörterbuch laden ausgewählt.",
            "mode_create": "Neues Wörterbuch erstellen ausgewählt.",
            "saved_dict": "Wörterbuch gespeichert in",
            "build_wheel": "Erzeuge nun das Rad...",
            "no_file": "Keine Datei gewählt. Beende.",
            "no_data": "Keine Wörterbuchdaten, beende.",
            "no_rings": "Keine Daten in rings[0], beende.",

            "root_full_overview": "=== KOMPLETTE ÜBERSICHT (Root) ===",
            "root_commands": "Root-Befehle: go X, a (neues 1. Level), view N (1..3), done",
            "item_commands": "Item-Befehle: r (rename), a (add), d (delete), done (zurück zu Root), go X",
            "invalid_cmd": "Unbekannter Befehl.",
            "choose_name": "Name für dieses Element (leer=Abbruch):",
            "choose_color": "Wählen Sie eine Farbe oder 'random': ",
            "invalid_color": "Ungültiger Farbindex, verwende random.",
            "random_chosen": "Zufällige Farbe gewählt: ",
            "colors_available": "Verfügbare Farben:",
            "cannot_rename_root": "Kann Root nicht umbenennen, ignoriert.",
            "cannot_delete_root": "Kann Root nicht löschen, ignoriert.",
            "fourth_level_forbidden": "4. Ebene nicht unterstützt.",
            "renamed": "Umbenannt.",
            "deleted": "Element gelöscht. Zurück zu Root.",
            "done_item": "Zurück zu Root.",
            "finish_editing": "Bearbeitung beendet. Speichere...",
            "invalid_path": "Ungültiger Pfad. Versuchen Sie es erneut.",

            "current_item": "Aktuelles Element: ",
            "view_updated": "Root-Ansichtstiefe geändert auf"
        }
    else:
        return {
            "intro": "=== Ласкаво просимо до Радорад: створити або завантажити словничок для трирівневого колеса ===",
            "ask_mode": "Що бажаєте зробити?\n1) Завантажити наявний словничок\n2) Створити новий словничок",
            "mode_load": "Обрано: завантажити наявний словничок.",
            "mode_create": "Обрано: створити новий словничок.",
            "saved_dict": "Словничок збережено у",
            "build_wheel": "Зараз будуємо колесо...",
            "no_file": "Файл не обрано. Вихід.",
            "no_data": "Немає даних словничка, вихід.",
            "no_rings": "Немає даних у rings[0], вихід.",

            "root_full_overview": "=== ПОВНИЙ ОГЛЯД СЛОВНИЧКА (root) ===",
            "root_commands": "Команди кореня: go X, a (додати 1-й рівень), view N (1..3), done",
            "item_commands": "Команди елемента: r (rename), a (add), d (delete), done (назад у root), go X",
            "invalid_cmd": "Невідома команда.",
            "choose_name": "Введіть назву для цього елемента (порожньо=скасувати):",
            "choose_color": "Оберіть колір або 'random': ",
            "invalid_color": "Невірний індекс кольору, використовую випадковий.",
            "random_chosen": "Випадковий колір: ",
            "colors_available": "Доступні кольори:",
            "cannot_rename_root": "Неможливо перейменувати root, ігноруємо.",
            "cannot_delete_root": "Неможливо вилучити root, ігноруємо.",
            "fourth_level_forbidden": "Не можна додати 4-й рівень.",
            "renamed": "Перейменовано.",
            "deleted": "Елемент вилучено. Повертаємося у root.",
            "done_item": "Повернення у root.",
            "finish_editing": "Редагування завершено. Зберігаємо...",
            "invalid_path": "Невірний шлях. Спробуйте ще раз.",

            "current_item": "Поточний елемент: ",
            "view_updated": "Глибину відображення кореня змінено на"
        }

##################################
# 2. COLOR DATA (rainbow)
##################################

BASE_COLORS = [
    {
        "hex": "#FFD300",
        "en": "Golden Yellow",
        "de": "Goldgelb",
        "uk": "Золотаво-жовтий"
    },
    {
        "hex": "#FA8C00",
        "en": "Orange",
        "de": "Orange",
        "uk": "Помаранчевий"
    },
    {
        "hex": "#CCAA55",
        "en": "Sandy Brown",
        "de": "Sandbraun",
        "uk": "Піщано-коричневий"
    },
    {
        "hex": "#77AAFF",
        "en": "Sky Blue",
        "de": "Himmelblau",
        "uk": "Небесно-блакитний"
    },
    {
        "hex": "#2E64FE",
        "en": "Azure",
        "de": "Azurblau",
        "uk": "Азуровий"
    },
    {
        "hex": "#8B41D9",
        "en": "Deep Purple",
        "de": "Tiefes Lila",
        "uk": "Глибоко-фіолетовий"
    },
    {
        "hex": "#CC66CC",
        "en": "Soft Magenta",
        "de": "Weiches Magenta",
        "uk": "М'яка пурпурова"
    },
    {
        "hex": "#CC6699",
        "en": "Pinkish",
        "de": "Rosig",
        "uk": "Рожевуватий"
    },
    {
        "hex": "#CC6666",
        "en": "Mellow Red",
        "de": "Mildes Rot",
        "uk": "Приглушено-червоний"
    },
    {
        "hex": "#66CCCC",
        "en": "Aqua",
        "de": "Aqua",
        "uk": "Аква"
    },
    {
        "hex": "#66CC99",
        "en": "Greenish",
        "de": "Grünlich",
        "uk": "Зелений-відтінок"
    },
    {
        "hex": "#CC9966",
        "en": "Tan",
        "de": "Hellbraun",
        "uk": "Світло-коричневий"
    }
]


def color_name_for_hex(h, lang):
    if not h:
        return ""
    h2=h.lower()
    for c in BASE_COLORS:
        if c["hex"].lower()==h2:
            return c.get(lang,"???")
    return "???"

##################################
# 3. PRINTING DICTIONARY with depth
##################################

def print_full_dictionary(ring1, lang, max_depth=3):
    """
    Print dictionary with indentation up to max_depth.
    level=0 => 1st-level, level=1 => 2nd-level, etc.
    """
    def recurse(items, level=0, path=""):
        if level>=max_depth:
            return
        indent="  "*level
        for i, it in enumerate(items, start=1):
            new_path=path+("."+str(i) if path else str(i))
            # if level=0 => 1st-level => show color
            c=""
            if level==0:
                col=it.get("color","")
                c2=color_name_for_hex(col, lang)
                if c2:
                    c=" ("+c2+")"
            print(f"{indent}{new_path}. {it['word']}{c}")
            sub=it.get("sub",[])
            if sub:
                recurse(sub, level+1, new_path)
    recurse(ring1,0,"")

##################################
# PATH UTILS
##################################

def path_depth(path):
    if not path:
        return 0
    return len(path.split("."))

def get_item_by_path(ring1, path):
    if not path:
        return None,None,None
    if path=="0":
        return None,None,None
    parts=path.split(".")
    current=ring1
    item=None
    parent=None
    parent_idx=None
    try:
        for p in parts:
            i=int(p)-1
            if i<0 or i>=len(current):
                return None,None,None
            item=current[i]
            parent=current
            parent_idx=i
            current=item.get("sub",[])
        return item, parent, parent_idx
    except:
        return None,None,None

def get_sublist_by_path(ring1, path):
    if not path or path=="0":
        return ring1
    parts=path.split(".")
    cur=ring1
    try:
        for p in parts:
            i=int(p)-1
            if i<0 or i>=len(cur):
                return None
            it=cur[i]
            cur=it.get("sub",[])
        return cur
    except:
        return None

##################################
# 4. SHOW subtree of current item
##################################

def show_current_item_and_subtree(ring1, path, msgs, lang):
    """
    Print "Current item: <path> => <word> (color if 1-lvl)"
    Then print full subtree with indentation
    """
    item, parent, idx = get_item_by_path(ring1, path)
    if not item:
        return
    # build line
    line = f"{msgs['current_item']}{path} => {item['word']}"
    d=path_depth(path)
    if d==1:
        col = item.get("color","")
        coln=color_name_for_hex(col, lang)
        if coln:
            line+= f" ({coln})"
    print(line)
    # now show subtree
    def recurse(items, level=1, p=path):
        indent="  "*level
        for i, it in enumerate(items, start=1):
            new_p = p+"."+str(i)
            print(f"{indent}{new_p}. {it['word']}")
            s=it.get("sub",[])
            if s:
                recurse(s, level+1, new_p)
    sub=item.get("sub",[])
    if sub:
        recurse(sub,1,path)

##################################
# 5. EDITING: rename, add, delete
##################################

def cmd_rename(ring1, path, msgs, lang):
    if not path or path=="0":
        print(msgs["cannot_rename_root"])
        return
    item, parent, idx=get_item_by_path(ring1,path)
    if not item:
        print(msgs["invalid_path"])
        return
    newname=input(msgs["choose_name"]+": ").strip()
    if newname:
        item["word"]=newname
        print(msgs["renamed"])
    d=path_depth(path)
    if d==1:
        # re-pick color
        print(msgs["colors_available"])
        for i,c in enumerate(BASE_COLORS, start=1):
            cname=c.get(lang,"???")
            print(f"   {i}) {cname}")
        color_choice=input(msgs["choose_color"]).strip().lower()
        if color_choice=="random":
            co=random.choice(BASE_COLORS)
            print(msgs["random_chosen"]+ co[lang])
            item["color"]=co["hex"]
        elif color_choice.isdigit():
            i2=int(color_choice)
            if i2<1 or i2> len(BASE_COLORS):
                print(msgs["invalid_color"])
                co2=random.choice(BASE_COLORS)
                print(msgs["random_chosen"]+co2[lang])
                item["color"]=co2["hex"]
            else:
                cobj=BASE_COLORS[i2-1]
                item["color"]=cobj["hex"]
        else:
            print(msgs["invalid_color"])
            co3=random.choice(BASE_COLORS)
            print(msgs["random_chosen"]+co3[lang])
            item["color"]=co3["hex"]

def cmd_delete(ring1, path, msgs):
    if not path or path=="0":
        print(msgs["cannot_delete_root"])
        return
    item, parent, idx = get_item_by_path(ring1, path)
    if item is None or parent is None:
        print(msgs["invalid_path"])
        return
    parent.pop(idx)
    print(msgs["deleted"])

def cmd_add(ring1, path, msgs, lang):
    d=path_depth(path)
    if d>=3:
        print(msgs["fourth_level_forbidden"])
        return
    if not path or path=="0":
        # add 1-lvl
        nm=input(msgs["choose_name"]+": ").strip()
        if not nm:
            return
        print(msgs["colors_available"])
        for i,c in enumerate(BASE_COLORS, start=1):
            cname=c.get(lang,"???")
            print(f"   {i}) {cname}")
        colchoice=input(msgs["choose_color"]).strip().lower()
        if colchoice=="random":
            co=random.choice(BASE_COLORS)
            print(msgs["random_chosen"]+co[lang])
            hx=co["hex"]
        elif colchoice.isdigit():
            i2=int(colchoice)
            if i2<1 or i2> len(BASE_COLORS):
                print(msgs["invalid_color"])
                co2=random.choice(BASE_COLORS)
                print(msgs["random_chosen"]+co2[lang])
                hx=co2["hex"]
            else:
                cobj=BASE_COLORS[i2-1]
                hx=cobj["hex"]
        else:
            print(msgs["invalid_color"])
            co3=random.choice(BASE_COLORS)
            print(msgs["random_chosen"]+co3[lang])
            hx=co3["hex"]
        ring1.append({"word":nm,"color":hx,"sub":[]})
    else:
        subl=get_sublist_by_path(ring1,path)
        if subl is None:
            print(msgs["invalid_path"])
            return
        nm=input(msgs["choose_name"]+": ").strip()
        if not nm:
            return
        subl.append({"word":nm,"sub":[]})

##################################
# 6. EDITING LOOP
##################################

def editing_loop(ring1, msgs, lang):
    """
    root => shows dictionary up to root_view_depth, commands: go X, a, view N, done
    item => show item + entire subtree, commands: r, a, d, done, go X
    'go 0' => root
    """
    current_path=""
    root_view_depth=3  # default = show all 3 levels
    while True:
        if not current_path:
            # root
            print(msgs["root_full_overview"])
            print_full_dictionary(ring1, lang, max_depth=root_view_depth)
            print(msgs["root_commands"])
            cmd = input("> ").strip().lower()
            if cmd.startswith("go "):
                p_ = cmd[3:].strip()
                if p_=="0":
                    # go root => no op
                    continue
                it, pr, idx= get_item_by_path(ring1, p_)
                if it is None and p_:
                    print(msgs["invalid_path"])
                else:
                    current_path=p_
            elif cmd=="a":
                cmd_add(ring1,"",msgs,lang)
            elif cmd=="done":
                print(msgs["finish_editing"])
                return
            elif cmd.startswith("view "):
                # parse depth
                d_str=cmd[5:].strip()
                try:
                    d_val=int(d_str)
                    if d_val<1:
                        d_val=1
                    elif d_val>3:
                        d_val=3
                    root_view_depth=d_val
                    print(f"{msgs['view_updated']} {root_view_depth}")
                except:
                    print(msgs["invalid_cmd"])
            else:
                print(msgs["invalid_cmd"])
        else:
            # we are in some item
            if current_path=="0":
                current_path=""
                continue
            it, pr, idx= get_item_by_path(ring1, current_path)
            if not it:
                current_path=""
                continue
            # show item + subtree
            show_current_item_and_subtree(ring1, current_path, msgs, lang)
            print(msgs["item_commands"])
            cmd=input("> ").strip().lower()
            if cmd=="r":
                cmd_rename(ring1, current_path, msgs, lang)
            elif cmd=="a":
                dp=path_depth(current_path)
                if dp>=3:
                    print(msgs["fourth_level_forbidden"])
                else:
                    cmd_add(ring1, current_path, msgs, lang)
            elif cmd=="d":
                cmd_delete(ring1, current_path, msgs)
                current_path=""
            elif cmd=="done":
                current_path=""
                print(msgs["done_item"])
            elif cmd.startswith("go "):
                p2=cmd[3:].strip()
                if p2=="0":
                    current_path=""
                else:
                    i2,pr2,ix2= get_item_by_path(ring1,p2)
                    if i2 is None and p2:
                        print(msgs["invalid_path"])
                    else:
                        current_path=p2
            else:
                print(msgs["invalid_cmd"])

##################################
# 7. WHEEL DRAWING
##################################

def ring_thickness(level):
    return 1.0 if level==1 else 3.0

def draw_sector_custom(ax, face_color, edge_color, inner_r, outer_r, theta1, theta2, line_w=0.5):
    wedge=mpatches.Wedge((0,0),r=outer_r,
                         theta1=theta1,theta2=theta2,
                         width=(outer_r-inner_r),
                         facecolor=face_color,
                         edgecolor=None,linewidth=0)
    ax.add_patch(wedge)
    outer_arc=mpatches.Arc((0,0),2*outer_r,2*outer_r,angle=0,
                           theta1=theta1,theta2=theta2,
                           color=edge_color,linewidth=line_w)
    ax.add_patch(outer_arc)
    inner_arc=mpatches.Arc((0,0),2*inner_r,2*inner_r,angle=0,
                           theta1=theta1,theta2=theta2,
                           color=edge_color,linewidth=line_w)
    ax.add_patch(inner_arc)
    rad_angle=math.radians(theta2)
    x_in=inner_r*math.cos(rad_angle)
    y_in=inner_r*math.sin(rad_angle)
    x_out=outer_r*math.cos(rad_angle)
    y_out=outer_r*math.sin(rad_angle)
    ax.plot([x_in,x_out],[y_in,y_out],color=edge_color,linewidth=line_w)

def count_leaves(item):
    sub=item.get("sub",[])
    if not sub:
        return 1
    s=0
    for c in sub:
        s+=count_leaves(c)
    return s

def lighten_towards_white(hex_color, alpha):
    if not hex_color:
        return "#FFFFFF"
    h2=hex_color.lstrip('#')
    r=int(h2[0:2],16)
    g=int(h2[2:4],16)
    b=int(h2[4:6],16)
    nr=int(r+(255-r)*alpha)
    ng=int(g+(255-g)*alpha)
    nb=int(b+(255-b)*alpha)
    return "#{:02X}{:02X}{:02X}".format(nr,ng,nb)

def darken_color_hls(hex_color,delta=0.2):
    if not hex_color:
        return "#FFFFFF"
    h2=hex_color.lstrip('#')
    r=int(h2[0:2],16)
    g=int(h2[2:4],16)
    b=int(h2[4:6],16)
    rf,gf,bf=r/255,g/255,b/255
    h,l,s=colorsys.rgb_to_hls(rf,gf,bf)
    l=max(0,l-delta)
    rd,gd,bd=colorsys.hls_to_rgb(h,l,s)
    return "#{:02X}{:02X}{:02X}".format(int(rd*255),
                                       int(gd*255),
                                       int(bd*255))

def draw_nested(ax, items, level, inner_r, start_angle, end_angle, parent_color=None):
    if not items:
        return
    total_leaves=sum(count_leaves(it) for it in items)
    if total_leaves<=0:
        return
    angle_range=end_angle-start_angle
    current_start=start_angle
    this_width=ring_thickness(level)
    outer_r=inner_r+this_width

    # Lighten factor
    if level==1:
        alpha=0.0
    elif level==2:
        alpha=0.3
    else:
        alpha=0.7

    for item in items:
        sub_leaves=count_leaves(item)
        frac=sub_leaves/float(total_leaves)
        seg_angle=angle_range*frac
        seg_start=current_start
        seg_end=seg_start+seg_angle
        current_start=seg_end

        base_col=item.get("color", parent_color) or "#FFFFFF"
        face_col=lighten_towards_white(base_col,alpha)
        edge_col=darken_color_hls(face_col,0.2)

        draw_sector_custom(ax,face_col,edge_col,
                           inner_r,outer_r,
                           seg_start,seg_end,0.3)

        mid_angle_deg=(seg_start+seg_end)/2
        mid_angle_rad=math.radians(mid_angle_deg)
        if level==1:
            text_radius_factor=0.45
            txt_angle=mid_angle_deg-90
        else:
            text_radius_factor=0.5
            txt_angle=mid_angle_deg

        r_text=inner_r+(outer_r-inner_r)*text_radius_factor
        x_text=r_text*math.cos(mid_angle_rad)
        y_text=r_text*math.sin(mid_angle_rad)
        ax.text(x_text,y_text,item["word"],
                ha='center',va='center',
                rotation=txt_angle,rotation_mode='anchor',
                fontsize=3,color='black')

        subitems=item.get("sub",[])
        if subitems:
            draw_nested(ax, subitems,
                        level+1,
                        outer_r, seg_start, seg_end,
                        base_col)

def build_and_show_wheel(ring1):
    fig, ax=plt.subplots(figsize=(11.69,16.54), dpi=300)
    ax.set_aspect("equal")
    ax.axis("off")
    draw_nested(ax, ring1, level=1,
                inner_r=1.0,
                start_angle=90,
                end_angle=450,
                parent_color=None)
    ax.set_xlim(-9,9)
    ax.set_ylim(-9,9)
    plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
    plt.show()

##################################
# MAIN
##################################

def main():
    lang=choose_language()
    msgs=get_messages(lang)
    print(msgs["intro"])

    print(msgs["ask_mode"])
    m=input("Enter 1/2: ").strip()
    script_dir=os.path.dirname(os.path.abspath(__file__))

    if m=="1":
        print(msgs["mode_load"])
        root=tk.Tk()
        root.withdraw()
        f=filedialog.askopenfilename(
            title="Select a dictionary file",
            initialdir=script_dir,
            filetypes=[("Dictionary files","*.json"),("All files","*.*")]
        )
        if not f:
            print(msgs["no_file"])
            return
        with open(f,"r",encoding="utf-8") as ff:
            data=json.load(ff)
        ring1=data["rings"][0]
    else:
        print(msgs["mode_create"])
        data={"rings":[[]]}
        ring1=data["rings"][0]

    editing_loop(ring1, msgs, lang)

    # save
    root=tk.Tk()
    root.withdraw()
    save=filedialog.asksaveasfilename(
        title="Save dictionary",
        initialdir=script_dir,
        defaultextension=".json",
        filetypes=[("Dictionary files","*.json"),("All files","*.*")]
    )
    if save:
        with open(save,"w",encoding="utf-8") as ff:
            json.dump(data,ff,ensure_ascii=False,indent=2)
        print(f"{msgs['saved_dict']} {save}")
    else:
        print("User canceled saving dictionary.")

    if not ring1:
        print(msgs["no_rings"])
        return
    print(msgs["build_wheel"])
    build_and_show_wheel(ring1)

if __name__=="__main__":
    main()
