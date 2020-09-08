"""
File: my_drawing
Name:Sharon
----------------------
身為忠實的萊恩迷 當然要來招收信徒♥
他們是韓國通訊軟體 Kakao talk 裡面的吉祥物
Ryan是一隻沒有鬃毛的獅子，會面無表情做一些很萌的動作
Tube是一隻膽小的鴨子，但是生氣的話會變成綠色的
Apeach則是一顆古靈精怪的桃子
啊他們總共有8個角色，但我畫完三個就累了．．．所以就先這樣XD

"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GArc, GPolygon
from campy.graphics.gwindow import GWindow

window = GWindow(950, 600, title='Kakao Friends;)')


def main():
    bg = GRect(950, 600)
    window.add(bg)
    bg.color = 'lightblue'
    bg.fill_color = 'lightblue'
    ryan()
    tube()
    peach()
    title = GLabel('KAKAO FRIENDS')
    title.color = 'cornflowerblue'
    title.font = 'Verdana-50-bold'
    window.add(title, x=255, y=500)
    title2 = GLabel('KAKAO FRIENDS')
    title2.color = 'ivory'
    title2.font = 'Verdana-50-bold'
    window.add(title2, x=251, y=500)


def ryan():
    r_face = GOval(200, 175)
    window.add(r_face, x=100, y=150)
    r_face.color = 'peru'
    r_face.fill_color = 'peru'
    r_l_ear = GOval(50, 55)
    window.add(r_l_ear, x=93, y=165)
    r_l_ear.color = 'peru'
    r_l_ear.fill_color = 'peru'
    r_r_ear = GOval(50, 55)
    window.add(r_r_ear, x=253, y=165)
    r_r_ear.color = 'peru'
    r_r_ear.fill_color = 'peru'

    r_l_brow = GRect(35, 5)
    window.add(r_l_brow, x=140, y=210)
    r_l_brow.filled = 1
    r_r_brow = GRect(35, 5)
    window.add(r_r_brow, x=225, y=210)
    r_r_brow.filled = 1
    r_l_eye = GOval(12, 12)
    window.add(r_l_eye, x=150, y=230)
    r_l_eye.filled = 1
    r_r_eye = GOval(12, 12)
    window.add(r_r_eye, x=235, y=230)
    r_r_eye.filled = 1

    r_nose1 = GOval(35, 30)
    r_nose1.color = 'ivory'
    r_nose1.filled = True
    r_nose1.fill_color = 'ivory'
    window.add(r_nose1, x=173, y=250)
    r_nose2 = GOval(35, 30)
    r_nose2.color = 'ivory'
    r_nose2.filled = True
    r_nose2.fill_color = 'ivory'
    window.add(r_nose2, x=197, y=250)
    r_nose3 = GOval(20, 15)
    r_nose3.filled = True
    window.add(r_nose3, x=193, y=245)
    ryan_name = GLabel('RYAN')
    ryan_name.font = 'Verdana-30-bold'
    window.add(ryan_name, x=155, y=380)


def tube():
    t_face = GOval(190, 160)
    window.add(t_face, x=380, y=150)
    t_face.color = 'ivory'
    t_face.fill_color = 'ivory'
    t_l_cheek = GOval(25, 15)
    window.add(t_l_cheek, x=400, y=232)
    t_l_cheek.color = 'lightpink'
    t_l_cheek.fill_color = 'lightpink'
    t_r_cheek = GOval(25, 15)
    window.add(t_r_cheek, x=510, y=232)
    t_r_cheek.color = 'lightpink'
    t_r_cheek.fill_color = 'lightpink'

    t_mouth1 = GRect(160, 20)
    window.add(t_mouth1, x=380, y=255)
    t_mouth1.color = 'gold'
    t_mouth1.fill_color = 'gold'
    t_mouth2 = GRect(150, 20)
    window.add(t_mouth2, x=390, y=275)
    t_mouth2.color = 'gold'
    t_mouth2.fill_color = 'gold'
    t_mouth3 = GOval(20, 20)
    window.add(t_mouth3, x=375, y=255)
    t_mouth3.color = 'gold'
    t_mouth3.fill_color = 'gold'
    t_mouth4 = GOval(20, 20)
    window.add(t_mouth4, x=380, y=275)
    t_mouth4.color = 'gold'
    t_mouth4.fill_color = 'gold'
    t_mouth5 = GOval(40, 40)
    window.add(t_mouth5, x=520, y=255)
    t_mouth5.color = 'gold'
    t_mouth5.fill_color = 'gold'
    t_mouth6 = GLine(385, 275, 535, 275)
    window.add(t_mouth6)
    t_mouth6.color = 'mustardyellow'

    t_nose1 = GOval(35, 32)
    window.add(t_nose1, x=450, y=240)
    t_nose1.color = 'gold'
    t_nose1.fill_color = 'gold'
    t_nose2 = GOval(4, 5)
    window.add(t_nose2, x=462, y=247)
    t_nose2.filled = True
    t_nose3 = GOval(4, 5)
    window.add(t_nose3, x=469, y=247)
    t_nose3.filled = True

    t_l_eye = GOval(10, 10)
    t_l_eye.filled = True
    window.add(t_l_eye, x=425, y=215)
    t_r_eye = GOval(10, 10)
    t_r_eye.filled = True
    window.add(t_r_eye, x=500, y=215)
    t_l_eye_2 = GArc(30, 12, 0, 200)
    t_l_eye_2.filled = True
    window.add(t_l_eye_2, x=415, y=195)
    t_r_eye_2 = GArc(30, 12, 0, 200)
    t_r_eye_2.filled = True
    window.add(t_r_eye_2, x=490, y=195)
    tube_name = GLabel('TUBE')
    tube_name.font = 'Verdana-30-bold'
    window.add(tube_name, x=430, y=380)


def peach():
    p_face1 = GPolygon()
    p_face1.add_vertex((750, 155))
    p_face1.add_vertex((670, 225))
    p_face1.add_vertex((835, 210))
    window.add(p_face1)
    p_face1.color = 'peach'
    p_face1.fill_color = 'peach'
    p_face2 = GOval(190, 140)
    window.add(p_face2, x=665, y=180)
    p_face2.color = 'peach'
    p_face2.fill_color = 'peach'

    p_l_eye = GOval(30, 30)
    window.add(p_l_eye, x=705, y=215)
    p_l_eye.filled = True
    p_l_eye.fill_color = 'darkgray2'
    p_l_eye2 = GOval(12, 12)
    window.add(p_l_eye2, x=708, y=220)
    p_l_eye2.filled = True
    p_l_eye2.fill_color = 'ivory'
    p_l_eye3 = GOval(9, 9)
    window.add(p_l_eye3, x=723, y=224)
    p_l_eye3.filled = True
    p_l_eye3.fill_color = 'ivory'
    p_l_eye4 = GOval(9, 9)
    window.add(p_l_eye4, x=717, y=232)
    p_l_eye4.filled = True
    p_l_eye4.fill_color = 'ivory'

    p_r_eye = GOval(30, 30)
    window.add(p_r_eye, x=785, y=215)
    p_r_eye.filled = True
    p_r_eye.fill_color = 'darkgray2'
    p_r_eye2 = GOval(12, 12)
    window.add(p_r_eye2, x=788, y=220)
    p_r_eye2.filled = True
    p_r_eye2.fill_color = 'ivory'
    p_r_eye3 = GOval(9, 9)
    window.add(p_r_eye3, x=803, y=224)
    p_r_eye3.filled = True
    p_r_eye3.fill_color = 'ivory'
    p_r_eye4 = GOval(9, 9)
    window.add(p_r_eye4, x=797, y=232)
    p_r_eye4.filled = True
    p_r_eye4.fill_color = 'ivory'

    p_mouth_1 = GOval(35, 30)
    window.add(p_mouth_1, x=730, y=260)
    p_mouth_1.color = 'firebrick'
    p_mouth_1.filled = True
    p_mouth_1.fill_color = 'firebrick'
    p_mouth_2 = GOval(35, 30)
    window.add(p_mouth_2, x=755, y=260)
    p_mouth_2.color = 'firebrick'
    p_mouth_2.filled = True
    p_mouth_2.fill_color = 'firebrick'
    p_mouth_3 = GOval(40, 12)
    window.add(p_mouth_3, x=740, y=280)
    p_mouth_3.color = 'firebrick'
    p_mouth_3.filled = True
    p_mouth_3.fill_color = 'firebrick'
    p_teeth = GOval(25, 25)
    window.add(p_teeth, x=747, y=250)
    p_teeth.color = 'ivory'
    p_teeth.filled = True
    p_teeth.fill_color = 'ivory'
    p_mouth_4 = GOval(40, 15)
    window.add(p_mouth_4, x=740, y=248)
    p_mouth_4.color = 'peach'
    p_mouth_4.filled = True
    p_mouth_4.fill_color = 'peach'

    p_l_cheek = GOval(35, 15)
    window.add(p_l_cheek, x=675, y=250)
    p_l_cheek.color = 'pink2'
    p_l_cheek.fill_color = 'pink2'
    p_r_cheek = GOval(35, 15)
    window.add(p_r_cheek, x=805, y=250)
    p_r_cheek.color = 'pink2'
    p_r_cheek.fill_color = 'pink2'

    peach_name = GLabel('APEACH')
    peach_name.font = 'Verdana-30-bold'
    window.add(peach_name, x=695, y=380)









if __name__ == '__main__':
    main()
