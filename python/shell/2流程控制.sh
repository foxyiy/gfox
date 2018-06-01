#条件语句
#if  /then / elif /else  fi 
#! /etc/sh
#echo "请输入yes/no"
#read YES_OR_NO
#if [ "$YES_OR_NO" = "yes" ]; then
#	echo "早上好"
#elif [ "$YES_OR_NO" = "no" ]; then
#	echo "晚上好"
#else
#	echo "输入错误"
#	exit 1
#fi
#exit 0

#选择语句
#case 可以匹配字符串和通配符末尾必须以;;结尾  找到后直接跳到esac执行
#echo "你是猪吗"
#read A
#case "$A" in
#yes|是)
#	echo "猪是不会玩电脑的";;
#[^N]*)
#	echo "这是猪的电脑";;
#*)
#	echo "回答错误的都是猪"
#	exit 1;;
#esac
#exit 0

#for循环
for VAR in a b c d ;do
 	echo "i am $VAR" 
done

#while 循环
read VAR
while [ "$VAR" -lt 10 ];do
 #	echo "$VAR"
	echo $((VAR+1))
	VAR=$(("$VAR+1"))
done


参数传递

$# 	传递到脚本的参数个数
$* 	以一个单字符串显示所有向脚本传递的参数。
如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。
$$ 	脚本运行的当前进程ID号
$! 	后台运行的最后一个进程的ID号
$@ 	与$*相同，但是使用时加引号，并在引号中返回每个参数。
如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。
$- 	显示Shell使用的当前选项，与set命令功能相同。
$? 	显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。
