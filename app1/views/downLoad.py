from django.http import StreamingHttpResponse
from django.http import HttpResponse

def file_download(request):
    # do something...
    with open('./4.txt') as f:
        c = f.read()
    return HttpResponse(c)



'''
def file_download(request):
    # do something...

    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = "./4.txt"
    response = StreamingHttpResponse(file_iterator(the_file_name))

    return response
'''

'''
def file_download(request):
    # do something...
    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = "./4.txt"
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response
'''