#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-08-21 18:08:36
# @Author  : sxmsr (582124404@qq.com)
# @Link    : www.baidu.com
# @Version : $Id$


# results = {"basic":results_basic,"now": results_now, "daily": results_daily,
    # "url": results_url, "sug": results_suggestion}
def autoreply(rs):
    if(rs["basic"][2]=="中国"):
        temp=rs["sug"][1]
    else:
        temp=""
    html = '''<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>最专业最全面的全球天气查询</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="http://code.jquery.com/mobile/1.0/jquery.mobile-1.0.min.css" rel="stylesheet" type="text/css">
<script src="http://code.jquery.com/jquery-1.6.4.min.js" type="text/javascript"></script>
<script src="http://code.jquery.com/mobile/1.0/jquery.mobile-1.0.min.js" type="text/javascript"></script>
</head>

<body>
<div data-role="page" id="page">
  <div data-role="header">
    <h1>'''+rs["basic"][2]+rs["basic"][1]+'''天气预报</h1>
  </div>
  
  	 <div data-role="content">
        <div class="content-primary" align="center" style="float:right">
        <img src="'''+rs["now"][1]+'''" width=100% height="100%">
        </div>
        <p>'''+rs["now"][0]+'''</p>
    </div>
    
    <div data-role="content">
        <div class="content-primary" style="text-indent:2em">
        <p>'''+temp+'''</p>
        </div>
        
    </div>
    <hr />
'''
    temp=""
    for i in range(0,len(rs['daily'])):
        temp=temp+'''<div data-role="content">
        <div class="content-primary" align="center" style="float:right">
        <img src="'''+rs["url"][i]+'''" width=100% height="100%">
        </div>
        <p>'''+rs["daily"][i]+'''</p>
    </div>
    <hr />'''        
                   
    rail='''    
  <div data-role="footer">
    <h4>sxmsr----友情提供</h4>
    <div align="center">
  	<img src="http://6.dlnuxz.sinaapp.com/static/2.jpg" width=10% height="10%"> 
    </div>
  </div>
  
</div>
</body>
</html>
'''
    return html+temp+rail


def autoreply2(rs,rs2):
    if(rs["basic"][2]=="中国"):
        temp=rs["sug"][1]
    else:
        temp=""
    html = '''<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>最专业最全面的全球天气查询</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="http://code.jquery.com/mobile/1.0/jquery.mobile-1.0.min.css" rel="stylesheet" type="text/css">
<script src="http://code.jquery.com/jquery-1.6.4.min.js" type="text/javascript"></script>
<script src="http://code.jquery.com/mobile/1.0/jquery.mobile-1.0.min.js" type="text/javascript"></script>
</head>

<body>
<div data-role="page" id="page">
<div data-role="header">
    <h1>绑定城市：'''+rs2["basic"][2]+rs2["basic"][1]+'''天气预报</h1>
</div>
  
  	 <div data-role="content">
        <div class="content-primary" align="center" style="float:right">
        <img src="'''+rs2["now"][1]+'''" width=100% height="100%">
        </div>
        <p>'''+rs2["now"][0]+'''</p>
    </div>
  


  <div data-role="header">
    <h1>'''+rs["basic"][2]+rs["basic"][1]+'''天气预报</h1>
  </div>
  
  	 <div data-role="content">
        <div class="content-primary" align="center" style="float:right">
        <img src="'''+rs["now"][1]+'''" width=100% height="100%">
        </div>
        <p>'''+rs["now"][0]+'''</p>
    </div>
    
    <div data-role="content">
        <div class="content-primary" style="text-indent:2em">
        <p>'''+temp+'''</p>
        </div>
        
    </div>
    <hr />
'''
    temp=""
    for i in range(0,len(rs['daily'])):
        temp=temp+'''<div data-role="content">
        <div class="content-primary" align="center" style="float:right">
        <img src="'''+rs["url"][i]+'''" width=100% height="100%">
        </div>
        <p>'''+rs["daily"][i]+'''</p>
    </div>
    <hr />'''        
                   
    rail='''    
  <div data-role="footer">
    <h4>sxmsr----友情提供</h4>
    <div align="center">
  	<img src="http://6.dlnuxz.sinaapp.com/static/2.jpg" width=10% height="10%"> 
    </div>
  </div>
  
</div>
</body>
</html>
'''
    return html+temp+rail