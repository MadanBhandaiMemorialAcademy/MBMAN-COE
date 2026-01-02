
import os
import django
from django.test import RequestFactory, Client
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test.utils import setup_test_environment

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
setup_test_environment()

from django.conf import settings
settings.ALLOWED_HOSTS += ['testserver']

from home.models import GalleryAlbum, GalleryImage

def test_bulk_delete():
    print("Testing bulk delete...")
    
    User = get_user_model()
    # Create a user
    user, created = User.objects.get_or_create(username='testadmin', email='test@example.com')
    if created:
        user.set_password('password')
        user.is_staff = True
        user.save()
    
    # Create an album
    album = GalleryAlbum.objects.create(title="Test Delete Album")
    
    # Create a valid GIF
    valid_gif = (
        b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00'
        b'\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'
    )
    
    # Create 3 images
    img1 = GalleryImage.objects.create(album=album, caption="Delete Me 1", image=SimpleUploadedFile("1.gif", valid_gif, "image/gif"))
    img2 = GalleryImage.objects.create(album=album, caption="Delete Me 2", image=SimpleUploadedFile("2.gif", valid_gif, "image/gif"))
    img3 = GalleryImage.objects.create(album=album, caption="Keep Me 3", image=SimpleUploadedFile("3.gif", valid_gif, "image/gif"))
    
    print(f"Initial image count: {GalleryImage.objects.filter(album=album).count()}")
    
    client = Client()
    client.force_login(user)
    
    # Select first 2 images to delete
    data = {
        'image_ids': [img1.id, img2.id]
    }
    
    response = client.post('/admin/gallery/bulk-delete/', data, follow=True)
    
    print(f"Response status: {response.status_code}")
    print(f"Final URL: {response.request['PATH_INFO']}")
    
    # Verify count
    remaining_count = GalleryImage.objects.filter(album=album).count()
    print(f"Remaining image count: {remaining_count}")
    
    if remaining_count == 1:
        remaining_img = GalleryImage.objects.filter(album=album).first()
        if remaining_img.caption == "Keep Me 3":
            print("SUCCESS: Only intended images were deleted!")
        else:
            print("FAILURE: Wrong image remaining.")
    else:
        print(f"FAILURE: Expected 1 image remaining, found {remaining_count}")

    # Cleanup
    GalleryImage.objects.filter(album=album).delete()
    album.delete()

if __name__ == "__main__":
    test_bulk_delete()
