# SymPy 绘图实验报告

## 一、实验信息

- 小组名称：cp010(liutao)
- 成员：朗昊宇
- 实验日期：2025.4.9

---

## 二、实验目的

- 熟悉SymPy的plot、plot_implicit、和plot3d_parametric_surface函数；
- 掌握曲线、隐函数和参数曲面的绘制方法。

---

## 三、实验内容与方法

分别说明三个问题的具体绘图方法和使用的函数接口。

---

## 四、实验结果与分析

### 问题1: 函数曲线 $\cos(\tan(\pi x))$ 绘制结果

*(![image](https://github.com/user-attachments/assets/4551ac36-bff7-496e-af07-713437b3d1b3)
)*
- **图像特征**：  
  - 在 $x \in (-0.4, 0.4)$ 内呈现周期性振荡，振幅稳定；  
  - 当 $x \to \pm 0.5$ 时，$\tan(\pi x) \to \infty$，导致 $\cos$ 值在 $[-1, 1]$ 间无限震荡，形成垂直渐近线；  
  - 图像在 $x = \pm 0.5$ 处出现间断（见图1）。  

### 问题2: 隐函数曲线 $e^y + \frac{\cos x}{x} + y = 0$ 绘制结果

*(![image](https://github.com/user-attachments/assets/e864a8aa-e4d2-465e-b040-015380f15778)
)*
**图像特征**：  
  - **对称性**：$x > 0$ 和 $x < 0$ 区域的曲线呈非对称分布，但整体趋势互补；  
  - **奇点处理**：$x = 0$ 附近无定义，曲线在 $x \to 0^\pm$ 时分别向 $y \to -\infty$ 和 $y \to +\infty$ 延伸；  
  - **渐进行为**：当 $|x| > 5$ 时，曲线近似为 $y \approx -x$ 的直线（见图2）。  

### 问题3: 参数曲面绘制结果

*(![image](https://github.com/user-attachments/assets/12969e69-1e6a-4e86-99a7-44ca969c4f2d)
)*
**几何特征**：  
  - **螺旋收缩**：随 $s$ 增大，$x$ 和 $y$ 分量因 $e^{-s}$ 指数衰减，形成围绕 $z$ 轴的收缩螺旋；  
  - **线性增长**：$z = t$ 使曲面沿 $z$ 轴线性延伸，整体呈现锥形螺旋结构；  
  - **初始截面**：当 $s = 0$ 时，截面为半径 1 的标准螺旋线（见图3）。  

---

## 五、实验总结与讨论

- 通过本实验你掌握了哪些绘图技巧？
- 实验中你遇到了哪些问题？如何解决？
- 你对SymPy的绘图功能有什么建议或意见？

---

## 六、参考文献

- SymPy官方文档：https://docs.sympy.org/latest/modules/plotting.html
