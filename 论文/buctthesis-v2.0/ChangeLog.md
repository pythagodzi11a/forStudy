# Changelog of BUCTthesis
在这里记录 BUCTthesis 中较为重要的改动。

## v2.0 - 2023/05/21
**从该版本起，仓库交由 [长城学生网络](https://github.com/the-ccsn) 维护。**

### Added
- 合并 `buctcover.cls` 至 `buctthesis.cls` 中。也就是说现在可以直接在 `main.tex` 中使用 `\makecover` 生成封面
- 现在 `taskbook` 环境后可以接受一个 `*` 号，使得输出的“任务书”不含页眉页脚

### Fixed
- 修改了几个选项的键名，现在更加易读了
- 现在默认加载 `xeCJKfntef` 宏包来生成封面的下划线
- 修复了本科“符号说明表”的 `denotation` 环境失效的问题
- 微调了本科目录的样式

### Deleted
- 删除了 `buctcover.cls` 文件

## v1.4 - 2022/06/21

### Added

- 新增本科封面的支持；与硕博一样，因字体关系，相关文件独立于模板本体
- 新命令 `\inlinecite`，适用于行间引用
- 硕博英文目录中，章增加了前缀字符。比如：第一章 `Chapter 1`、附录A `Appendix A`

### Fixed

- 图表注：标签和文字的字体所对应的宏现在作区分
- 修复了图表标签序号在“附录”中变成阿拉伯数字的问题

## v1.3 - 2022/03/06
**本版本提交至CTAN；如无意外，将随 TeX Live 2022 发布。**
### Fixed

- Unicode 的带圈数字即从 ① （`U+2460`）到 ⑩ （`U+2469`）现在使用中文字体
- 修改了说明文档和示例文档的几个小问题

## v1.2 - 2021/09/10

### Added

- 增加 `fontset` 选项，从而可在非 Windows 系统下选择**中文**字库。

### Fixed

- 封面的下划线现在支持动态调整，具体长度与标题首行相等
- 英文摘要中的论文标题现在能正确换行了，且调整了垂直间距

## v1.1 - 2021/03/29

**本版本提交至CTAN**

### Added

- 增加论文封面，仅支持硕博

## v1.0 - 2021/02/18

### Added

- 增加硕博论文模板，`\documentclass[]{buctthesis}` 必须指定类型

### Fixed

- `denotation` 环境第二列宽的默认值的单位修正
- 本科中文摘要的关键词中，字体都使用中易黑体

### Deleted

- 模板发行版中取消 `blank` 文件夹，建议写作时直接在示例文件中修改

## Beta.v0.9.6 - 2020/12/10

### Added

- 启用 `DocStrip`，增加文件 `buctthesis.dtx` 和 `buctthesis.ins`，以后将说明将在 `buctthesis.pdf` 查看；同时对示例文件进行大幅更改
- `\buctsetup` 命令中增加一个 `studentid` 键
- “诚信声明” 现在使用 `\makedeclare` 命令：其后可跟一个可选参数，参数为扫描页的路径

### Changed

- 自定义命令的 `myconfig.tex` 文件更改为 `mycfg.sty`
- 更改了 `\buctsetup` 命令中的键名称大小写
- 调整“任务书”中部分垂直间距，并在“进度安排”的表格里画上了竖线
- 重排“摘要”部分，且现在中英文摘要只能排在不同页上
- 设计图纸： `\designfig` -> `\dcaption`；以前需要在 `\caption` 后跟上 `\designfig` ，现在简化成了一个命令 `\dcaption`
- `denotation` 环境现在只接受一个参数，控制第二列宽度

### Deleted

- 删除了校徽和校名的插图
- 删除公式编号中“式”字
- 删除 `declare` 、 `abstract*` 和 `abstracten*`环境

## Beta.v0.9.5 - 2020/08/17

### Added

- 文档类选项 `openany` | `openright` ，适用于单双页打印：前者为原先设置；而后者会在适当之处插入一完全空白页，使得章页右开
- 现在多余的文档类选项将传递至 `ctexbook`

### Changed

- 重写字体配置，修改字体切换的命令：粗体、黑体等有所变化
- 微调双面摘要的垂直间距
- 文档类选项 `TextBlack` 重命名为 `submit`
- 代码的标签编号以 `-` 而不是 `.` 连接，形如 `代码 2-1`
- “任务书”中，插入论文信息部分命令修改为带可选星号的 `\taskinfo` 命令。原定义 `\taskinfo` -> `\taskinfo*` ，`\Taskinfo` -> `\taskinfo`。类似于“摘要”的环境，带星号的是按照《规范》来定义的，无星号的则是为了应对一些变化
- 修改了数学公式中的字体

### Deleted

- 删除文档类选项 `LessTOC` ，代之以相应位置的 PDF 书签
- 删除了“符号说明”中表格的表头
- 删除了 `dcolumn` 宏包，其功能与 `siunitx` 有所重合

## Beta.v0.9.4 - 2020/06/08

### Changed

- 格式控制从宏包改为文档类
- 主文件 `buctthesis.tex` 更名为 `main.tex` ，并将“诚信声明” `declare.tex` 、“任务书” `taskbook.tex` 和“摘要” `abstract.tex` 整合成一个文件 `frontmatter.tex`
- “任务书”部分代码简化
- 英文摘要关键词的字体改为中易黑体
- 将“前言”编入 `\frontmatter` 里，将“第一章”设置为第一页

### Added

- 主文件中增加 `\buctsetup` 命令，代替以往的多个 `\def` 来存储论文的相关信息
- 以 `threeparttable` 宏包来排版有脚注的表格
- 以 `gbt7714` 宏包控制参考文献格式

### Deleted

- 删除原先的参考文献格式控制文件 `gbt7714-2005.bst`

## Beta.v0.9.3 - 2020/04/08

### Changed

- 脚注：修复正文里脚注标记与前后文字的间距问题；脚注文字固定在页面底部且跨页重置计数
- 使用 `unicode-math` 宏包来配置数学字体
- `\emph{}` `\em` 命令：中文改用加粗的宋体而非楷体，西文改用粗体而非斜体

### Deleted

- 删除了算法的宏包，根据需要自行在 `myconfig.tex` 中调用
- 删除 `bm` 宏包

### Added

- 新增“任务书”部分
- 新文件 `myconfig.tex`，用于装载宏包或自定义命令
- 使用 `pdfpages` 宏包的相关命令来插入扫描PDF，可替换诚信声明、摘要页等
- 新环境 `dfigure` ，用于排版机械专业的设计图纸，在主文件的生成目录命令后使用  `\listofdesignfigures` 产生“设计图纸目录”；原定义 `\designfig` 仍然可以在普通插图中使用，但效果不同

## Beta.v0.9.2 - 2020/03/14

### Changed

- 重构宏包代码，重排了部分文本。
- 取消等宽字体的使用，一律使用 Times New Roman，并稍微修改了代码环境
- 现在使用 `\cite{}` 实现上标引用参考文献
- 现在使用 `subcaption` 宏包来插入并列子图，而 `subfigure` 宏包好久没更新了
- 一级编号列表环境的序号改变了样式
- 修改章节标题间距、缩短插图后的间距，列表环境现在改为正常的行间距
- 章、节、小节标题一律使用加粗的宋体，浮动体标签和数学定理内容改为宋体
- “诚信申明”改为“诚信声明”；修正了“前言”的拼写错误
- 在“结论”这一章标题中间加上了一个全角空格
- 简化了“符号说明”的代码

### Deleted

- 删除了在上个版本在摘要部分加入的作者及导师信息
- 删除参考文献的文件 bibliography.tex，简化原来的代码并移动至主文件
- 删除了一些宏包

### Added

- 宏包载入多了选项：`TextBlack` 用于将超链接全部设置为黑色，`LessTOC` 将会取消将“第一章”之前的所有内容编目（这与《规范》的示例相同）

## Beta.v0.9.1 - 2020/02/06

### Changed

- 正文字号修正
- 摘要同页排版的环境（ `abstract*` 与 `abstracten*` ），关键词的代码( `\keywords` 和 `\keywordsen` ）和格式
- 行距调整至近似 Microsoft Word 中 22 磅
- 修改节标题的前间距、小节标题的前后间距
- 代码环境，关键字增设粗体、环境背景颜色减弱至浅灰色的10%
- 修改目录部分的缩进
- 改用数字带圈圈的脚注
- 修改列表环境的间距
- 删除了部分数学类的环境
- 更改了hyperref宏包设置，凸显超链接以便于查看

### Added

- 摘要部分的作者（ `\author` 和 `\authoren` ）、导师（ `\thesupervisor` 和 `\thesupervisoren` ）等信息
- 增加“设计图纸”编入目录的命令 `\designfig`
- 增加了化学类的宏包、算法的宏包

## Beta.v0.9.0 - 2020/01/23

The first version. Hello World!
