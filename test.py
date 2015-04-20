#coding:utf-8

from zccx.handle import Handle

s = Handle('o_HVEuK5VYfCGNJGc6MrwY2rFF5I')
print(s.bind(u"绑定 韩龙 B1304013!"))
print(s.bind(u"绑定 韩龙! B13040133"))
print(s.bind(u"绑定 韩龙 B13040133"))
print(s.consult())
