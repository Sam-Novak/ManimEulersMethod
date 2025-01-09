from manim import *

class main(Scene):
    def construct(self):
        all_scenes = [Intro,SimpleAttempt,SimpleAttemptLines,SimpleAttemptExplained]
        for test in all_scenes:
            test.construct(self)   
        
class Intro(Scene):
    def construct(self):
        Euler= Text("Euler's Method")
        self.wait(1)
        self.play(Write(Euler))
        self.wait(1)
        SimpleEQ = MathTex(r"\frac{dy}{dx} = y")
        self.play(Euler.animate.shift(2*UP))
        self.play(Write(SimpleEQ))
        self.wait(1)
        self.play(Transform(SimpleEQ,Text("m = y")))
        self.play(SimpleEQ.animate.to_edge(DL,buff=0.5),Euler.animate.shift(3*UP))
        self.clear()

class SimpleAttempt(Scene):
    def construct(self):
        my=Text("m = y").to_edge(DL,buff=0.5)
        self.add(my)

        grid = Axes(
            x_range=(-1,5,1),
            y_range=(-1,5,1),
            x_length=5,
            y_length=5,
        )

        self.add(grid)
        self.play(Write(grid.add_coordinates()),run_time=2)
        
        AllReals=Square(side_length=6, stroke_color = BLACK, stroke_opacity=0, fill_color = RED, fill_opacity = 0.75,)
        self.play(Write(AllReals))
        self.play(AllReals.animate.fade(darkness=1))
        
        Point01=Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1))
        Point01.move_to((0,0,0))
        self.play(DrawBorderThenFill(Point01))

        # grid.shift(RIGHT)
        goal=grid.coords_to_point(0,2,0)
        
        Point01Line=always_redraw(lambda :
                    DashedLine(start= Point01.get_center(),end=goal,color=GREEN_C)
        )

        InitialX = Text("When x=0")
        InitialX.to_edge(DL,buff=0.5).shift(1*UP)
        
        self.play(Write(Point01Line,run_time=0.2))
        self.play(Write(InitialX),Point01.animate.move_to(goal))

        goal=grid.coords_to_point(0,1,0)
        InitialY = Text("Y=1")
        InitialY.to_edge(DL,buff=0.5).shift(2*UP)
        
        self.play(Write(Point01Line,run_time=0.2))
        self.play(Write(InitialY),Point01.animate.move_to(goal))

        Initial = MathTex("f(0)=1")
        Initial.to_edge(DL,buff=0.5).shift(1*UP)
        self.play(InitialX.animate.become(Initial),InitialY.animate.become(Initial))

        self.clear()
   
