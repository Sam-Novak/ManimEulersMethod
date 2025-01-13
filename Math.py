from manim import *
import math

class main(Scene):
    def construct(self):
        all_scenes = [Intro,
                      SimpleAttempt,
                      SimpleAttemptLines,
                      SimpleAttemptExplained,
                      SecondAttempt, 
                      Problem2,
                      Problem3]
        for test in all_scenes:
            test.construct(self)   
        
class BaseMaterials(Scene):
    def my(): return Text("m = y").to_edge(DL,buff=0.5)
    
    def Initial(): return MathTex("f(0)=1").to_edge(DL,buff=0.5).shift(1*UP)
    
    def Grid(): return Axes(x_range=(-1,5,1),
                y_range=(-1,5,1),
                x_length=5,
                y_length=5,
                ).add_coordinates().set_z_index(-10).shift(2*RIGHT)
    
    def Grid2(): return Axes(x_range=(-1,5,1),
                y_range=(-2,10,2),
                x_length=5,
                y_length=5,
                ).add_coordinates().set_z_index(-10).shift(2*RIGHT)

    def DataTable(): return Table(
        table=[["0.0","1.0","1.0"],
                ["1.0","2.0","2.0"],
                ["2.0","4.0","4.0"],
                ["3.0","8.0","8.0"]],
        col_labels=[Text("x"),Text("y"),MathTex(r"\frac{dy}{dx}")]
    ).scale(0.6).to_edge(UL).shift(0.3*DOWN)

    def Point1(Grid=Grid()): return Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1)).move_to(Grid.c2p(0,1)).set_z_index(3)  
    def Point2(Grid=Grid()): return (Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1))).move_to(Grid.c2p(1,2)).set_z_index(3)
    def Point3(Grid=Grid()): return (Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1))).move_to(Grid.c2p(2,4)).set_z_index(3)
    def Point4(Grid=Grid()): return Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1)).move_to(Grid.c2p(3,8)).set_z_index(3)

    def Segment1(Grid=Grid()): return Line(start=Grid.c2p(0,1,0),end=Grid.c2p(1,2,0),color=RED,stroke_width=6).set_z_index(-3)        
    def Segment2(Grid=Grid()): return Line(start=Grid.c2p(1,2,0),end=Grid.c2p(2,4,0),color=RED,stroke_width=6).set_z_index(-3)
    def Segment3(Grid=Grid()): return Line(start=Grid.c2p(2,4,0),end=Grid.c2p(3,8,0),color=RED,stroke_width=6).set_z_index(-3)
    def Ray4(Grid=Grid()): return Arrow(start=Grid.c2p(3,8,0),end=Grid.c2p(3.5,12,0),color=RED,buff=0,tip_shape=StealthTip)
    
    def eulersMethod(Equation, Initial,step,PointCount, MakeFancyPoints=False, MakeLines= False,Grid=Grid()):
        Points = [Initial]
        
        for i in range(1,PointCount):
            Points.append((Points[i-1][0]+step,Points[i-1][1]+step*Equation(*Points[i-1])))
            
        Pnts = VGroup()
        for pnt in Points:
            Pnts.add(Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1
                    ).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1)
                    ).move_to(Grid.c2p(pnt[0],pnt[1])).set_z_index(3))
            
        Lines = VGroup()
        for i in range(PointCount-1):
            Lines.add(Line(start=Grid.c2p(*Points[i])
                    ,end=Grid.c2p(*Points[i+1])
                    ,color=RED,stroke_width=6).set_z_index(-3))
            
        if not MakeFancyPoints and not MakeLines:
            return Points    
        if MakeFancyPoints and not MakeLines:
            return Pnts
        if MakeLines and not MakeFancyPoints:
            return Lines    
        if MakeFancyPoints and MakeLines:
            return Pnts,Lines
            
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
        self.add(BaseMaterials.my())

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

        self.play(Point01.animate.shift(2*RIGHT),grid.animate.shift(2*RIGHT))
        self.clear()
   
