#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-08-20 13:14:40
# @Author  : sxmsr (582124404@qq.com)
# @Link    : www.baidu.com
# @Version : $Id$

import sae
import urlparse
import xml.etree.ElementTree as ET
import urllib2
import json
import sae.const
import MySQLdb
import urllib
import tpl
import weather
import web



def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, response_headers)
    method = environ['REQUEST_METHOD']
    #global rs
    if method == "GET":
        query = environ['QUERY_STRING']
        #echostr = urlparse.parse_qs(query)['echostr']
        title=urlparse.parse_qs(query)['title']
        Content=title[0]
        if(Content.find("@")!=-1):
            question1 = Content.split('@')[0].strip()
            question2 = Content.split('@')[1].strip()
            rs1 = weather.weather(question1)
            rs2 = weather.weather(question2)
            html=web.autoreply2(rs1,rs2)
            #return echostr
            return html
        else:
            rs = weather.weather(Content)
            html=web.autoreply(rs)
           # return echostr
            return html
        #return echostr
    elif method == "POST":
        post = environ['wsgi.input']
        root = ET.parse(post)
        fromUser = root.findtext(".//FromUserName")
        toUser = root.findtext(".//ToUserName")
        CreateTime = root.findtext(".//CreateTime")
        Content = root.findtext(".//Content")
        MsgType = root.findtext(".//MsgType")
        
        db = MySQLdb.connect(
            host=sae.const.MYSQL_HOST, port=int(sae.const.MYSQL_PORT),
            user=sae.const.MYSQL_USER, passwd=sae.const.MYSQL_PASS, db=sae.const.MYSQL_DB, charset='utf8')
        c = db.cursor()

            
        if MsgType == "event":
            Event = root.findtext(".//Event")
            if Event == "subscribe":
                #reply = "关注消息"
                sql = "INSERT INTO main (`id` ,`openid`) VALUES (NULL,  '" + fromUser + "')"
                c.execute(sql)
                mtpl = tpl.texttpl(fromUser, toUser, CreateTime,\
                                   "请输入城市名称或者拼音查询\n(国内城市支持中英文，国外城市只支持英文)\n每个用户可绑定一个常用城市，格式如下：\n绑定@城市名\n解除绑定格式如下：\n解除@")
                
            elif Event == "unsubscribe":
                sql = "DELETE FROM main WHERE `openid` = '" +fromUser + "'"
                c.execute(sql)
                #reply = "取消关注消息"

        elif MsgType == "text":
            Content = Content.encode('UTF-8').strip()
            
            if(Content.find("绑定@")!=-1):
                Content = Content.split('@')[1]
                #.strip()
                rs = weather.weather(Content)
                if(rs["basic"][0]=="ok"):
                    sql = "UPDATE main SET `menu`='" + Content + "' WHERE `openid` = '" + fromUser + "'"
                    c.execute(sql)
                    mtpl = tpl.texttpl(fromUser, toUser, CreateTime, "绑定成功")
            elif(Content.find("解除@")!=-1):
                sql = "UPDATE main SET `menu`=NULL WHERE `openid` = '" + fromUser + "'"
                c.execute(sql)
            	mtpl = tpl.texttpl(fromUser, toUser, CreateTime, "解除成功")
            
            else:
                rs = weather.weather(Content)
        
                if(rs["basic"][0]=="ok"):
                    sql = "SELECT * FROM main WHERE `openid` = '" + fromUser + "'"
                    c.execute(sql)
                    rows = c.fetchone()
                    city = rows[2].encode("UTF-8")
                    if(len(city)>0):
                        Content =rs["basic"][1]+"@"+city
                    
                    #return tpl.texttpl(fromUser, toUser, CreateTime, Content+"国外城市只支持英文)")
                    urlargu={'title':Content}
                    urlargu=urllib.urlencode(urlargu)
                    url="http://6.dlnuxz.sinaapp.com?"+urlargu
                    mtpl = tpl.newstpl(fromUser, toUser, CreateTime, rs["basic"][2]+rs["basic"][1]+"天气预报", rs["now"][0], rs["now"][1], url)
                else:
                    mtpl = tpl.texttpl(fromUser, toUser, CreateTime, "查询出错,请输入城市名称或者拼音查询\n(国内城市支持中英文，国外城市只支持英文)\n每个用户可绑定一个常用城市，格式如下：\n绑定@城市名\n解除绑定格式如下：\n解除@")

        return mtpl


application = sae.create_wsgi_app(app)
