#!bin/sh
#批量创建目录
is_dir()
{
	DIR=$1
	if [ ! -d $DIR ];then
		return 1
	else
		return 0
	fi
}
for DIR in "$@";do
	if is_dir "$DIR"
		then :
	else
		echo "$DIR不存在 现在创建"
		mkdir "$DIR" 
		if [ $? -ne 0 ];then
			echo "创建失败"
			exit 1
		fi
	fi
done
