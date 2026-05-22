from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from .models import Photo
from .forms import RecipePhotoForm


# 🔐 ROLE CHECK MIXIN (RBAC CORE)
class RoleRequiredMixin(UserPassesTestMixin):
    allowed_roles = []

    def test_func(self):
        user = self.request.user

        if user.is_superuser:
            return True

        return user.groups.filter(name__in=self.allowed_roles).exists()


# =========================
# GALLERY VIEW (READ + CREATE)
# =========================
@method_decorator(never_cache, name='dispatch')
class GalleryListView(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'gallery/home.html'
    context_object_name = 'photos'
    login_url = '/login/'

    def get_queryset(self):
        user = self.request.user

        # Admin sees everything
        if user.groups.filter(name='Admin').exists() or user.is_superuser:
            return Photo.objects.all()

        # Normal user sees only their uploads
        return Photo.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipePhotoForm()
        return context

    def post(self, request, *args, **kwargs):
        form = RecipePhotoForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()

        return redirect('gallery_home')


# =========================
# UPDATE (RBAC CONTROLLED)
# =========================
@method_decorator(never_cache, name='dispatch')
class PhotoUpdateView(LoginRequiredMixin, RoleRequiredMixin, UpdateView):
    model = Photo
    form_class = RecipePhotoForm
    template_name = 'gallery/edit.html'
    success_url = reverse_lazy('gallery_home')

    allowed_roles = ['Admin', 'Editor']  # roles allowed to edit

    def get_queryset(self):
        user = self.request.user

        if user.groups.filter(name='Admin').exists():
            return Photo.objects.all()

        return Photo.objects.filter(user=user)


# =========================
# DELETE (ADMIN ONLY RBAC)
# =========================
@method_decorator(never_cache, name='dispatch')
class PhotoDeleteView(LoginRequiredMixin, RoleRequiredMixin, DeleteView):
    model = Photo
    template_name = 'gallery/delete.html'
    success_url = reverse_lazy('gallery_home')

    allowed_roles = ['Admin']  # only Admin can delete

    def get_queryset(self):
        return Photo.objects.all()