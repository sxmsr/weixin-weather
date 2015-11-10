# -*- coding: utf-8 -*-


def texttpl(fromUser,toUser,CreateTime,content):
	text = '''<xml>
            <ToUserName>''' + fromUser + '''</ToUserName>
            <FromUserName>''' + toUser + '''</FromUserName>
            <CreateTime>''' + CreateTime + '''</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content>''' + content + '''</Content>
            </xml>'''
	return text
	
def newstpl(fromUser,toUser,CreateTime,title,desc,pic,url):
	news = '''<xml>
            <ToUserName>'''+fromUser+'''</ToUserName>
            <FromUserName>'''+toUser+'''</FromUserName>
            <CreateTime>'''+CreateTime+'''</CreateTime>
            <MsgType><![CDATA[news]]></MsgType>
            <ArticleCount>1</ArticleCount>
            <Articles>
            <item>
            <Title>''' + title + '''</Title> 
            <Description>''' + desc + '''</Description>
            <PicUrl>''' + pic + '''</PicUrl>
            <Url>''' + url + '''</Url>
            </item>
            </Articles>
            </xml>'''
        return news
