from manimlib.imports import *


class Jz(Scene):
    CONFIG = {'logo': '/Users/qi/ManimInstall/manim_3feb/LOGO.png'}

    def construct(self):
        logo = ImageMobject(self.logo)
        logo.set_height(0.75)
        logo.shift(UP * 3.55 + LEFT * 5.08)
        self.add(logo)

        ## Making pvject
        Title = TextMobject("计算机组成原理", color="#9a8cc8")
        Title.scale(3)
        T1 = TextMobject("地址设计", color=RED)
        T1.scale(0.45)
        T2 = TextMobject("字编址", color="#4b6cc7")
        T2.scale(0.4)

        T2_1 = TextMobject(" | ", color=RED)
        T2_1.scale(0.4)
        T2_2 = TextMobject("字节编址", color="#4b6cc7")
        T2_2.scale(0.4)

        line1 = Line(np.array([-8, 3.15, 0]), np.array([8, 3.15, 0]), color=GREY)

        JT = TexMobject(r"\begin{split} \Rightarrow \end{split} ", color=RED)
        JT.scale(1)


        dui1 = TexMobject(r"\begin{split} \checkmark \end{split} ", color=RED)
        dui1.scale(0.6)
        cuo1 = TexMobject(r"\begin{split} \times \end{split} ", color=RED)
        cuo1.scale(0.6)

        eg = TexMobject(r"\begin{split} eg: \end{split} ", color=RED)
        eg.scale(1)


        字节编址字符 = ['以','\\ 字节\\ ','编址时。']
        字节编址 = TextMobject(字节编址字符[0],字节编址字符[1],字节编址字符[2])
        字节编址.scale(0.65)
        字节编址[0].set_color(WHITE)
        字节编址[1].set_color(RED)
        字节编址[2].set_color(WHITE)
        字编址字符 = ['以','\\ 字\\ ','编址时。']
        字编址 = TextMobject(字编址字符[0],字编址字符[1],字编址字符[2])
        字编址.scale(0.65)
        字编址[0].set_color(WHITE)
        字编址[1].set_color(RED)
        字编址[2].set_color(WHITE)

        #例
        例题 = TexMobject(
                            r"\text{假设主存容量为}",      #0
                            r"512K\times 16",            #1
                            r"\text{位，Cache容量为}",    #2
                            r"4096\times 16",            #3
                            r"\text{位，块长为}",         #4
                            r"\ 4\ ",                    #5
                            r"\text{个}",                #6
                            r"\ 16\ ",                   #7
                            r"\text{位的字。}"            #8
        )
        例题.scale(0.7)
        例题.set_color("#d0e1e4")
        例题[1].set_color("#ff7bb9")
        例题[3].set_color("#ff7bb9")
        例题[5].set_color("#ff7bb9")
        例题[7].set_color("#ff7bb9")

        问题题目 = [
            r"\text{(1)在直接映射方式下，设计主存的地址格式。}",
            r"\text{(2)在全相联映射方式下，设计主存的地址格式。}",
            r"\text{(3)在二路组相联映射方式下，设计主存的地址格式。}",
            r"\text{(4)若主存容量为} 512K\times 32 \text{位，块长不变，在四路组相联映射方式下，设计主存的地址格式。}"
        ]
        问题 = TexMobject(
            问题题目[0],
            问题题目[1],
            问题题目[2],
            问题题目[3]
        )
        问题.scale(0.5)
        问题.set_color("#47ffa6")

        Cache = [
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            TexMobject(     # 4
                r"\begin{split} \vdots \end{split}"
            ),
            TexMobject(  # 5
                r"\overbrace{\hspace{2.5cm}} "
            ),
            TextMobject(  # 6
                "Cache"
            ),
            TexMobject(  # 7
                r"\overbrace{\hspace{2.95cm}} "
            ),
            TextMobject(  # 8
                "一个16位的字"
            ),
            TexMobject(  # 9
                r"\begin{split} \text{共} \ 4096\ &÷\ (2\times 4)\text{个组}\\ &\Downarrow \\2^{^{12}}\ &÷\ 2^{^3}=2^{^9}\\ &\Downarrow \\ &9\text{位} \end{split}"
            ),
            Rectangle(  # 10
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(  # 11
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            TexMobject(  # 12
                r"\overbrace{\hspace{1.23cm}} "
            ),
            TexMobject(  # 13
                r"\overbrace{\hspace{1.23cm}} "
            ),
            TexMobject(  # 14
                r"\overbrace{\hspace{2.48cm}} "
            ),
            TexMobject(     # 15
                r"\begin{split} \vdots \end{split}"
            ),
            TexMobject(     # 16
                r"\begin{split} \vdots \end{split}"
            ),
            TexMobject(     # 17
                r"\begin{split} \text{}4&\text{个}\text{字}\\&\Downarrow \\1&\text{个}\text{块}\end{split}"
            ),
            TexMobject(     # 18
                 r"\begin{split} \text{}4&\text{个}\text{字}\\&\Downarrow \\1&\text{个}\text{块}\end{split}"
            ),
            TexMobject(     # 19
                 r"\begin{split} 2&\text{个}\text{块}\\&\Downarrow \\1&\text{个}\text{组}\end{split}"
            ),
            TexMobject(  # 20
                r"\overbrace{\hspace{2.5cm}} "
            ),TexMobject(     # 21
                 r"\begin{split} \text{共}&4096\text{个字}\\&\Downarrow \\&2^{^{12}}\text{个}\text{字}\end{split}"
            )
        ]
        Cache[4].scale(0.55)
        Cache[5].scale(0.5)
        Cache[20].scale(0.5)
        Cache[21].scale(0.3)
        Cache[7].scale(0.5)
        Cache[6].scale(0.35)
        Cache[8].scale(0.45)
        Cache[9].scale(0.45)
        Cache[15].scale(0.4)
        Cache[16].scale(0.5)
        Cache[5].rotate(TAU / 4)
        Cache[20].rotate(3 * TAU / 4)
        Cache[12].rotate(TAU / 4)
        Cache[12].scale(0.3)
        Cache[13].rotate(TAU / 4)
        Cache[13].scale(0.3)
        Cache[14].rotate(TAU / 4)
        Cache[14].scale(0.3)
        Cache[17].scale(0.25)
        Cache[18].scale(0.25)
        Cache[19].scale(0.35)

        块内 = [
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width = 1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            TexMobject(
                r"\begin{split} \vdots \end{split}"
            ),
            TexMobject(     # 5
                r"\overbrace{\hspace{2.5cm}} "
            ),
            TextMobject(    # 6
                "一个字块"
            ),
            TexMobject(     # 7
                r"\overbrace{\hspace{2.95cm}} "
            ),
            TextMobject(  # 8
                "一个16位的字"
            ),
            TexMobject(  # 9
                r"\begin{split}  \text{共}&\ 4\ \text{个}\\ &\Downarrow \\&2^{^2}\\ &\Downarrow \\ &2\text{位} \end{split}"
            )
        ]
        块内[4].scale(0.55)
        块内[5].scale(0.5)
        块内[7].scale(0.5)
        块内[6].scale(0.35)
        块内[8].scale(0.45)
        块内[9].scale(0.45)
        块内[5].rotate(TAU/4)
        回答 = [
            r"\begin{split}    \text{由主存容量}&:512K\times 16\text{位}\Rightarrow 2^{^{19}}\text{字}\\ \text{可得}&:\text{主存地址为}19\text{位} \end{split}",
            r"\begin{split}    \text{由块长为}&:4\text{个}16\text{位的字}\Rightarrow 2^{^{2}}\text{字}\\ \text{可得}&:\text{字块内地址为}2\text{位} \end{split}",
            r"\begin{split}    \text{由Cache容量}&:4096\times 16\text{位}\Rightarrow 2^{^{12}}\text{字; 一块有4个16位的字}\Rightarrow 2^{^2}\text{字}\\&\hspace{0.34cm} 2^{^{12}}÷\ 2^{^2}=2^{^{10}}  \\ \text{可得}&:\text{Cache字块地址为}10\text{位}     \end{split}",
            r"\begin{split}    \text{则主存字块标记为:}&19-10-2\\&=7\text{位}     \end{split}"
        ]
        答案 = TexMobject(
            回答[0],
            回答[1],
            回答[2],
            回答[3]
        )
        答案.scale(0.5)









        地址内字 = TextMobject(
            "主存字块标记",
            "Cache字块地址",
            "字块内地址"
        )
        地址内字.scale(0.45)


        地址框 = Rectangle(
            color=WHITE,
            height=0.8,
            width=6.0
        )
        地址线1 = Line(np.array([-1.0, 0.4, 0]), np.array([-1.0, -0.4, 0]), color="#613377")
        地址线2 = Line(np.array([1.0, 0.4, 0]), np.array([1.0, -0.4, 0]), color="#613377")
        地址虚线1 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        地址虚线2 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        地址虚线3 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        地址虚线4 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        地址 = VGroup(地址框,地址线1,地址线2,地址内字)
        地址虚线 = VGroup(地址虚线1,地址虚线2,地址虚线3,地址虚线4)
        地址.set_color("#613377")
        地址虚线.set_color("#613377")
        地址内字.set_color("#b88d97")

        虚线内未知字段 = [
            "?",
            "?",
            "?"
        ]
        虚线内未知 = TextMobject(
            虚线内未知字段[0],
            虚线内未知字段[1],
            虚线内未知字段[2]
        )
        虚线内未知.scale(0.7)
        虚线内已知字段 = [
            "7",
            "10",
            "2"
        ]
        虚线内已知 = TextMobject(
            虚线内已知字段[0],
            虚线内已知字段[1],
            虚线内已知字段[2]
        )
        虚线内已知.scale(0.7)

        地址括号上字 = TextMobject(
            "共",
            "19",
            "位"
        )
        地址括号上字.scale(0.45)

        地址括号 = TexMobject(r"\overbrace{\hspace{4.25cm}}")
        地址括号.shift(DOWN * 1)



        #第二问
        全答案 = [
            TexMobject(
                r"\text{则主存字块标记为:}&19-2\\&=17\text{位}"
            )
        ]
        全答案[0].scale(0.5)
        全地址内字 = TextMobject(
            "主存字块标记",
            "字块内地址"
        )
        全地址内字.scale(0.45)

        全地址框 = Rectangle(
            color=WHITE,
            height=0.8,
            width=6.0
        )

        全地址线2 = Line(np.array([1.0, 0.4, 0]), np.array([1.0, -0.4, 0]), color="#613377")
        全地址虚线1 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        全地址虚线3 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        全地址虚线4 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        全地址 = VGroup(全地址框, 全地址线2, 全地址内字)
        全地址虚线 = VGroup(全地址虚线1, 全地址虚线3, 全地址虚线4)
        全地址.set_color("#613377")
        全地址虚线.set_color("#613377")
        全地址内字.set_color("#b88d97")

        全虚线内未知 = TextMobject(
            虚线内未知字段[0],
            虚线内未知字段[1]
        )
        全虚线内未知.scale(0.7)
        全虚线内已知字段 = [
            "17",
            "2"
        ]
        全虚线内已知 = TextMobject(
            全虚线内已知字段[0],
            全虚线内已知字段[1],
        )
        全虚线内已知.scale(0.7)

        全地址括号上字 = TextMobject(
            "共",
            "19",
            "位"
        )
        全地址括号上字.scale(0.45)

        全地址括号 = TexMobject(r"\overbrace{\hspace{4.25cm}}")
        全地址括号.shift(DOWN * 1)

        # 引导线条
        Line1 = Line(np.array([-5.9, 3.15, 0]), np.array([-5.9, -3.15, 0]), color=GREY)
        Line3 = Line(np.array([-4.9, 3.15, 0]), np.array([-4.9, -3.15, 0]), color=GREY)
        Line4 = Line(np.array([-6.92, 3.15, 0]), np.array([-6.92, -3.15, 0]), color=GREY)



        self.wait(0.3)
        self.play(Write(Title))
        self.wait(1)
        self.play(
            Title.scale, 0.3,
            Title.move_to, UP * 3.45 + RIGHT * 0.2,
            run_time=2
        )
        T1.next_to(Title.get_corner(RIGHT), RIGHT)
        T1.shift(DOWN * 0.1 + RIGHT * 0.2)
        T2.next_to(T1.get_corner(RIGHT), RIGHT)
        T2.shift(DOWN * 0.0 + LEFT * 0 + RIGHT * 0.1)
        T2_1.next_to(T2.get_corner(RIGHT), RIGHT)
        T2_1.shift(DOWN * 0.0 + LEFT * 0.1 + RIGHT * 0.0)
        T2_2.next_to(T2_1.get_corner(RIGHT), RIGHT)
        T2_2.shift(DOWN * 0.0 + LEFT * 0.1 + RIGHT * 0.0)
        T2_1.shift(DOWN*0.01)
        T = VGroup(T2,T2_1,T2_2)

        # 第三问
        组地址内字 = TextMobject(
            "主存字块标记",
            "组地址",
            "字块内地址"
        )
        组地址内字.scale(0.45)

        组地址框 = Rectangle(
            color=WHITE,
            height=0.8,
            width=6.0
        )
        组地址线1 = Line(np.array([-1.0, 0.4, 0]), np.array([-1.0, -0.4, 0]), color="#613377")
        组地址线2 = Line(np.array([1.0, 0.4, 0]), np.array([1.0, -0.4, 0]), color="#613377")
        组地址虚线1 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        组地址虚线2 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        组地址虚线3 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        组地址虚线4 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        组地址 = VGroup(组地址框, 组地址线1, 组地址线2, 组地址内字)
        组地址虚线 = VGroup(组地址虚线1, 组地址虚线2, 组地址虚线3, 组地址虚线4)
        组地址.set_color("#613377")
        组地址虚线.set_color("#613377")
        组地址内字.set_color("#b88d97")

        组虚线内未知字段 = [
            "?",
            "?",
            "?"
        ]
        组虚线内未知 = TextMobject(
            组虚线内未知字段[0],
            组虚线内未知字段[1],
            组虚线内未知字段[2]
        )
        组虚线内未知.scale(0.7)
        组虚线内已知字段 = [
            "8",
            "9",
            "2"
        ]
        组虚线内已知 = TextMobject(
            组虚线内已知字段[0],
            组虚线内已知字段[1],
            组虚线内已知字段[2]
        )
        组虚线内已知.scale(0.7)

        组地址括号上字 = TextMobject(
            "共",
            "19",
            "位"
        )
        组地址括号上字.scale(0.45)

        组地址括号 = TexMobject(r"\overbrace{\hspace{4.25cm}}")
        组地址括号.shift(DOWN * 1)

        组回答 = [
            r"\begin{split}    \text{由主存容量}&:512K\times 16\text{位}\Rightarrow 2^{^{19}}\text{字}\\ \text{可得}&:\text{主存地址为}19\text{位} \end{split}",
            r"\begin{split}    \text{由块长为}&:4\text{个}16\text{位的字}\Rightarrow 2^{^{2}}\text{字}\\ \text{可得}&:\text{字块内地址为}2\text{位} \end{split}",
            r"\begin{split}    &\text{由二路组相联，即分为若干组，其中一组内有2个字块，且一字块内有4个字}\\\text{即:}4096\times 16\text{位}\Rightarrow 2^{^{12}}\text{字; 一块有4个16位的字}\Rightarrow 2^{^2}\text{字}\\&\hspace{0.34cm} 2^{^{12}}÷\ 2^{^2}=2^{^{10}}  \\ \text{可得}&:\text{Cache字块地址为}10\text{位}     \end{split}",
            r"\begin{split}    \text{则主存字块标记为:}&19-9-2\\&=8\text{位}     \end{split}"
        ]
        组答案 = TexMobject(
            组回答[0],
            组回答[1],
            组回答[2],
            组回答[3]
        )
        组答案.scale(0.5)

        # 第四问
        四组地址内字 = TextMobject(
            "主存字块标记",
            "组地址",
            "字块内地址"
        )
        四组地址内字.scale(0.45)

        四组地址框 = Rectangle(
            color=WHITE,
            height=0.8,
            width=6.0
        )
        四组地址线1 = Line(np.array([-1.0, 0.4, 0]), np.array([-1.0, -0.4, 0]), color="#613377")
        四组地址线2 = Line(np.array([1.0, 0.4, 0]), np.array([1.0, -0.4, 0]), color="#613377")
        四组地址虚线1 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        四组地址虚线2 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        四组地址虚线3 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        四组地址虚线4 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        四组地址 = VGroup(四组地址框, 四组地址线1, 四组地址线2, 四组地址内字)
        四组地址虚线 = VGroup(四组地址虚线1, 四组地址虚线2, 四组地址虚线3, 四组地址虚线4)
        四组地址.set_color("#613377")
        四组地址虚线.set_color("#613377")
        四组地址内字.set_color("#b88d97")

        四组虚线内未知字段 = [
            "?",
            "?",
            "?"
        ]
        四组虚线内未知 = TextMobject(
            四组虚线内未知字段[0],
            四组虚线内未知字段[1],
            四组虚线内未知字段[2]
        )
        四组虚线内未知.scale(0.7)
        四组虚线内已知字段 = [
            "10",
            "8",
            "2"
        ]
        四组虚线内已知 = TextMobject(
            四组虚线内已知字段[0],
            四组虚线内已知字段[1],
            四组虚线内已知字段[2]
        )
        四组虚线内已知.scale(0.7)

        四组地址括号上字 = TextMobject(
            "共",
            "20",
            "位"
        )
        四组地址括号上字.scale(0.45)

        四组地址括号 = TexMobject(r"\overbrace{\hspace{4.25cm}}")
        四组地址括号.shift(DOWN * 1)

        四组回答 = [
            r"\begin{split}    \text{由主存容量}&:512K\times 32\text{位，然一字16位}\Rightarrow 512K\times 32= 512K\times 16\times 2\\&= 2^{^{20}}\text{字}\\ \text{可得}&:\text{主存地址为}20\text{位} \end{split}",
            r"\begin{split}    \text{由块长为}&:4\text{个}16\text{位的字}\Rightarrow 2^{^{2}}\text{字}\\ \text{可得}&:\text{字块内地址为}2\text{位} \end{split}",
            r"\begin{split}    &\text{由二路组相联，即分为若干组，其中一组内有2个字块，且一字块内有4个字}\\\text{即:}4096\times 16\text{位}\Rightarrow 2^{^{12}}\text{字; 一块有4个16位的字}\Rightarrow 2^{^2}\text{字}\\&\hspace{0.34cm} 2^{^{12}}÷\ 2^{^2}=2^{^{10}}  \\ \text{可得}&:\text{Cache字块地址为}10\text{位}     \end{split}",
            r"\begin{split}    \text{则主存字块标记为:}&20-8-2\\&=10\text{位}     \end{split}"
        ]
        四组答案 = TexMobject(
            四组回答[0],
            四组回答[1],
            四组回答[2],
            四组回答[3]
        )
        四组答案.scale(0.5)

        四Cache = [
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            TexMobject(     # 4
                r"\begin{split} \vdots \end{split}"
            ),
            TexMobject(  # 5
                r"\overbrace{\hspace{2.5cm}} "
            ),
            TextMobject(  # 6
                "Cache"
            ),
            TexMobject(  # 7
                r"\overbrace{\hspace{2.95cm}} "
            ),
            TextMobject(  # 8
                "一个16位的字"
            ),
            TexMobject(  # 9
                r"\begin{split} \text{共} \ 4096\ &÷\ (4\times 4)\ \text{个组}\\ &\Downarrow \\2^{^{12}}\ &÷\ 2^{^4}=2^{^8}\\ &\Downarrow \\ &8\text{位} \end{split}"
            ),
            Rectangle(  # 10
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(  # 11
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            TexMobject(  # 12
                r"\overbrace{\hspace{1.23cm}} "
            ),
            TexMobject(  # 13
                r"\overbrace{\hspace{1.23cm}} "
            ),
            TexMobject(  # 14
                r"\overbrace{\hspace{3cm}} "
            ),
            TexMobject(     # 15
                r"\begin{split} \vdots \end{split}"
            ),
            TexMobject(     # 16
                r"\begin{split} \vdots \end{split}"
            ),
            TexMobject(     # 17
                r"\begin{split} \text{}4&\text{个}\text{字}\\&\Downarrow \\1&\text{个}\text{块}\end{split}"
            ),
            TexMobject(     # 18
                 r"\begin{split} \text{}4&\text{个}\text{字}\\&\Downarrow \\1&\text{个}\text{块}\end{split}"
            ),
            TexMobject(     # 19
                 r"\begin{split} 4&\text{个}\text{块}\\&\Downarrow \\1&\text{个}\text{组}\end{split}"
            ),
            TexMobject(  # 20
                r"\overbrace{\hspace{2.5cm}} "
            ),TexMobject(     # 21
                 r"\begin{split} \text{共}&4096\text{个字}\\&\Downarrow \\&2^{^{12}}\text{个}\text{字}\end{split}"
            )
        ]
        四Cache[4].scale(0.55)
        四Cache[5].scale(0.5)
        四Cache[20].scale(0.5)
        四Cache[21].scale(0.3)
        四Cache[7].scale(0.5)
        四Cache[6].scale(0.35)
        四Cache[8].scale(0.45)
        四Cache[9].scale(0.45)
        四Cache[15].scale(0.4)
        四Cache[16].scale(0.5)
        四Cache[5].rotate(TAU / 4)
        四Cache[20].rotate(3 * TAU / 4)
        四Cache[12].rotate(TAU / 4)
        四Cache[12].scale(0.3)
        四Cache[13].rotate(TAU / 4)
        四Cache[13].scale(0.3)
        四Cache[14].rotate(TAU / 4)
        四Cache[14].scale(0.3)
        四Cache[17].scale(0.25)
        四Cache[18].scale(0.25)
        四Cache[19].scale(0.35)












        ###字节
        字节Cache = [
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            TexMobject(  # 4
                r"\begin{split} \vdots \end{split}"
            ),
            TexMobject(  # 5
                r"\overbrace{\hspace{2.5cm}} "
            ),
            TextMobject(  # 6
                "Cache"
            ),
            TexMobject(  # 7
                r"\overbrace{\hspace{2.95cm}} "
            ),
            TexMobject(  # 8
                r"\text{共2个字节}\Rightarrow 2^{^1}"
            ),
            TexMobject(  # 9
                r"\begin{split} \text{共} \ 4096\ &÷\ (2\times 4)\text{个组}\\ &\Downarrow \\2^{^{12}}\ &÷\ 2^{^3}=2^{^9}\\ &\Downarrow \\ &9\text{位} \end{split}"
            ),
            Rectangle(  # 10
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(  # 11
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            TexMobject(  # 12
                r"\overbrace{\hspace{1.23cm}} "
            ),
            TexMobject(  # 13
                r"\overbrace{\hspace{1.23cm}} "
            ),
            TexMobject(  # 14
                r"\overbrace{\hspace{2.48cm}} "
            ),
            TexMobject(  # 15
                r"\begin{split} \vdots \end{split}"
            ),
            TexMobject(  # 16
                r"\begin{split} \vdots \end{split}"
            ),
            TexMobject(  # 17
                r"\begin{split} \text{}4\times &2\text{个}\text{字节}\\&\Downarrow \\1&\text{个}\text{块}\end{split}"
            ),
            TexMobject(  # 18
                r"\begin{split} \text{}4\times &2\text{个}\text{字节}\\&\Downarrow \\1&\text{个}\text{块}\end{split}"
            ),
            TexMobject(  # 19
                r"\begin{split} 2&\text{个}\text{块}\\&\Downarrow \\1&\text{个}\text{组}\end{split}"
            ),
            TexMobject(  # 20
                r"\overbrace{\hspace{2.5cm}} "
            ), TexMobject(  # 21
                r"\begin{split} \text{共}4&096\text{个字}\\&\Downarrow \\2^{^{12}}&\times 2^{^1}\text{个}\text{字节}\end{split}"
            ),
            Line(       # 22
                np.array([0, 0.4375, 0]),
                np.array([0, -0.175, 0]),
                stroke_width=1
            ),
            Line(       # 23
                np.array([0, 0.1875, 0]),
                np.array([0, -0.1875, 0]),
                stroke_width=1
            ),
            TexMobject(  # 24
                r"\overbrace{\hspace{1.4cm}} "
            ),
            TexMobject(  # 25
                r"\overbrace{\hspace{1.4cm}} "
            ),
            TexMobject(  # 26
                r"8b "
            ),
            TexMobject(  # 27
                r"8b "
            ),
            TexMobject(  # 28
                r"1B "
            ),
            TexMobject(  # 29
                r"1B "
            )
        ]
        字节Cache[4].scale(0.55)
        字节Cache[5].scale(0.5)
        字节Cache[20].scale(0.5)
        字节Cache[21].scale(0.3)
        字节Cache[7].scale(0.5)
        字节Cache[6].scale(0.35)
        字节Cache[8].scale(0.45)
        字节Cache[9].scale(0.45)
        字节Cache[15].scale(0.4)
        字节Cache[16].scale(0.5)
        字节Cache[5].rotate(TAU / 4)
        字节Cache[20].rotate(3 * TAU / 4)
        字节Cache[12].rotate(TAU / 4)
        字节Cache[12].scale(0.3)
        字节Cache[13].rotate(TAU / 4)
        字节Cache[13].scale(0.3)
        字节Cache[14].rotate(TAU / 4)
        字节Cache[14].scale(0.3)
        字节Cache[17].scale(0.25)
        字节Cache[18].scale(0.25)
        字节Cache[19].scale(0.35)

        字节Cache[24].scale(0.5)
        字节Cache[25].scale(0.5)
        字节Cache[26].scale(0.25)
        字节Cache[27].scale(0.25)
        字节Cache[28].scale(0.35)
        字节Cache[29].scale(0.35)

        字节块内 = [
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            TexMobject(
                r"\begin{split} \vdots \end{split}"
            ),
            TexMobject(  # 5
                r"\overbrace{\hspace{2.5cm}} "
            ),
            TextMobject(  # 6
                "一个字块"
            ),
            TexMobject(  # 7
                r"\overbrace{\hspace{2.95cm}} "
            ),
            TexMobject(  # 8
                r"2^{^1}个字节\Rightarrow 1\text{位}"
            ),
            TexMobject(  # 9
                r"\begin{split}  \text{共}&\ 4\ \text{个}\\ &\Downarrow \\&2^{^2}\\ &\Downarrow \\ &2\text{位} \end{split}"
            ),
            Line(       # 10
                np.array([0, 0.375, 0]),
                np.array([0, -0.375, 0]),
                stroke_width=1
            ),
            Line(       # 11
                np.array([0, 0.125, 0]),
                np.array([0, -0.125, 0]),
                stroke_width=1
            ),
            TexMobject(  # 12
                r"\overbrace{\hspace{1.4cm}} "
            ),
            TexMobject(  # 13
                r"\overbrace{\hspace{1.4cm}} "
            ),
            TexMobject(  # 14
                r"8b "
            ),
            TexMobject(  # 15
                r"8b "
            ),
            TexMobject(  # 16
                r"1B "
            ),
            TexMobject(  # 17
                r"1B "
            ),
            TexMobject(  # 18
                r"\xrightarrow{\hspace{1.2cm}} "
            ),
            TexMobject(  # 19
                r"\xrightarrow{\hspace{1.2cm}} "
            ),
            TexMobject(  # 20
                r"2+1=3\text{位} "
            )
        ]
        字节块内[4].scale(0.55)
        字节块内[5].scale(0.5)
        字节块内[7].scale(0.5)
        字节块内[6].scale(0.35)
        字节块内[8].scale(0.45)
        字节块内[9].scale(0.45)
        字节块内[5].rotate(TAU / 4)
        字节块内[12].scale(0.5)
        字节块内[13].scale(0.5)
        字节块内[14].scale(0.35)
        字节块内[15].scale(0.35)
        字节块内[16].scale(0.35)
        字节块内[17].scale(0.35)
        字节块内[19].rotate(3* TAU / 4)
        字节块内[20].scale(0.45)
        字节回答 = [
            r"\begin{split}    \text{由主存容量}&:512K\times 16\text{位}\Rightarrow 2^{^{19}}\text{字}\\ \text{可得}&:\text{主存地址为}19\text{位} \end{split}",
            r"\begin{split}    \text{由块长为}&:4\text{个}16\text{位的字}\Rightarrow 2^{^{2}}\text{字}\\ \text{可得}&:\text{字块内地址为}2\text{位} \end{split}",
            r"\begin{split}    \text{由Cache容量}&:4096\times 16\text{位}\Rightarrow 2^{^{12}}\times 2^{^1}\text{字节; 一块有4个16位的字}\Rightarrow 2^{^2}\times 2^{^1}\text{字节}\\&\hspace{0.34cm} (2^{^{12}}\times 2^{^{1}})÷\ (2^{^2}\times 2^{^{1}})=2^{^{10}}  \\ \text{可得}&:\text{Cache字块地址为}10\text{位}     \end{split}",
            r"\begin{split}    \text{则主存字块标记为:}&19-10-3\\&=6\text{位}     \end{split}"
        ]
        字节答案 = TexMobject(
            字节回答[0],
            字节回答[1],
            字节回答[2],
            字节回答[3]
        )
        字节答案.scale(0.5)

        字节地址内字 = TextMobject(
            "主存字块标记",
            "Cache字块地址",
            "字块内地址"
        )
        字节地址内字.scale(0.45)

        字节地址框 = Rectangle(
            color=WHITE,
            height=0.8,
            width=6.0
        )
        字节地址线1 = Line(np.array([-1.0, 0.4, 0]), np.array([-1.0, -0.4, 0]), color="#613377")
        字节地址线2 = Line(np.array([1.0, 0.4, 0]), np.array([1.0, -0.4, 0]), color="#613377")
        字节地址虚线1 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        字节地址虚线2 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        字节地址虚线3 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        字节地址虚线4 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        字节地址 = VGroup(字节地址框, 字节地址线1, 字节地址线2, 字节地址内字)
        字节地址虚线 = VGroup(字节地址虚线1, 字节地址虚线2, 字节地址虚线3, 字节地址虚线4)
        字节地址.set_color("#613377")
        字节地址虚线.set_color("#613377")
        字节地址内字.set_color("#b88d97")

        字节虚线内未知字段 = [
            "?",
            "?",
            "?"
        ]
        字节虚线内未知 = TextMobject(
            字节虚线内未知字段[0],
            字节虚线内未知字段[1],
            字节虚线内未知字段[2]
        )
        字节虚线内未知.scale(0.7)
        字节虚线内已知字段 = [
            "6",
            "10",
            "3"
        ]
        字节虚线内已知 = TextMobject(
            字节虚线内已知字段[0],
            字节虚线内已知字段[1],
            字节虚线内已知字段[2]
        )
        字节虚线内已知.scale(0.7)

        字节地址括号上字 = TextMobject(
            "共",
            "19",
            "位"
        )
        字节地址括号上字.scale(0.45)

        字节地址括号 = TexMobject(r"\overbrace{\hspace{4.25cm}}")
        字节地址括号.shift(DOWN * 1)

        # 第二问
        字节全答案 = [
            TexMobject(
                r"\text{则主存字块标记为:}&19-3\\&=16\text{位}"
            )
        ]
        字节全答案[0].scale(0.5)
        字节全地址内字 = TextMobject(
            "主存字块标记",
            "字块内地址"
        )
        字节全地址内字.scale(0.45)

        字节全地址框 = Rectangle(
            color=WHITE,
            height=0.8,
            width=6.0
        )

        字节全地址线2 = Line(np.array([1.0, 0.4, 0]), np.array([1.0, -0.4, 0]), color="#613377")
        字节全地址虚线1 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        字节全地址虚线3 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        字节全地址虚线4 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        字节全地址 = VGroup(字节全地址框, 字节全地址线2, 字节全地址内字)
        字节全地址虚线 = VGroup(字节全地址虚线1, 字节全地址虚线3, 字节全地址虚线4)
        字节全地址.set_color("#613377")
        字节全地址虚线.set_color("#613377")
        字节全地址内字.set_color("#b88d97")

        字节全虚线内未知 = TextMobject(
            字节虚线内未知字段[0],
            字节虚线内未知字段[1]
        )
        字节全虚线内未知.scale(0.7)
        字节全虚线内已知字段 = [
            "16",
            "3"
        ]
        字节全虚线内已知 = TextMobject(
            字节全虚线内已知字段[0],
            字节全虚线内已知字段[1],
        )
        字节全虚线内已知.scale(0.7)

        字节全地址括号上字 = TextMobject(
            "共",
            "19",
            "位"
        )
        字节全地址括号上字.scale(0.45)

        字节全地址括号 = TexMobject(r"\overbrace{\hspace{4.25cm}}")
        字节全地址括号.shift(DOWN * 1)



        # 第三问
        字节组地址内字 = TextMobject(
            "主存字块标记",
            "组地址",
            "字块内地址"
        )
        字节组地址内字.scale(0.45)

        字节组地址框 = Rectangle(
            color=WHITE,
            height=0.8,
            width=6.0
        )
        字节组地址线1 = Line(np.array([-1.0, 0.4, 0]), np.array([-1.0, -0.4, 0]), color="#613377")
        字节组地址线2 = Line(np.array([1.0, 0.4, 0]), np.array([1.0, -0.4, 0]), color="#613377")
        字节组地址虚线1 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        字节组地址虚线2 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        字节组地址虚线3 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        字节组地址虚线4 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        字节组地址 = VGroup(字节组地址框, 字节组地址线1, 字节组地址线2, 字节组地址内字)
        字节组地址虚线 = VGroup(字节组地址虚线1, 字节组地址虚线2, 字节组地址虚线3, 字节组地址虚线4)
        字节组地址.set_color("#613377")
        字节组地址虚线.set_color("#613377")
        字节组地址内字.set_color("#b88d97")

        字节组虚线内未知字段 = [
            "?",
            "?",
            "?"
        ]
        字节组虚线内未知 = TextMobject(
            字节组虚线内未知字段[0],
            字节组虚线内未知字段[1],
            字节组虚线内未知字段[2]
        )
        字节组虚线内未知.scale(0.7)
        字节组虚线内已知字段 = [
            "7",
            "9",
            "3"
        ]
        字节组虚线内已知 = TextMobject(
            字节组虚线内已知字段[0],
            字节组虚线内已知字段[1],
            字节组虚线内已知字段[2]
        )
        字节组虚线内已知.scale(0.7)

        字节组地址括号上字 = TextMobject(
            "共",
            "19",
            "位"
        )
        字节组地址括号上字.scale(0.45)

        字节组地址括号 = TexMobject(r"\overbrace{\hspace{4.25cm}}")
        字节组地址括号.shift(DOWN * 1)

        字节组回答 = [
            r"\begin{split}    \text{由主存容量}&:512K\times 16\text{位}\Rightarrow 2^{^{19}}\text{字}\\ \text{可得}&:\text{主存地址为}19\text{位} \end{split}",
            r"\begin{split}    \text{由块长为}&:4\text{个}16\text{位的字}\Rightarrow 2^{^{2}}\text{字}\\ \text{可得}&:\text{字块内地址为}2\text{位} \end{split}",
            r"\begin{split}    &\text{由二路组相联，即分为若干组，其中一组内有2个字块，且一字块内有4个字}\\\text{即:}4096\times 16\text{位}\Rightarrow 2^{^{12}}\text{字; 一块有4个16位的字}\Rightarrow 2^{^2}\text{字}\\&\hspace{0.34cm} 2^{^{12}}÷\ 2^{^2}=2^{^{10}}  \\ \text{可得}&:\text{Cache字块地址为}10\text{位}     \end{split}",
            r"\begin{split}    \text{则主存字块标记为:}&19-9-2\\&=8\text{位}     \end{split}"
        ]
        字节组答案 = TexMobject(
            字节组回答[0],
            字节组回答[1],
            字节组回答[2],
            字节组回答[3]
        )
        字节组答案.scale(0.5)

        # 第四问
        字节四组地址内字 = TextMobject(
            "主存字块标记",
            "组地址",
            "字块内地址"
        )
        字节四组地址内字.scale(0.45)

        字节四组地址框 = Rectangle(
            color=WHITE,
            height=0.8,
            width=6.0
        )
        字节四组地址线1 = Line(np.array([-1.0, 0.4, 0]), np.array([-1.0, -0.4, 0]), color="#613377")
        字节四组地址线2 = Line(np.array([1.0, 0.4, 0]), np.array([1.0, -0.4, 0]), color="#613377")
        字节四组地址虚线1 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        字节四组地址虚线2 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        字节四组地址虚线3 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        字节四组地址虚线4 = DashedLine(start=UP * 0.5, end=DOWN * 0.5)
        字节四组地址 = VGroup(字节四组地址框, 字节四组地址线1, 字节四组地址线2, 字节四组地址内字)
        字节四组地址虚线 = VGroup(字节四组地址虚线1, 字节四组地址虚线2, 字节四组地址虚线3, 字节四组地址虚线4)
        字节四组地址.set_color("#613377")
        字节四组地址虚线.set_color("#613377")
        字节四组地址内字.set_color("#b88d97")

        字节四组虚线内未知字段 = [
            "?",
            "?",
            "?"
        ]
        字节四组虚线内未知 = TextMobject(
            字节四组虚线内未知字段[0],
            字节四组虚线内未知字段[1],
            字节四组虚线内未知字段[2]
        )
        字节四组虚线内未知.scale(0.7)
        字节四组虚线内已知字段 = [
            "10",
            "8",
            "2"
        ]
        字节四组虚线内已知 = TextMobject(
            字节四组虚线内已知字段[0],
            字节四组虚线内已知字段[1],
            字节四组虚线内已知字段[2]
        )
        字节四组虚线内已知.scale(0.7)

        字节四组地址括号上字 = TextMobject(
            "共",
            "20",
            "位"
        )
        字节四组地址括号上字.scale(0.45)

        字节四组地址括号 = TexMobject(r"\overbrace{\hspace{4.25cm}}")
        字节四组地址括号.shift(DOWN * 1)

        字节四组回答 = [
            r"\begin{split}    \text{由主存容量}&:512K\times 32\text{位，然一字16位}\Rightarrow 512K\times 32= 512K\times 16\times 2\\&= 2^{^{20}}\text{字}\\ \text{可得}&:\text{主存地址为}20\text{位} \end{split}",
            r"\begin{split}    \text{由块长为}&:4\text{个}16\text{位的字}\Rightarrow 2^{^{2}}\text{字}\\ \text{可得}&:\text{字块内地址为}2\text{位} \end{split}",
            r"\begin{split}    &\text{由二路组相联，即分为若干组，其中一组内有2个字块，且一字块内有4个字}\\\text{即:}4096\times 16\text{位}\Rightarrow 2^{^{12}}\text{字; 一块有4个16位的字}\Rightarrow 2^{^2}\text{字}\\&\hspace{0.34cm} 2^{^{12}}÷\ 2^{^2}=2^{^{10}}  \\ \text{可得}&:\text{Cache字块地址为}10\text{位}     \end{split}",
            r"\begin{split}    \text{则主存字块标记为:}&20-8-2\\&=10\text{位}     \end{split}"
        ]
        字节四组答案 = TexMobject(
            字节四组回答[0],
            字节四组回答[1],
            字节四组回答[2],
            字节四组回答[3]
        )
        字节四组答案.scale(0.5)

        字节四Cache = [
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            TexMobject(  # 4
                r"\begin{split} \vdots \end{split}"
            ),
            TexMobject(  # 5
                r"\overbrace{\hspace{2.5cm}} "
            ),
            TextMobject(  # 6
                "Cache"
            ),
            TexMobject(  # 7
                r"\overbrace{\hspace{2.95cm}} "
            ),
            TextMobject(  # 8
                "一个16位的字"
            ),
            TexMobject(  # 9
                r"\begin{split} \text{共} \ 4096\ &÷\ (4\times 4)\ \text{个组}\\ &\Downarrow \\2^{^{12}}\ &÷\ 2^{^4}=2^{^8}\\ &\Downarrow \\ &8\text{位} \end{split}"
            ),
            Rectangle(  # 10
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            Rectangle(  # 11
                color=WHITE,
                height=0.25,
                width=2.0,
                stroke_width=1
            ),
            TexMobject(  # 12
                r"\overbrace{\hspace{1.23cm}} "
            ),
            TexMobject(  # 13
                r"\overbrace{\hspace{1.23cm}} "
            ),
            TexMobject(  # 14
                r"\overbrace{\hspace{3cm}} "
            ),
            TexMobject(  # 15
                r"\begin{split} \vdots \end{split}"
            ),
            TexMobject(  # 16
                r"\begin{split} \vdots \end{split}"
            ),
            TexMobject(  # 17
                r"\begin{split} \text{}4&\text{个}\text{字}\\&\Downarrow \\1&\text{个}\text{块}\end{split}"
            ),
            TexMobject(  # 18
                r"\begin{split} \text{}4&\text{个}\text{字}\\&\Downarrow \\1&\text{个}\text{块}\end{split}"
            ),
            TexMobject(  # 19
                r"\begin{split} 4&\text{个}\text{块}\\&\Downarrow \\1&\text{个}\text{组}\end{split}"
            ),
            TexMobject(  # 20
                r"\overbrace{\hspace{2.5cm}} "
            ), TexMobject(  # 21
                r"\begin{split} \text{共}&4096\text{个字}\\&\Downarrow \\&2^{^{12}}\text{个}\text{字}\end{split}"
            )
        ]
        字节四Cache[4].scale(0.55)
        字节四Cache[5].scale(0.5)
        字节四Cache[20].scale(0.5)
        字节四Cache[21].scale(0.3)
        字节四Cache[7].scale(0.5)
        字节四Cache[6].scale(0.35)
        字节四Cache[8].scale(0.45)
        字节四Cache[9].scale(0.45)
        字节四Cache[15].scale(0.4)
        字节四Cache[16].scale(0.5)
        字节四Cache[5].rotate(TAU / 4)
        字节四Cache[20].rotate(3 * TAU / 4)
        字节四Cache[12].rotate(TAU / 4)
        字节四Cache[12].scale(0.3)
        字节四Cache[13].rotate(TAU / 4)
        字节四Cache[13].scale(0.3)
        字节四Cache[14].rotate(TAU / 4)
        字节四Cache[14].scale(0.3)
        字节四Cache[17].scale(0.25)
        字节四Cache[18].scale(0.25)
        字节四Cache[19].scale(0.35)

        ## 字节Position
        字节地址内字[0].shift(DOWN * 0 + LEFT * 0.52)
        字节地址内字[1].shift(DOWN * 0 + LEFT * 0.14)
        字节地址内字[2].shift(DOWN * 0 + RIGHT * 0.43)
        字节地址.shift(DOWN * 2)
        字节地址括号.shift(DOWN * 0.2)
        字节地址括号上字.next_to(字节地址括号.get_corner(UP), UP)
        字节地址括号上字.shift(DOWN * 0.1)
        字节地址虚线1.shift(DOWN * 2.9 + LEFT * 3)
        字节地址虚线2.next_to(字节地址线1, DOWN)
        字节地址虚线2.shift(UP * 0.25)
        字节地址虚线3.next_to(字节地址线2, DOWN)
        字节地址虚线3.shift(UP * 0.25)
        字节地址虚线4.shift(DOWN * 2.9 + RIGHT * 3)
        字节虚线内未知[0].next_to(字节地址内字[0].get_corner(DOWN), DOWN)
        字节虚线内未知[0].shift(DOWN * 0.5)
        字节虚线内未知[1].next_to(字节地址内字[1].get_corner(DOWN), DOWN)
        字节虚线内未知[1].shift(DOWN * 0.5)
        字节虚线内未知[2].next_to(字节地址内字[2].get_corner(DOWN), DOWN)
        字节虚线内未知[2].shift(DOWN * 0.5)

        字节虚线内已知[0].next_to(字节虚线内未知[0], 0)
        字节虚线内已知[1].next_to(字节虚线内未知[1], 0)
        字节虚线内已知[2].next_to(字节虚线内未知[2], 0)

        # 全相联
        字节全地址内字[0].shift(DOWN * 0 + LEFT * 0.33)
        字节全地址内字[1].shift(DOWN * 0 + RIGHT * 1.3)
        字节全地址.shift(DOWN * 2)
        字节全地址括号.shift(DOWN * 0.2)
        字节全地址括号上字.next_to(字节全地址括号.get_corner(UP), UP)
        字节全地址括号上字.shift(DOWN * 0.1)
        字节全地址虚线1.shift(DOWN * 2.9 + LEFT * 3)

        字节全地址虚线3.next_to(字节地址线2, DOWN)
        字节全地址虚线3.shift(UP * 0.25)
        字节全地址虚线4.shift(DOWN * 2.9 + RIGHT * 3)
        字节全虚线内未知[0].next_to(字节全地址内字[0].get_corner(DOWN), DOWN)
        字节全虚线内未知[0].shift(DOWN * 0.5)
        字节全虚线内未知[1].next_to(字节地址内字[2].get_corner(DOWN), DOWN)
        字节全虚线内未知[1].shift(DOWN * 0.5)

        字节全虚线内已知[0].next_to(字节全虚线内未知[0], 0)
        字节全虚线内已知[1].next_to(字节虚线内未知[2], 0)

        # 组
        字节组地址内字[0].shift(DOWN * 0 + LEFT * 1.05)
        字节组地址内字[1].shift(DOWN * 0 + LEFT * 0.14)
        字节组地址内字[2].shift(DOWN * 0 + RIGHT * 0.96)
        字节组地址.shift(DOWN * 2)
        字节组地址括号.shift(DOWN * 0.2)
        字节组地址括号上字.next_to(字节组地址括号.get_corner(UP), UP)
        字节组地址括号上字.shift(DOWN * 0.1)
        字节组地址虚线1.shift(DOWN * 2.9 + LEFT * 3)
        字节组地址虚线2.next_to(字节组地址线1, DOWN)
        字节组地址虚线2.shift(UP * 0.25)
        字节组地址虚线3.next_to(字节组地址线2, DOWN)
        字节组地址虚线3.shift(UP * 0.25)
        字节组地址虚线4.shift(DOWN * 2.9 + RIGHT * 3)
        字节组虚线内未知[0].next_to(字节组地址内字[0].get_corner(DOWN), DOWN)
        字节组虚线内未知[0].shift(DOWN * 0.5)
        字节组虚线内未知[1].next_to(字节组地址内字[1].get_corner(DOWN), DOWN)
        字节组虚线内未知[1].shift(DOWN * 0.5)
        字节组虚线内未知[2].next_to(字节组地址内字[2].get_corner(DOWN), DOWN)
        字节组虚线内未知[2].shift(DOWN * 0.5)

        字节组虚线内已知[0].next_to(字节组虚线内未知[0], 0)
        字节组虚线内已知[1].next_to(字节组虚线内未知[1], 0)
        字节组虚线内已知[2].next_to(字节组虚线内未知[2], 0)

        # 四组
        字节四组地址内字[0].shift(DOWN * 0 + LEFT * 1.05)
        字节四组地址内字[1].shift(DOWN * 0 + LEFT * 0.14)
        字节四组地址内字[2].shift(DOWN * 0 + RIGHT * 0.96)
        字节四组地址.shift(DOWN * 2)
        字节四组地址括号.shift(DOWN * 0.2)
        字节四组地址括号上字.next_to(字节四组地址括号.get_corner(UP), UP)
        字节四组地址括号上字.shift(DOWN * 0.1)
        字节四组地址虚线1.shift(DOWN * 2.9 + LEFT * 3)
        字节四组地址虚线2.next_to(字节四组地址线1, DOWN)
        字节四组地址虚线2.shift(UP * 0.25)
        字节四组地址虚线3.next_to(字节四组地址线2, DOWN)
        字节四组地址虚线3.shift(UP * 0.25)
        字节四组地址虚线4.shift(DOWN * 2.9 + RIGHT * 3)
        字节四组虚线内未知[0].next_to(字节四组地址内字[0].get_corner(DOWN), DOWN)
        字节四组虚线内未知[0].shift(DOWN * 0.5)
        字节四组虚线内未知[1].next_to(字节四组地址内字[1].get_corner(DOWN), DOWN)
        字节四组虚线内未知[1].shift(DOWN * 0.5)
        字节四组虚线内未知[2].next_to(字节四组地址内字[2].get_corner(DOWN), DOWN)
        字节四组虚线内未知[2].shift(DOWN * 0.5)

        字节四组虚线内已知[0].next_to(字节四组虚线内未知[0], 0)
        字节四组虚线内已知[1].next_to(字节四组虚线内未知[1], 0)
        字节四组虚线内已知[2].next_to(字节四组虚线内未知[2], 0)

        字节四组答案[0].next_to(0, 0)
        字节四组答案[1].next_to(0, 0)
        字节四组答案[2].next_to(0, 0)
        字节四组答案[3].next_to(0, 0)

        字节答案[0].next_to(0, 0)
        字节答案[1].next_to(0, 0)
        字节答案[2].next_to(0, 0)
        字节答案[3].next_to(0, 0)

        字节组答案[0].next_to(0, 0)
        字节组答案[1].next_to(0, 0)
        字节组答案[2].next_to(0, 0)
        字节答案[2].shift(RIGHT * 0.6)
        字节组答案[3].next_to(0, 0)

        字节块内[1].next_to(字节块内[0].get_corner(DOWN), 0)
        字节块内[1].shift(DOWN * 0.125)
        字节块内[2].next_to(字节块内[1].get_corner(DOWN), 0)
        字节块内[2].shift(DOWN * 0.125)
        字节块内[3].next_to(字节块内[2].get_corner(DOWN), 0)
        字节块内[3].shift(DOWN * 0.8)
        字节块内[4].next_to(字节块内[2].get_corner(DOWN), 0)
        字节块内[4].shift(DOWN * 0.34)
        for i in range(5):
            字节块内[i].shift(RIGHT * 5 + UP * 1.2)
        字节块内[5].shift(RIGHT * 3.8 + UP * 0.47)
        字节块内[6].next_to(字节块内[3], DOWN)
        字节块内[7].next_to(字节块内[0], UP)
        字节块内[7].shift(DOWN * 0.12 + UP * 0.25)
        字节块内[8].next_to(字节块内[7], UP)
        字节块内[8].shift(DOWN * 0.12 + DOWN * 0.05)
        字节块内[9].next_to(字节块内[5], LEFT)
        字节块内[9].shift(RIGHT * 0.12)

        字节块内[10].next_to(字节块内[1], 0)
        字节块内[11].next_to(字节块内[3], 0)

        字节块内[12].next_to(字节块内[0], 0)
        字节块内[12].shift(LEFT * 0.5 + UP * 0.25)
        字节块内[13].next_to(字节块内[0], 0)
        字节块内[13].shift(RIGHT * 0.5 + UP * 0.25)

        字节块内[14].next_to(字节块内[0], 0)
        字节块内[14].shift(LEFT * 0.5)
        字节块内[15].next_to(字节块内[0], 0)
        字节块内[15].shift(RIGHT * 0.5)

        字节块内[16].next_to(字节块内[0], 0)
        字节块内[16].shift(LEFT * 0.5 + UP * 0.45)
        字节块内[17].next_to(字节块内[0], 0)
        字节块内[17].shift(RIGHT * 0.5 + UP * 0.45)

        字节块内[18].next_to(字节块内[3], 0)
        字节块内[18].shift(RIGHT * 0.0 + DOWN * 0.7)
        字节块内[19].next_to(字节块内[2], 0)
        字节块内[19].shift(RIGHT * 1.5 + DOWN * 0.2)

        字节块内[20].next_to(字节块内[18], 0)
        字节块内[20].shift(RIGHT * 1.8 + DOWN * 0.0)

        for i in range(21):
            字节块内[i].shift(LEFT * 1.5)


        # Cache
        字节Cache[1].next_to(字节Cache[0].get_corner(DOWN), 0)
        字节Cache[2].next_to(字节Cache[1].get_corner(DOWN), 0)
        字节Cache[3].next_to(字节Cache[2].get_corner(DOWN), 0)
        字节Cache[4].next_to(字节Cache[3].get_corner(DOWN), 0)
        字节Cache[4].shift(DOWN * 0.34)
        字节Cache[10].next_to(字节Cache[4].get_corner(DOWN), 0)
        字节Cache[10].shift(DOWN * 0.34)
        字节Cache[11].next_to(字节Cache[10].get_corner(DOWN), 0)
        for i in range(15):
            字节Cache[i].shift(RIGHT * 5 + UP * 1.2)
        字节Cache[5].shift(LEFT * 2.6 + DOWN * 0.73)
        字节Cache[6].next_to(字节Cache[11], DOWN)
        字节Cache[7].next_to(字节Cache[0], UP)
        字节Cache[7].shift(UP * 0.18)
        字节Cache[8].next_to(字节Cache[7], UP)
        字节Cache[8].shift(DOWN * 0.2 )
        字节Cache[9].next_to(字节Cache[5], LEFT)
        字节Cache[9].shift(RIGHT * 0.12)
        字节Cache[12].shift(DOWN * 0.125 + LEFT * 1.12)
        字节Cache[13].next_to(字节Cache[12], 0)
        字节Cache[13].shift(DOWN * 0.53)
        字节Cache[14].shift(DOWN * 0.385 + LEFT * 1.8)
        字节Cache[15].next_to(字节Cache[13], 0)
        字节Cache[15].shift(DOWN * 0.53 + RIGHT * 0.02)
        字节Cache[16].next_to(字节Cache[14], 0)
        字节Cache[16].shift(DOWN * 0.88 + RIGHT * 0.02)
        字节Cache[17].next_to(字节Cache[12], 0)
        字节Cache[18].next_to(字节Cache[13], 0)
        字节Cache[19].next_to(字节Cache[14], 0)
        字节Cache[17].shift(LEFT * 0.33)
        字节Cache[18].shift(LEFT * 0.33)
        字节Cache[19].shift(LEFT * 0.385)
        字节Cache[20].next_to(字节Cache[5], 0)
        字节Cache[20].shift(RIGHT * 3.8)
        字节Cache[21].next_to(字节Cache[20], 0)
        字节Cache[21].shift(RIGHT * 0.673)

        字节Cache[22].next_to(字节Cache[1], 0)
        字节Cache[22].shift(DOWN * 0.0625)

        字节Cache[23].next_to(字节Cache[11], 0)
        字节Cache[23].shift(LEFT * 0 + UP * 0.0625 + DOWN * 0.0)
        字节Cache[24].next_to(字节Cache[0], 0)
        字节Cache[24].shift(RIGHT * 0.5 + UP * 0.25)

        字节Cache[25].next_to(字节Cache[0], 0)
        字节Cache[25].shift(LEFT * 0.5 + UP * 0.25)
        字节Cache[26].next_to(字节Cache[0], 0)
        字节Cache[26].shift(RIGHT * 0.5 + UP * 0.0625)

        字节Cache[27].next_to(字节Cache[0], 0)
        字节Cache[27].shift(LEFT * 0.5 + UP * 0.0625)
        字节Cache[28].next_to(字节Cache[0], 0)
        字节Cache[28].shift(RIGHT * 0.5 + UP * 0.45)
        字节Cache[29].next_to(字节Cache[0], 0)
        字节Cache[29].shift(LEFT * 0.5 + UP * 0.45)

        字节Cache[17].shift(LEFT * 0.05)
        字节Cache[18].shift(LEFT * 0.05)
        字节Cache[19].shift(LEFT * ( 0.05 + 0.05 ) )
        字节Cache[14].shift(LEFT * ( 0.05 + 0.05 ) )
        字节Cache[21].shift(LEFT * ( 0.05 + 0.05 ) )
        字节Cache[16].shift(LEFT * ( 0.05 + 0.05 ) )
        字节Cache[5].shift( LEFT * ( 0.05 + 0.05 ) )

        for i in range(30):
            字节Cache[i].shift(LEFT * 1.0 )

        # 四Cache
        字节四Cache[1].next_to(字节四Cache[0].get_corner(DOWN), 0)
        字节四Cache[2].next_to(字节四Cache[1].get_corner(DOWN), 0)
        字节四Cache[3].next_to(字节四Cache[2].get_corner(DOWN), 0)
        字节四Cache[4].next_to(字节四Cache[3].get_corner(DOWN), 0)
        字节四Cache[4].shift(DOWN * 0.34)
        字节四Cache[10].next_to(字节四Cache[4].get_corner(DOWN), 0)
        字节四Cache[10].shift(DOWN * 0.34)
        字节四Cache[11].next_to(字节四Cache[10].get_corner(DOWN), 0)
        for i in range(15):
            字节四Cache[i].shift(RIGHT * 5 + UP * 1.2)
        字节四Cache[5].shift(LEFT * 2.6 + DOWN * 0.73)
        字节四Cache[6].next_to(字节四Cache[11], DOWN)
        字节四Cache[7].next_to(字节四Cache[0], UP)
        字节四Cache[7].shift(DOWN * 0.12)
        字节四Cache[8].next_to(字节四Cache[7], UP)
        字节四Cache[8].shift(DOWN * 0.2)
        字节四Cache[9].next_to(字节四Cache[5], LEFT)
        字节四Cache[9].shift(RIGHT * 0.12)
        字节四Cache[12].shift(DOWN * 0.125 + LEFT * 1.12)
        字节四Cache[13].next_to(字节四Cache[12], 0)
        字节四Cache[13].shift(DOWN * 0.53)
        字节四Cache[14].shift(DOWN * 0.47 + LEFT * 1.8)
        字节四Cache[15].next_to(字节四Cache[13], 0)
        字节四Cache[15].shift(DOWN * 0.53 + RIGHT * 0.02)
        字节四Cache[16].next_to(字节四Cache[14], 0)
        字节四Cache[16].shift(DOWN * 0.88 + RIGHT * 0.02)
        字节四Cache[17].next_to(字节四Cache[12], 0)
        字节四Cache[18].next_to(字节四Cache[13], 0)
        字节四Cache[19].next_to(字节四Cache[14], 0)
        字节四Cache[17].shift(LEFT * 0.33)
        字节四Cache[18].shift(LEFT * 0.33)
        字节四Cache[19].shift(LEFT * 0.385)
        字节四Cache[20].next_to(字节四Cache[5], 0)
        字节四Cache[20].shift(RIGHT * 3.8)
        字节四Cache[21].next_to(字节四Cache[20], 0)
        字节四Cache[21].shift(RIGHT * 0.473)





        ## Position
        例题.shift(LEFT * 0.3 + UP * 2.86)
        地址内字[0].shift(DOWN * 0 + LEFT * 0.52)
        地址内字[1].shift(DOWN * 0 + LEFT * 0.14)
        地址内字[2].shift(DOWN * 0 + RIGHT * 0.43)
        地址.shift(DOWN * 2)
        字节编址.next_to(T, DOWN*2.6)
        字节编址.shift(LEFT * 9.15)
        字编址.next_to(T, DOWN * 2.6)
        字编址.shift(LEFT * 9.33)
        问题[0].next_to(字编址.get_corner(DOWN),DOWN*0.5)
        问题[0].shift(RIGHT * 2.59)
        问题[1].next_to(字编址.get_corner(DOWN), DOWN * 0.5)
        问题[1].shift(RIGHT * 2.73)
        问题[2].next_to(字编址.get_corner(DOWN), DOWN * 0.5)
        问题[2].shift(RIGHT * 2.99)
        问题[3].next_to(字编址.get_corner(DOWN), DOWN * 0.5)
        问题[3].shift(RIGHT * 5.3)
        地址括号.shift(DOWN * 0.2)
        地址括号上字.next_to(地址括号.get_corner(UP), UP)
        地址括号上字.shift(DOWN * 0.1)
        地址虚线1.shift(DOWN * 2.9 + LEFT * 3)
        地址虚线2.next_to(地址线1,DOWN)
        地址虚线2.shift(UP * 0.25)
        地址虚线3.next_to(地址线2, DOWN)
        地址虚线3.shift(UP * 0.25)
        地址虚线4.shift(DOWN * 2.9 + RIGHT * 3)
        虚线内未知[0].next_to(地址内字[0].get_corner(DOWN),DOWN)
        虚线内未知[0].shift(DOWN * 0.5)
        虚线内未知[1].next_to(地址内字[1].get_corner(DOWN), DOWN)
        虚线内未知[1].shift(DOWN * 0.5)
        虚线内未知[2].next_to(地址内字[2].get_corner(DOWN), DOWN)
        虚线内未知[2].shift(DOWN * 0.5)

        虚线内已知[0].next_to(虚线内未知[0],0)
        虚线内已知[1].next_to(虚线内未知[1],0)
        虚线内已知[2].next_to(虚线内未知[2],0)

        #全相联
        全地址内字[0].shift(DOWN * 0 + LEFT * 0.33)
        全地址内字[1].shift(DOWN * 0 + RIGHT * 1.3)
        全地址.shift(DOWN * 2)
        全地址括号.shift(DOWN * 0.2)
        全地址括号上字.next_to(全地址括号.get_corner(UP), UP)
        全地址括号上字.shift(DOWN * 0.1)
        全地址虚线1.shift(DOWN * 2.9 + LEFT * 3)


        全地址虚线3.next_to(地址线2, DOWN)
        全地址虚线3.shift(UP * 0.25)
        全地址虚线4.shift(DOWN * 2.9 + RIGHT * 3)
        全虚线内未知[0].next_to(全地址内字[0].get_corner(DOWN), DOWN)
        全虚线内未知[0].shift(DOWN * 0.5)
        全虚线内未知[1].next_to(地址内字[2].get_corner(DOWN), DOWN)
        全虚线内未知[1].shift(DOWN * 0.5)


        全虚线内已知[0].next_to(全虚线内未知[0], 0)
        全虚线内已知[1].next_to(虚线内未知[2], 0)

        # 组
        组地址内字[0].shift(DOWN * 0 + LEFT * 1.05)
        组地址内字[1].shift(DOWN * 0 + LEFT * 0.14)
        组地址内字[2].shift(DOWN * 0 + RIGHT * 0.96)
        组地址.shift(DOWN * 2)
        组地址括号.shift(DOWN * 0.2)
        组地址括号上字.next_to(组地址括号.get_corner(UP), UP)
        组地址括号上字.shift(DOWN * 0.1)
        组地址虚线1.shift(DOWN * 2.9 + LEFT * 3)
        组地址虚线2.next_to(组地址线1, DOWN)
        组地址虚线2.shift(UP * 0.25)
        组地址虚线3.next_to(组地址线2, DOWN)
        组地址虚线3.shift(UP * 0.25)
        组地址虚线4.shift(DOWN * 2.9 + RIGHT * 3)
        组虚线内未知[0].next_to(组地址内字[0].get_corner(DOWN), DOWN)
        组虚线内未知[0].shift(DOWN * 0.5)
        组虚线内未知[1].next_to(组地址内字[1].get_corner(DOWN), DOWN)
        组虚线内未知[1].shift(DOWN * 0.5)
        组虚线内未知[2].next_to(组地址内字[2].get_corner(DOWN), DOWN)
        组虚线内未知[2].shift(DOWN * 0.5)

        组虚线内已知[0].next_to(组虚线内未知[0], 0)
        组虚线内已知[1].next_to(组虚线内未知[1], 0)
        组虚线内已知[2].next_to(组虚线内未知[2], 0)

        # 四组
        四组地址内字[0].shift(DOWN * 0 + LEFT * 1.05)
        四组地址内字[1].shift(DOWN * 0 + LEFT * 0.14)
        四组地址内字[2].shift(DOWN * 0 + RIGHT * 0.96)
        四组地址.shift(DOWN * 2)
        四组地址括号.shift(DOWN * 0.2)
        四组地址括号上字.next_to(四组地址括号.get_corner(UP), UP)
        四组地址括号上字.shift(DOWN * 0.1)
        四组地址虚线1.shift(DOWN * 2.9 + LEFT * 3)
        四组地址虚线2.next_to(四组地址线1, DOWN)
        四组地址虚线2.shift(UP * 0.25)
        四组地址虚线3.next_to(四组地址线2, DOWN)
        四组地址虚线3.shift(UP * 0.25)
        四组地址虚线4.shift(DOWN * 2.9 + RIGHT * 3)
        四组虚线内未知[0].next_to(四组地址内字[0].get_corner(DOWN), DOWN)
        四组虚线内未知[0].shift(DOWN * 0.5)
        四组虚线内未知[1].next_to(四组地址内字[1].get_corner(DOWN), DOWN)
        四组虚线内未知[1].shift(DOWN * 0.5)
        四组虚线内未知[2].next_to(四组地址内字[2].get_corner(DOWN), DOWN)
        四组虚线内未知[2].shift(DOWN * 0.5)

        四组虚线内已知[0].next_to(四组虚线内未知[0], 0)
        四组虚线内已知[1].next_to(四组虚线内未知[1], 0)
        四组虚线内已知[2].next_to(四组虚线内未知[2], 0)

        四组答案[0].next_to(0, 0)
        四组答案[1].next_to(0, 0)
        四组答案[2].next_to(0, 0)
        四组答案[3].next_to(0, 0)

        '''''
        答案[0].shift(UP * 0.5 + RIGHT * 5)
        答案[1].shift(LEFT * 1)
        '''
        答案[0].next_to(0, 0)
        答案[1].next_to(0, 0)
        答案[2].next_to(0,0)
        答案[3].next_to(0, 0)

        组答案[0].next_to(0, 0)
        组答案[1].next_to(0, 0)
        组答案[2].next_to(0, 0)
        组答案[3].next_to(0, 0)

        块内[1].next_to(块内[0].get_corner(DOWN), 0)
        块内[1].shift(DOWN * 0.125)
        块内[2].next_to(块内[1].get_corner(DOWN), 0)
        块内[2].shift(DOWN * 0.125)
        块内[3].next_to(块内[2].get_corner(DOWN), 0)
        块内[3].shift(DOWN * 0.8)
        块内[4].next_to(块内[2].get_corner(DOWN), 0)
        块内[4].shift(DOWN * 0.34)
        for i in range(5):
            块内[i].shift(RIGHT * 5 + UP * 1.2)
        块内[5].shift(RIGHT * 3.8 + UP * 0.47)
        块内[6].next_to(块内[3],DOWN)
        块内[7].next_to(块内[0], UP)
        块内[7].shift(DOWN * 0.12)
        块内[8].next_to(块内[7], UP)
        块内[8].shift(DOWN * 0.12)
        块内[9].next_to(块内[5], LEFT)
        块内[9].shift(RIGHT * 0.12)
        #Cache
        Cache[1].next_to(Cache[0].get_corner(DOWN), 0)
        Cache[2].next_to(Cache[1].get_corner(DOWN), 0)
        Cache[3].next_to(Cache[2].get_corner(DOWN), 0)
        Cache[4].next_to(Cache[3].get_corner(DOWN), 0)
        Cache[4].shift(DOWN * 0.34)
        Cache[10].next_to(Cache[4].get_corner(DOWN), 0)
        Cache[10].shift(DOWN * 0.34)
        Cache[11].next_to(Cache[10].get_corner(DOWN), 0)
        for i in range(15):
            Cache[i].shift(RIGHT * 5 + UP * 1.2)
        Cache[5].shift(LEFT * 2.6 + DOWN * 0.73)
        Cache[6].next_to(Cache[11], DOWN)
        Cache[7].next_to(Cache[0], UP)
        Cache[7].shift(DOWN * 0.12)
        Cache[8].next_to(Cache[7], UP)
        Cache[8].shift(DOWN * 0.2)
        Cache[9].next_to(Cache[5], LEFT)
        Cache[9].shift(RIGHT * 0.12)
        Cache[12].shift(DOWN * 0.125 + LEFT * 1.12)
        Cache[13].next_to(Cache[12],0)
        Cache[13].shift(DOWN * 0.53)
        Cache[14].shift(DOWN * 0.385 + LEFT * 1.8)
        Cache[15].next_to(Cache[13], 0)
        Cache[15].shift(DOWN * 0.53 + RIGHT * 0.02)
        Cache[16].next_to(Cache[14], 0)
        Cache[16].shift(DOWN * 0.88 + RIGHT * 0.02)
        Cache[17].next_to(Cache[12], 0)
        Cache[18].next_to(Cache[13], 0)
        Cache[19].next_to(Cache[14], 0)
        Cache[17].shift(LEFT * 0.33)
        Cache[18].shift(LEFT * 0.33)
        Cache[19].shift(LEFT * 0.385)
        Cache[20].next_to(Cache[5], 0)
        Cache[20].shift(RIGHT * 3.8)
        Cache[21].next_to(Cache[20], 0)
        Cache[21].shift(RIGHT * 0.473)



        #四Cache
        四Cache[1].next_to(四Cache[0].get_corner(DOWN), 0)
        四Cache[2].next_to(四Cache[1].get_corner(DOWN), 0)
        四Cache[3].next_to(四Cache[2].get_corner(DOWN), 0)
        四Cache[4].next_to(四Cache[3].get_corner(DOWN), 0)
        四Cache[4].shift(DOWN * 0.34)
        四Cache[10].next_to(四Cache[4].get_corner(DOWN), 0)
        四Cache[10].shift(DOWN * 0.34)
        四Cache[11].next_to(四Cache[10].get_corner(DOWN), 0)
        for i in range(15):
            四Cache[i].shift(RIGHT * 5 + UP * 1.2)
        四Cache[5].shift(LEFT * 2.6 + DOWN * 0.73)
        四Cache[6].next_to(四Cache[11], DOWN)
        四Cache[7].next_to(四Cache[0], UP)
        四Cache[7].shift(DOWN * 0.12)
        四Cache[8].next_to(四Cache[7], UP)
        四Cache[8].shift(DOWN * 0.2)
        四Cache[9].next_to(四Cache[5], LEFT)
        四Cache[9].shift(RIGHT * 0.12)
        四Cache[12].shift(DOWN * 0.125 + LEFT * 1.12)
        四Cache[13].next_to(四Cache[12],0)
        四Cache[13].shift(DOWN * 0.53)
        四Cache[14].shift(DOWN * 0.47 + LEFT * 1.8)
        四Cache[15].next_to(四Cache[13], 0)
        四Cache[15].shift(DOWN * 0.53 + RIGHT * 0.02)
        四Cache[16].next_to(四Cache[14], 0)
        四Cache[16].shift(DOWN * 0.88 + RIGHT * 0.02)
        四Cache[17].next_to(四Cache[12], 0)
        四Cache[18].next_to(四Cache[13], 0)
        四Cache[19].next_to(四Cache[14], 0)
        四Cache[17].shift(LEFT * 0.33)
        四Cache[18].shift(LEFT * 0.33)
        四Cache[19].shift(LEFT * 0.385)
        四Cache[20].next_to(四Cache[5], 0)
        四Cache[20].shift(RIGHT * 3.8)
        四Cache[21].next_to(四Cache[20], 0)
        四Cache[21].shift(RIGHT * 0.473)

        ## showing object

        # 导引线条
        self.play(Write(Line1),Write(Line3),Write(Line4))

        # 画标题
        self.play(Write(line1), Write(T1), Write(T))

        self.wait(1.5)

        #内容开始
        self.play(
            Write(字编址),
            FadeIn(T2.set_color("#fdafc0"))
        )
        self.play(
            Write(例题)
        )
        '''''
        #第一问开始
        self.play(
            FadeInFrom(问题[0],UP)
        )

        self.play(
            FadeIn(地址)
        )
        self.play(
            Write(地址虚线)
        )
        self.play(
            Write(虚线内未知)
        )
        self.play(
            Write(答案[0])
        )

        self.play(
            FadeOutAndShiftDown(答案[0],UP)
        )

        self.play(
            FadeInFrom(地址括号,DOWN)
        )
        self.play(
            FadeInFrom(地址括号上字,DOWN)
        )
        self.play(
            Write(答案[1]),
            Write(块内[0]),
            Write(块内[1]),
            Write(块内[2]),
            Write(块内[3]),
            Write(块内[4]),
            FadeIn(块内[6])
        )
        self.play(
            FadeInFrom(块内[5], RIGHT*0.2),
            FadeInFrom(块内[7], DOWN*0.2)
        )
        self.play(
            FadeInFrom(块内[9], RIGHT * 0.2),
            FadeInFrom(块内[8], DOWN * 0.2)
        )

        self.play(
            FadeOutAndShiftDown(答案[1], UP),
            ReplacementTransform(虚线内未知[2], 虚线内已知[2]),
            FadeOutAndShiftDown(块内[0], RIGHT),
            FadeOutAndShiftDown(块内[1], RIGHT),
            FadeOutAndShiftDown(块内[2], RIGHT),
            FadeOutAndShiftDown(块内[3], RIGHT),
            FadeOutAndShiftDown(块内[4], RIGHT),
            FadeOutAndShiftDown(块内[5], RIGHT),
            FadeOutAndShiftDown(块内[6], RIGHT),
            FadeOutAndShiftDown(块内[7], RIGHT),
            FadeOutAndShiftDown(块内[8], RIGHT),
            FadeOutAndShiftDown(块内[9], RIGHT),
        )
        self.play(
            Write(答案[2])
        )
        self.play(
            FadeOutAndShiftDown(答案[2], UP),
            ReplacementTransform(虚线内未知[1], 虚线内已知[1])
        )
        self.play(
            Write(答案[3])
        )
        self.play(
            FadeOutAndShiftDown(答案[3], UP),
            ReplacementTransform(虚线内未知[0], 虚线内已知[0])
        )
        self.play(
            FadeOutAndShiftDown(地址括号, UP),
            FadeOutAndShiftDown(地址括号上字, UP)
        )
        self.play(
            ApplyMethod(地址.shift, UP * 1.8),
            ApplyMethod(地址虚线.shift, UP * 1.8),
            ApplyMethod(虚线内已知.shift, UP * 1.8),
        )
        self.play(
            FadeOut(地址),
            FadeOut(地址虚线),
            FadeOut(虚线内已知)
        )
        地址.shift( DOWN * 1.8)
        地址虚线.shift( DOWN * 1.8)
        虚线内已知.shift( DOWN * 1.8)

        self.play(
            FadeOutAndShiftDown(问题[0], DOWN),
            FadeInFrom(问题[1],UP)
        )


        # 第二问

        self.play(
            FadeIn(全地址)
        )
        self.play(
            Write(全地址虚线)
        )
        self.play(
            Write(全虚线内未知)
        )
        self.play(
            Write(答案[0])
        )

        self.play(
            FadeOutAndShiftDown(答案[0], UP)
        )

        self.play(
            FadeInFrom(全地址括号, DOWN)
        )
        self.play(
            FadeInFrom(全地址括号上字, DOWN)
        )
        self.play(
            Write(答案[1]),
            Write(块内[0]),
            Write(块内[1]),
            Write(块内[2]),
            Write(块内[3]),
            Write(块内[4]),
            FadeIn(块内[6])
        )
        self.play(
            FadeInFrom(块内[5], RIGHT * 0.2),
            FadeInFrom(块内[7], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(块内[9], RIGHT * 0.2),
            FadeInFrom(块内[8], DOWN * 0.2)
        )

        self.play(
            FadeOutAndShiftDown(答案[1], UP),
            ReplacementTransform(全虚线内未知[1], 全虚线内已知[1]),
            FadeOutAndShiftDown(块内[0], RIGHT),
            FadeOutAndShiftDown(块内[1], RIGHT),
            FadeOutAndShiftDown(块内[2], RIGHT),
            FadeOutAndShiftDown(块内[3], RIGHT),
            FadeOutAndShiftDown(块内[4], RIGHT),
            FadeOutAndShiftDown(块内[5], RIGHT),
            FadeOutAndShiftDown(块内[6], RIGHT),
            FadeOutAndShiftDown(块内[7], RIGHT),
            FadeOutAndShiftDown(块内[8], RIGHT),
            FadeOutAndShiftDown(块内[9], RIGHT),
        )
        self.play(
            Write(全答案[0])
        )
        self.play(
            FadeOutAndShiftDown(全答案[0], UP),
            ReplacementTransform(全虚线内未知[0], 全虚线内已知[0])
        )
        self.play(
            FadeOutAndShiftDown(全地址括号, UP),
            FadeOutAndShiftDown(全地址括号上字, UP)
        )
        self.play(
            ApplyMethod(全地址.shift, UP * 1.8),
            ApplyMethod(全地址虚线.shift, UP * 1.8),
            ApplyMethod(全虚线内已知.shift, UP * 1.8),
        )
        self.play(
            FadeOut(全地址),
            FadeOut(全地址虚线),
            FadeOut(全虚线内已知)
        )
        self.play(
            FadeOutAndShiftDown(问题[1], DOWN),
            FadeInFrom(问题[2], UP)
        )



        # 第三问
        self.play(
            FadeIn(组地址)
        )
        self.play(
            Write(组地址虚线)
        )
        self.play(
            Write(组虚线内未知)
        )
        self.play(
            Write(答案[0])
        )

        self.play(
            FadeOutAndShiftDown(答案[0], UP)
        )

        self.play(
            FadeInFrom(组地址括号, DOWN)
        )
        self.play(
            FadeInFrom(组地址括号上字, DOWN)
        )
        self.play(
            Write(答案[1]),
            Write(块内[0]),
            Write(块内[1]),
            Write(块内[2]),
            Write(块内[3]),
            Write(块内[4]),
            FadeIn(块内[6])
        )
        self.play(
            FadeInFrom(块内[5], RIGHT * 0.2),
            FadeInFrom(块内[7], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(块内[9], RIGHT * 0.2),
            FadeInFrom(块内[8], DOWN * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(答案[1], UP),
            ReplacementTransform(组虚线内未知[2], 组虚线内已知[2]),
            FadeOutAndShiftDown(块内[0], RIGHT),
            FadeOutAndShiftDown(块内[1], RIGHT),
            FadeOutAndShiftDown(块内[2], RIGHT),
            FadeOutAndShiftDown(块内[3], RIGHT),
            FadeOutAndShiftDown(块内[4], RIGHT),
            FadeOutAndShiftDown(块内[5], RIGHT),
            FadeOutAndShiftDown(块内[6], RIGHT),
            FadeOutAndShiftDown(块内[7], RIGHT),
            FadeOutAndShiftDown(块内[8], RIGHT),
            FadeOutAndShiftDown(块内[9], RIGHT),
        )

        #Cache 入
        self.play(
            Write(Cache[0]),
            Write(Cache[1]),
            Write(Cache[2]),
            Write(Cache[3]),
            Write(Cache[4]),
            Write(Cache[10]),
            Write(Cache[11]),
            FadeIn(Cache[6])
        )
        self.play(
            FadeInFrom(Cache[20], LEFT * 0.2),
            FadeInFrom(Cache[7], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(Cache[21], LEFT * 0.2),
            FadeInFrom(Cache[8], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(Cache[12], RIGHT * 0.2),
            FadeInFrom(Cache[13], RIGHT * 0.2)
        )
        self.play(
            FadeInFrom(Cache[17], RIGHT * 0.2),
            FadeInFrom(Cache[18], RIGHT * 0.2)
        )
        self.play(
            Write(Cache[15])
        )
        self.play(
            FadeInFrom(Cache[14], RIGHT * 0.2)
        )
        self.play(
            FadeInFrom(Cache[19], RIGHT * 0.2)
        )
        self.play(
            Write(Cache[16])
        )
        self.play(
            FadeInFrom(Cache[5], RIGHT * 0.2)
        )
        self.play(
            FadeInFrom(Cache[9], RIGHT * 0.2)
        )

        #答案
        self.play(
            ReplacementTransform(组虚线内未知[1], 组虚线内已知[1])
        )

        #Cache 出
        self.play(
            FadeOutAndShiftDown(Cache[9], RIGHT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(Cache[5], RIGHT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(Cache[19], RIGHT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(Cache[14], RIGHT * 0.2),
            FadeOutAndShiftDown(Cache[16], RIGHT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(Cache[17], RIGHT * 0.2),
            FadeOutAndShiftDown(Cache[18], RIGHT * 0.2),
            FadeOutAndShiftDown(Cache[8], DOWN * 0.2),
            FadeOutAndShiftDown(Cache[21], LEFT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(Cache[12], RIGHT * 0.2),
            FadeOutAndShiftDown(Cache[13], RIGHT * 0.2),
            FadeOutAndShiftDown(Cache[15], RIGHT * 0.2),
            FadeOutAndShiftDown(Cache[7], DOWN * 0.2),
            FadeOutAndShiftDown(Cache[20], LEFT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(Cache[0], RIGHT * 0.2),
            FadeOutAndShiftDown(Cache[1], RIGHT * 0.2),
            FadeOutAndShiftDown(Cache[2], RIGHT * 0.2),
            FadeOutAndShiftDown(Cache[3], RIGHT * 0.2),
            FadeOutAndShiftDown(Cache[10], RIGHT * 0.2),
            FadeOutAndShiftDown(Cache[11], RIGHT * 0.2),
            FadeOutAndShiftDown(Cache[4], RIGHT * 0.2),
            FadeOutAndShiftDown(Cache[6], RIGHT * 0.2),
            FadeOutAndShiftDown(Cache[3], RIGHT * 0.2)
        )
        self.play(
            Write(组答案[3])
        )

        self.play(
            FadeOutAndShiftDown(组答案[3], UP),
            ReplacementTransform(组虚线内未知[0], 组虚线内已知[0])
        )

        self.play(
            FadeOutAndShiftDown(组地址括号, UP),
            FadeOutAndShiftDown(组地址括号上字, UP)
        )
        self.play(
            ApplyMethod(组地址.shift, UP * 1.8),
            ApplyMethod(组地址虚线.shift, UP * 1.8),
            ApplyMethod(组虚线内已知.shift, UP * 1.8),
        )
        self.play(
            FadeOut(组地址),
            FadeOut(组地址虚线),
            FadeOut(组虚线内已知)
        )
        组地址.shift(DOWN * 1.8)
        组地址虚线.shift(DOWN * 1.8)
        组虚线内已知.shift(DOWN * 1.8)
        self.play(
            FadeOutAndShiftDown(问题[2], DOWN),
            FadeInFrom(问题[3], UP)
        )

        # 第四问
        self.play(
            FadeIn(四组地址)
        )
        self.play(
            Write(四组地址虚线)
        )
        self.play(
            Write(四组虚线内未知)
        )
        self.play(
            Write(四组答案[0])
        )

        self.play(
            FadeOutAndShiftDown(四组答案[0], UP)
        )

        self.play(
            FadeInFrom(四组地址括号, DOWN)
        )
        self.play(
            FadeInFrom(四组地址括号上字, DOWN)
        )
        self.play(
            Write(答案[1]),
            Write(块内[0]),
            Write(块内[1]),
            Write(块内[2]),
            Write(块内[3]),
            Write(块内[4]),
            FadeIn(块内[6])
        )
        self.play(
            FadeInFrom(块内[5], RIGHT * 0.2),
            FadeInFrom(块内[7], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(块内[9], RIGHT * 0.2),
            FadeInFrom(块内[8], DOWN * 0.2)
        )

        self.play(
            FadeOutAndShiftDown(答案[1], UP),
            ReplacementTransform(四组虚线内未知[2], 四组虚线内已知[2]),
            FadeOutAndShiftDown(块内[0], RIGHT),
            FadeOutAndShiftDown(块内[1], RIGHT),
            FadeOutAndShiftDown(块内[2], RIGHT),
            FadeOutAndShiftDown(块内[3], RIGHT),
            FadeOutAndShiftDown(块内[4], RIGHT),
            FadeOutAndShiftDown(块内[5], RIGHT),
            FadeOutAndShiftDown(块内[6], RIGHT),
            FadeOutAndShiftDown(块内[7], RIGHT),
            FadeOutAndShiftDown(块内[8], RIGHT),
            FadeOutAndShiftDown(块内[9], RIGHT),
        )
        # 四Cache 入
        self.play(
            Write(四Cache[0]),
            Write(四Cache[1]),
            Write(四Cache[2]),
            Write(四Cache[3]),
            Write(四Cache[4]),
            Write(四Cache[10]),
            Write(四Cache[11]),
            FadeIn(四Cache[6])
        )
        self.play(
            FadeInFrom(四Cache[20], LEFT * 0.2),
            FadeInFrom(四Cache[7], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(四Cache[21], LEFT * 0.2),
            FadeInFrom(四Cache[8], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(四Cache[12], RIGHT * 0.2),
            FadeInFrom(四Cache[13], RIGHT * 0.2)
        )
        self.play(
            FadeInFrom(四Cache[17], RIGHT * 0.2),
            FadeInFrom(四Cache[18], RIGHT * 0.2)
        )
        self.play(
            Write(四Cache[15])
        )
        self.play(
            FadeInFrom(四Cache[14], RIGHT * 0.2)
        )
        self.play(
            FadeInFrom(四Cache[19], RIGHT * 0.2)
        )
        self.play(
            Write(四Cache[16])
        )
        self.play(
            FadeInFrom(四Cache[5], RIGHT * 0.2)
        )
        self.play(
            FadeInFrom(四Cache[9], RIGHT * 0.2)
        )

        # 答案
        self.play(
            ReplacementTransform(四组虚线内未知[1], 四组虚线内已知[1])
        )

        # Cache 出
        self.play(
            FadeOutAndShiftDown(四Cache[9], RIGHT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(四Cache[5], RIGHT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(四Cache[19], RIGHT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(四Cache[14], RIGHT * 0.2),
            FadeOutAndShiftDown(四Cache[16], RIGHT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(四Cache[17], RIGHT * 0.2),
            FadeOutAndShiftDown(四Cache[18], RIGHT * 0.2),
            FadeOutAndShiftDown(四Cache[8], DOWN * 0.2),
            FadeOutAndShiftDown(四Cache[21], LEFT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(四Cache[12], RIGHT * 0.2),
            FadeOutAndShiftDown(四Cache[13], RIGHT * 0.2),
            FadeOutAndShiftDown(四Cache[15], RIGHT * 0.2),
            FadeOutAndShiftDown(四Cache[7], DOWN * 0.2),
            FadeOutAndShiftDown(四Cache[20], LEFT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(四Cache[0], RIGHT * 0.2),
            FadeOutAndShiftDown(四Cache[1], RIGHT * 0.2),
            FadeOutAndShiftDown(四Cache[2], RIGHT * 0.2),
            FadeOutAndShiftDown(四Cache[3], RIGHT * 0.2),
            FadeOutAndShiftDown(四Cache[10], RIGHT * 0.2),
            FadeOutAndShiftDown(四Cache[11], RIGHT * 0.2),
            FadeOutAndShiftDown(四Cache[4], RIGHT * 0.2),
            FadeOutAndShiftDown(四Cache[6], RIGHT * 0.2),
            FadeOutAndShiftDown(四Cache[3], RIGHT * 0.2)
        )
        self.play(
            Write(四组答案[3])
        )

        self.play(
            FadeOutAndShiftDown(四组答案[3], UP),
            ReplacementTransform(四组虚线内未知[0], 四组虚线内已知[0])
        )

        self.play(
            FadeOutAndShiftDown(四组地址括号, UP),
            FadeOutAndShiftDown(四组地址括号上字, UP)
        )
        self.play(
            ApplyMethod(四组地址.shift, UP * 1.8),
            ApplyMethod(四组地址虚线.shift, UP * 1.8),
            ApplyMethod(四组虚线内已知.shift, UP * 1.8),
        )
        self.play(
            FadeOut(四组地址),
            FadeOut(四组地址虚线),
            FadeOut(四组虚线内已知)
        )
        四组地址.shift(DOWN * 1.8)
        四组地址虚线.shift(DOWN * 1.8)
        四组虚线内已知.shift(DOWN * 1.8)
        self.play(
            FadeOut(问题[3])
        )

        '''''
        ###字编址结束
        self.play(
            FadeOut(字编址),
            FadeIn(T2.set_color("#4b6cc7"))
        )
        self.play(
            Write(字节编址),
            FadeIn(T2_2.set_color("#fdafc0"))
        )
        ###字节编址开始
        # 第一问开始
        self.play(
            FadeInFrom(问题[0], UP)
        )

        self.play(
            FadeIn(字节地址)
        )
        self.play(
            Write(字节地址虚线)
        )
        self.play(
            Write(字节虚线内未知)
        )
        self.play(
            Write(字节答案[0])
        )

        self.play(
            FadeOutAndShiftDown(字节答案[0], UP)
        )

        self.play(
            FadeInFrom(字节地址括号, DOWN)
        )
        self.play(
            FadeInFrom(字节地址括号上字, DOWN)
        )
        #块内开始

        self.play(
            Write(字节块内[0]),
            Write(字节块内[1]),
            Write(字节块内[2]),
            Write(字节块内[3]),
            Write(字节块内[4]),
            Write(字节块内[10]),
            Write(字节块内[11]),
            Write(字节块内[14]),
            Write(字节块内[15]),
            FadeIn(字节块内[6])
        )
        self.play(
            FadeInFrom(字节块内[12], DOWN * 0.2),
            FadeInFrom(字节块内[13], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(字节块内[16], DOWN * 0.2),
            FadeInFrom(字节块内[17], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(字节块内[5], RIGHT * 0.2),
            FadeInFrom(字节块内[7], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(字节块内[9], RIGHT * 0.2),
            FadeInFrom(字节块内[8], DOWN * 0.2)
        )
        self.play(
            Write(字节块内[18]),
            Write(字节块内[19])
        )
        self.play(
            Write(字节块内[20])
        )
        self.play(
            ReplacementTransform(字节虚线内未知[2], 字节虚线内已知[2]),
            FadeOut(字节块内[20])
        )
        self.play(
            FadeOut(字节块内[18]),
            FadeOut(字节块内[19])
        )
        self.play(
            FadeOutAndShiftDown(字节块内[9], RIGHT * 0.2),
            FadeOutAndShiftDown(字节块内[8], DOWN * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节块内[5], RIGHT * 0.2),
            FadeOutAndShiftDown(字节块内[7], DOWN * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节块内[16], DOWN * 0.2),
            FadeOutAndShiftDown(字节块内[17], DOWN * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节块内[12], DOWN * 0.2),
            FadeOutAndShiftDown(字节块内[13], DOWN * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节块内[0], RIGHT),
            FadeOutAndShiftDown(字节块内[1], RIGHT),
            FadeOutAndShiftDown(字节块内[2], RIGHT),
            FadeOutAndShiftDown(字节块内[3], RIGHT),
            FadeOutAndShiftDown(字节块内[4], RIGHT),
            FadeOutAndShiftDown(字节块内[10], RIGHT),
            FadeOutAndShiftDown(字节块内[11], RIGHT),
            FadeOutAndShiftDown(字节块内[14], RIGHT),
            FadeOutAndShiftDown(字节块内[15], RIGHT),
            FadeOutAndShiftDown(字节块内[6], RIGHT),
        )
        #块内结束
        self.play(
            Write(字节答案[2])
        )
        self.play(
            FadeOutAndShiftDown(字节答案[2], UP),
            ReplacementTransform(字节虚线内未知[1], 字节虚线内已知[1])
        )
        self.play(
            Write(字节答案[3])
        )
        self.play(
            FadeOutAndShiftDown(字节答案[3], UP),
            ReplacementTransform(字节虚线内未知[0], 字节虚线内已知[0])
        )
        self.play(
            FadeOutAndShiftDown(字节地址括号, UP),
            FadeOutAndShiftDown(字节地址括号上字, UP)
        )
        self.play(
            ApplyMethod(字节地址.shift, UP * 1.8),
            ApplyMethod(字节地址虚线.shift, UP * 1.8),
            ApplyMethod(字节虚线内已知.shift, UP * 1.8),
        )
        self.play(
            FadeOut(字节地址),
            FadeOut(字节地址虚线),
            FadeOut(字节虚线内已知)
        )
        地址.shift(DOWN * 1.8)
        地址虚线.shift(DOWN * 1.8)
        虚线内已知.shift(DOWN * 1.8)

        self.play(
            FadeOutAndShiftDown(问题[0], DOWN),
            FadeInFrom(问题[1], UP)
        )

        # 第二问

        self.play(
            FadeIn(字节全地址)
        )
        self.play(
            Write(字节全地址虚线)
        )
        self.play(
            Write(字节全虚线内未知)
        )
        self.play(
            Write(字节答案[0])
        )

        self.play(
            FadeOutAndShiftDown(字节答案[0], UP)
        )

        self.play(
            FadeInFrom(字节全地址括号, DOWN)
        )
        self.play(
            FadeInFrom(字节全地址括号上字, DOWN)
        )
        #块内开始
        self.play(
            Write(字节块内[0]),
            Write(字节块内[1]),
            Write(字节块内[2]),
            Write(字节块内[3]),
            Write(字节块内[4]),
            Write(字节块内[10]),
            Write(字节块内[11]),
            Write(字节块内[14]),
            Write(字节块内[15]),
            FadeIn(字节块内[6])
        )
        self.play(
            FadeInFrom(字节块内[12], DOWN * 0.2),
            FadeInFrom(字节块内[13], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(字节块内[16], DOWN * 0.2),
            FadeInFrom(字节块内[17], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(字节块内[5], RIGHT * 0.2),
            FadeInFrom(字节块内[7], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(字节块内[9], RIGHT * 0.2),
            FadeInFrom(字节块内[8], DOWN * 0.2)
        )
        self.play(
            Write(字节块内[18]),
            Write(字节块内[19])
        )
        self.play(
            Write(字节块内[20])
        )
        self.play(
            ReplacementTransform(字节全虚线内未知[1], 字节全虚线内已知[1]),
            FadeOut(字节块内[20])
        )
        self.play(
            FadeOut(字节块内[18]),
            FadeOut(字节块内[19])
        )
        self.play(
            FadeOutAndShiftDown(字节块内[9], RIGHT * 0.2),
            FadeOutAndShiftDown(字节块内[8], DOWN * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节块内[5], RIGHT * 0.2),
            FadeOutAndShiftDown(字节块内[7], DOWN * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节块内[16], DOWN * 0.2),
            FadeOutAndShiftDown(字节块内[17], DOWN * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节块内[12], DOWN * 0.2),
            FadeOutAndShiftDown(字节块内[13], DOWN * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节块内[0], RIGHT),
            FadeOutAndShiftDown(字节块内[1], RIGHT),
            FadeOutAndShiftDown(字节块内[2], RIGHT),
            FadeOutAndShiftDown(字节块内[3], RIGHT),
            FadeOutAndShiftDown(字节块内[4], RIGHT),
            FadeOutAndShiftDown(字节块内[10], RIGHT),
            FadeOutAndShiftDown(字节块内[11], RIGHT),
            FadeOutAndShiftDown(字节块内[14], RIGHT),
            FadeOutAndShiftDown(字节块内[15], RIGHT),
            FadeOutAndShiftDown(字节块内[6], RIGHT),
        )
        #块内结束
        self.play(
            Write(字节全答案[0])
        )
        self.play(
            FadeOutAndShiftDown(字节全答案[0], UP),
            ReplacementTransform(字节全虚线内未知[0], 字节全虚线内已知[0])
        )
        self.play(
            FadeOutAndShiftDown(字节全地址括号, UP),
            FadeOutAndShiftDown(字节全地址括号上字, UP)
        )
        self.play(
            ApplyMethod(字节全地址.shift, UP * 1.8),
            ApplyMethod(字节全地址虚线.shift, UP * 1.8),
            ApplyMethod(字节全虚线内已知.shift, UP * 1.8),
        )
        self.play(
            FadeOut(字节全地址),
            FadeOut(字节全地址虚线),
            FadeOut(字节全虚线内已知)
        )
        self.play(
            FadeOutAndShiftDown(问题[1], DOWN),
            FadeInFrom(问题[2], UP)
        )

        # 第三问
        self.play(
            FadeIn(字节组地址)
        )
        self.play(
            Write(字节组地址虚线)
        )
        self.play(
            Write(字节组虚线内未知)
        )
        self.play(
            Write(字节答案[0])
        )

        self.play(
            FadeOutAndShiftDown(字节答案[0], UP)
        )

        self.play(
            FadeInFrom(字节组地址括号, DOWN)
        )
        self.play(
            FadeInFrom(字节组地址括号上字, DOWN)
        )
        # 块内开始
        self.play(
            Write(字节块内[0]),
            Write(字节块内[1]),
            Write(字节块内[2]),
            Write(字节块内[3]),
            Write(字节块内[4]),
            Write(字节块内[10]),
            Write(字节块内[11]),
            Write(字节块内[14]),
            Write(字节块内[15]),
            FadeIn(字节块内[6])
        )
        self.play(
            FadeInFrom(字节块内[12], DOWN * 0.2),
            FadeInFrom(字节块内[13], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(字节块内[16], DOWN * 0.2),
            FadeInFrom(字节块内[17], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(字节块内[5], RIGHT * 0.2),
            FadeInFrom(字节块内[7], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(字节块内[9], RIGHT * 0.2),
            FadeInFrom(字节块内[8], DOWN * 0.2)
        )
        self.play(
            Write(字节块内[18]),
            Write(字节块内[19])
        )
        self.play(
            Write(字节块内[20])
        )
        self.play(
            ReplacementTransform(字节组虚线内未知[2], 字节组虚线内已知[2]),
            FadeOut(字节块内[20])
        )
        self.play(
            FadeOut(字节块内[18]),
            FadeOut(字节块内[19])
        )
        self.play(
            FadeOutAndShiftDown(字节块内[9], RIGHT * 0.2),
            FadeOutAndShiftDown(字节块内[8], DOWN * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节块内[5], RIGHT * 0.2),
            FadeOutAndShiftDown(字节块内[7], DOWN * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节块内[16], DOWN * 0.2),
            FadeOutAndShiftDown(字节块内[17], DOWN * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节块内[12], DOWN * 0.2),
            FadeOutAndShiftDown(字节块内[13], DOWN * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节块内[0], RIGHT),
            FadeOutAndShiftDown(字节块内[1], RIGHT),
            FadeOutAndShiftDown(字节块内[2], RIGHT),
            FadeOutAndShiftDown(字节块内[3], RIGHT),
            FadeOutAndShiftDown(字节块内[4], RIGHT),
            FadeOutAndShiftDown(字节块内[10], RIGHT),
            FadeOutAndShiftDown(字节块内[11], RIGHT),
            FadeOutAndShiftDown(字节块内[14], RIGHT),
            FadeOutAndShiftDown(字节块内[15], RIGHT),
            FadeOutAndShiftDown(字节块内[6], RIGHT),
        )
        # 块内结束
        # Cache 入
        self.play(
            Write(字节Cache[0]),
            Write(字节Cache[1]),
            Write(字节Cache[2]),
            Write(字节Cache[3]),
            Write(字节Cache[4]),
            Write(字节Cache[10]),
            Write(字节Cache[11]),
            Write(字节Cache[22]),
            Write(字节Cache[23]),
            Write(字节Cache[26]),
            Write(字节Cache[27]),
            FadeIn(字节Cache[6])
        )
        self.play(
            FadeInFrom(字节Cache[24], DOWN * 0.2),
            FadeInFrom(字节Cache[25], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(字节Cache[28], DOWN * 0.2),
            FadeInFrom(字节Cache[29], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(字节Cache[20], LEFT * 0.2),
            FadeInFrom(字节Cache[7], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(字节Cache[21], LEFT * 0.2),
            FadeInFrom(字节Cache[8], DOWN * 0.2)
        )
        self.play(
            FadeInFrom(字节Cache[12], RIGHT * 0.2),
            FadeInFrom(字节Cache[13], RIGHT * 0.2)
        )
        self.play(
            FadeInFrom(字节Cache[17], RIGHT * 0.2),
            FadeInFrom(字节Cache[18], RIGHT * 0.2)
        )
        self.play(
            Write(字节Cache[15])
        )
        self.play(
            FadeInFrom(字节Cache[14], RIGHT * 0.2)
        )
        self.play(
            FadeInFrom(字节Cache[19], RIGHT * 0.2)
        )
        self.play(
            Write(字节Cache[16])
        )
        self.play(
            FadeInFrom(字节Cache[5], RIGHT * 0.2)
        )
        self.play(
            FadeInFrom(字节Cache[9], RIGHT * 0.2)
        )

        # 答案
        self.play(
            ReplacementTransform(字节组虚线内未知[1], 字节组虚线内已知[1])
        )

        '''''
        # Cache 出
        self.play(
            FadeOutAndShiftDown(字节Cache[9], RIGHT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节Cache[5], RIGHT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节Cache[19], RIGHT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节Cache[14], RIGHT * 0.2),
            FadeOutAndShiftDown(字节Cache[16], RIGHT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节Cache[17], RIGHT * 0.2),
            FadeOutAndShiftDown(字节Cache[18], RIGHT * 0.2),
            FadeOutAndShiftDown(字节Cache[8], DOWN * 0.2),
            FadeOutAndShiftDown(字节Cache[21], LEFT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节Cache[12], RIGHT * 0.2),
            FadeOutAndShiftDown(字节Cache[13], RIGHT * 0.2),
            FadeOutAndShiftDown(字节Cache[15], RIGHT * 0.2),
            FadeOutAndShiftDown(字节Cache[7], DOWN * 0.2),
            FadeOutAndShiftDown(字节Cache[20], LEFT * 0.2)
        )
        self.play(
            FadeOutAndShiftDown(字节Cache[0], RIGHT * 0.2),
            FadeOutAndShiftDown(字节Cache[1], RIGHT * 0.2),
            FadeOutAndShiftDown(字节Cache[2], RIGHT * 0.2),
            FadeOutAndShiftDown(字节Cache[3], RIGHT * 0.2),
            FadeOutAndShiftDown(字节Cache[10], RIGHT * 0.2),
            FadeOutAndShiftDown(字节Cache[11], RIGHT * 0.2),
            FadeOutAndShiftDown(字节Cache[4], RIGHT * 0.2),
            FadeOutAndShiftDown(字节Cache[6], RIGHT * 0.2),
            FadeOutAndShiftDown(字节Cache[3], RIGHT * 0.2)
        )
        '''





        self.wait(1)
        '''
        self.add(全地址)
        self.add(全地址括号)
        self.add(全地址括号上字)
        self.add(全地址虚线)
        '''




        """"
        #全部结束
        self.wait(1)
        self.play(
            FadeOut(line1),
            FadeOut(T1),
            FadeOut(T2),
            run_time=1.5
        )
        self.play(
            Title.scale, 3.33,
            Title.move_to, DOWN * 0 + LEFT * 0.0,
            run_time=2
        )
        self.wait(1)
        self.play(FadeOut(Title), run_time=3)

        self.play(
            logo.set_height, 1,
            logo.move_to, UP * 0.2,
            run_time=2
        )
        self.play(FadeOut(logo))

        self.wait(1)

        self.remove(logo)
        logo.move_to(UP * 0.2)
        logo.set_height(1)
        self.add(logo)
        """






