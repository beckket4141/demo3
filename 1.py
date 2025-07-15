path=[1,2,3]
dest=4
print(f"find path:{'->'.join(map(str,path))}->{dest}")

#demo
pathstr=['1','2','3']
result=list(map(int,pathstr))
print(result)  # 输出：[1, 2, 3]

dictstr=['a:1','b:2']
result=[dict([item.split(':')]) for item in dictstr]
print(result)  # 输出: [{'a': '1'}, {'b': '2'}]

print(f"{'...'.join(pathstr)}")