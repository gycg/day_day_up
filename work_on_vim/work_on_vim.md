* [0.vim安装markdown插件](#0)
* [1.shell键盘操作技巧](#1)
* [2.vim键盘操作技巧](#2)

<h3 id="0">vim安装markdown插件</h3>

先安装[Vundle](http://github.com/VundleVim/Vundle.Vim), 一个vim插件管理器。参考[Vundle的安装和配置](https://github.com/VundleVim/Vundle.Vim#quick-start)。  
通过Vundle安装tabular和vim-markdown，参考[vim-markdown的安装](https://github.com/plasticboy/vim-markdown#installation) 。tabular的作用是对齐文本，vim-markdown是用来进行语法高亮和匹配规则。  
除此之外，还要安装vim-instant-markdown才能实现实时预览。参考[vim-instant-markdown的安装](https://github.com/suan/vim-instant-markdown#installation)。  

<h3 id="1">shell键盘操作技巧</h3>

所谓的键盘操作技巧，指的是在敲命令行的时候，一些快捷的移动、删除方式，用来提高命令行操作的效率。这些技巧的设计原则是尽量使所有的操作都能在主键盘中完成，减少到鼠标或功能键时的延迟。比如用Ctrl-a代替Home键的功能。  

快捷键|功能
-|:-
Ctrl-r|搜索历史命令；按下Esc再按q退出该模式
Ctrl-p|显示前一条命令
Ctrl-n|显示后一条命令
Ctrl-o<br>Ctrl-j<br>Ctrl-m|执行当前输入的命令， 相当于Enter
Ctrl-c|终止当前正在运行的命令或取消已经输入的命令
Ctrl-a|将光标移动到行首
Ctrl-e|将光标移动到行尾
Ctrl-t|交换光标前两个字符的位置
Ctrl-h|往后删除一个字符
Ctrl-d|如果已经有输入的字符，则往前删除一个字符，否则注销并关闭shell（exit）
Ctrl-b|往后移动一个字符
Ctrl-f|往前移动一个字符
Alt-b|往后移动一个单词
Alt-f|往前移动一个单词
Ctrl-k|从当前光标删除到行尾
Ctrl-w|从当前光标剪切到第一个空格
Ctrl-u|从当前光标剪切到行首
Ctrl-k|从当前光标剪切到行尾
Alt-d|从当前光标剪切到当前词尾
Alt-Backspace|从当前光标剪切到当前词头，若已在开头，剪切前一个单词
Ctrl-y|粘贴
Ctrl-l|清除屏幕
Ctrl-Shift-c|复制选中的文本
Ctrl-Shift-v|粘贴选中的文本
Ctrl-z|把当前进程转到后台运行，使用fg命令恢复
Ctrl-s|锁住终端
Ctrl-q|恢复终端
Ctrl-x-u|撤销操作

<h3 id="2">vim键盘操作技巧</h3>

类似于shell，vim也有一套快捷键操作。vim有三种常用模式，Command mode、Insert mode和Last line mode。进入vim时所处的就是Command mode，以下快捷键大多是在这个mode下操作。按下a/i/o进入Insert mode， 可以开始编辑文本。在Command mode下输入冒号“：“进入Last line mode。
#### vim命令行参数
用vim打开文件时，可以加一些参数。用法：vim [arguments] filename1 [filename2 ...]。  

参数|描述
-|:-
+[num]|打开时光标停在第[num]行。默认为最后一行
+/{pat}|打开时光标停在第一次匹配到{pat}的地方
-b|二进制文件模式
-d|文件比较模式。必须列出两个以上文件，同vimdiff
-g|GUI gvim模式（如果已编译并且可用）
-h|输出帮助信息
-r/-L|恢复模式，崩溃之后使用。这时文件夹中应该有.swp文件
-M/-R|关闭修改和写功能
-n|禁止产生.swp文件，空间有限的特定设备需要使用
-x|写文件时使用加密，将提示输入密钥
--noplugin|略过加载插件
--version|展示版本号

#### Command mode
##### 光标移动命令
快捷键|功能
-|:-
h, j, k, l|将光标向左、下、上、右移动一格
-/+|上下移动光标，光标处于行首
Ctrl-d/u|向下/上滚动半屏
n Ctrl-d/u|向下/上滚动n行，将n设为新的“半屏”标准
Ctrl-f/b|向前/后滚动一屏
n Ctrl-d/u|向前/后滚动n屏
Ctrl-y/e|向前/后滚动一行
n Ctrl-y/e|向前/后滚动n行
M|将光标移动到页面中间
W/B|将光标向后/前移动一个单词（空格分词）
w/b|将光标向后/前移动一个单词（移动到第一个非字母数字的字符）
E/e|将光标移动到单词的结尾（分别是第一个空格处和第一个非字母数字处）
0|将光标移动到行首
:\<digit\>|将光标移动到第\<digit\>行
$|将光标移动到行尾
^|将光标移动到非空格的行首
)|将光标移动到下一句的开始（以“.”、“?”、“!”分隔）
(|将光标移动到当前句的开始
}|将光标移动到下一段的开始（以空行或某些nroff macros分隔，[参考](http://home.fnal.gov/~mengel/man_page_notes.html)）
{|将光标移动到当前段的开始
]]|将光标移动到下一部分的开始（或某些nroff macros分隔）
[[|将光标移动到当前部分的开始
G|将光标移动到文件末尾
gg|将光标移动到文件开始
%|将光标移动到对应的括号（光标要放在括号上面）
'.|将光标移动到之前修改的那一行
m\<alpha\>|将当前行标记为\<alpha\>，\<alpha\>表示一个任意字母
'\<alpha\>|将光标移动到m\<alpha\>标记的那一行
]'|将光标移动到下一个小写标记
['|将光标移动到上一个小写标记
##### 编辑命令
快捷键|功能
-|:-
i|进入Insert mode，从当前光标处插入
I|进入Insert mode，从当前行首插入
a|进入Insert mode，从当前光标后一格插入
A|进入Insert mode，从当前行尾插入
o|进入Insert mode，从下一行开始插入
O|进入Insert mode，从上一行开始插入
ESC|退出Insert mode，进入Command mode
u|撤销上一次操作
U<br>Ctrl-r|撤销上一次撤销
dd|删除当前行
3dd|从当前行开始删除3行
D|从光标删除到行尾
C|从光标删除到行尾并且进入Insert mode
dw|删除单词
4dw|删除4个单词
d)|从光标删除到当前句子末尾
d$|从光标删除到行尾
d-|删除当前行和上一行
dfx|从光标删除到当前行中第一次出现的字母“x”
d'x|从当前行删除到标记“x“的行
'ad'b|从标记”a”的行删除到标记“b“的行
d/cat|从当前光标处删除到第一次出现”cat“的地方，但不删除”cat“本身
c*|如cw、c)、c$等，相当于先进行d相对的操作，再进入Insert mode
x|删除光标处的字符
X|删除光标前的字符
Y<br>yy|复制当前行
p|将剪贴板内容粘贴到当前行的下一行
P|将剪贴板内容粘贴到当前行的上一行
rx|替换光标处的字符为“x“
R|进入Replace模式
s|进入Insert mode并删除光标处的字符
S|进入Insert mode并删除当前行的内容
J|将当前行和下一行拼接起来
~|将光标处的字母转换大小写
Ctrl-a<br>Ctrl-x|将光标处的数字加1/减1
.|重复上一次操作
#### 查找命令
快捷键|功能
-|:-
/search_string{CR}|查找search_string
?search_string{CR}|向上查找search_string
/\\<search_word\\>{CR}|查找search_word。仅查找单独出现的，例如：/\\<s\\>不会查找“string”中的“s“，但是会找到”s=f(x)“中的”s“
n|定位到下一个search_string出现的地方
N|定位到上一个search_string出现的地方
fx<br>Fx|将光标移动到”x“第一次出现的地方，仅限同一行<br>向后查找
nfx<br>nFx|将光标移动到”x“第n次出现的地方，仅限同一行<br>向后查找
tx<br>Tx|将光标移动到”x“第一次出现处的前一个字符，仅限同一行<br>向后查找
ntx<br>nTx|将光标移动到”x“第n次出现处的前一个字符，仅限同一行<br>向后查找

查找时可以用以下模式进行匹配：  

模式|描述
-|:-
.|可以匹配任意单个字符
^|行首
^A|以”A“开头的行
$|行尾
$A|以”A“结尾的行
[abc]|匹配包含abc中的任意一个字符
\\ |关闭字符特殊含义。”\\.“不匹配任意字符，而是匹配点“.”这个符号
\d|匹配任意数字
\s|匹配空格
*|匹配0个、1个或多个*之前的字符
+|匹配1个或多个+之前的字符
?|匹配0个或1个?之前的字符
string1\|string2|匹配string1或string2
a.b|以a开始以b结束，中间有一个任意字符的字符串
^.$|匹配只包含一个字符的行
#### 信息命令
快捷键|功能
-|:-
Ctrl-g<br>:f|列出文件信息：文件名，总行数，光标的位置
:set list<br>:set nolist|显示Tab和EOF标记<br>关闭Tab和EOF显示
:args|显示所用的命令行参数
ZZ|保存更改并退出
:wq|保存更改并退出
:w|保存更改
:w!|保存更改，临时扩展文件权限
:w filename|不退出的情况下，将更改内容存入新的名为filename的文件
:q!|不保存更改退出
:qa|退出所有打开的文件





:1,10<  反缩进
