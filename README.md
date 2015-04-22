南邮早操查询微信公众号
---------------------------
微信公众号 南邮晨跑次数查 后台

Dependencies
----------------------------
* [werobot](https://github.com/whtsky/WeRoBot)<br>
    WeRoBot是一个微信机器人框架
* MySQLdb <br>
    mysql数据库

Build table
-----------------------------
* settings.py中设置MySQL的相信息，以及库名
* build.sql<br>建表数据

API
-----------------------------
zccx库demo:<br>

    from zccx.handle import Handle
    #初始化对象
    h = Handle(wetoken)
    #查询该对象绑定者的信息
    print(h.consult())
    #绑定
    print(h.bind(msg))
