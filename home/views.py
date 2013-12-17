# -*- coding: utf-8 -*-

#crudgenerator auto-generated code.
#crudgenetaror date: 15th December 2013 15:05


from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from models import Upload


__all__ = ('UploadListView', 'UploadUpdateView',
           'UploadCreateView', 'UploadDeleteView')


class UploadListView(ListView):
    model = Upload
    paginate_by = 20


class UploadDeleteView(DeleteView):
    model = Upload

    def get_success_url(self):
        return reverse("home:upload:list", args=(1,))


class UploadCreateView(CreateView):
    model = Upload

    def get_success_url(self):
        return reverse("home:upload:list", args=(1,))


class UploadUpdateView(UpdateView):
    model = Upload

    def get_success_url(self):
        return reverse("home:upload:list", args=(1,))
# -*- coding: utf-8 -*-

#crudgenerator auto-generated code.
#crudgenetaror date: 15th December 2013 15:28


from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from models import Upload


__all__ = ('UploadListView', 'UploadUpdateView',
           'UploadCreateView', 'UploadDeleteView')


class UploadListView(ListView):
    model = Upload
    paginate_by = 20


class UploadDeleteView(DeleteView):
    model = Upload

    def get_success_url(self):
        return reverse("home:upload:list", args=(1,))


class UploadCreateView(CreateView):
    model = Upload

    def get_success_url(self):
        return reverse("home:upload:list", args=(1,))


class UploadUpdateView(UpdateView):
    model = Upload

    def get_success_url(self):
        return reverse("home:upload:list", args=(1,))