class SimpleAttemptLines(Scene):
    def construct(self):
        my=Text("m = y").to_edge(DL,buff=0.5)
        Initial = MathTex("f(0)=1").to_edge(DL,buff=0.5).shift(1*UP)

        Grid = Axes(
            x_range=(-1,5,1),
            y_range=(-1,5,1),
            x_length=5,
            y_length=5,
        ).add_coordinates().set_z_index(-10)
        
        DataTable=Table(
            table=[["0.00","1.00","1.00"],
                   ["0.00","1.00","1.00"],
                   ["0.00","1.00","1.00"],
                   ["0.00","1.00","1.00"]],
            col_labels=[Text("x"),Text("y"),MathTex(r"\frac{dy}{dx}")]
            
        ).scale(0.6).to_edge(UL).shift(0.3*DOWN)
        
        DataTable[5].set_points_by_ends(end=(DataTable[5].get_start()[0],DataTable[2].get_start()[1],0),start= DataTable[5].get_end())
        DataTable[6].set_points_by_ends(end=(DataTable[6].get_start()[0],DataTable[2].get_start()[1],0),start= DataTable[6].get_end())

        DataTable[0][3]=Text("0.00",).move_to(DataTable[0][3].get_center()).scale(0.6)
        DataTable[0][4]=Text("1.00",).move_to(DataTable[0][4].get_center()).scale(0.6)
        DataTable[0][5]=Text("1.00",).move_to(DataTable[0][5].get_center()).scale(0.6)
        DataTable[0][6]=Text("0.00",).move_to(DataTable[0][6].get_center()).scale(0.6)
        DataTable[0][7]=Text("0.00",).move_to(DataTable[0][7].get_center()).scale(0.6)
        DataTable[0][8]=Text("0.00",).move_to(DataTable[0][8].get_center()).scale(0.6)
        DataTable[0][9]=Text("0.00",).move_to(DataTable[0][9].get_center()).scale(0.6)
        DataTable[0][10]=Text("0.00",).move_to(DataTable[0][10].get_center()).scale(0.6)
        DataTable[0][11]=Text("0.00",).move_to(DataTable[0][11].get_center()).scale(0.6)
        DataTable[0][12]=Text("3.00",).move_to(DataTable[0][12].get_center()).scale(0.6)
        DataTable[0][13]=Text("8.00",).move_to(DataTable[0][13].get_center()).scale(0.6)
        DataTable[0][14]=Text("8.00",).move_to(DataTable[0][14].get_center()).scale(0.6)

        InitialPoint=Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1))
        InitialPoint.move_to(Grid.coords_to_point(0,1)).set_z_index(3)

        Slope1b=Arrow(start=Grid.c2p(0,1,0),end=Grid.c2p(-1.2,-0.2,0),color=RED,buff=0,tip_shape=StealthTip)
        Slope1=Arrow(start=Grid.c2p(0,1,0),end=Grid.c2p(4.2,5.2,0),color=RED,buff=0,tip_shape=StealthTip)     

        PointTwo=(Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1)))
        PointTwo.move_to(Grid.c2p(0.001,1,0))
        
        DataTable[0][6] = always_redraw(
            lambda : Text(
                text=f'{Grid.p2c(PointTwo.get_center())[0]:.2f}',
                
                ).move_to(DataTable[0][6].get_center()).scale(0.6)
        )
        
        DataTable[0][7] = always_redraw(
            lambda : Text(
                text=f'{Grid.p2c(PointTwo.get_center())[1]:.2f}',
                
                ).move_to(DataTable[0][7].get_center()).scale(0.6)
        )

        DataTable[0][8] = always_redraw(
            lambda : Text(
                text=f'{Grid.p2c(PointTwo.get_center())[1]:.2f}',
                
                ).move_to(DataTable[0][8].get_center()).scale(0.6)
        )

        PointTwo.shift(2*RIGHT)
        
        SlopeTwoA = always_redraw(
            lambda : DashedLine(start=(PointTwo.get_center()),end=(PointTwo.get_center())-normalize((1,Grid.p2c(PointTwo.get_center())[1],0)),color=GREEN_C)
        )
        SlopeTwoB = always_redraw(
            lambda : DashedLine(start=(PointTwo.get_center()),end=(PointTwo.get_center())+normalize((1,Grid.p2c(PointTwo.get_center())[1],0)),color=GREEN_C)
        )
        
        self.add(Initial,my,Grid,InitialPoint)

        self.play(Write(Slope1),Write(Slope1b))   

        self.play(
            Write(DataTable[0][0:6]),
            Write(DataTable[5:]),
            Write(DataTable[1]),
            Grid.animate.shift(2*RIGHT),
            Slope1.animate.shift(2*RIGHT),
            Slope1b.animate.shift(2*RIGHT),
            InitialPoint.animate.shift(2*RIGHT),
            )
    
        self.play(FadeIn(PointTwo))

        self.play(
            DataTable[5].animate.set_points_by_ends(end=(DataTable[5].get_start()[0],DataTable[3].get_start()[1],0),start= DataTable[5].get_start()),
            DataTable[6].animate.set_points_by_ends(end=(DataTable[6].get_start()[0],DataTable[3].get_start()[1],0),start= DataTable[6].get_start()),
            Write(DataTable[2]),
            Write(DataTable[0][6:9])
        )
        
        self.play(Write(SlopeTwoA),Write(SlopeTwoB))

        self.play(PointTwo.animate.move_to(Grid.c2p(3.5,4.5,0)),run_time=1.5)
        self.play(PointTwo.animate.move_to(Grid.c2p(-0.5,0.5,0)),run_time=1.6)
        self.play(PointTwo.animate.move_to(Grid.c2p(1,2,0)))

        DataTable[0][6].clear_updaters()
        DataTable[0][7].clear_updaters()
        DataTable[0][8].clear_updaters()
        
        self.play(Unwrite(SlopeTwoA),Unwrite(SlopeTwoB))

        Slope1.set_points_by_ends(start=Grid.c2p(1,2,0),end=Grid.c2p(4.2,5.2,0))
        Segment1=Line(start=Grid.c2p(0,1,0),end=Grid.c2p(1,2,0),color=RED,stroke_width=6).set_z_index(-3)
        Slope2=Arrow(start=Grid.c2p(1,2,0),end=Grid.c2p(2.8,5.6,0),color=RED,buff=0,tip_shape=StealthTip)
        
        self.add(Segment1)
        self.play(
            Unwrite(Slope1b),
            Transform(Slope1,Slope2)
        )
        #============================          

        PointThree=(Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1)))
        PointThree.move_to(Grid.c2p(1,2,0))
        
        DataTable[0][9] = always_redraw(
            lambda : Text(
                text=f'{Grid.p2c(PointThree.get_center())[0]:.2f}',
                
                ).move_to(DataTable[0][9].get_center()).scale(0.6)
        )
        
        DataTable[0][10] = always_redraw(
            lambda : Text(
                text=f'{Grid.p2c(PointThree.get_center())[1]:.2f}',
                
                ).move_to(DataTable[0][10].get_center()).scale(0.6)
        )

        DataTable[0][11] = always_redraw(
            lambda : Text(
                text=f'{Grid.p2c(PointThree.get_center())[1]:.2f}',
                
                ).move_to(DataTable[0][11].get_center()).scale(0.6)
        )
        
        SlopeThreeA = always_redraw(
            lambda : DashedLine(start=(PointThree.get_center()),end=(PointThree.get_center())-normalize((1,Grid.p2c(PointThree.get_center())[1],0)),color=GREEN_C)
        )
        SlopeThreeB = always_redraw(
            lambda : DashedLine(start=(PointThree.get_center()),end=(PointThree.get_center())+normalize((1,Grid.p2c(PointThree.get_center())[1],0)),color=GREEN_C)
        )

        self.play(FadeIn(PointThree))

        self.play(
            DataTable[5].animate.set_points_by_ends(end=(DataTable[5].get_start()[0],DataTable[4].get_start()[1],0),start= DataTable[5].get_start()),
            DataTable[6].animate.set_points_by_ends(end=(DataTable[6].get_start()[0],DataTable[4].get_start()[1],0),start= DataTable[6].get_start()),
            Write(DataTable[3]),
            Write(DataTable[0][9:12])
        )

        self.play(Write(SlopeThreeA),Write(SlopeThreeB))

        self.play(PointThree.animate.move_to(Grid.c2p(2.4,4.8,0)),run_time=2)
        self.play(PointThree.animate.move_to(Grid.c2p(2,4,0)))

        DataTable[0][9].clear_updaters()
        DataTable[0][10].clear_updaters()
        DataTable[0][11].clear_updaters()

        self.play(Unwrite(SlopeThreeA),Unwrite(SlopeThreeB))
        
        PointThree.set_z_index(3)

        Slope2B=Arrow(start=Grid.c2p(1,1,0),end=Grid.c2p(4.5,4.5,0),color=RED,buff=0,tip_shape=StealthTip)
        Slope3=Arrow(start=Grid.c2p(2,2,0),end=Grid.c2p(3.8,5.6,0),color=RED,buff=0,tip_shape=StealthTip)

        newPoints=[(Grid.coords_to_point(0,0.5,0)[0],  Grid.coords_to_point(0,0.5,0)[1],  3),
                   (Grid.coords_to_point(0,0.5,0)[0],  Grid.coords_to_point(0,0.5,0)[1], -3),
                   (Grid.coords_to_point(1,1  ,0)[0],  Grid.coords_to_point(1,1  ,0)[1], -3),
                   (Grid.coords_to_point(1,1  ,0)[0],  Grid.coords_to_point(1,1  ,0)[1],  3),
                   (Grid.coords_to_point(2,2  ,0)[0],  Grid.coords_to_point(2,2  ,0)[1],  0)]
        
        self.remove(Slope1)

        self.play(Transform(Grid,Axes(
                                      x_range=(-1,5,1),
                                      y_range=(-2,10,2),
                                      x_length=5,
                                      y_length=5,
                                      ).add_coordinates().set_z_index(-10).shift(2*RIGHT)),
                  InitialPoint.animate.move_to(newPoints[0]),
                  Segment1.animate.set_points_by_ends(start=newPoints[1],end=newPoints[2]),
                  PointTwo.animate.move_to(newPoints[3]),
                  PointThree.animate.move_to(newPoints[4]),
                  Transform(Slope2,Slope2B)
                )
        
        self.remove(Slope2)
        Slope2B.set_points_by_ends(start=Grid.c2p(2,2,0),end=Grid.c2p(4.5,4.5,0))

        Segment2=Line(start=Grid.c2p(1,1,0),end=Grid.c2p(2,2,0),color=RED,stroke_width=6).set_z_index(-3)
        self.add(Segment2)

        self.play(Transform(Slope2B,Slope3))
        self.remove(Slope3)
        self.play(
            DataTable[5].animate.set_points_by_ends(end=(DataTable[5].get_start()[0],2*DataTable[4].get_start()[1]-DataTable[3].get_start()[1],0),start= DataTable[5].get_start()),
            DataTable[6].animate.set_points_by_ends(end=(DataTable[6].get_start()[0],2*DataTable[4].get_start()[1]-DataTable[3].get_start()[1],0),start= DataTable[6].get_start()),
            Write(DataTable[4]),
            Write(DataTable[0][12:])
        )
        PointFour=Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1))
        PointFour.move_to(Grid.c2p(3,4,0))
        PointFour.set_z_index(3)
        self.play(Write(PointFour))
        Segment3=Line(start=Grid.c2p(2,2,0),end=Grid.c2p(3,4,0),color=RED,stroke_width=6).set_z_index(-3)
        self.add(Segment3)
        Slope2B.set_points_by_ends(start=Grid.c2p(3,4,0),end=Grid.c2p(3.8,5.6,0))
        Slope4=Arrow(start=Grid.c2p(3,4,0),end=Grid.c2p(3.5,6,0),color=RED,buff=0,tip_shape=StealthTip)
        self.play(Transform(Slope2B,Slope4))

        self.clear()

