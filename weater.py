#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-08-20 13:14:40
# @Author  : sxmsr (582124404@qq.com)
# @Link    : www.baidu.com
# @Version : $Id$


import urlparse
import xml.etree.ElementTree as ET
import urllib2
import json
import tpl


def weather(Content):

    Content = Content.strip()
    url = 'https://api.heweather.com/x3/weather?city=' + \
        Content+'&key=526b6a82ca034ab3a3a572f8a8d3728b'
    response = urllib2.urlopen(url)
    html = response.read()
    content = json.loads(html)
    results_basic = []
    results_now = []
    results_daily = []
    results_url = []
    results_suggestion = []
    results = {"basic": results_basic, "now": results_now, "daily": results_daily,
               "url": results_url, "sug": results_suggestion}
    basic = ""
    pic_url = ""
    results_basic.append(
        content["HeWeather data service 3.0"][0].get("status").encode('UTF-8'))
    if(content["HeWeather data service 3.0"][0].get("status") == 'ok'):

        results_basic.append(
            content["HeWeather data service 3.0"][0]["basic"].get("city").encode('UTF-8'))
        results_basic.append(
            content["HeWeather data service 3.0"][0]["basic"].get("cnty").encode('UTF-8'))
        results_basic.append(
            content["HeWeather data service 3.0"][0]["basic"]["update"].get("loc").encode('UTF-8'))
        # 取now
        basic = ""
        pic_url = ""
        txt = content["HeWeather data service 3.0"][0][
            "now"]["cond"].get("txt")  # 天气状况描述
        code = content["HeWeather data service 3.0"][0][
            "now"]["cond"].get("code")  # 天气状况代码
        if(txt):
            day = txt.encode('UTF-8')
            day_picurl = "http://files.heweather.com/cond_icon/" + \
                code.encode('UTF-8')+".png"
            basic = basic + "【实时天气】: "+day+"  "
            pic_url = day_picurl

        fl = content["HeWeather data service 3.0"][0][
            "now"].get("fl")  # 体感温度
        hum = content["HeWeather data service 3.0"][0][
            "now"].get("hum")  # 相对湿度（%）

        basic = basic+"    体感温度: " + \
            fl.encode('UTF-8')+" 相对湿度: "+hum.encode('UTF-8')+"（%）    \n"

        pcpn = content["HeWeather data service 3.0"][0][
            "now"].get("pcpn")  # 降水量（mm）
        pres = content["HeWeather data service 3.0"][
            0]["now"].get("pres")  # 气压
        tmp = content["HeWeather data service 3.0"][0][
            "now"].get("tmp")  # 温度

        basic = basic+"降水量: " + \
            pcpn.encode('UTF-8')+"mm  气压: "+pres.encode('UTF-8') + \
            "    温度: "+tmp.encode('UTF-8')+"℃ \n"

        vis = content["HeWeather data service 3.0"][0][
            "now"].get("vis")  # 能见度（km）

        deg = content["HeWeather data service 3.0"][0][
            "now"]["wind"].get("deg")  # 风向（360度）
        winddir = content["HeWeather data service 3.0"][0][
            "now"]["wind"].get("dir")  # 风向

        sc = content["HeWeather data service 3.0"][0][
            "now"]["wind"].get("sc")  # 风力
        spd = content["HeWeather data service 3.0"][0][
            "now"]["wind"].get("spd")  # 风速（kmph）

        basic = basic+"能见度: "+vis.encode('UTF-8')+"km   风向"+winddir.encode('UTF-8') + \
            "  "+deg.encode('UTF-8')+"° 风力: "+sc.encode('UTF-8') + \
            " 风速: "+spd.encode('UTF-8')+"kmph"+"\n"

        if(content["HeWeather data service 3.0"][0].get('aqi')):
            aqi = content["HeWeather data service 3.0"][0][
                "aqi"]["city"].get("aqi")  # 空气质量指数
            co = content["HeWeather data service 3.0"][0][
                "aqi"]["city"].get("co")  # 一氧化碳1小时平均值(ug/m³)
            no2 = content["HeWeather data service 3.0"][0][
                "aqi"]["city"].get("no2")  # 二氧化氮1小时平均值(ug/m³)
            o3 = content["HeWeather data service 3.0"][0][
                "aqi"]["city"].get("o3")  # 臭氧1小时平均值(ug/m³)
            pm10 = content["HeWeather data service 3.0"][0][
                "aqi"]["city"].get("pm10")  # PM10 1小时平均值(ug/m³)
            pm25 = content["HeWeather data service 3.0"][0][
                "aqi"]["city"].get("pm25")  # PM2.5 1小时平均值(ug/m³)
            qlty = content["HeWeather data service 3.0"][0][
                "aqi"]["city"].get("qlty")  # 空气质量类别
            so2 = content["HeWeather data service 3.0"][0][
                "aqi"]["city"].get("so2")  # 二氧化硫1小时平均值(ug/m³)
            basic = basic+"空气质量指数："+aqi.encode('UTF-8')+"   空气质量类别："+qlty.encode('UTF-8') + \
                "\n二氧化氮1小时平均值："+no2.encode('UTF-8')+"ug/m³ 臭氧1小时平均值："+o3.encode('UTF-8') +\
                "ug/m³ PM10 1小时平均值："+pm10.encode('UTF-8')+"ug/m³ \nPM2.5 1小时平均值："+pm25.encode('UTF-8') +\
                "ug/m³ 一氧化碳1小时平均值：" + \
                co.encode('UTF-8')+"ug/m³ 二氧化硫1小时平均值：" + \
                so2.encode('UTF-8')+"ug/m³ \n"
        print basic
        results_now.append(basic)
        results_now.append(pic_url)

        # 取daily
        for x in xrange(0, len(content["HeWeather data service 3.0"][0][
                "daily_forecast"])):
            basic = ""
            pic_url = ""
            date = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x].get("date")  # 预报日期
            basic = basic+"日期: " + date.encode('UTF-8')+"\n"
            txt_d = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x]["cond"].get("txt_d")  # 白天天气状况描述
            code_d = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x]["cond"].get("code_d")  # 白天天气状况代码

            txt_n = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x]["cond"].get("txt_n")  # 夜间天气状况描述
            code_n = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x]["cond"].get("code_n")  # 夜间天气状况代码

            if(txt_n):
                night = txt_n.encode("UTF-8")
                night_picurl = "http://files.heweather.com/cond_icon/" + \
                    code_n.encode('UTF-8')+".png"
                basic = basic + " 夜间: "+night
                pic_url = night_picurl

            if(txt_d):
                day = txt_d.encode('UTF-8')
                day_picurl = "http://files.heweather.com/cond_icon/" + \
                    code_d.encode('UTF-8')+".png"
                basic = basic + " 白天: "+day+"  "
                pic_url = day_picurl

            sr = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x]["astro"].get("sr")  # 日出时间
            ss = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x]["astro"].get("ss")  # 日落时间

            basic = basic+"    日出时间: " + \
                sr.encode('UTF-8')+" 日落时间: "+ss.encode('UTF-8')+"    \n"

            hum = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x].get("hum")  # 相对湿度（%）
            pcpn = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x].get("pcpn")  # 降水量（mm）
            pop = content["HeWeather data service 3.0"][
                0]["daily_forecast"][x].get("pop")  # 降水概率
            pres = content["HeWeather data service 3.0"][
                0]["daily_forecast"][x].get("pres")  # 气压
            tmpmax = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x]["tmp"].get("max")  # 最高温度
            tmpmin = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x]["tmp"].get("min")  # 最低温度
            # return mtpl1
            basic = basic+"相对湿度: "+hum.encode('UTF-8')+"%   "+"降水量: "+pcpn.encode('UTF-8')+"mm  降水概率: " + \
                pop.encode('UTF-8')+"   气压: "+pres.encode('UTF-8')+"    温度: " + \
                tmpmax.encode('UTF-8')+"℃~"+tmpmin.encode('UTF-8')+"℃  \n"

            vis = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x].get("vis")  # 能见度（km）

            deg = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x]["wind"].get("deg")  # 风向（360度）
            winddir = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x]["wind"].get("dir")  # 风向
            sc = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x]["wind"].get("sc")  # 风力
            spd = content["HeWeather data service 3.0"][0][
                "daily_forecast"][x]["wind"].get("spd")  # 风速（kmph）

            basic = basic+" 能见度: "+vis.encode('UTF-8')+"km   风向："+winddir.encode('UTF-8') + \
                "  "+deg.encode('UTF-8')+"° 风力: "+sc.encode('UTF-8') + \
                " 风速: "+spd.encode('UTF-8')+"kmph"+"\n"
            print basic
            results_daily.append(basic)
            results_url.append(pic_url)

        # 取建议
        if(content["HeWeather data service 3.0"][0].get("suggestion")):
            basic1 = ""
            basic2 = ""
            pic_url = ""
            comf = content["HeWeather data service 3.0"][
                0].get("suggestion")["comf"].get("txt")  # 舒适度指数
            drsg = content["HeWeather data service 3.0"][
                0].get("suggestion")["drsg"].get("txt")  # 穿衣指数
            flu = content["HeWeather data service 3.0"][
                0].get("suggestion")["flu"].get("txt")  # 感冒指数
            cw = content["HeWeather data service 3.0"][
                0].get("suggestion")["cw"].get("txt")  # 洗车指数
            sport = content["HeWeather data service 3.0"][
                0].get("suggestion")["sport"].get("txt")  # 运动指数
            trav = content["HeWeather data service 3.0"][
                0].get("suggestion")["trav"].get("txt")  # 旅游指数
            uv = content["HeWeather data service 3.0"][
                0].get("suggestion")["uv"].get("txt")  # 紫外线指数
            if(comf):
                basic1 = basic1 + " \n舒适度指数: "+comf.encode('UTF-8')
            if(drsg):
                basic1 = basic1 + " \n穿衣指数: "+drsg.encode('UTF-8')
            if(flu):
                basic1 = basic1 + " \n感冒指数: "+flu.encode('UTF-8')
            basic2 = basic1 + " \n洗车指数: "+cw.encode('UTF-8') +\
                " \n运动指数: "+sport.encode('UTF-8') + " \n旅游指数: "+trav.encode('UTF-8') +\
                " \n紫外线指数: "+uv.encode('UTF-8')
            print basic2
            results_suggestion.append(basic1)
            results_suggestion.append(basic2)
    else:
        pass
    return results
# results = {"basic":results_basic,"now": results_now, "daily": results_daily,
    # "url": results_url, "sug": results_suggestion}
if __name__ == '__main__':
    rs = weather("北京")
    print rs["basic"][0], rs["basic"][1], rs["basic"][2]
