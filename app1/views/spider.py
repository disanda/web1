import urllib
from django.shortcuts import render
from django.shortcuts import redirect
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko    ) Chrome/58.0.3029.96 Safari/537.36'
}

def f(request):
    if request.method =='POST':
        weba = request.POST.get('weba')
        response1 = urllib.request.urlopen(weba)
        html = response1.read()
        f = open('./4.txt', 'wb')
        f.write(html)
        f.close()
        return redirect('app_spider.html')
    elif request.method == 'GET':
        with open('./4.txt', "r") as f:  # 设置文件对象
            str = f.read()  # 可以是随便对文件的操作
        return render(request, 'app_spider.html', {'web': str})
