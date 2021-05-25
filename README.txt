# 分子动力学模拟实验

## 文件说明

* CH4_O2.car, Material Studio 生成的文件, 共 10 个 CH4 和 20 个 O2
* CH4_O2.lammpstrj, VMD 生成的文件, 包含各原子坐标
* CH4_O2_processed.lammpstrj.csv, 交换原子类型并插入数值为 1.0 的一列得到的文件, 用于修改 data.CHO, 由 process_lammpstrj.py 生成
* my_data.CHO, Atoms 部分已替换为上述 csv 文件的内容
* my_in.CHO, 已添加 fix 和运行次数, 运行 5,000,000 个 timestep
* my_species.out, 反应生成的 Timestep-物种数据文件
* my_species_processed.csv, 处理过后便于绘图的 Timestep-物种数据, 由 process_species.py 生成

Created by 李俊宏, 2021.05.25