class SimpleAttemptExplained(Scene):
    def construct(self):
        my=Text("m = y").to_edge(DL,buff=0.5)
        Initial = MathTex("f(0)=1").to_edge(DL,buff=0.5).shift(1*UP)
        
        Grid = Axes(x_range=(-1,5,1),
                    y_range=(-2,10,2),
                    x_length=5,
                    y_length=5,
                    ).add_coordinates().set_z_index(-10).shift(2*RIGHT)

        DataTable=Table(
            table=[["0.0","1.0","1.0"],
                   ["0.0","1.0","1.0"],
                   ["0.0","1.0","1.0"],
                   ["0.0","1.0","1.0"]],
            col_labels=[Text("x"),Text("y"),MathTex(r"\frac{dy}{dx}")]
        ).scale(0.6).to_edge(UL).shift(0.3*DOWN)

        DataTable[0][3]=Text("0.0",).move_to(DataTable[0][3].get_center()).scale(0.6)
        DataTable[0][4]=Text("1.0",).move_to(DataTable[0][4].get_center()).scale(0.6)
        DataTable[0][5]=Text("1.0",).move_to(DataTable[0][5].get_center()).scale(0.6)
        DataTable[0][6]=Text("1.0",).move_to(DataTable[0][6].get_center()).scale(0.6)
        DataTable[0][7]=Text("2.0",).move_to(DataTable[0][7].get_center()).scale(0.6)
        DataTable[0][8]=Text("2.0",).move_to(DataTable[0][8].get_center()).scale(0.6)
        DataTable[0][9]=Text("2.0",).move_to(DataTable[0][9].get_center()).scale(0.6)
        DataTable[0][10]=Text("4.0",).move_to(DataTable[0][10].get_center()).scale(0.6)
        DataTable[0][11]=Text("4.0",).move_to(DataTable[0][11].get_center()).scale(0.6)
        DataTable[0][12]=Text("3.0",).move_to(DataTable[0][12].get_center()).scale(0.6)
        DataTable[0][13]=Text("8.0",).move_to(DataTable[0][13].get_center()).scale(0.6)
        DataTable[0][14]=Text("8.0",).move_to(DataTable[0][14].get_center()).scale(0.6)

        PointOne=Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1))
        PointOne.move_to(Grid.c2p(0,1)).set_z_index(3)  

        PointTwo=(Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1)))
        PointTwo.move_to(Grid.c2p(1,2)).set_z_index(3)

        PointThree=(Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1)))
        PointThree.move_to(Grid.c2p(2,4)).set_z_index(3)

        PointFour=Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1))
        PointFour.move_to(Grid.c2p(3,8)).set_z_index(3)

        Segment1=Line(start=Grid.c2p(0,1,0),end=Grid.c2p(1,2,0),color=RED,stroke_width=6).set_z_index(-3)        
        Segment2=Line(start=Grid.c2p(1,2,0),end=Grid.c2p(2,4,0),color=RED,stroke_width=6).set_z_index(-3)
        Segment3=Line(start=Grid.c2p(2,4,0),end=Grid.c2p(3,8,0),color=RED,stroke_width=6).set_z_index(-3)
        Ray4=Arrow(start=Grid.c2p(3,8,0),end=Grid.c2p(3.5,12,0),color=RED,buff=0,tip_shape=StealthTip)

        self.add(
            my,
            Initial,
            Grid,
            DataTable,
            PointOne,
            PointTwo,
            PointThree,
            PointFour,
            Segment1,
            Segment2,
            Segment3,
            Ray4
        )
        
        ApproximationText= MathTex(r"f(x)=2^x",color=PURPLE_A).scale(1.3)
        ApproximationText.to_edge(DL,buff=0.5).shift(2.5*RIGHT)
        self.play(Write(ApproximationText))
        Approximation = Grid.plot(function=lambda x:2**x,x_range=(-0.1,3),color=PURPLE,stroke_width=9)
        self.play(Write(Approximation),
                  Unwrite(Segment1),
                  Unwrite(Segment2),
                  Unwrite(Segment3),
                  Unwrite(Ray4),
                  run_time=2)
        
        RealText= MathTex(r"f(x)=e^x",color=GREEN_A).scale(1.3)
        RealText.to_edge(DL,buff=1.5).shift(1.5*RIGHT)
        RealGraph = Grid.plot(function= lambda x:2.71828**x,x_range=(-0.1,4),color=GREEN_A,stroke_width=9)
        self.play(Write(RealText),
                  Write(RealGraph))
        
        self.play(Transform(DataTable[0][2],MathTex(r"e^x",color=GREEN_A).move_to(DataTable[0][2].get_center()).scale(1)),
                  Transform(DataTable[0][5],Text("1",color=GREEN_A).move_to(DataTable[0][5].get_center()).scale(.6)),
                  Transform(DataTable[0][8],Text("2.7",color=GREEN_A).move_to(DataTable[0][8].get_center()).scale(.6)),
                  Transform(DataTable[0][11],Text("7.4",color=GREEN_A).move_to(DataTable[0][11].get_center()).scale(.6)),
                  Transform(DataTable[0][14],Text("20.1",color=GREEN_A).move_to(DataTable[0][14].get_center()).scale(.6)),
                  Transform(DataTable[0][1],MathTex(r"2^x",color=PURPLE).move_to(DataTable[0][1].get_center()).scale(1)),
                  Transform(DataTable[0][4],Text("1.0",color=PURPLE).move_to(DataTable[0][4].get_center()).scale(.6)),
                  Transform(DataTable[0][7],Text("2.0",color=PURPLE).move_to(DataTable[0][7].get_center()).scale(.6)),
                  Transform(DataTable[0][10],Text("4.0",color=PURPLE).move_to(DataTable[0][10].get_center()).scale(.6)),
                  Transform(DataTable[0][13],Text("8.0",color=PURPLE).move_to(DataTable[0][13].get_center()).scale(.6)),
        )
        
        ErrorValues= VGroup(
            Text("Error",stroke_color=RED_E,color=RED_E).move_to(DataTable[0][2 ]).shift(1.6*RIGHT).scale(0.7),
            Text("0%"   ,stroke_color=RED_E,color=RED_E).move_to(DataTable[0][5 ]).shift(1.6*RIGHT).scale(0.7),
            Text("26%"  ,stroke_color=RED_E,color=RED_E).move_to(DataTable[0][8 ]).shift(1.6*RIGHT).scale(0.7),
            Text("46%"  ,stroke_color=RED_E,color=RED_E).move_to(DataTable[0][11]).shift(1.6*RIGHT).scale(0.7),
            Text("60%"  ,stroke_color=RED_E,color=RED_E).move_to(DataTable[0][14]).shift(1.6*RIGHT).scale(0.7))
        
        self.play(Write(ErrorValues))
        
        TotalError = Text("47%"  ,stroke_color=RED_E,color=RED_E).move_to(DataTable[0][8]).shift(1.6*RIGHT)
        
        self.play(Transform(ErrorValues,TotalError))
        self.wait()

        self.play(mob.animate.shift(15*LEFT) for mob in self.mobjects)
        
        Limit =MathTex(r"\lim_{x \to \infty} \frac{f(x)}{x}").scale(2)
        self.play(Write(Limit))
        LimitProblem= VGroup(MathTex(r"\frac{dy}{dx}=y").shift(UP).scale(2),Text("f(0)=1").shift(DOWN*1.2).scale(1.5))

        LimitProblem.shift(RIGHT*3)

        self.play(
            Limit.animate.shift(LEFT*3),
            Write(LimitProblem)
        )
        
        Estimation = MathTex(r"f(x)=2^x",color=RED).scale(2).move_to(LimitProblem)
        self.play(Transform(LimitProblem,Estimation))
        euqalsign= Text("≈").scale(2)
        true=MathTex(r"\lim_{x \to \infty} \frac{e^x}{x}",color=GREEN).scale(2).shift(RIGHT*3)
        self.remove(LimitProblem,Estimation,TotalError)
        self.play(Transform(Estimation,MathTex(r"\lim_{x \to \infty} \frac{2^x}{x}",color=RED).scale(2).shift(LEFT*3)),FadeOut(Limit))
        self.play(Write(true),Write(euqalsign))
        self.play(Indicate(euqalsign))

        self.play(mob.animate.shift(15*RIGHT) for mob in self.mobjects)

        self.remove(
            Limit,
            LimitProblem,
            Estimation,
            euqalsign,
            true
        )

        self.clear()
        