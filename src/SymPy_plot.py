"""
SymPy 绘图练习模板

本模板包含三个绘图练习，分别演示：
1. 基本函数绘图
2. 隐函数绘图 
3. 参数曲面绘图

学生需要完成每个函数中的TODO部分来实现相应绘图功能。
"""

import sympy as sp
from sympy.plotting import plot, plot_implicit, plot3d_parametric_surface

def problem1():
    """绘制函数 cos(tan(pi*x)) 的图像"""
    x = sp.symbols('x')
    expr = sp.cos(sp.tan(sp.pi * x))  # 定义符号表达式
    plot(
        expr, (x, -1, 1),
        xlabel='x', ylabel='y',
        title=r'$\cos(\tan(\pi x))$ 振荡曲线',
        xlim=(-1.1, 1.1), ylim=(-2, 2)  # 限制坐标轴范围
    )
    
def problem2():
    """绘制隐函数 e^y + cos(x)/x + y = 0 的对称曲线"""
    x, y = sp.symbols('x y')
    expr = sp.Eq(sp.exp(y) + sp.cos(x)/x + y, 0)  # 构建隐式方程
    plot_implicit(
        expr,
        (x, -10, 10), (y, -10, 10),
        points=800,                  # 提高采样点保证曲线平滑
        xlabel='x', ylabel='y',
        title=r'隐函数 $e^y + \frac{\cos x}{x} + y = 0$',
        line_color='darkred'          # 自定义曲线颜色
    )
    

def problem3():
    """绘制三维参数曲面"""
    """绘制指数衰减螺旋曲面 (e^{-s}cos(t), e^{-s}sin(t), t)"""
    s, t = sp.symbols('s t')
    x = sp.exp(-s) * sp.cos(t)      # x 分量随 s 指数衰减
    y = sp.exp(-s) * sp.sin(t)      # y 分量随 s 指数衰减
    z = t                           # z 分量线性增长
    plot3d_parametric_surface(
        x, y, z,
        (s, 0, 8), (t, 0, 5*sp.pi), # 参数范围设置
        xlabel='x', ylabel='y', zlabel='z',
        title='三维螺旋曲面: $x=e^{-s}\cos t,\ y=e^{-s}\sin t,\ z=t$',
        surface_color='goldenrod'    # 自定义曲面颜色
    )

if __name__ == "__main__":
    # 依次运行三个问题的绘图函数
    problem1()
    problem2()
    problem3()