class SimpleAttemptLines(Scene):
    def construct(self):
        
        DataTable = BaseMaterials.DataTable()
        Grid = BaseMaterials.Grid()
        
        self.add(
            BaseMaterials.my(),
            BaseMaterials.Initial(),
            Grid,)
        
        DataTable[5].set_points_by_ends(end=(DataTable[5].get_start()[0],DataTable[2].get_start()[1],0),start= DataTable[5].get_end())
        DataTable[6].set_points_by_ends(end=(DataTable[6].get_start()[0],DataTable[2].get_start()[1],0),start= DataTable[6].get_end())

        InitialPoint=Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1))
        InitialPoint.move_to(Grid.coords_to_point(0,1)).set_z_index(3)

        Slope1b=Arrow(start=Grid.c2p(0,1,0),end=Grid.c2p(-1.2,-0.2,0),color=RED,buff=0,tip_shape=StealthTip)
        Slope1=Arrow(start=Grid.c2p(0,1,0),end=Grid.c2p(4.2,5.2,0),color=RED,buff=0,tip_shape=StealthTip)     

        Point2=(Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1)))
        Point2.move_to(Grid.c2p(0.001,1,0))
        
        DataTable[0][6] = always_redraw(
            lambda : Text(
                text=f'{Grid.p2c(Point2.get_center())[0]:.1f}',
                
                ).move_to(DataTable[0][6].get_center()).scale(0.6)
        )
        
        DataTable[0][7] = always_redraw(
            lambda : Text(
                text=f'{Grid.p2c(Point2.get_center())[1]:.1f}',
                
                ).move_to(DataTable[0][7].get_center()).scale(0.6)
        )

        DataTable[0][8] = always_redraw(
            lambda : Text(
                text=f'{Grid.p2c(Point2.get_center())[1]:.1f}',
                
                ).move_to(DataTable[0][8].get_center()).scale(0.6)
        )

        Point2.shift(2*RIGHT)
        
        Slope2A = always_redraw(
            lambda : DashedLine(start=(Point2.get_center()),end=(Point2.get_center())-normalize((1,Grid.p2c(Point2.get_center())[1],0)),color=GREEN_C)
        )
        Slope2B = always_redraw(
            lambda : DashedLine(start=(Point2.get_center()),end=(Point2.get_center())+normalize((1,Grid.p2c(Point2.get_center())[1],0)),color=GREEN_C)
        )
    
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
    
        self.play(FadeIn(Point2))

        self.play(
            DataTable[5].animate.set_points_by_ends(end=(DataTable[5].get_start()[0],DataTable[3].get_start()[1],0),start= DataTable[5].get_start()),
            DataTable[6].animate.set_points_by_ends(end=(DataTable[6].get_start()[0],DataTable[3].get_start()[1],0),start= DataTable[6].get_start()),
            Write(DataTable[2]),
            Write(DataTable[0][6:9])
        )
        
        self.play(Write(Slope2A),Write(Slope2B))

        self.play(Point2.animate.move_to(Grid.c2p(3.5,4.5,0)),run_time=1.5)
        self.play(Point2.animate.move_to(Grid.c2p(-0.5,0.5,0)),run_time=1.6)
        self.play(Point2.animate.move_to(Grid.c2p(1,2,0)))

        DataTable[0][6].clear_updaters()
        DataTable[0][7].clear_updaters()
        DataTable[0][8].clear_updaters()
        
        self.play(Unwrite(Slope2A),Unwrite(Slope2B))

        Slope1.set_points_by_ends(start=Grid.c2p(1,2,0),end=Grid.c2p(4.2,5.2,0))
        Segment1=Line(start=Grid.c2p(0,1,0),end=Grid.c2p(1,2,0),color=RED,stroke_width=6).set_z_index(-3)
        Slope2=Arrow(start=Grid.c2p(1,2,0),end=Grid.c2p(2.8,5.6,0),color=RED,buff=0,tip_shape=StealthTip)
        
        self.add(Segment1)
        self.play(
            Unwrite(Slope1b),
            Transform(Slope1,Slope2)
        )
        #============================          

        Point3=(Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1)))
        Point3.move_to(Grid.c2p(1,2,0))
        
        DataTable[0][9] = always_redraw(
            lambda : Text(
                text=f'{Grid.p2c(Point3.get_center())[0]:.1f}',
                
                ).move_to(DataTable[0][9].get_center()).scale(0.6)
        )
        
        DataTable[0][10] = always_redraw(
            lambda : Text(
                text=f'{Grid.p2c(Point3.get_center())[1]:.1f}',
                
                ).move_to(DataTable[0][10].get_center()).scale(0.6)
        )

        DataTable[0][11] = always_redraw(
            lambda : Text(
                text=f'{Grid.p2c(Point3.get_center())[1]:.1f}',
                
                ).move_to(DataTable[0][11].get_center()).scale(0.6)
        )
        
        Slope3A = always_redraw(
            lambda : DashedLine(start=(Point3.get_center()),end=(Point3.get_center())-normalize((1,Grid.p2c(Point3.get_center())[1],0)),color=GREEN_C)
        )
        Slope3B = always_redraw(
            lambda : DashedLine(start=(Point3.get_center()),end=(Point3.get_center())+normalize((1,Grid.p2c(Point3.get_center())[1],0)),color=GREEN_C)
        )

        self.play(FadeIn(Point3))

        self.play(
            DataTable[5].animate.set_points_by_ends(end=(DataTable[5].get_start()[0],DataTable[4].get_start()[1],0),start= DataTable[5].get_start()),
            DataTable[6].animate.set_points_by_ends(end=(DataTable[6].get_start()[0],DataTable[4].get_start()[1],0),start= DataTable[6].get_start()),
            Write(DataTable[3]),
            Write(DataTable[0][9:12])
        )

        self.play(Write(Slope3A),Write(Slope3B))

        self.play(Point3.animate.move_to(Grid.c2p(2.4,4.8,0)),run_time=2)
        self.play(Point3.animate.move_to(Grid.c2p(2,4,0)))

        DataTable[0][9].clear_updaters()
        DataTable[0][10].clear_updaters()
        DataTable[0][11].clear_updaters()

        self.play(Unwrite(Slope3A),Unwrite(Slope3B))
        
        Point3.set_z_index(3)

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
                                      ).add_coordinates().set_z_index(-10).shift(4*RIGHT)),
                  InitialPoint.animate.move_to(newPoints[0]),
                  Segment1.animate.set_points_by_ends(start=newPoints[1],end=newPoints[2]),
                  Point2.animate.move_to(newPoints[3]),
                  Point3.animate.move_to(newPoints[4]),
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
        Point4=Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1))
        Point4.move_to(Grid.c2p(3,4,0))
        Point4.set_z_index(3)
        self.play(Write(Point4))
        Segment3=Line(start=Grid.c2p(2,2,0),end=Grid.c2p(3,4,0),color=RED,stroke_width=6).set_z_index(-3)
        self.add(Segment3)
        Slope2B.set_points_by_ends(start=Grid.c2p(3,4,0),end=Grid.c2p(3.8,5.6,0))
        Slope4=Arrow(start=Grid.c2p(3,4,0),end=Grid.c2p(3.5,6,0),color=RED,buff=0,tip_shape=StealthTip)
        self.play(Transform(Slope2B,Slope4))

        self.clear()

