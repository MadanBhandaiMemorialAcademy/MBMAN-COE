
import os
import django
# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.conf import settings
settings.ALLOWED_HOSTS += ['testserver']

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, Client
from django.contrib.auth import get_user_model
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test.utils import setup_test_environment
setup_test_environment()

from home.models import GalleryAlbum, GalleryImage
from home.views import gallery_add

def test_bulk_upload():
    print("Testing bulk upload...")
    
    User = get_user_model()
    # Create a user
    user, created = User.objects.get_or_create(username='testadmin', email='test@example.com')
    if created:
        user.set_password('password')
        user.is_staff = True
        user.save()
    
    # Create an album
    album = GalleryAlbum.objects.create(title="Test Album")
    
    # Create a minimal valid GIF image
    valid_gif = (
        b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00'
        b'\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'
    )
    
    # Prepare multiple files
    image1 = SimpleUploadedFile("image1.gif", valid_gif, content_type="image/gif")
    image2 = SimpleUploadedFile("image2.gif", valid_gif, content_type="image/gif")
    
    # Create request
    factory = RequestFactory()
    data = {
        'album': album.id,
        'caption': 'Bulk Upload Test',
        'is_spotlight': False,
        'is_cover': False,
        'display_order': 0,
    }
    
    # IMPORTANT: SimpleUploadedFile doesn't work directly with data dict for multiple files in RequestFactory easily
    # We need to construct the POST data correctly. 
    # Actually, RequestFactory.post handles data, but for files...
    
    # Let's use Client instead, it's easier for file uploads
    client = Client()
    client.force_login(user)
    
    # Prepare data for client
    data_client = {
        'album': album.id,
        'caption': 'Bulk Upload Test',
        'display_order': 0,
        'image': [image1, image2], # List of files
    }
    
    response = client.post('/admin/gallery/add/', data_client, follow=True)
    print(f"Final URL: {response.request['PATH_INFO']}")
    print(f"Redirect chain: {response.redirect_chain}")
    print(f"Content (first 500 chars): {response.content[:500]}")
    
    
    if response.status_code == 200:
        print(f"Templates used: {[t.name for t in response.templates]}")
        # Check context for form errors
        # Context is a list of contexts
        if response.context:
            for ctx in response.context:
                if 'form' in ctx:
                    if ctx['form'].errors:
                        print(f"Form Errors: {ctx['form'].errors}")
                    else:
                         print("Form in context but no errors found.")
        else:
             print("No context found.")
             if b'bg-red-50' in response.content or b'errorlist' in response.content:
                 print("Found error markers in HTML content!")
                 print(response.content.decode('utf-8')) # Print full content to debug
             
    elif response.status_code == 302:
         print(f"Redirected to: {response.url}")
    
    # Check if images were created
    images_count = GalleryImage.objects.filter(album=album, caption='Bulk Upload Test').count()
    
    print(f"Response status: {response.status_code}")
    print(f"Images created: {images_count}")
    
    if images_count == 2:
        print("SUCCESS: 2 images were created!")
    else:
        print(f"FAILURE: Expected 2 images, found {images_count}")

    # Cleanup
    GalleryImage.objects.filter(album=album, caption='Bulk Upload Test').delete()
    album.delete()

if __name__ == "__main__":
    test_bulk_upload()
