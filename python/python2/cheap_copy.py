#写一个复制一个文件夹所有内容的程序
#总体思想： 写一个copy文件的程序 让多个进程同时执行这一段代码
from multiprocessing import Pool,Manager
import os

def copy(file_name,target,old_file_name):
	fr=open(old_file_name+"/"+file_name,"r")
	fw=open(target+"/"+file_name,"w")
	count = fr.read()
	fw.write(count)
	fr.close()
	fw.close()
	
def main():
	#第一步当然是获取要copy的文件名了
	old_file_name=input("please input fileName")
	new_file_name=old_file_name+"附件"
	#获取文件内所有文件名的列表
	file_all_name=os.listdir(old_file_name)
	os.mkdir(new_file_name)
	#创建一个进程池
	pool=Pool(5)
	q = Manager().Queue()
	num=1
	for name in file_all_name:
		pool.apply_async(copy,(name,new_file_name,old_file_name))
		q.put(num)
		copy_rate=num/len(file_all_name)
		print("\r%.2f"%copy_rate,end='')
		num+=1
	pool.close()
	pool.join()
main()