class SimpleAttemptExplained(Scene):
    def construct(self):
        my = BaseMaterials.my()
        Initial=BaseMaterials.Initial()
        
        DataTable = BaseMaterials.DataTable()
        Grid = BaseMaterials.Grid2()

        Point1=BaseMaterials.Point1(Grid)
        Point2=BaseMaterials.Point2(Grid)
        Point3=BaseMaterials.Point3(Grid)
        Point4=BaseMaterials.Point4(Grid)
        
        Segment1=BaseMaterials.Segment1(Grid)
        Segment2=BaseMaterials.Segment2(Grid)
        Segment3=BaseMaterials.Segment3(Grid)
        Ray4=BaseMaterials.Ray4(Grid)

        self.add(
            my,
            Initial,
            Grid,
            DataTable,
            Point1,
            Point2,
            Point3,
            Point4,
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
        
        Estimation = MathTex(r"g(x)=2^x",color=RED).scale(2).move_to(LimitProblem)
        self.play(Transform(LimitProblem,Estimation))
        euqalsign= Text("≈").scale(2)
        true=MathTex(r"\lim_{x \to \infty} \frac{e^x}{x}",color=GREEN).scale(2).shift(RIGHT*3)
        self.remove(LimitProblem,Estimation,TotalError,ErrorValues)
        self.play(Transform(Estimation,MathTex(r"\lim_{x \to \infty} \frac{2^x}{x}",color=RED).scale(2).shift(LEFT*3)),FadeOut(Limit))
        self.play(Write(true),Write(euqalsign))
        self.play(Indicate(euqalsign))
    
        self.play(mob.animate.shift(15*RIGHT) for mob in self.mobjects)
        
        self.play(Unwrite(Approximation),
                  Unwrite(RealGraph),
                  Unwrite(ApproximationText),
                  Transform(DataTable,BaseMaterials.DataTable()))
        
        self.play(RealText.animate.shift(DOWN))
        
class SecondAttempt(Scene):
    def construct(self):
        my = BaseMaterials.my()
        Initial=BaseMaterials.Initial()
        
        DataTable = BaseMaterials.DataTable()
        Grid = BaseMaterials.Grid2()

        Point1=BaseMaterials.Point1(Grid)
        Point2=BaseMaterials.Point2(Grid)
        Point3=BaseMaterials.Point3(Grid)
        Point4=BaseMaterials.Point4(Grid)
        
        Segment1=BaseMaterials.Segment1(Grid)
        Segment2=BaseMaterials.Segment2(Grid)
        Segment3=BaseMaterials.Segment3(Grid)
        Ray4=BaseMaterials.Ray4()
        RealText= MathTex(r"f(x)=e^x",color=GREEN_A).scale(1.3).to_edge(DL,buff=.5).shift(2.5*RIGHT)
        
        self.add(
            my,
            Initial,
            Grid,
            DataTable,
            Point1,
            Point2,
            Point3,
            Point4,
            Segment1,
            Segment2,
            Segment3,
            Ray4,
            RealText
        )
        
        self.play(Indicate(DataTable[0][3]))
        self.play(Indicate(DataTable[0][6]))
        
        self.play(Transform(DataTable[0][6],Text("0.5").move_to(DataTable[0][6]).scale(0.6)))
        
        self.play(
            Transform(DataTable[0][7],Text("1.5").move_to(DataTable[0][7]).scale(0.6)),
            Transform(DataTable[0][8],Text("1.5").move_to(DataTable[0][8]).scale(0.6)),
        )
        
        self.play(
            Transform(DataTable[0][9],Text("1.0").move_to(DataTable[0][9]).scale(0.6)),
            Transform(DataTable[0][10],Text("2.3").move_to(DataTable[0][10]).scale(0.6)),
            Transform(DataTable[0][11],Text("2.3").move_to(DataTable[0][11]).scale(0.6)),
            Transform(DataTable[0][12],Text("1.5").move_to(DataTable[0][12]).scale(0.6)),
            Transform(DataTable[0][13],Text("3.4").move_to(DataTable[0][13]).scale(0.6)),
            Transform(DataTable[0][14],Text("3.4").move_to(DataTable[0][14]).scale(0.6)),
        )
        
        self.play(
            Transform(DataTable[0][9],Text("...").move_to(DataTable[0][9]).scale(0.6)),
            Transform(DataTable[0][10],Text("...").move_to(DataTable[0][10]).scale(0.6)),
            Transform(DataTable[0][11],Text("...").move_to(DataTable[0][11]).scale(0.6)),
            Transform(DataTable[0][12],Text("3").move_to(DataTable[0][12]).scale(0.6)),
            Transform(DataTable[0][13],Text("11.4").move_to(DataTable[0][13]).scale(0.6)),
            Transform(DataTable[0][14],Text("11.4").move_to(DataTable[0][14]).scale(0.6)),
        )
        
        self.play(
            Unwrite(Point1),
            Unwrite(Point2),
            Unwrite(Point3),
            Unwrite(Point4),
            Unwrite(Segment1),
            Unwrite(Segment2),
            Unwrite(Segment3),
            Unwrite(Ray4)
        )
        SecondPoints = [(0,1)]
        step =0.5
        for i in range(1,7):
            SecondPoints.append((SecondPoints[i-1][0]+step,1.5*SecondPoints[i-1][1]))

        SecondCircles = VGroup()
    
        for pnt in SecondPoints:
            SecondCircles.add(Circle(radius=0.1,fill_color=BLUE,stroke_opacity=0,fill_opacity=1
                  ).add(Circle(radius=0.03,fill_color=BLUE_E,stroke_opacity=0,fill_opacity=1)
                  ).move_to(Grid.c2p(pnt[0],pnt[1])).set_z_index(3))
        
        SecondLines = VGroup()
        for i in range(6):
            SecondLines.add(Line(start=Grid.c2p(*SecondPoints[i])
                                 ,end=Grid.c2p(*SecondPoints[i+1])
                                 ,color=RED,stroke_width=6).set_z_index(-3))
            
        self.play(Write(SecondCircles),
                  Write(SecondLines))
        
        ApproximationText= MathTex(r"g(x)=2.25^x",color=PURPLE_A).scale(1)
        ApproximationText.to_edge(DL,buff=1.5).shift(1.5*RIGHT)
        
        self.play(Write(ApproximationText))
        
        
        RealGraph = Grid.plot(function= lambda x:2.71828**x,x_range=(-0.1,4),color=GREEN_A,stroke_width=9)
        self.play(Write(RealGraph))
        
        self.play(mob.animate.shift(15*RIGHT) for mob in self.mobjects)
        
class Problem2(Scene):
    def construct(self):
        Background = NumberPlane(
            x_range=(-1,15,1),
            x_length=17*0.9,
            y_range=(-6,6,1),
            y_length=13*0.9,
        )
        
        self.play(Write(Background))
        
        DataRectangle = Rectangle(color=GRAY_D,height=4.5,width=4,fill_opacity=1,stroke_opacity=0).to_edge(UR,buff=0.5).fade(0.2)
        self.play(Write(DataRectangle))
        self.wait()
        
        Ex2 = MathTex(r"\frac{dy}{dx} &= \frac{1}{x+y} \\ f(0.5) &= 0.5 \\ f(5) &= ? \\ \text{Step} &= 0.5 ").move_to(DataRectangle.get_center())
        self.play(Write(Ex2))
        
        self.play(Indicate(Ex2[0][:11]))
        self.play(Indicate(Ex2[0][11:21]))
        self.play(Indicate(Ex2[0][21:27]))
        self.play(Indicate(Ex2[0][27:]))
        
        def Equation(x,y):
            return 1/(x+y)
        
        
        Points, Lines = BaseMaterials.eulersMethod(Equation,(0.5,0.5),0.5,10,True,True,Grid=Background)
        self.play(Write(Points),
                  FadeIn(Lines))
        
        answer = Text("f(5) ≈ 3.25")
        self.play(Write(answer))
        
        self.play(Unwrite(answer),Unwrite(Points),Unwrite(Lines),Unwrite(Ex2),Unwrite(DataRectangle))
        self.clear()
        
class Problem3(Scene):
    def construct(self):
        Background = NumberPlane(
            x_range=(-1,15,1),
            x_length=17*0.9,
            y_range=(-6,6,1),
            y_length=13*0.9,
        )
        
        DataRectangle = Rectangle(color=GRAY_D,height=4.5,width=4,fill_opacity=1,stroke_opacity=0).to_edge(UR,buff=0.5).fade(0.2)
        
        self.add(Background,DataRectangle)
        
        Ex3 = MathTex(r"\frac{dy}{dx} &= -2.3y \\ f(0) &= 1 \\ f(5) &= ? \\ \text{Step} &= 1 ").move_to(DataRectangle.get_center())
        self.play(Write(Ex3))
        
        self.play(Indicate(Ex3[0][:11]))
        self.play(Indicate(Ex3[0][11:17]))
        self.play(Indicate(Ex3[0][17:23]))
        self.play(Indicate(Ex3[0][23:]))
        
        def Equation(x,y):
            return -2.3*y
        
        Points, Lines = BaseMaterials.eulersMethod(Equation,(0,1),1,10,True,True,Grid=Background)
        
        
        self.play(Write(Points), Write(Lines))
        
        sinGraphtext = MathTex(r"x*sin(x)").scale(2)
        sinGraph = Background.plot(function= lambda x:(x+0.5)*math.sin(3*(x+0.5)),x_range=(-0.1,9),color=PURPLE,stroke_width=9)
        self.play(Write(sinGraph),Write(sinGraphtext))
        self.wait()
        self.play(Unwrite(sinGraph),Unwrite(sinGraphtext))
        
        realGraphtext = MathTex(r"e^{-2.3x}").scale(2)
        realGraph = Background.plot(function= lambda x:2.71828**(x*-2.3),x_range=(-0.1,9),color=GREEN,stroke_width=9)
        self.play(Write(realGraph),Write(realGraphtext))
        
        self.play(realGraphtext.animate.to_edge(DR))
        self.wait()
        
        self.play(Indicate(Ex3[0][23:]))
        
        
        self.play(Indicate(Points[0]))
        self.wait() 
        self.play(Indicate(Points[1]))
        for i in range(len(Points[2:6])):
            self.play(Indicate(Points[2+i]))
        
        self.play(Transform(Ex3[0][28:],Text("0.5").move_to(Ex3[0][28:])))
        
        NewPoints, NewLines = BaseMaterials.eulersMethod(Equation,(0,1),0.7,10,True,True,Grid=Background)
        
        self.play(Transform(Points,NewPoints),Transform(Lines,NewLines))
        
        answer =Text("f(5) ≈ 0").scale(2)
        
        self.play(Write(answer))
         
        
        