import requests
import random
import os

"""
     
"""
ROOT = "/Users/zistrong/weibo/tupian/"
weiboUid = '6156565462'
COOKIE = "XSRF-TOKEN=xE2IeZRrUTwIB4RIK867rq5i; ALF=1727658425; SUB=_2A25L1hzoDeRhGedG4lMR-CfPzjmIHXVoqhAgrDV8PUJbkNAGLVr-kW1NUO-thYpEDBYvTgcEWbQg3_AfeuqpLWay; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWeb-f5RYX4HJdmooGMfAwn5JpX5KzhUgL.Fo2R1K271h.0SK-2dJLoIEXLxK-LBKBLBK.LxK-L1-eLBo5LxKBLB.eLB.eLxK.L1h5L1hqLxKqL1KML1h-t; WBPSESS=9bmT3m6gOoILhbR4p8a1L2tL6Q6KlRgks0Bjt_8G-P7HDGS6P2ekjjZxd3QDRxf6shjSmeMXVCjFNE270Y3p_BU2LZ_t4j9p5iwQeutQKpTBIWcwTlHFyIOPq8trpvgmZlgB6hhEiPmkTiAIPQ7Fdw==; PC_TOKEN=84dcac6818"
def weiboImg(uid):
    """
    下载微博图片
    @param uid 微博ID
    """
    album_id = getAlbum_peitu(uid)
    weiboName = getWeiboName(uid)
    if not weiboName:
        weiboName = uid
    
    print('正在下载相册：' + weiboName)
    page = 1

    while True:
        list = []
        albumUrl = "https://photo.weibo.com/photos/get_all?uid={0}&album_id={1}&count=30&page={2}&type=3&__rnd={3}".format(uid, album_id, page, random.random())
        jsonObject = getData(getPageContent(albumUrl))
        for pic in jsonObject.get('photo_list'):
            list.append("https://wx2.sinaimg.cn/original/" + pic.get('pic_name'))
        downloadAlbulme({weiboName: list}, album_id)
        page+=1
        if not list:
            break
        if page>3:
            break

    print('下载完成：' + weiboName)




def getAlbum_peitu(uid):
    albums = getAlbums(uid)
    for (k, v) in albums.items():
        if v == '微博配图':
            return k
    
    return None

def getWeiboName(uid):
    url = "https://weibo.com/ajax/user/popcard/get?id={0}".format(uid)
    return getData(getPageContent(url)).get('screen_name')


def getPageContent(url):
    return get(url, header={'Cookie': COOKIE})

def get(url, header):
    """
    @param url URL地址
    @param header 请求头
    """
    req =  requests.get(url, headers = header)
    return req.json() if req.status_code == 200 else {}

def getRawData(url, header={'Cookie': COOKIE}):
    req =  requests.get(url, headers= header)
    return req.content if req.status_code == 200 else None

def getData(json):
    return json.get('data')

def getAlbums(uid):
    url = "https://photo.weibo.com/albums/get_all?uid={0}&__rnd={1}".format(uid, random.random())
    data = getData(getPageContent(url))
    albums = {}
    for album in data.get('album_list'):
        albums[album.get('album_id')] = album.get('caption')
    return albums

def downloadAlbulme(pics: dict, album_id):
    for key, entry in pics.items():
        os.makedirs(ROOT+key + os.sep+album_id, exist_ok = True)
        os.chdir(ROOT+key + os.sep+album_id)
        for imgUrl in entry:
            imgName = imgUrl[imgUrl.rindex('/')+1:]
            with open(imgName, "wb") as img:
                img.write(bytes(getRawData(imgUrl)))




def queryFans(uid):
    fans = []
    page = 1
    while True:
        url = "https://weibo.com/ajax/friendships/friends?relate=fans&page={0}&uid={1}&type=all&newFollowerCount=0".format(page, uid)
        users = getPageContent(url).get('users')
        if not users:
            break
        for user in users:
            fans.append(user.get('id'))
        page+=1

    return fans

def queryFollow(uid):
    follows = []
    page = 1
    while True:
        url ='https://weibo.com/ajax/friendships/friends?uid={0}&page={1}'.format(uid, page)
        users = getPageContent(url).get('users')
        if not users:
            break
        for user in users:
            follows.append(user.get('id'))
        page+=1
    return follows

print(queryFollow(weiboUid))