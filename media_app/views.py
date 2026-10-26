from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import MediaItem, Category
from .forms import MediaItemForm


def media_gallery(request):
    """
    Main gallery view supporting filtering by media_type (image, video, audio)
    and search keyword.
    """
    media_type = request.GET.get('type')
    category_slug = request.GET.get('category')
    search_query = request.GET.get('q')

    items = MediaItem.objects.all()

    if media_type in ['image', 'video', 'audio', 'pdf']:
        items = items.filter(media_type=media_type)

    if category_slug:
        items = items.filter(category__slug=category_slug)

    if search_query:
        items = items.filter(title__icontains=search_query)

    categories = Category.objects.all()

    context = {
        'items': items,
        'categories': categories,
        'selected_type': media_type,
        'selected_category': category_slug,
        'search_query': search_query,
        'total_count': items.count(),
    }
    return render(request, 'media_app/gallery.html', context)


def media_detail(request, pk):
    """
    Detailed player / view for a single multimedia asset.
    Increments view count on access.
    """
    item = get_object_or_404(MediaItem, pk=pk)
    item.views_count += 1
    item.save(update_fields=['views_count'])

    related_items = MediaItem.objects.filter(media_type=item.media_type).exclude(pk=item.pk)[:4]

    context = {
        'item': item,
        'related_items': related_items,
    }
    return render(request, 'media_app/detail.html', context)


def upload_media(request):
    """
    Upload portal for images, videos, and audio.
    """
    if request.method == 'POST':
        form = MediaItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save()
            messages.success(request, f"'{new_item.title}' was successfully uploaded!")
            return redirect('media_detail', pk=new_item.pk)
    else:
        form = MediaItemForm()

    return render(request, 'media_app/upload.html', {'form': form})
