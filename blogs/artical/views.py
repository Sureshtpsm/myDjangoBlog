from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from artical.models import Posts,Comments
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.utils import timezone


class myviewclass():
    def listPosts(request):
        artical_list    = Posts.objects.order_by('post_date')[:5]
        template        = loader.get_template('artical/index.html')
        resultext       = RequestContext(request, {
            'artical_list': artical_list,
        })
        return HttpResponse(template.render(resultext))

    def detail(request):
        return render(request, 'artical/detail.html')


    def addpost(request):
        res = Posts(post_title=request.POST['post_title'],post_content=request.POST['post_content'], post_date=timezone.now())
        res.save()
        return HttpResponseRedirect(reverse('artical:listPosts'))

    def updateartical(request):
        artical              = get_object_or_404(Posts, pk=request.POST['post_id'])
        artical.post_content = request.POST['post_content']
        artical.save()
        return render(request, 'artical/articledetail.html', {'artical': artical})

    def addcomment(request):
        resc = Comments(comments=request.POST['comments'],post_id=request.POST['post_id'], comments_date=timezone.now())
        resc.save()
        artical = get_object_or_404(Posts, pk=request.POST['post_id'])
        return render(request, 'artical/articledetail.html', {'artical': artical})

    def articledetail(request, artical_id):
        artical = get_object_or_404(Posts, pk=artical_id)
        return render(request, 'artical/articledetail.html', {'artical': artical})

    def editartical(request, artical_id):
        artical = get_object_or_404(Posts, pk=artical_id)
        return render(request, 'artical/editartical.html', {'artical': artical})

    def deleteartical(request, artical_id):
        comments = get_object_or_404(Posts, pk=artical_id)
        comments.delete()
        return render(request, 'artical/index.html')
