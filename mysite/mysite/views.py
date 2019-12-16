#This file is created by -Afroz

from django.http import HttpResponse
def index(request):
    s = '''<h1> Welcome to my first page of Django<br></h1>
            <h2>Navigation Bar<br></h2>
            <a href="https://www.facebook.com/">Facebook</a><br>
            <a href="https://www.flipkart.com/">Flipkart</a><br>
            <a href="https://www.hindustantimes.com">News</a><br>
            <a href="https://www.google.com/">Google</a><br><br><br>
            <form>
            <input type="button" value="Go back!" onclick="history.back()">
            </form>'''
    return HttpResponse(s)

def about(request):
    s = ''' <h2>I am Afroz Hussain and Learning Djnago<br></h2>
        <form>
            <input type="button" value="Go back!" onclick="history.back()">
        </form>'''
    return HttpResponse(s)

def removepunc(request):
    s = ''' <h2>This is to remove punctuation<br></h2>
        <form>
            <input type="button" value="Go back!" onclick="history.back()">
        </form>'''
    return HttpResponse(s)
   
